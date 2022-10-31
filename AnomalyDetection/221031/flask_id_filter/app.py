# # 1) 데이터 id 값 가져오기
# from flask import Flask
# from flask import request
# from flask import render_template

# # MongoDB 연결
# from flask_pymongo import PyMongo
# from pymongo import MongoClient

# app = Flask(__name__)
# # app.config["MONGO_URI"] = "mongodb://localhost:27017/myflask"    # 프로토콜명 // 주소:포트/ DB name

# client = MongoClient("mongodb+srv://gani:hilee5868@cluster0.h7jyl5v.mongodb.net/?retryWrites=true&w=majority")
# # mongo = PyMongo(app)

# # 주소 설정
# @app.route("/write", methods = ["GET", "POST"])


# def board_write() :
#     # method가 POST 인지 GET인지 구분
#     if request.method == "POST" :
#         # Template을 write.html로 보여준다
#         name = request.form.get("name")
#         title = request.form.get("title")
#         contents = request.form.get("contents")

#         # board 라는 컬렉션에 접근 있으면 접근, 없으면 생성
#         # board = mongo.db.board

#         db = client.myflask
        
#         post = {
#             "name" : name,
#             "title" : title,
#             "contents" : contents
#         }

#         data = db.myflask.insert_one(post)
#         # 글작성으로 들어온 데이터에 대한 id값 가져오기 위해 inserted_id 사용
#         return str(data.inserted_id)

#     else :
#         return render_template("write.html")

# if __name__ == "__main__" :
#     app.run(host = "0.0.0.0", debug = True, port = 8000)


# 2) template filter 사용
from flask import Flask
from flask import request
from flask import render_template

# MongoDB 연결
from flask_pymongo import PyMongo
from pymongo import MongoClient
from datetime import datetime
import time 

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/myflask"    # 프로토콜명 // 주소:포트/ DB name

client = MongoClient("mongodb+srv://gani:hilee5868@cluster0.h7jyl5v.mongodb.net/?retryWrites=true&w=majority")
# mongo = PyMongo(app)

# 주소 설정
@app.route("/write", methods = ["GET", "POST"])

def board_write() :
    # method가 POST 인지 GET인지 구분
    if request.method == "POST" :
        # Template을 write.html로 보여준다
        name = request.form.get("name")
        title = request.form.get("title")
        contents = request.form.get("contents")
        
        # timestape는 밀리세컨드로 값 반환. 초로 변환하기 위해 1000 곱하기
        # 소수점이 나오는 걸 방지하기 위해 round 반환
        current_utc_time = round(datetime.utcnow().timestamp() * 1000)

        # board 라는 컬렉션에 접근 있으면 접근, 없으면 생성
        # board = mongo.db.board
        db = client.myflask

        post = {
            "name" : name,
            "title" : title,
            "contents" : contents,
            "pubdate" : current_utc_time,
            "view" : 0
        }

        data = db.myflask.insert_one(post)
        # 글작성으로 들어온 데이터에 대한 id값 가져오기 위해 inserted_id 사용
        return str(data.inserted_id)

    else :
        return render_template("write.html")


# html 에서 함수처럼 사용하기 위해 templat_filter 사용
@app.template_filter("format_time")
def format_time(value) :
    if value is None :
        return ""

    # 클라이언트 현재 시간
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    value = datetime.fromtimestamp((int(value) / 1000) + offset)
    return value.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__" :
    app.run(host = "0.0.0.0", debug = True, port = 8000)