# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import pandas as pd


# plt.style.use('seaborn')
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)


# def animation(i):
#   AAPL_STOCK = pd.read_csv('/home/ubuntu/FPDS/20220929/sendinginfo_20220929.csv')
#   AAPL_STOCK = AAPL_STOCK[:20000]
#   x = []
#   y = []

#   x = AAPL_STOCK[0:i]['insert_date_time']
#   y = AAPL_STOCK[0:i]['cnt_mt1']

#   ax.clear()
#   ax.plot(x, y)

# animation = FuncAnimation(fig, func=animation, interval=1)
# plt.show()

# animation.save('animation1.gif', writer='imagemagick', fps=3, dpi=100)


import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd


plt.style.use('seaborn')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)


def animation(i):
    AAPL_STOCK = pd.read_csv('/home/ubuntu/FPDS/20220929/sendinginfo_20220929.csv')
    AAPL_STOCK = AAPL_STOCK[:20000]
    x = []
    y1 = []
    y2 = []

    x = AAPL_STOCK[0:i]['insert_date_time']
    y1 = AAPL_STOCK[0:i]['cnt_mt1']
    y2 = AAPL_STOCK[0:i]['cnt_wait']

    ax.cla()
    ax.plot(x,y1, label='cnt_mt1')
    ax.plot(x,y2, label='cnt_wait')

    plt.legend(loc = 'upper left')
    plt.tight_layout()

animation = FuncAnimation(plt.gcf(), func=animation, interval=100)
plt.show()