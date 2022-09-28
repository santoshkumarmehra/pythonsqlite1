import sqlite3

mydb = sqlite3.connect("psql.db")
# print(connection.total_changes)

cursor = mydb.cursor()


def checkemail2(email):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from student")
    myresult = mycursor.fetchall()
    s=set()
    for a,b,c,d in myresult:
        s.add(c)
    if email in s:
        print('--user already present please choose different user name--')
        email=input('Enter your email: ')
        checkemail2(email)
    else:
        return email