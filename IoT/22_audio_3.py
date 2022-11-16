# Callback Mode를 이용하여 5초간 음성 데이터 받아서 파일로 저장

import pyaudio      # 오디오 입출력 라이브러리
import wave         # wave 파일 다루기
import time

SAMPLE_RATE = 44100             # 흘러나오는 소리나 음성에 대해 초당 표본 추출할 횟수 (1초당 음성을 n번 추출)
FORMAT = pyaudio.paInt16        # 표본 추출 1개의결과를 저장할 데이터 크기 (표본 추출 1개에 대해 16비트 정수로 저장)
CHANNELS = 1                    # 표본 추출할 소리나 음성의 흐름 개수 (1 이면 Mono, 2 이면 Stereo)
CHUNK = 512                     # stream.read 함수를 통해 소리나 음성의 흐름을 읽어올 때 한 번에 읽어올 표본 추출의 개수
RECORD_SECOND = 5               # 음성 녹음 시간
WAVE_OUTPUUT_FILENAME = "output.wav"        # 음성 녹음 저장할 파일의 이름

p = pyaudio.PyAudio()           # PyAudio 객체 생성

# 입력 받은 음성 저장할 빈 목록 생성
frames = []

# callback 함수 정의
# 소리나 음성 입력을 받아 처리하는 함수 -> 소리의 입력이 있을 때 callback 함수로 호출해달라고 등록
def callback(in_date, frame_count, time_info, status) :
    frames.append(in_data)
    return (None, pyaudio.paContinue)

# 오디오 흐름 연다
stream = p.open(format = FORMAT,    
                channels = CHANNELS,
                rate = SAMPLE_RATE,
                input = True,
                frames_per_buffer = CHUNK,
                stream_callback = callback)     # 오디오 입력을 계속 받겠다

# 음성 녹음 시작
print("Start to record the audio")

# 오디오 입력 시작
stream.start_stream()

cnt = 0

# 5초간 오디오 입력 받기
# 오디오 입력이 활성화 상태이면 0.1 초 동안 대기, cnt 값 증가, cnt가 RECORD_SECOND * 10 보다 크면 while 빠지기
while stream.is_active() :
    time.sleep(0.1)
    cnt += 1
    if cnt > RECORD_SECOND * 10 :
        break

# 음성 녹음 끝
print("Recording is finished")

# 오디오 입력 흐름 멈춤
stream.stop_stream()
# 오디오 입력 흐름 닫음
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUUT_FILENAME, "wb")     # 이진 파일 쓰기로 연다
wf.setnchannels(CHANNELS)                       # 녹음 파일의 채널 개수
wf.setsampwidth(p.get_sample_size(FORMAT))      # 녹음 파일의 오디오 데이터 하나의 크기
wf.setframerate(SAMPLE_RATE)                    # 녹음 파일의 1초당 표본 추출된 오디오 데이터의 개수
wf.writeframes(b''.join(frames))                # 입력받은 음성 데이터 붙이기
wf.close()                                      # 녹음 파일 닫기