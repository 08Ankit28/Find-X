import random
print("*****FIND X *****")
print("Welcome to the game.\nThe rules for the game are as follows:\nYou have to guess the coordinates of where the X is hidden.\nThe first number you input will be the column number and the second number you choose will be the row number.")
a=random.randint(0,2)
b=random.randint(0,2)
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
map[a][b]="X"
g=a+1
h=b+1
position = input("Where do you think the treasure is? ")
v=int(position[0])
ho=int(position[1])

if v==g:
    if ho==h:
        print("Hurrah!! You have won the game.")
        print(f"{row1}\n{row2}\n{row3}")
    else:
        print("Alas! You lost it ")
        c=str(a+1)
        d=str(b+1)
        print("Thr right answer was "+c+d)
        print(f"{row1}\n{row2}\n{row3}")
else:
    print("Alas! You lost it ")
    e=str(a+1)
    f=str(b+1)
    print("Thr right answer was "+e+f)
    print(f"{row1}\n{row2}\n{row3}")