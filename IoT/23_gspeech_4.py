# 음성을 듣고 응답하는 LED 제어 프로그램

from gtts import gTTS
import os

# 불을 켜겠습니다 음성을 저장할 led_on.mp3 만들고 재생
led_on = gTTS(text =u "불을 켭니다.", lang = "ko")
led_on.save("led_on.mp3")
os.system("mpg321 led_on.mp3")

# 불을 끄겠습니다 음성을 저장할 led_off.mp3 만들고 재생
led_off = gTTS(text =u "불을 끕니다.", lang = "ko")
led_off.save("led_off.mp3")
os.system("mpg321 led_off.mp3")