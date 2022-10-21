# 2. 두개 변수 그래프
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pandas.core.indexes import interval

fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(-10, 500))
line, = ax.plot([], [], lw=3)

 
def animate(i):
    data = pd.read_csv("/home/ubuntu/FPDS/20220929/sendinginfo_20220929.csv")
    #data = load_file(temp)
    data = data[:30000]
    print(data.columns)
    # data =pd.read_csv('data4.csv')
    x = data['insert_date_time']
    y1 = data['cnt_mt1']
    y2 = data['cnt_wait']
 
    plt.cla()
    plt.plot(x,y1, label='cnt_mt1')
    plt.plot(x,y2,label='cnt_wait')
    
    plt.legend(loc = 'upper left')
    plt.tight_layout()
    line.set_data(x, y1)    
    
    return line,
 
# ani = FuncAnimation(plt.gcf(), animate, interval = 10)
ani = FuncAnimation(plt.gcf(), animate, interval = 100)
# (Figure 객체, 프레임마다 반복해서 호출할 함수, 반복 가능한 객체를 입력, 프레임 간격)
 
plt.tight_layout()
plt.show()