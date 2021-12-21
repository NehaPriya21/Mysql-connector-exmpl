#Author Priya
import mysql.connector


nehapriya=mysql.connector.connect(host='localhost',user='guest',database='NSIT',password='guest123')

Sno = raw_input("Sno")

sql_delete_query ="delete from course_detail where Sno= '"+Sno+"'"
cursor = nehapriya.cursor()
cursor.execute(sql_delete_query)
nehapriya.commit()

sql_select_query ="select * from course_detail where Sno='"+Sno+"'"
cursor = nehapriya.cursor()
cursor.execute(sql_select_query)
course_name=cursor.fetchall()

for row in course_name:
 print("%s " % row)
  
