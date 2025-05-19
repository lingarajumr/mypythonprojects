import random
x=int(input("enter no.of digits in password::"))
y=int(input("enter no.of letters in password::"))
z=int(input("enter no.of symbol in password::"))
a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
b=['1','2','3','4','6','7','8','9']
c=['#','$','%','^','&','*','(',')','-','_','=','+']
d=[]
for i in range(x):
    v=random.choice(b)
    d.append(v)
for i in range(y):
    e=random.choice(a)
    d.append(e)
for i in range(z):
    f=random.choice(c)
    d.append(f)
random.shuffle(d)
s=''.join(d)
print(" your password is ::",s)
a=input("enter the password::")
if s==a:
    print("done")
else:
    print("please enter right password")



