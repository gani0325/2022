import pandas_datareader.data as web
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html

# 데이터를 가져오려는 소스, 시작 날짜/시간, 종료 날짜/시간을 지정
# 반환은 Pandas 데이터 프레임
stock = 'TSLA'

start = datetime.datetime(2015, 1, 1, 0, 0)
end = datetime.datetime.now()
df = web.DataReader(stock, 'yahoo', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)

#print(df.info())

app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='정적 그래프!'),

    html.Div(children='''
        테슬라 주식 그래프를 만들어보자!!.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.Close, 'type': 'line', 'name': stock},
            ],
            'layout': {
                'title': stock
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8090 ,debug=True)