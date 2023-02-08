print("content-type:text/html\n")

import cgi
import mysql.connector
print("<h1>Welcome To Python</h1>")
print("<hr/>")
print("<h1>Using Input Tag</h1>")
print("<body bgcolor='red'>")
form = cgi.FieldStorage()
name = form.getvalue("name")
email = form.getvalue("email")
subject = form.getvalue("subject")
message = form.getvalue("message")

conn = mysql.connector.connect(
    host="localhost", username='root', password='Test@123', database='diptish')
my_cusror = conn.cursor()
query = "insert into contact (name,email,subject,message) values (%s,%s,%s,%s)"
arg = (name,email,subject,message)
my_cusror.execute(query, arg)
conn.commit()
conn.close()
print("<h3>record inserted successfully</h3>")
print("<a href='http://127.0.0.1:5500/portfolio/HTML%20files/home1.html'>click here to go backy</a>")
