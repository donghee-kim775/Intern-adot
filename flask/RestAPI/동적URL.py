from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Hello, World!'

@app.route('/user/<user_name>/<int:user_id>')
def user(user_name, user_id):
    return f'Hello, {user_name}({user_id})!'
# 반환 값을 f'' -> f-string 포맷을 활용해서 문자열에 변수를 넣음

if __name__ == '__main__':
    app.run(debug=True)