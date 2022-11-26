# MicrophoneStream 클래스 구현하기
# Callback Mode를 이용하여 마이크로부터 음성을 받아보기

import pyaudio
from six.moves import queue

class MicrophoneStream(object) :
    def __init__(self, rate, chunk) :
        self._rate = rate
        self._chunk = chunk
        self.buff = queue.Queue()
        self.closed = True
    
    def __enter__(self) :
        # 오디오 입력 흐름 열기
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            # 표본 추출 데이터 1개에 대한 데이터 크기
            format = pyaudio.paInt16
            # 표본 추출할 녹음 채널의 개수
            channels = 1,
            # 초당 표본 추출할 녹음 데이터 개수
            rate = self._rate,
            # 입력 스트림 여부
            input = True,
            # 콜백 함수를 통해 톨올 콜백 함수를 등록
            frames_per_buffer = self._chunk,
            stream_callback = self._fill_buffer,
        )
        # 오디오 흐름의 닫힘 여부 알려줌
        self.closed = False
        return self
    
    def __exit__(self, type, value, traceback) :
        # 오디오 입력 흐름 멈추기
        self._audio_stream.stop_stream()
        # 오디오 입력 흐름 닫기
        self._audio_stream.close()
        self.closed = True
        # 큐 비우기
        self._buff.put(None)
        self._audio_interface.terminate()


    # 녹음 입력 받는 함수
    def _fill_buffer(self, in_data, frame_count, time_info, status_flags) :
        self._buffer.put(in_data)
        return None, pyaudio.paContinue

    # generate는 for문과 함께 사용, 내부적으로 yield 문을 통해 값을 무한정 제공
    def generate(self) :
        while not self.closed() :
            chunk = self._buff.get()
            if chunk is None :
                return
            data = [chunk]

            while True :
                try :
                    chunk = self._buff.get(block = False)
                    if chunk is None :
                        return
                    data.append(chunk)
                except queue.Empty() :
                    break
            yield b''.join(data)
            