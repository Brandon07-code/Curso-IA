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

# 1. Silenciar las 2 pausas donde sonaron los bips en Johan Audio 2
wav_path = os.path.join(temp_dir, "enh_02_johan_objetivos_ml.wav")
with wave.open(wav_path, 'rb') as w:
    params = w.getparams()
    framerate = w.getframerate()
    frames = w.readframes(w.getnframes())
    samples = list(struct.unpack(f'<{len(frames)//2}h', frames))

def silence_interval(start_sec, end_sec, fade_sec=0.01):
    s_idx = int(start_sec * framerate) * 2
    e_idx = int(end_sec * framerate) * 2
    f_len = int(fade_sec * framerate) * 2
    
    # Fade out
    for i in range(f_len):
        idx = s_idx + i
        if idx < len(samples):
            factor = 0.5 * (1 + math.cos(math.pi * i / f_len))
            samples[idx] = int(samples[idx] * factor)
    
    # Complete silence in between
    for idx in range(s_idx + f_len, e_idx - f_len):
        if idx < len(samples):
            samples[idx] = 0
            
    # Fade in
    for i in range(f_len):
        idx = e_idx - f_len + i
        if idx < len(samples):
            factor = 0.5 * (1 - math.cos(math.pi * i / f_len))
            samples[idx] = int(samples[idx] * factor)

# Silenciar bip 1 (54s - 55s en video)
silence_interval(11.20, 11.40)
# Silenciar bip 2 (1:05 - 1:08 en video)
silence_interval(23.55, 23.85)

with wave.open(wav_path, 'wb') as w:
    w.setparams(params)
    w.writeframes(struct.pack(f'<{len(samples)}h', *samples))

print("Bips eliminados con desvanecimiento suave.")

# 2. Re-renderizar seg_02.mp4
slide_p = os.path.join(slide_dir, "slide_02_objetivos.png")
out_seg2 = os.path.join(temp_dir, "seg_02.mp4")
cmd_seg2 = [
    ffmpeg, "-y",
    "-loop", "1",
    "-framerate", "30",
    "-i", slide_p,
    "-i", wav_path,
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-crf", "19",
    "-tune", "stillimage",
    "-pix_fmt", "yuv420p",
    "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=30",
    "-c:a", "aac",
    "-b:a", "192k",
    "-ar", "48000",
    "-ac", "2",
    "-shortest",
    out_seg2
]
run_cmd(cmd_seg2)
print("seg_02.mp4 reconstruido sin bips.")

# 3. Concatenar video final completo
final_list = os.path.join(temp_dir, "final_video_list.txt")
out_final = r"C:\Users\Brandon\Desktop\Avance2_Grupo04_PAVIA_Entrega.mp4"
desktop_final = r"C:\Users\Brandon\Desktop\Avance2_Grupo04_PAVIA.mp4"

cmd_final = [
    ffmpeg, "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", final_list,
    "-c", "copy",
    "-movflags", "+faststart",
    out_final
]
run_cmd(cmd_final)
shutil.copy2(out_final, desktop_final)
print("=== VIDEO 100% LIMPIO GENERADO ===")
