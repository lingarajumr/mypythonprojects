class Quiz:
    def __init__(self,score,question,a):
        self.score=score
        self.question=question
        self.a=a
    def marks(self):
     print(f" your score is {self.score}/{self.question}")
    def percentage(self):
        self.a=(self.score/self.question)*100
        print(f"your percentage is this quiz is::{int(ans.a)}% ")
print('''*************************
welcome to quiz game
*************************''')
print('''the ability of one class to acquire methods and attributes of another class is call______.
A.inheritance
B.Abstraction
C.polymorphism
D.objects''')
ans=Quiz(0,0,0)
ans.option1=input("enter the your answer(A/B/C/D):")
ans.question+=1
if ans.option1=='A':
    ans.score+=1
else:
    print("the answer is A")
ans.marks()
print('''the ability of one class to acquire methods and attributes of another class is call______.
A.inheritance
B.Abstraction
C.polymorphism
D.objects''')
ans.option2=input("enter the your answer(A/B/C/D):")
ans.question+=1
if ans.option2=='A':
    ans.score+=1
else:
    print("the answer is A")
ans.marks()
print('''the ability of one class to acquire methods and attributes of another class is call______.
A.inheritance
B.Abstraction
C.polymorphism
D.objects''')
ans.option3=input("enter the your answer(A/B/C/D):")
ans.question+=1
if ans.option3=='A':
    ans.score+=1
else:
    print("the answer is A")
ans.marks()
ans.percentage()