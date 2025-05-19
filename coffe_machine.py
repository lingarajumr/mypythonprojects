print('''hai every have a nice drink

latte':200,'espresso':250,'capichino':300

''')
stuff={'capichino':{'milk':20000,'choco':2000,'foam':10000},'latte':{'gie':2000,'bean':2000,'water':3000  },'esppresso':{'crema':1000,'power':900,'suger':2000}}
def report():
    print(stuff)
case='yes'
while case=='yes':
    menu = {'latte': 200, 'espresso': 250, 'capichino': 300}
    coffee = input("what your want (latte/espresso/capichino) ?::")
    x = int(input("how many 5Rs coins ?::"))
    y = int(input("how many 10RS coins ?::"))
    z = int(input("how many 20rs coins ?::"))
    w = 5 * x + 10 * y + 20 * z
    if coffee=='latte':
        if stuff['latte']['gie'] > 500 and stuff['latte']['bean'] > 500 and stuff['latte']['water'] > 750:
            if w > menu['latte'] or w == menu['latte']:
                print("here is your coffe")
                c = w - menu['latte']
                print(f"you have insert ::{w} .the change is ::{c}")
                stuff['latte']['gie'] = stuff['latte']['gie'] - 500
                stuff['latte']['bean'] = stuff['latte']['bean'] - 500
                stuff['latte']['water'] = stuff['latte']['water'] - 400
            if w < menu['latte']:
                d = menu['latte'] - w
                print(f"sorry you  have insert ::{w} . but {d} money for coffe")
        else:
            print(f''' sorry ...there are insufficient ingredients.....
....you can go with other coffee.....''')


    if coffee == 'espresso':
        if stuff['espresso']['crema'] > 250 and stuff['espresso']['power'] >150 and stuff['espresso']['suger'] > 500:
            if w > menu['espresso'] or w == menu['espresso']:
                print("here is your coffe")
                c = w - menu['espresso']
                print(f"you have insert ::{w} .the change is ::{c}")
                stuff['espresso']['crema'] = stuff['espresso']['crema'] - 250
                stuff['espresso']['power'] = stuff['espresso']['power'] - 150
                stuff['espresso']['suger'] = stuff['espresso']['suger'] - 500
            if w < menu['espresso']:
                d = menu['espresso'] - w
                print(f"sorry you  have insert ::{w} . but {d} money for coffe")
        else:
            print(f''' sorry ...there are insufficient ingredients.....
            ....you can go with other coffee.....''')
    if coffee == 'capichino':
        if stuff['capichino']['milk'] > 250 and stuff['capichino']['choco'] > 150 and stuff['capichino']['foam'] > 500:
            if w > menu['capichino'] or w == menu['capichino']:
                print("here is your coffe")
                c = w - menu['capichino']
                print(f"you have insert ::{w} .the change is ::{c}")
                stuff['capichino']['milk'] = stuff['capichino']['milk'] - 500
                stuff['capichino']['choco'] = stuff['capichino']['choco'] - 500
                stuff['capichino']['foam'] = stuff['capichino']['foam'] - 200
            if w < menu['capichino']:
                d = menu['capichino'] - w
                print(f"sorry you  have insert ::{w} . but {d} money for coffe")
        else:
            print(f''' sorry ...there are insufficient ingredients.....
                       ....you can go with other coffee.....''')
    wish=input("do you want report (yes or no) ? ::")
    if wish=='yes':
        report()
    case = input("would you like to drink any other (yes or no) ?::")
print('''... thank you hope you visit again...''')



