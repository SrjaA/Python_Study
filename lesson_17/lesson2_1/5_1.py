import pyttsx3

engine = pyttsx3.init()     # инициализация движка
# зададим свойства
engine.setProperty('rate', 150)     # скорость речи
engine.setProperty('volume', 0.9)   # громкость (0-1)

en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"

# Use female English voice
engine.setProperty('voice', en_voice_id)
engine.say('Run,baby,run')

# Use female Russian voice
#engine.setProperty('voice', ru_voice_id)
#engine.say('Михалыч, погнали!')

# очистка очереди и воспроизведение текста
engine.runAndWait()

# выполнение кода останавливается, пока весь текст не сказан