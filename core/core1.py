import sqlite3
import base64
from getpass import getpass

mydb = sqlite3.connect("psql.db")
# print(mydb.total_changes)


mycursor = mydb.cursor()

def registration(name,city,email,password,password2):
    if password==password2:
        sample_string = password
        sample_string_bytes = sample_string.encode("ascii")
  
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")
        password=base64_string
        sql=mycursor.execute("insert into student (name,city,email,password) values('{}','{}','{}','{}')".format(name,city,email,password))
        mydb.commit()
        print("--You have successfully registered--")
        return True
    else:
        print('--Try again!--')
        email=input('Enter your email: ')
        password = getpass(prompt = 'Enter the password')
        password2 = getpass(prompt = 'Enter the password')

def login(flag):
    if flag==0:
        while True:
            print("\t","---please login--- ")
            email=input("Enter your email: ")
            password = getpass(prompt = 'Enter the password')
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * from student")
            myresult = mycursor.fetchall()
            s=set()
            s1=set()
            for a,b,c,d in myresult:
                base64_string =d
                base64_bytes = base64_string.encode("ascii")
                sample_string_bytes = base64.b64decode(base64_bytes)
                sample_string = sample_string_bytes.decode("ascii")
                val2=sample_string
                s.add(c)
                s1.add(val2)
            if email in s and password in s1:
                print("--You have successfully login--")
                flag=1
                return flag
            else:
                print("--Try again!--")
    elif flag==1:
        while True:
            print("\t","---please login--- ")
            email=input("Enter your email: ")
            password = getpass(prompt = 'Enter the password')
            flag=3
            mycursor = mydb.cursor()
            mycursor.execute("select * from student")
            myresult = mycursor.fetchall()
            s=set()
            s1=set()
            for a,b,c,d in myresult:
                base64_string =d
                base64_bytes = base64_string.encode("ascii")
                sample_string_bytes = base64.b64decode(base64_bytes)
                sample_string = sample_string_bytes.decode("ascii")
                val2=sample_string
                s.add(c)
                s1.add(val2)
                # print(s1)
            if email in s and password in s1:
                    print("You have successfully login")
                    flag=4
                    return True
            elif flag==3:
                print("--Try again--")
            else:
                return False         

def checkregistration():
    while True:    
        x=input("--select option--\nA:Registration\nB:login\nchoose your option: ").upper()
        if x=="A":
            mycursor.execute("SELECT * from student")
            myresult = mycursor.fetchall()
            while True:
                from emailvalidation1 import checkemail1
                name=input("Enter your name: ")
                city=input("Enter your city: ")
                email=input("Enter your email: ")
                from checkemail1 import checkemail2
                t=checkemail2(email)
                email=checkemail1(t)
                # password=input("Enter your password: ")
                # password2=input("Re-enter your password: ")
                password = getpass(prompt = 'Enter the password')
                password2 = getpass(prompt = 'Enter the password')
                flag=0
                for a,b,c,d in myresult:
                    if c==t and d==password and d==password:
                        print("You are already registered")
                        flag=login(flag)
                        break
                if flag==1:
                    return True
                else:
                    t=registration(name,city,email,password,password2)                
                    if t==True:
                        flag=1
                        rl=login(flag)
                    break
            if (flag==1) or (rl==True):
                break            
        elif x=="B":
            flag=1
            t=login(flag)
            if t==True:
                break
            elif t==False:
                checkregistration()
        else:
            print("select option correctly")
    return flag 
checkregistration()      



