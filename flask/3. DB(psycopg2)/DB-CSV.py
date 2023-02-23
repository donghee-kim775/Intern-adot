import psycopg2 as db
import pandas as pd

# connect를 통해 연결할 주소, 포트, 계정과 비밀번호를 전달한다.
conn = db.connect(host='host', dbname='dbname',user='user',password='password',port='5532')

# 정상적으로 연결되면 데이터를 조작하기 위한 인스턴스를 생성한다.
cursor = conn.cursor()

def insertdata(Date, Open, High, Low, Close, AdjClose, Volume):
    cursor.execute("INSERT INTO tsla(Date, Open, High, Low, Close, AdjClose, Volume) values(%s, %s, %s, %s, %s, %s, %s)", (Date, Open, High, Low, Close, AdjClose, Volume))
    conn.commit()


# CSV 데이터 -> DB : INSERT

# csv파일 경로
Test = pd.read_csv("C:/Users/Galaxy/Desktop/kaggledata/TSLA.csv")

for index, row in Test.iterrows():
    insertdata(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

conn.commit()

# DB -> DataFrame : save

# 데이터 가져오기
ms = pd.read_sql("SELECT * FROM tsla", conn, index_col='date')
