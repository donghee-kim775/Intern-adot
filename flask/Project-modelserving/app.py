from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import tensorflow as tf
import numpy as np
import pandas as pd
import psycopg2 as db

app = Flask(__name__)


# connect를 통해 연결할 주소, 포트, 계정과 비밀번호를 전달한다.
conn = db.connect(host='host', dbname='dbname',user='user',password='password',port='5532')

# 데이터 가져오기
cursor = conn.cursor()

# 데이터 가져오기
data = pd.read_sql("SELECT * FROM tsla", conn, index_col='date')

@app.route('/file_upload', methods=['GET','POST'])
def file_upload():
    if request.method == 'POST'
        data = request.files['file2'].read()
        return data

@app.route("/model", methods=['POST'])
def model(data):
    if request.method == 'POST':
        # 최고가와 최저가의 중간가격으로 예측하기 위한 설정
        high_prices = data['High'].values
        low_prices = data['Low'].values
        mid_prices = (high_prices + low_prices) / 2

        # window size
        seq_len = 50

        # 50개보고 1개 예측
        sequence_length = seq_len + 1

        result = []

        for index in range(len(mid_prices) - sequence_length):
            result.append(mid_prices[index: index + sequence_length])

        # 정규화
        normalized_data = []

        for window in result:
            normalized_window = [((float(p) / float(window[0])) - 1) for p in window]
            normalized_data.append(normalized_window)

        result = np.array(normalized_data)

        model = tf.keras.models.load_model('lstmstock.h5')
        prediction = model.predict(result)
        y_preds = prediction.tolist()
        days = list(range(1,len(y_preds)+1))
        return render_template('prediction', days=days, y_preds=y_preds)

        
if __name__ == '__main__':
    app.run(port="9999", debug = True)