a=['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b=[]
c=['@', '#', '$', '%', '&', '*', '+']
d=['1', '2', '3', '4', '5', '6', '7', '8', '9']
print('''the password should consist 
atleast one letter in (a to z)
atleast one letter in (A to Z)
atleast one number in (1 to 9)
atleast one letter in (@,#,$,%,&,*,+)''')
y=input(" enter the password::")
x=list(y)
l=len(x)
v=0
s=0
t=0
u=0
if v==0:
 for j in a:
  for i in x:
   if j==i:
     v+=1
  if v==1:
      break
if v==0:
    print("you missed the small leter")
if s==0:
 for j in b:
  for i in x:
   if j==i:
     s+=1
  if s==1:
      break
if s==0:
    print("you missed the capital leter")
if t==0:
 for j in c:
  for i in x:
   if j==i:
     t+=1
  if t==1:
      break
if t==0:
    print("you missed the symbols")
if u==0:
 for j in d:
  for i in x:
    if j==i:
      u+=1
    if u==1:
      break
if u==0:
    print("you missed the number")
o=v+s+u+t
print(o)
j="".join(x)
if o==4:
    key=input("confirm password")
else:
    print("choose right password")
if key==y:
    print("welcome")
else:
    print("please enter correct password")




















