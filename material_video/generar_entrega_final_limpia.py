import os
import wave
import struct
import math
import subprocess
import shutil

ffmpeg = r"C:\Users\Brandon\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe"
base_dir = r"C:\Users\Brandon\Desktop\CursoIA\material_video"
temp_dir = os.path.join(base_dir, "temp_segments")
slide_dir = os.path.join(base_dir, "slides")

def run_cmd(cmd):
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print("ERROR:", res.stderr[-500:])
        raise RuntimeError(f"Fallo: {cmd[0]}")

print("=== 1. Procesando audio de Johan para Slide 6 ===")
wav_in = os.path.join(temp_dir, "true_slide6_audio.wav")
wav_cut = os.path.join(temp_dir, "slide6_cut_temp.wav")

with wave.open(wav_in, 'rb') as w:
    params = w.getparams()
    framerate = w.getframerate()
    frames = w.readframes(w.getnframes())
    samples = list(struct.unpack(f"<{len(frames)//2}h", frames))

# Cortar 'en la clase 12' (8.15s a 9.58s) con crossfade de 15ms
cut_start = int(8.15 * framerate) * 2
cut_end = int(9.58 * framerate) * 2
crossfade_len = int(0.015 * framerate) * 2

part1 = samples[:cut_start]
part2 = samples[cut_end:]

for i in range(crossfade_len):
    w1 = 1.0 - (i / crossfade_len)
    w2 = i / crossfade_len
    idx1 = len(part1) - crossfade_len + i
    idx2 = i
    part1[idx1] = int(part1[idx1] * w1 + part2[idx2] * w2)

new_samples = part1 + part2[crossfade_len:]

# Función para silenciar micro-pausas con ruidos/taps de micrófono
def silence_range(arr, start_sec, end_sec, fade_sec=0.01):
    s_idx = int(start_sec * framerate) * 2
    e_idx = int(end_sec * framerate) * 2
    f_len = int(fade_sec * framerate) * 2
    
    for i in range(f_len):
        idx = s_idx + i
        if idx < len(arr):
            arr[idx] = int(arr[idx] * (0.5 * (1 + math.cos(math.pi * i / f_len))))
            
    for idx in range(s_idx + f_len, e_idx - f_len):
        if idx < len(arr):
            arr[idx] = 0
            
    for i in range(f_len):
        idx = e_idx - f_len + i
        if idx < len(arr):
            arr[idx] = int(arr[idx] * (0.5 * (1 - math.cos(math.pi * i / f_len))))

# Silenciar golpes de aire en pausas
silence_range(new_samples, 0.85, 1.05)     # Golpe inicial antes de hablar
silence_range(new_samples, 9.80, 9.98)     # Golpe en pausa 1
silence_range(new_samples, 22.15, 22.42)   # Golpe en pausa 2

# Suavizar pips residuales y saturaciones
fixed = 0
for i in range(12, len(new_samples) - 12):
    val = new_samples[i]
    delta = abs(new_samples[i] - new_samples[i-1])
    if abs(val) >= 28000 or (delta > 22000 and abs(val) > 18000):
        new_samples[i] = (new_samples[i-10] + new_samples[i+10]) // 2
        fixed += 1

print(f"Recortado 'en la clase 12' y eliminados {fixed} pips.")

with wave.open(wav_cut, 'wb') as w:
    w.setparams((params[0], params[1], params[2], len(new_samples)//2, params[4], params[5]))
    w.writeframes(struct.pack(f"<{len(new_samples)}h", *new_samples))

# Filtro final de limpieza en FFmpeg
wav_final = os.path.join(temp_dir, "slide6_final_clean.wav")
cmd_filter = [
    ffmpeg, "-y",
    "-i", wav_cut,
    "-af", "adeclick,highpass=f=80,equalizer=f=3000:t=q:w=1.2:g=2.0,alimiter=limit=0.9",
    "-ar", "48000", "-ac", "2",
    wav_final
]
run_cmd(cmd_filter)

print("=== 2. Re-renderizando seg_06.mp4 con Slide corregida y audio limpio ===")
slide6 = os.path.join(slide_dir, "slide_06_proximos_pasos.png")
seg6 = os.path.join(temp_dir, "seg_06.mp4")
cmd_seg6 = [
    ffmpeg, "-y",
    "-loop", "1", "-framerate", "30",
    "-i", slide6, "-i", wav_final,
    "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-tune", "stillimage", "-pix_fmt", "yuv420p",
    "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=30",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-shortest",
    seg6
]
run_cmd(cmd_seg6)

print("=== 3. Concatenando video final completo con +faststart ===")
final_list = os.path.join(temp_dir, "final_video_list.txt")
out_desktop1 = r"C:\Users\Brandon\Desktop\PAVIA_Avance2_Sustentacion_FINAL.mp4"
out_desktop2 = r"C:\Users\Brandon\Desktop\Avance2_Grupo04_PAVIA.mp4"

cmd_final = [
    ffmpeg, "-y",
    "-f", "concat", "-safe", "0",
    "-i", final_list,
    "-c", "copy", "-movflags", "+faststart",
    out_desktop1
]
run_cmd(cmd_final)

try:
    shutil.copy2(out_desktop1, out_desktop2)
except Exception as e:
    print("Nota: archivo anterior bloqueado por reproductor, se guardo como PAVIA_Avance2_Sustentacion_FINAL.mp4")

print("=== PROCESO COMPLETADO EXITOSAMENTE ===")
print("Video final guardado en:", out_desktop1)
