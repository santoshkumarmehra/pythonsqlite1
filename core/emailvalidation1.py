import re

def checkemail1(s):
    pat = "[a-zA-Z-_\.\-]+@[a-zA-Z]+\.[a-z]{2,3}$"
    if re.match(pat,s):
        return s
    else:
        print("--Try again--")
        s=input("Enter your email: ")
        checkemail1(s)