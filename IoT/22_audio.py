# 음성녹음 하고 재생하기

import pyaudio      # 오디오 입출력 라이브러리
import wave         # wave 파일 다루기

SAMPLE_RATE = 44100             # 흘러나오는 소리나 음성에 대해 초당 표본 추출할 횟수 (1초당 음성을 n번 추출)
FORMAT = pyaudio.paInt16        # 표본 추출 1개의결과를 저장할 데이터 크기 (표본 추출 1개에 대해 16비트 정수로 저장)
CHANNELS = 1                    # 표본 추출할 소리나 음성의 흐름 개수 (1 이면 Mono, 2 이면 Stereo)
CHUNK = 512                     # stream.read 함수를 통해 소리나 음성의 흐름을 읽어올 때 한 번에 읽어올 표본 추출의 개수
RECORD_SECOND = 5               # 음성 녹음 시간
WAVE_OUTPUUT_FILENAME = "output.wav"        # 음성 녹음 저장할 파일의 이름

p = pyaudio.PyAudio()           # PyAudio 객체 생성

# 오디오 흐름 연다
stream = p.open(format = FORMAT,    
                channels = CHANNELS,
                rate = SAMPLE_RATE,
                input = True,
                frames_per_buffer = CHUNK)

# 음성 녹음 시작
print("Start to record the audio")

# 입력 받은 음성 저장할 빈 목록 생성
frames = []

# 음성 데이터응 읽음
for i in range(0, int(SAMPLE_RATE / CHUNK * RECORD_SECOND)) :
    data = stream.read(CHUNK)
    frames.append(data)

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