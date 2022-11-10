# 누적값 없애고
# 라이브 그래프 만들기

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import numpy as np

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# Initialize communication with TMP102
def load_file()  :
    # 데이터 로드
    data = pd.read_csv("20220929/test.csv")
    # 단일 변수 선택
    temp = data[["date_time", "test"]]
    # insert_date_time 를 기준으로 집계 합
    uni_temp = data.groupby(["date_time"], as_index=False).sum()
    print(uni_temp)
    return uni_temp

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):
    data = load_file()

    xs = []
    ys = []

    # Add x and y to lists
    #xs.append(data["insert_date_time"])
    #ys.append(data["cnt_slowque"])
    xs = np.array(data["date_time"])
    ys = np.array(data["test"])

    
    # Limit x and y lists to 20 items
    xs = xs[i:i+20]
    ys = ys[i:i+20]

    print(xs)
    print(ys)
    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)
    
    # xs = np.delete(xs, i, axis = 0)
    # ys = np.delete(ys, i, axis = 0)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('live chart')
    plt.ylabel('test')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=100)
plt.show()