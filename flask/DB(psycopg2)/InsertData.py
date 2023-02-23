import psycopg2 as db

# connect를 통해 연결할 주소, 포트, 계정과 비밀번호를 전달한다.
conn = db.connect(host='host', dbname='dbname',user='user',password='password',port='5532')

# 정상적으로 연결되면 데이터를 조작하기 위한 인스턴스를 생성한다.
cursor = conn.cursor()

# SQL 쿼리만 사용
cursor.execute("INSERT INTO employee(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES('KIM', 'DONGEHEE', 24, 'B', 15);")
conn.commit()

# placeholder 사용
cursor.execute("INSERT INTO employee(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) values(%s, %s, %s, %s, %s);",
	 ('KIM', 'DONGEHEE', 24, 'B', 15))
# 정수인 24를 넣는데 %s를 넣는 이유?
# sql 쿼리문에선 %s는 단순 컬럼값을 대치하는 역할을 하는 아이이니 무조건 %s만 사용한다.
conn.commit()