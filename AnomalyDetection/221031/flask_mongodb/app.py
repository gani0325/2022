from flask import Flask
from flask import request
from flask import render_template

# MongoDB 연결
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/myflask"    # 프로토콜명 // 주소:포트/ DB name

client = MongoClient("mongodb+srv://gani:hilee5868@cluster0.h7jyl5v.mongodb.net/?retryWrites=true&w=majority")
# mongo = PyMongo(app)

# 주소 설정
@app.route("/write", methods = ["GET", "POST"])
db = client.myflask

def board_write() :
    # method가 POST 인지 GET인지 구분
    if request.method == "POST" :
        # Template을 write.html로 보여준다
        name = request.form.get("name")
        title = request.form.get("title")
        contents = request.form.get("contents")

        # board 라는 컬렉션에 접근 있으면 접근, 없으면 생성
        # board = mongo.db.board

        # board = mongo.db.board
        post = {
            "name" : name,
            "title" : title,
            "contents" : contents
        }

        db.myflask.insert_one(post)

    else :
        return render_template("write.html")

if __name__ == "__main__" :
    app.run(host = "0.0.0.0", debug = True, port = 8000)



# from flask import Flask, request
# from flask import render_template
# from flask_pymongo import PyMongo
# from pymongo import MongoClient

# app = Flask(__name__)

# mongo = PyMongo()

# client = MongoClient('mongodb://localhost', 27017)   # 로컬환경에서 mongo db 연결
# # client = MongoClient('mongodb://test:test@localhost', 27017)    # db 인증 계정 생성 후 연결 방법

# # neuruWeb = 스키마 이름을 느루웹으로 만듬
# db = client.neuruWeb

# @app.route('/')
# def home():
#     return 'This is home!'


# # db write 부분 write.html에서 post로 보낸 데이터 받아서 db에 저장
# @app.route('/write', methods=["GET", "POST"])
# def board_write():
#    if request.method == "POST":
#       name = request.form.get("name")
#       title = request.form.get("title")
#       contents = request.form.get("contents")
#       print(name, title, contents)
        
#       doc = {
#          "name": name,
#          "title": title,
#          "contents": contents,
#         }
#     # db = neuru web 이라는 스키마임, 스키마 아래에 board라는 컬랙션을 생성후 데이터를 넣음
#       db.board.insert_one(doc)

#       return render_template("write.html")
#    else:
#       return render_template("write.html")


# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)