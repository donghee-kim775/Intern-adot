import psycopg2 as db

# connect를 통해 연결할 주소, 포트, 계정과 비밀번호를 전달한다.
conn = db.connect(host='host', dbname='dbname',user='user',password='password',port='5532')

# 정상적으로 연결되면 데이터를 조작하기 위한 인스턴스를 생성한다.
cursor = conn.cursor()

# 테이블 생성하는 CREATE쿼리문을 작성한다.
sql ='''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
	 INCOME float
)'''

# PostgreSQL에서 SQL 명령을 실행하기 위해 execute함수를 사용한다.
cursor.execute(sql)

# 쿼리를 PostgreSQL에 전달하여 실행
conn.commit()