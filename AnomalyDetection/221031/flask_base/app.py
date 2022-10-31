from django.shortcuts import render
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


# 주소 설정
@app.route("/write", methods = ["GET", "POST"])

def board_write() :
    # method가 POST 인지 GET인지 구분
    if request.method == "POST" :
        # Template을 write.html로 보여준다
        name = request.form.get("name")
        title = request.form.get("title")
        contents = request.form.get("contents")
    else :
        return render_template("write.html")

if __name__ == "__main__" :
    app.run(host = "0.0.0.0", debug = True, port = 8000)
