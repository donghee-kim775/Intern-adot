import sys
from flask import Flask, render_template

# Flask 인스턴스 생성
app = Flask(__name__)

#----------------------------------------------

# 웹표현.route()매소드 사용
# 맨 앞에 @붙는 것 : 장식자(decorator)
# flask에서는 이러한 장식자가 URL 연결에 활용된다.
# 장식자를 사용하면 다음 행의 함수부터 장식자가 적용

@app.route("/")
def index():
    return render_template("index.html")
		# render_template : 해당 경로의 template파일을 자동적으로 접근하여 html파일을 불러와줌

@app.route("/user",)
def hello_user():
    return "Hello, User!"

# URL뒤에 <>을 이용해 가변 경로를 적는다
@app.route("/user/<userName>"):
		return "Hello, %s"%(userName)
#-------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True) # 웹앱 실행 요청