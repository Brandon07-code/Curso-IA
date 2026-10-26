import os
import wave
import struct
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

# 1. Reparar spikes/clipping en 02_johan y 05_brandon
def repair_spikes(wav_path):
    with wave.open(wav_path, 'rb') as w:
        params = w.getparams()
        frames = w.readframes(w.getnframes())
        samples = list(struct.unpack(f'<{len(frames)//2}h', frames))
    
    fixed = 0
    for i in range(len(samples)):
        if abs(samples[i]) >= 32000:
            prev_val = samples[max(0, i - 12)]
            next_val = samples[min(len(samples) - 1, i + 12)]
            samples[i] = int((prev_val + next_val) / 2)
            fixed += 1
    
    with wave.open(wav_path, 'wb') as w:
        w.setparams(params)
        w.writeframes(struct.pack(f'<{len(samples)}h', *samples))
    print(f"Reparados {fixed} samples en {os.path.basename(wav_path)}")

repair_spikes(os.path.join(temp_dir, "02_johan_objetivos_ml.wav"))
repair_spikes(os.path.join(temp_dir, "05_brandon_perceptron_docker.wav"))

# 2. Aplicar filtro de claridad de voz (realce de presencia vocal, filtro antipop/graves y limitador)
print("Aplicando filtro de máxima claridad vocal...")
enhanced_wavs = {}
for name in [
    "01_brandon_intro_problematica.wav",
    "02_johan_objetivos_ml.wav",
    "03_johan_datos_limpieza.wav",
    "04_brandon_seaborn.wav",
    "05_brandon_perceptron_docker.wav",
    "06_johan_proximos_pasos.wav"
]:
    raw_w = os.path.join(temp_dir, name)
    enh_w = os.path.join(temp_dir, "enh_" + name)
    # Filtro: corta ruidos bajo 80Hz, da brillo a consonantes en 3kHz, y limita a -0.5 dB
    cmd = [
        ffmpeg, "-y",
        "-i", raw_w,
        "-af", "highpass=f=80,equalizer=f=3000:t=q:w=1.2:g=3,alimiter=limit=0.92",
        enh_w
    ]
    run_cmd(cmd)
    enhanced_wavs[name] = enh_w

# 3. Regenerar segmentos con los audios cristalinos
def build_seg(slide_name, enh_wav_name, out_name):
    slide_p = os.path.join(slide_dir, slide_name)
    audio_p = enhanced_wavs[enh_wav_name]
    out_p = os.path.join(temp_dir, out_name)
    cmd = [
        ffmpeg, "-y",
        "-loop", "1",
        "-framerate", "30",
        "-i", slide_p,
        "-i", audio_p,
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
        out_p
    ]
    run_cmd(cmd)

print("Regenerando segmentos de video con audio mejorado...")
build_seg("slide_01_portada.png", "01_brandon_intro_problematica.wav", "seg_01.mp4")
build_seg("slide_02_objetivos.png", "02_johan_objetivos_ml.wav", "seg_02.mp4")
build_seg("slide_03_datos_limpieza.png", "03_johan_datos_limpieza.wav", "seg_03.mp4")
build_seg("slide_04_seaborn.png", "04_brandon_seaborn.wav", "seg_04.mp4")

# Segmento 5
clip_path = os.path.join(base_dir, "terminal_docker_clip.mp4")
part1_path = os.path.join(temp_dir, "seg_05_part1.mp4")
part2_path = os.path.join(temp_dir, "seg_05_part2.mp4")
seg5_path = os.path.join(temp_dir, "seg_05.mp4")
seg5_list = os.path.join(temp_dir, "seg05_video_list.txt")

cmd_seg5 = [
    ffmpeg, "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", seg5_list,
    "-i", enhanced_wavs["05_brandon_perceptron_docker.wav"],
    "-c:v", "copy",
    "-c:a", "aac",
    "-b:a", "192k",
    "-ar", "48000",
    "-ac", "2",
    "-shortest",
    seg5_path
]
run_cmd(cmd_seg5)

build_seg("slide_06_proximos_pasos.png", "06_johan_proximos_pasos.wav", "seg_06.mp4")

# 4. Concatenar final
print("Concatenando video final...")
final_list = os.path.join(temp_dir, "final_video_list.txt")
out_final = os.path.join(base_dir, "Avance2_Grupo04_PAVIA_final.mp4")
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

desktop_final = r"C:\Users\Brandon\Desktop\Avance2_Grupo04_PAVIA.mp4"
shutil.copy2(out_final, desktop_final)
print("=== PROCESO COMPLETADO AL 100% ===")
