import speech_recognition as sr

r = sr.Recognizer()
wav = r"C:\Users\Brandon\Desktop\CursoIA\material_video\temp_segments\true_slide6_audio.wav"

slices = [
    (5.5, 2.7),  # "usar la libreria scikit-learn"
    (8.2, 1.4),  # "en la clase 12" ?
    (9.6, 2.0),  # "ahi vamos a probar" ?
    (11.0, 3.0), # "modelos supervisados"
]

for start, dur in slices:
    with sr.AudioFile(wav) as source:
        r.record(source, duration=start)
        audio_slice = r.record(source, duration=dur)
    try:
        t = r.recognize_google(audio_slice, language='es-CO')
        print(f"{start:4.1f}s - {start+dur:4.1f}s: '{t}'")
    except Exception as e:
        print(f"{start:4.1f}s - {start+dur:4.1f}s: (unrecognized)")
