from gtts import gTTS

audio = 'audio.mp3'
language = 'ru'
text = 'Здесь нужно ввести ваш текст.'
sp = gTTS(text, lang=language, slow=False)
sp.save(audio)
