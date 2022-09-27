# 대시보드 프로젝트를 진행

"""
 *    Project Name    : Dash board
 *    Description     : serial data monitoring
 *    File Name       : app.py
 *    Author          : https://dschloe.github.io/python/dash/dash_project/ + https://alpaca-gt.tistory.com/307
 *    Note            : serial data Dashboard
 *    Date            : 2022. 09. 26
 *    Change Date     : 2022. 09. 27
"""

# 1. data load
import dash                             # 대시보드 어플리케이션 초기화
import dash_core_components as dcc      # 동적 구성요소들(예: 그래프, 드롭다운 메뉴, 날짜 기간 등) 작성할 수 있도록 도와주는 기능
import dash_html_components as html     # html 태그에 접근
import pandas as pd                     # 데이터 수집 및 가공을 제공할 수 있는 함수 지원
import numpy as np
from dash.dependencies import Output, Input

# step 2. Data Import
data = pd.read_csv("coding/220927/avocado.csv", index_col=0)
# data = data.query("type == 'conventional' and region == 'Albany'")      # type = conventional 과, region = Albany 만 추출하는 행을 추출
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")          
data.sort_values("Date", inplace=True)                                  # 날짜의 오름차순으로 정렬하는 코드
#print(data.info())
#print(data[['region', 'type', 'Date']].head()) 


# step 3. Dash Class
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

# 외부에서 css sheet 갖고오기
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)        # app = dash.Dash(__name__)
app.title = "Avocado Analytics: Understand Your Avocados!"

"""
Dash HTML Components : HTML components용 Wrappers를 제공 => 문단, 제목 또는 목록과 같은 요소를 작성
Dash Core Components : 대화형 사용자 인터페이스를 만들기 위한 Python 추상화를 제공 => 그래프, 슬라이더 또는 드롭다운과 같은 interactive elements를 만드는 데 사용
"""


# step 4. HTML
app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="🥑", className="header-emoji"),
                html.H1(
                    children="Avocado Analytics", className="header-title"
                ),
                html.P(
                    children="Analyze the behavior of avocado prices"
                    " and the number of avocados sold in the US"
                    " between 2015 and 2018",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Region", className="menu-title"),
                        dcc.Dropdown(
                            id="region-filter",
                            options=[
                                {"label": region, "value": region}
                                for region in np.sort(data.region.unique())
                            ],
                            value="Albany",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children="Type", className="menu-title"),
                        dcc.Dropdown(
                            id="type-filter",
                            options=[
                                {"label": avocado_type, "value": avocado_type}
                                for avocado_type in data.type.unique()
                            ],
                            value="organic",
                            clearable=False,
                            searchable=False,
                            className="dropdown",
                        ),
                    ],
                ),
                html.Div(
                    children=[
                        html.Div(
                            children="Date Range",
                            className="menu-title"
                            ),
                        dcc.DatePickerRange(
                            id="date-range",
                            min_date_allowed=data.Date.min().date(),
                            max_date_allowed=data.Date.max().date(),
                            start_date=data.Date.min().date(),
                            end_date=data.Date.max().date(),
                        ),
                    ]
                ),
            ],
            className="menu",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart", config={"displayModeBar": False},
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="volume-chart", config={"displayModeBar": False},
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)


@app.callback(
    [Output("price-chart", "figure"), Output("volume-chart", "figure")],
    [
        Input("region-filter", "value"),
        Input("type-filter", "value"),
        Input("date-range", "start_date"),
        Input("date-range", "end_date"),
    ],
)
def update_charts(region, avocado_type, start_date, end_date):
    mask = (
        (data.region == region)
        & (data.type == avocado_type)
        & (data.Date >= start_date)
        & (data.Date <= end_date)
    )
    filtered_data = data.loc[mask, :]
    price_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["AveragePrice"],
                "type": "lines",
                "hovertemplate": "$%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Average Price of Avocados",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"tickprefix": "$", "fixedrange": True},
            "colorway": ["#17B897"],
        },
    }

    volume_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["Total Volume"],
                "type": "lines",
            },
        ],
        "layout": {
            "title": {"text": "Avocados Sold", "x": 0.05, "xanchor": "left"},
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#E12D39"],
        },
    }
    return price_chart_figure, volume_chart_figure


# step 5. dash board release (localhost)
"""
Flask 기반의 서버로 작동
파라미터 debug=True 를 하게되면, 수정입력을 해도 서버를 restarting 하지 않고 새로고침으로 변화를 확인
"""
if __name__ == "__main__":
    app.run_server(debug=True,host = '127.0.0.1')