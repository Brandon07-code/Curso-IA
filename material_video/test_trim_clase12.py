import wave
import struct
import math
import speech_recognition as sr

wav_in = r"C:\Users\Brandon\Desktop\CursoIA\material_video\temp_segments\true_slide6_audio.wav"
wav_out = r"C:\Users\Brandon\Desktop\CursoIA\material_video\temp_segments\slide6_audio_no_clase12.wav"

with wave.open(wav_in, 'rb') as w:
    params = w.getparams()
    framerate = w.getframerate()
    frames = w.readframes(w.getnframes())
    samples = list(struct.unpack(f"<{len(frames)//2}h", frames))

print(f"Total samples: {len(samples)} ({len(samples)/(framerate*2):.2f}s)")

# 1. Quitar 'en la clase 12': desde 8.15s hasta 9.58s
cut_start = int(8.15 * framerate) * 2
cut_end = int(9.58 * framerate) * 2
crossfade_len = int(0.015 * framerate) * 2  # 15ms crossfade

# Aplicar crossfade suave entre cut_start y cut_end
part1 = samples[:cut_start]
part2 = samples[cut_end:]

# Mezclar los bordes para cero chasquido
for i in range(crossfade_len):
    w1 = 1.0 - (i / crossfade_len)
    w2 = i / crossfade_len
    idx1 = len(part1) - crossfade_len + i
    idx2 = i
    mixed = int(part1[idx1] * w1 + part2[idx2] * w2)
    part1[idx1] = mixed

new_samples = part1 + part2[crossfade_len:]

# 2. Reparar todos los pips y saturaciones en new_samples
# Cualquier sample >= 32000 o salto violento delta > 25000 se suaviza
fixed_pips = 0
for i in range(10, len(new_samples) - 10):
    val = new_samples[i]
    delta = abs(new_samples[i] - new_samples[i-1])
    if abs(val) >= 31000 or (delta > 26000 and abs(val) > 20000):
        # Promediar con muestras antes y después
        avg = (new_samples[i-10] + new_samples[i+10]) // 2
        new_samples[i] = avg
        fixed_pips += 1

print(f"Pips y saturaciones reparadas: {fixed_pips}")

with wave.open(wav_out, 'wb') as w:
    w.setparams((params[0], params[1], params[2], len(new_samples)//2, params[4], params[5]))
    w.writeframes(struct.pack(f"<{len(new_samples)}h", *new_samples))

print(f"Nuevo audio guardado: {len(new_samples)/(framerate*2):.2f}s")

# Verificar transcripción de los primeros 15 segundos
r = sr.Recognizer()
with sr.AudioFile(wav_out) as source:
    audio_check = r.record(source, duration=15.0)
try:
    text = r.recognize_google(audio_check, language='es-CO')
    print("TRANSCRIPCIÓN DE LOS PRIMEROS 15 SEGUNDOS:")
    print(f"'{text}'")
except Exception as e:
    print("Error transcribiendo:", e)
