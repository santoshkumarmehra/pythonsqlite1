from distutils.cmd import Command
import email
import sqlite3

connection = sqlite3.connect("psql.db")
# print(connection.total_changes)

cursor = connection.cursor()
# Command="CREATE TABLE student(name text,city text, email text,password text)"
# cursor.execute(Command)
# connection.commit()
# name=input("name: ")
# city=input("city: ")
# email=input("email: ")
# password=input("password: ")
# cursor.execute("insert into student (name,city,email,password) values('{}','{}','{}','{}')".format(name,city,email,password))
# connection.commit()

r="select * from student"
fetch = cursor.execute(r).fetchall()
for i in fetch:
    print(i)
# r="delete from student"
# cursor.execute(r)
# connection.commit()
















# cursor.execute("CREATE TABLE student(name text,city text, email text,password text)")
# while True:
#     name=input("Enter your name: ")
#     city=input("Enter your city: ")
#     email=input("Enter your email: ")
#     password=input("Enter your password: ")
#     sql = "INSERT INTO student (name,city,email,password) VALUES (?,?,?,?)".format(name,city,email,password)
#     # val = (name,city,email,password)
#     # cursor.execute(sql, val)
#     connection.commit()
#     x=int(input("1:More user\n2:exit\nSelect option: "))
#     if x==2:
#         break
# rows = cursor.execute("SELECT * from student").fetchall()
# print(rows)
# for t in rows:
#     for j in t:
#         print(j)
    
