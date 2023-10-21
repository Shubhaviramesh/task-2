import string
import random
len=int(input("Enter the length of the password:"))
lower = ("abcdefghijklmnopqrstuvwxyz")
upper = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
digits = ("1234567890")
symbols = ("!@#$%^&*()_-.")
str = lower+upper+digits+symbols
pwd=random.sample(str,len)
password="".join(pwd)
print (password)