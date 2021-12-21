#Author Priya
import mysql.connector


nehapriya=mysql.connector.connect(host='localhost',user='guest',database='NSIT',password='guest123')
Sno1=raw_input("Sno_old")
Sno = raw_input("Sno_upadted")
course_id = raw_input("Course id: ")
course_name = raw_input("Course Name: ")
course_fee = raw_input("Fee: ")

sql_update_query ="update course_detail set Sno= %s,course_id= %s,course_name= %s,course_fee= %s where Sno= %s"
data_course=(Sno,course_id,course_name,course_fee,Sno1)
cursor = nehapriya.cursor()
cursor.execute(sql_update_query,data_course)
nehapriya.commit()


sql_select_query ="select * from course_detail where Sno='"+Sno+"'"
cursor = nehapriya.cursor()
cursor.execute(sql_select_query)
course_name=cursor.fetchall()
for row in course_name:
 print("%s %s %s %s " % row)

