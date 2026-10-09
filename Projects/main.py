import random
computer= random.choice([1,2,3])
print("Welcome to the Rock, Paper, Scissor Game!\nINSTRUCTIONS\n 'r' for Rock\n 'p' for Paper\n 's' for Scissor")
inuser=input("Choose Your Move:  ")
dict={'r':1,'p':2,'s':3}
user=dict[inuser]
reversedict={1:'Rock',2:'Paper',3:'Scissor'}
print(f"You choose {reversedict[user]} Vs Computer choose {reversedict[computer]}")
if computer==user:
    print("Its a Draw!")
else:
    if computer==1 and user==2:
        print("You Win!")
    elif computer==1 and user==3:
        print("You Lose!")
    elif computer==2 and user==1:
        print("You Lose!")
    elif computer==2 and user==3:
        print("You Win!")
    elif computer==3 and user==1:
        print("You Win!")
    elif computer==3 and user==2:
        print("You Lose!")
    else:
        print("Invalid choice")
        