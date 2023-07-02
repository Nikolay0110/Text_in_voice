from gtts import gTTS

audio = 'audio.mp3'
language = 'ru'
text = 'Ебаный нахуй, пиздец как жарко на улице, а я поехал заниматься фундаметом. Вечером точно пиво буду пить.'
sp = gTTS(text, lang=language, slow=False)
sp.save(audio)