# gtts 라이브러리를 이용하여 한글을 한국어 음성으로 변환

import os
from google.cloud import speech
from gtts import gTTS       # google text to speech의 약자 -> 구글에서 제공하는 문자음성 변환 모듈
from micstream import MicrophoneStream

os.ENVIRON[ "GOOGLE_APPLICATION_CREDENTIALS" ] = \
    "gc-speech.json"

# Audio recording parameters
RATE = 44100                # 초당 추출할 소리의 개수
CHUNK = int(RATE / 10)      # 100ms, 한번에 얻어올 소리의 개수

# 음성으로 변환할 문자열 받기
def do_TTS(text) :
    tts = gTTS(text = text, lang = "ko")
    a = os.path.exists("read.mp3")
    if a :
        os.remove("read.mp3")
    # 문자열을 음성 파일로 저장
    tts.save("read.mp3")
    # mpg321 프로그램은 mp3 파일 재생 프로그램
    os.system("mpg321 read.mp3")

def listen_print_loop(responses) :
    # 응답한 결과 값들의 각 응답에서 적당한 문자열을 찾아 출력
    for response in responses :
        result = response.results[0]
        transcript = result.alternatives[0].transcript
        # 변환된 문자열을 음성 파일로 저장
        print(transcript)

        if '종료' in transcript or '그만' in transcript :
            print("종료합니다...")
            break

language_code = "ko-KR"

clinet = speech.SpeechClinet()
config = speech.RecognitionConfig(
    encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz = RATE,
    language_code = language_code)

streaming_config = speech.StreamingRecognitionConfig(config = config)

with MicrophoneStream(RATE, CHUNK) as stream :
    audio_generator = stream.generate()
    requests = (speech.StreamingRecognizeRequest(auio_content = content)
                for content in audio_generator)
    responsese = clinet.streaming_recognize(streaming_config, requests)

    listen_print_loop(responsese)