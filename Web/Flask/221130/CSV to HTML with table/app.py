
# importing flask
from flask import Flask, render_template
  
# importing pandas module
import pandas as pd
  
# flask 객체를 app 에 할당
app = Flask(__name__)
  
  
# reading the data in the csv file
df = pd.read_csv('test.csv')
df.to_csv('sample_testdata.csv', index=None)
  
  
# route to html page - "table"
# 해당 라우팅 경로로 요청이 왔을 때 실행할 함수를 바로 밑에 작성함
@app.route('/')
@app.route('/table')
def table():
    # converting csv to html
    data = pd.read_csv('test.csv')
    return render_template('table.html', tables=[data.to_html()], titles=[''])
  
# 플라스크 서버 구동 (서버로 구동한 IP 와 포트를 옵션으로 넣어줌)
if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))