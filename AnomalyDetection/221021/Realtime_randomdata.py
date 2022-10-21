# random 데이터
import random                       # 무작위의 수를 생성
from itertools import count         # 1,2,3... 순차적인 수를 생성
import pandas as pd

# animation 효과, 실시간 데이터 반영
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
plt.style.use('fivethirtyeight')
 
x_val = []
y_val = []
 
index = count()
 
def animate(i):
    x_val.append(next(index))                   # 순차적인 수를 생성
    y_val.append(random.randint(0,5))           # 0~5 사이의 랜덤한 정수를 생성
    plt.cla()                                   # 앞선 그래프를 삭제
    plt.plot(x_val, y_val)
 
ani = FuncAnimation(plt.gcf(), animate, interval = 1000)
# plt.gcf() : 현재 그래프 모양을 가져오기
# animate : 애니메이션 효과를 적용
# interval : 1000 -> 1000 밀리초 마다 적용
 
 
plt.tight_layout()          # 자동으로 명시된 여백에 관련된 서브플롯 파라미터 조정
plt.show()