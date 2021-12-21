#Author Priya
import mysql.connector


nehapriya=mysql.connector.connect(host='localhost',user='guest',database='NSIT',password='guest123')

Sno = raw_input("Sno")
course_id = raw_input("Course id: ")
course_name = raw_input("Course Name: ")
course_fee = raw_input("Fee: ")

sql_insert_query ="insert into course_detail (Sno,course_id,course_name,course_fee) values (%s, %s, %s, %s)"
data_course=(Sno,course_id,course_name,course_fee)
cursor = nehapriya.cursor()
cursor.execute(sql_insert_query,data_course)
nehapriya.commit()


sql_select_query ="select * from course_detail where Sno='"+Sno+"'"
cursor = nehapriya.cursor()
cursor.execute(sql_select_query)
course_name=cursor.fetchall()
for row in course_name:
 print("%s %s %s %s " % row)
  
