# 한국어 음성을 듣고 구글 speech 라이브러리를 이용하여 문자열로 변환하기

import os
from google.cloud import speech
from micstream import MicrophoneStream

os.ENVIRON[ "GOOGLE_APPLICATION_CREDENTIALS" ] = \
    "gc-speech.json"

# Audio recording parameters
RATE = 44100                # 초당 추출할 소리의 개수
CHUNK = int(RATE / 10)      # 100ms, 한번에 얻어올 소리의 개수

# 구글 클라우드에서 얻어온 음성 인식 결과를 문자열로 출력
def listen_print_loop(responses) :
    # 응답한 결과 값들의 각 응답에서 적당한 문자열을 찾아 출력
    for response in responses :
        result = response.results[0]
        transcript = result.alternatives[0].transcript

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
