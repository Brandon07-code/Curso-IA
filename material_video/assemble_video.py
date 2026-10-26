import os
import subprocess
import shutil

ffmpeg = r"C:\Users\Brandon\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe"
base_dir = r"C:\Users\Brandon\Desktop\CursoIA\material_video"
audio_dir = os.path.join(base_dir, "audios")
slide_dir = os.path.join(base_dir, "slides")
temp_dir = os.path.join(base_dir, "temp_segments")
os.makedirs(temp_dir, exist_ok=True)

def run_cmd(cmd):
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print("ERROR en comando:", " ".join(cmd[:4]))
        print(res.stderr[-500:])
        raise RuntimeError(f"Fallo ffmpeg: {cmd[0]}")

# Paso 1: Decodificar cada audio a WAV limpio a 48kHz estéreo para eliminar cualquier salto o beep
print("--- Paso 1: Normalizando audios a PCM WAV sin distorsión ---")
audio_files = [
    "01_brandon_intro_problematica.ogg",
    "02_johan_objetivos_ml.ogg",
    "03_johan_datos_limpieza.ogg",
    "04_brandon_seaborn.ogg",
    "05_brandon_perceptron_docker.ogg",
    "06_johan_proximos_pasos.ogg"
]

wav_map = {}
for a in audio_files:
    ogg_p = os.path.join(audio_dir, a)
    wav_p = os.path.join(temp_dir, a.replace(".ogg", ".wav"))
    cmd = [
        ffmpeg, "-y",
        "-i", ogg_p,
        "-af", "aresample=async=1000:first_pts=0",
        "-ar", "48000",
        "-ac", "2",
        wav_p
    ]
    run_cmd(cmd)
    wav_map[a] = wav_p
print("Audios WAV normalizados con éxito.")

# Función para armar segmento de imagen + audio
def make_still_segment(slide_name, audio_name, out_name):
    slide_path = os.path.join(slide_dir, slide_name)
    audio_path = wav_map[audio_name]
    out_path = os.path.join(temp_dir, out_name)
    print(f"Generando {out_name}...")
    cmd = [
        ffmpeg, "-y",
        "-loop", "1",
        "-framerate", "30",
        "-i", slide_path,
        "-i", audio_path,
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
        out_path
    ]
    run_cmd(cmd)

# Segmentos 1 a 4
make_still_segment("slide_01_portada.png", "01_brandon_intro_problematica.ogg", "seg_01.mp4")
make_still_segment("slide_02_objetivos.png", "02_johan_objetivos_ml.ogg", "seg_02.mp4")
make_still_segment("slide_03_datos_limpieza.png", "03_johan_datos_limpieza.ogg", "seg_03.mp4")
make_still_segment("slide_04_seaborn.png", "04_brandon_seaborn.ogg", "seg_04.mp4")

# Segmento 5: SINCRONIZACIÓN PERFECTA
# En el audio 5 (68.75s), Brandon explica la terminal en los primeros ~20 segs y luego las gráficas.
# Mostramos la terminal en vivo durante 20 segundos y luego pasamos a la diapositiva de gráficas durante los 48.75 segs restantes.
print("Generando seg_05.mp4 con sincronización exacta (Terminal 20s + Diapositiva Resultados 48.75s)...")
clip_path = os.path.join(base_dir, "terminal_docker_clip.mp4")
part1_path = os.path.join(temp_dir, "seg_05_part1.mp4")
cmd_part1 = [
    ffmpeg, "-y",
    "-i", clip_path,
    "-t", "20.0",
    "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=30",
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-crf", "19",
    "-pix_fmt", "yuv420p",
    "-an",
    part1_path
]
run_cmd(cmd_part1)

part2_path = os.path.join(temp_dir, "seg_05_part2.mp4")
slide5_path = os.path.join(slide_dir, "slide_05_perceptron_resultados.png")
cmd_part2 = [
    ffmpeg, "-y",
    "-loop", "1",
    "-framerate", "30",
    "-i", slide5_path,
    "-t", "48.747",
    "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=30",
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-crf", "19",
    "-tune", "stillimage",
    "-pix_fmt", "yuv420p",
    "-an",
    part2_path
]
run_cmd(cmd_part2)

seg5_list_path = os.path.join(temp_dir, "seg05_video_list.txt")
with open(seg5_list_path, "w", encoding="ascii") as f:
    f.write("file 'seg_05_part1.mp4'\n")
    f.write("file 'seg_05_part2.mp4'\n")

seg5_path = os.path.join(temp_dir, "seg_05.mp4")
audio5_wav = wav_map["05_brandon_perceptron_docker.ogg"]
cmd_seg5 = [
    ffmpeg, "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", seg5_list_path,
    "-i", audio5_wav,
    "-c:v", "copy",
    "-c:a", "aac",
    "-b:a", "192k",
    "-ar", "48000",
    "-ac", "2",
    "-shortest",
    seg5_path
]
run_cmd(cmd_seg5)

# Segmento 6
make_still_segment("slide_06_proximos_pasos.png", "06_johan_proximos_pasos.ogg", "seg_06.mp4")

# Concatenar todos los 6 segmentos y mover átomo moov al inicio (+faststart)
print("--- Concatenando video final completo con +faststart ---")
final_list_path = os.path.join(temp_dir, "final_video_list.txt")
with open(final_list_path, "w", encoding="ascii") as f:
    f.write("file 'seg_01.mp4'\n")
    f.write("file 'seg_02.mp4'\n")
    f.write("file 'seg_03.mp4'\n")
    f.write("file 'seg_04.mp4'\n")
    f.write("file 'seg_05.mp4'\n")
    f.write("file 'seg_06.mp4'\n")

out_course = os.path.join(base_dir, "Avance2_Grupo04_PAVIA.mp4")
cmd_final = [
    ffmpeg, "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", final_list_path,
    "-c", "copy",
    "-movflags", "+faststart",
    out_course
]
run_cmd(cmd_final)

# Copiar a Desktop
out_desktop = r"C:\Users\Brandon\Desktop\Avance2_Grupo04_PAVIA.mp4"
shutil.copy2(out_course, out_desktop)
print("=== VIDEO FINAL RECONSTRUIDO CON ÉXITO ===")
