# 1. 한 개 변수 그래프
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pandas.core.indexes import interval
 

def load_file(data)  :
    # Load the data
    # data = pd.read_csv("FPDS/20220929/sendinginfo_20220929.csv")

    df = pd.concat([data['insert_date_time'][:20000], data['cnt_mt1'][:20000]], axis = 1)
    print(df)
    # df = df.set_index("insert_date_time")
    # df['cnt_wait'].plot(figsize = (12, 4), grid = True)
    return df

fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(-10, 500))
line, = ax.plot([], [], lw=3)

 
def animate(i):
    temp = pd.read_csv("/home/ubuntu/FPDS/20220929/sendinginfo_20220929.csv")
    data = load_file(temp)
    print(data.columns)
    # data =pd.read_csv('data4.csv')
    x = data['insert_date_time']
    y1 = data['cnt_mt1']
    # y2 = data['total_2']
 
    plt.cla()
    plt.plot(x,y1, label='insert_date_time')
    # plt.plot(x,y2,label='유튜브')
    
    # plt.legend(loc = 'upper left')
    # plt.tight_layout()
    line.set_data(x, y1)    
    
    return line,
 
# ani = FuncAnimation(plt.gcf(), animate, interval = 10)
ani = FuncAnimation(fig, animate, interval = 10)
# anim = FuncAnimation(fig, animate, frames=200, interval=50)
# (Figure 객체, 프레임마다 반복해서 호출할 함수, 반복 가능한 객체를 입력, 프레임 간격)
 
plt.tight_layout()
plt.show()


# gif 저장하기
#graph_ani.save('graph_ani.gif', writer='imagemagick', fps=3, dpi=100)