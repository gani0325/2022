import json
import random
import time
from datetime import datetime
import pandas as pd

from flask import Flask, Response, render_template, stream_with_context

app = Flask(__name__)
random.seed()  # Initialize the random number generator


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chart-data')
def chart_data():
    def generate_random_data():

        uni_temp = []

        # 데이터 로드
        data = pd.read_csv("./data/test.csv")
    
        for i in range(1, len(data)) :
            uni_temp.append(data["cnt_wait"][i])
        print(uni_temp)
        while True:
            json_data = json.dumps(
                {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': uni_temp})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    response = Response(stream_with_context(generate_random_data()), mimetype="text/event-stream")
    # 브라우저 및 공유 캐시(예: 프록시, CDN)의 캐싱 을 제어하는 ​​요청 및 응답 모두에서 지시문 (명령)을 포함
    response.headers["Cache-Control"] = "no-cache"
    # 응답 헤더 정보 및 사용 통계.
    response.headers["X-Accel-Buffering"] = "no"
    return response


if __name__ == '__main__':
    app.run(debug=True, threaded=True)

