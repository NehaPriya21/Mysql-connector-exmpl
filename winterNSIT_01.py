#Author Priya
import mysql.connector


nehapriya=mysql.connector.connect(host='localhost',user='guest',database='NSIT',password='guest123')

id = raw_input("course_id")
print("the id is  ",id)
print id
sql_select_query ="select course_name from course_detail where course_id='"+id+"'"
cursor = nehapriya.cursor()
cursor.execute(sql_select_query)
course_name=cursor.fetchall()
for row in course_name:
 print("course_name = %s" % row[0])
  
