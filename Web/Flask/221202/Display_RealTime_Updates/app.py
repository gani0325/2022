from flask import Flask, render_template, request
from flask_socketio import SocketIO
from random import random
from threading import Lock
from datetime import datetime
import pandas as pd

"""
Background Thread
"""
thread = None
thread_lock = Lock()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gani!'
socketio = SocketIO(app, cors_allowed_origins='*')

"""
Get current date time
"""
def get_current_datetime(years):
    #now = datetime.now()
    return years.strftime("%m-%d-%Y %H:%M:%S")

"""
Generate random sequence of dummy sensor values and send it to our clients
"""

CNT_WAIT = []
YEARS = []
def data_load() :
    data = pd.read_csv('./data/test.csv')
    
    for i in range(len(data)) :
        CNT_WAIT.append(int(data["cnt_wait"][i]))
        YEARS.append(data["insert_date_time"][i])

    return CNT_WAIT, YEARS

def background_thread():
    print("Generating random sensor values")
    CNT_WAIT_data, YEARS_data = data_load()
    #YEARS_data = get_current_datetime(YEARS_data)
    cnt = 0
    while True:
        # 랜덤 상수를 value : 옆에 넣으면 랜덤 그래프 완성
        # dummy_sensor_value = round(random() * 100, 3)
        print(CNT_WAIT_data[cnt])
        print(YEARS_data[cnt])
        # print(dummy_sensor_value)
        
        socketio.emit('updateSensorData', {'value': CNT_WAIT_data[cnt], "date": YEARS_data[cnt]})
        cnt += 1
        socketio.sleep(1)


"""
Serve root index file
"""
@app.route('/')
def index():
    return render_template('index.html')

"""
Decorator for connect
"""
@socketio.on('connect')
def connect():
    global thread
    print('Client connected')

    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)

"""
Decorator for disconnect
"""
@socketio.on('disconnect')
def disconnect():
    print('Client disconnected',  request.sid)

if __name__ == '__main__':
    socketio.run(app)