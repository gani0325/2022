# # Dash와 Python을 사용하여 실시간 업데이트 그래프를 생성
# # https://pythonprogramming.net/live-graphs-data-visualization-application-dash-python-tutorial/ 참고

import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque

X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)

# 임의의 움직임을 추가하여 일부 데이터를 시뮬레이션
app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1*1000
        ),
    ]
)

# 임의의 데이터를 추가
@app.callback(Output('live-graph', 'figure'),
              [Input('graph-update', 'n_intervals')])

def update_graph_scatter(input_data):
    X.append(X[-1]+1)
    Y.append(Y[-1]+Y[-1]*random.uniform(-0.1,0.1))

    # 함수가 실행될 때마다 몇 가지 새로운 데이터를 추가했으므로 계속해서 그래프를 작성하려고 함
    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            )

    # x와 y에 대한 목록을 전달해야 하므로 deque개체를 유지할 수 없음
    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                yaxis=dict(range=[min(Y),max(Y)]),)}

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080 ,debug=True)