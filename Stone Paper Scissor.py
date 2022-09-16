import random

def gameWin(comp,you):
    if comp== you:
        return None
    elif comp=='r':
        if you=='s':
            return False
        elif you=='p':
            return True
    elif comp=='s':
        if you=='p':
            return False 
        elif you=='r':
            return True
    elif comp=='p':
        if you=='r':
            return False 
        elif you=='s':
            return True
print("comp turn:Rock(r) or Paper(p) or Scissor(s)?\n")
randomNo=random.randint(1,3)
print(randomNo)
if randomNo==1:
    comp='r'
elif randomNo==2:
    comp='p'
elif randomNo==3:
    comp='s'

you=input("Your turn:Rock(r) or Paper(p) or Scissor(s)?\n")

a= gameWin(comp,you)

print(f"Comp chose {comp}")
print(f"You chose {you}")

if a==None:
    print("game is tie!")
elif a:
    print("You win :)")
else:
    print("You lose :(")

        