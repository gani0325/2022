# Callback Mode를 이용하여 녹음한 파일 재생

import pyaudio      # 오디오 입출력 라이브러리
import wave         # wave 파일 다루기
import time
import sys

CHUNK = 512                     # stream.read 함수를 통해 소리나 음성의 흐름을 읽어올 때 한 번에 읽어올 표본 추출의 개수

if len(sys.argv) < 2 :
    print("Plays a wave file. %s filename.wav" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')

p = pyaudio.PyAudio()           # PyAudio 객체 생성

# callback 함수 정의
# 소리나 음성 입력을 받아 처리하는 함수 -> 소리의 입력이 있을 때 callback 함수로 호출해달라고 등록
# 바이트 단위의 데이터 크기, 출력 데이터에 대한 시간 정보, 출력 데이터에 대한 상태 정보
def callback(in_date, frame_count, time_info, status) :
    # 출력 데이터를 frame_count 만큼 wave 파일에서 읽어 내 output_data에 할당
    output_data = wf.readframes(frame_count)
    # OS로 전달되어 스피커로 출력, 오디오 출력이 더 있다는 의미
    return (output_data, pyaudio.paContinue)

# 오디오 흐름 연다
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),    
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True,
                stream_callback = callback)     # 오디오 입력을 계속 받겠다

# 오디오 출력 시작
stream.start_stream()

# 5초간 오디오 입력 받기
# 오디오 입력이 활성화 상태이면 0.1 초 동안 대기
while stream.is_active() :
    time.sleep(0.1)

# 오디오 입력 흐름 멈춤
stream.stop_stream()
# 오디오 입력 흐름 닫음
stream.close()
# 녹음 파일 닫기
wf.close()                                      
p.terminate()