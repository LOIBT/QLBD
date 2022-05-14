# from flask import Flask 
# import cx_Oracle

# app = Flask(__name__) 
# @app.route('/') 
# def index(): 
#     try: 
#         con = cx_Oracle.connect('hr', 'hr', 'localhost:1521/orcl') 

#         cursor = con.cursor() 
#         cursor.execute("insert into seminar1.SKILL values (13,'Testing13',null)")
#         con.commit() 
      
#         return '<h1>SUCCESS!</h1>'
#     except cx_Oracle.DatabaseError as e: 
#         return '<h1>There is a problem with Oracle</h1>'
#     finally: 
#         if cursor: 
#             cursor.close() 
#         if con: 
#             con.close() 


import cx_Oracle

#create connection
conn = cx_Oracle.connect('hr/hr@//localhost:1521/orcl')
print(conn.version)

#create cursor 
cur =conn.cursor()

sql_create = """
CREATE TABLE ABC (
    FIRST_NAME11 VARCHAR2(50),
    LAST_NAME11 VARCHAR2(50),
    COMPANY11 VARCHAR2(50),
    AGE11 NUMBER
)
"""

cur.execute(sql_create)
print('Table Created.')