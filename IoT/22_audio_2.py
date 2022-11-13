# 녹음 재생하기

import pyaudio      # 오디오 입출력 라이브러리
import wave         # wave 파일 다루기
import sys

CHUNK = 512                     # stream.read 함수를 통해 소리나 음성의 흐름을 읽어올 때 한 번에 읽어올 표본 추출의 개수

if len(sys.argv) < 2 :
    print("Plays a wave file %s filename.wav" % sys.argv[0] )
    sys.exit(-1)

wf = wave.open(sys.argv[1], "rb")

p = pyaudio.PyAudio()           # PyAudio 객체 생성

# 오디오 흐름 연다
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),    
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

data = wf.readframes(CHUNK)

# wf에 대해 readframes 함수를 호출하여 CHUNK 만큼의 데이터 읽기
# 결과 값은 data 변수로 받기
while data :
    stream.write(data)
    data = wf.readframes(CHUNK)

# 오디오 입력 흐름 멈춤
stream.stop_stream()
# 오디오 입력 흐름 닫음
stream.close()
# 녹음 파일 닫기
wf.close()
# pyaudio 객체 동작 종료
p.terminate()