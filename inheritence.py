a = input("enter the word ")
print('''        ..**   welcome to hangman game    **..
..**    you have guess the word in six mistakes   **..
...**                    good luck                **..


''')

input("give hint::")
a = list(a)
x = len(a)
x = x + 6
c = []
y = 0
z = 0
for i in a:
    c.append('_')
print(c)
for i in range(x):
    b = input("guess the letter:: ")
    if b == a[y]:
        c[y] = b
        y += 1
        print(c)
    else:
        z += 1
        print(f"you enter {b} it is not correct")
        if z == 1:
            print('''            +=============+
                    |        * 
                    o        *
                             *    
                             *
             ##################      ''')
        if z == 2:
            print('''            +=============+
                    |        * 
                    o        *
                    |        *    
                             *
             ##################      ''')
        if z == 3:
            print('''            +=============+
                    |        * 
                    o        *
                   /|        *    
                             *
             ##################      ''')
        if z == 4:
            print('''            +=============+
                    |        * 
                    o        *
                   /|\\      *    
                             *
             ##################      ''')
        if z == 5:
            print('''            +=============+
                    |        * 
                    o        *
                   /|\\      *    
                   /         *
             ##################      ''')
        if z == 6:
            print('''            +=============+
                    |        * 
                    o        *
                   /|\\      *    
                   / \\      *
             ##################      ''')

    if a == c:
        break
if a == c:
    print()
    print('''..**   congrat\'s you won the game  **...''')
else:
    print()
    print(">>> sorry.... you lost the game <<<<<<<....!")