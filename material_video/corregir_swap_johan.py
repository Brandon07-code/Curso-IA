import os
import subprocess
import shutil

ffmpeg = r"C:\Users\Brandon\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe"
base_dir = r"C:\Users\Brandon\Desktop\CursoIA\material_video"
temp_dir = os.path.join(base_dir, "temp_segments")
slide_dir = os.path.join(base_dir, "slides")
user_dir = r"C:\Users\Brandon\.gemini\antigravity\brain\67c5e738-f869-450f-bee8-46f8f03497cf\.user_uploaded"

print("--- 1. Asignando Audio CORRECTO a Slide 2 (Objetivos de ML y Perceptrón desde cero) ---")
# Audio 3 de Johan: uploaded_media_2
p2 = os.path.join(user_dir, "uploaded_media_2_1792978100158.ogg")
wav2 = os.path.join(temp_dir, "true_slide2_audio.wav")
subprocess.run([
    ffmpeg, "-y", "-i", p2,
    "-af", "aresample=async=1000:first_pts=0,highpass=f=80,equalizer=f=3000:t=q:w=1.2:g=3,alimiter=limit=0.92",
    "-ar", "48000", "-ac", "2", wav2
], check=True)

slide2 = os.path.join(slide_dir, "slide_02_objetivos.png")
seg2 = os.path.join(temp_dir, "seg_02.mp4")
subprocess.run([
    ffmpeg, "-y", "-loop", "1", "-framerate", "30",
    "-i", slide2, "-i", wav2,
    "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-tune", "stillimage", "-pix_fmt", "yuv420p",
    "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=30",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-shortest",
    seg2
], check=True)

print("--- 2. Asignando Audio CORRECTO a Slide 6 (Próximos Pasos, Scikit-Learn y Clase 12) ---")
# Audio 1 de Johan: uploaded_media_0
p0 = os.path.join(user_dir, "uploaded_media_0_1792978100158.ogg")
wav6 = os.path.join(temp_dir, "true_slide6_audio.wav")
subprocess.run([
    ffmpeg, "-y", "-i", p0,
    "-af", "aresample=async=1000:first_pts=0,highpass=f=80,equalizer=f=3000:t=q:w=1.2:g=3,alimiter=limit=0.92",
    "-ar", "48000", "-ac", "2", wav6
], check=True)

slide6 = os.path.join(slide_dir, "slide_06_proximos_pasos.png")
seg6 = os.path.join(temp_dir, "seg_06.mp4")
subprocess.run([
    ffmpeg, "-y", "-loop", "1", "-framerate", "30",
    "-i", slide6, "-i", wav6,
    "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-tune", "stillimage", "-pix_fmt", "yuv420p",
    "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=30",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-shortest",
    seg6
], check=True)

print("--- 3. Concatenando video final con sincronización y orden 100% perfecto ---")
final_list = os.path.join(temp_dir, "final_video_list.txt")
out_final = r"C:\Users\Brandon\Desktop\PAVIA_Avance2_PERFECTO.mp4"
subprocess.run([
    ffmpeg, "-y", "-f", "concat", "-safe", "0",
    "-i", final_list, "-c", "copy", "-movflags", "+faststart",
    out_final
], check=True)

desktop_final = r"C:\Users\Brandon\Desktop\Avance2_Grupo04_PAVIA.mp4"
shutil.copy2(out_final, desktop_final)
print("=== ¡VIDEO REPARADO CON ÉXITO TOTAL! ===")
