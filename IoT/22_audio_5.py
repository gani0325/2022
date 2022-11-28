# MicrophoneStream 클래스 이용해 음성 녹음 수행

import pyaudio      # 오디오 입출력 라이브러리
import wave         # wave 파일 다루기

from micstream import MicrophoneStream

SAMPLE_RATE = 44100                 # 흘러나오는 소리나 음성에 대해 초당 표본 추출할 횟수 (1초당 음성을 n번 추출)
FORMAT = pyaudio.paInt16            # 표본 추출 1개의결과를 저장할 데이터 크기 (표본 추출 1개에 대해 16비트 정수로 저장)
CHANNELS = 1                        # 표본 추출할 소리나 음성의 흐름 개수 (1 이면 Mono, 2 이면 Stereo)
CHUNK = int(SAMPLE_RATE / 10)       # stream.read 함수를 통해 소리나 음성의 흐름을 읽어올 때 한 번에 읽어올 표본 추출의 개수
WAVE_OUTPUUT_FILENAME = "output_3.wav"        # 음성 녹음 저장할 파일의 이름

p = pyaudio.PyAudio()           # PyAudio 객체 생성

wf = wave.open(WAVE_OUTPUUT_FILENAME, "wb")     # 이진 파일 쓰기로 연다
wf.setnchannels(CHANNELS)                       # 녹음 파일의 채널 개수
wf.setsampwidth(p.get_sample_size(FORMAT))      # 녹음 파일의 오디오 데이터 하나의 크기
wf.setframerate(SAMPLE_RATE)                    # 녹음 파일의 1초당 표본 추출된 오디오 데이터의 개수

try :
    # 파일 입출력, 소켓 통신, 메시지 큐 통신 등을 할 때 할당받은 내부 자원을 자동으로 해제하기 위해 사용
    # __enter__ 함수에서 파일 입출력, 소켓 통신, 메시지 큐 통신 등을 위한 자원 할당
    # __exit__ 함수에서 파일 입출력, 소켓 통신, 메시지 큐 통신 등을 위해 할당받은 자원을 해제
    with MicrophoneStream(SAMPLE_RATE, CHUNK) as stream :
        audio_generator = stream.generate()
        # audio_generator가 생성하는 값을 content로 받아 녹음 파일에 저장
        for content in audio_generator :
            wf.writeframes(content)

except : pass

# 녹음 파일 닫기
wf.close()                                      
p.terminate()