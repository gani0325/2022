# # 대시보드 프로젝트를 진행

# """
#  *    Project Name    : Dash board
#  *    Description     : serial data monitoring
#  *    File Name       : Python Dash board with Heroku.py
#  *    Author          : Black Logic
#  *    Note            : Real time Dashboard
#  *    Date            : 2022. 09. 26
#  *    Change Date     :
# """

# # 1. data load
# import dash                             # 대시보드 어플리케이션 초기화
# import dash_core_components as dcc      # 동적 구성요소들(예: 그래프, 드롭다운 메뉴, 날짜 기간 등) 작성할 수 있도록 도와주는 기능
# import dash_html_components as html     # html 태그에 접근
# import pandas as pd                     # 데이터 수집 및 가공을 제공할 수 있는 함수 지원

# # step 2. Data Import
# data = pd.read_csv("avocado.csv", index_col=0)
# data = data.query("type == 'conventional' and region == 'Albany'")      # type = conventional 과, region = Albany 만 추출하는 행을 추출
# data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")          
# data.sort_values("Date", inplace=True)                                  # 날짜의 오름차순으로 정렬하는 코드

# # step 3. Dash Class
# app = dash.Dash(__name__)

# """
# Dash HTML Components : HTML components용 Wrappers를 제공 => 문단, 제목 또는 목록과 같은 요소를 작성
# Dash Core Components : 대화형 사용자 인터페이스를 만들기 위한 Python 추상화를 제공 => 그래프, 슬라이더 또는 드롭다운과 같은 interactive elements를 만드는 데 사용
# """


# # step 4. HTML
# app.layout = html.Div(                              # 일종의 parent component
# 	  # Header Message
#     children=[
#         html.H1(children="Temp Analytics",),        # html.h1은 h1 태그, html.p은 p 태그
#         html.P(
#             children="Temp",
#         ),
#         # 그래프		
#         dcc.Graph(                                  # 그래프가 구현되는 코드
#             figure={
#                 "data": [
#                     {
#                         "x": data["Date"],
#                         "y": data["AveragePrice"],
#                         "type": "lines",
#                     },
#                 ],
#                 "layout": {"title": "Title_1"},
#             },
#         ),
#         dcc.Graph(                                  # 그래프가 구현되는 코드
#             figure={
#                 "data": [
#                     {
#                         "x": data["Date"],
#                         "y": data["Total Volume"],
#                         "type": "lines",
#                     },
#                 ],
#                 "layout": {"title": "Title_2"},
#             },
#         ),
#     ]
# )



# # step 5. dash board release (localhost)
# """
# Flask 기반의 서버로 작동
# 파라미터 debug=True 를 하게되면, 수정입력을 해도 서버를 restarting 하지 않고 새로고침으로 변화를 확인
# """
# if __name__ == "__main__":
#     app.run_server(debug=True)
    


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)