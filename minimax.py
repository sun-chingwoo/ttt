player_human="O"
player_ai="X"


boa=[" " for i in range(1,10)]

def dis():
    for i in range(0,7,3):
        for j in range(i,i+3):
            print(f" {boa[j]} |",end="")
        print("")
        if j <8 :
            print("-"*12)

def checkwin():
    answer = [(0, 1, 2),(3, 4, 5),(6, 7, 8),(0, 3, 6),(1, 4, 7),(2, 5, 8),(0, 4, 8),(2, 4, 6)]
    for a,b,c in answer:
        if boa[a]==boa[b]==boa[c] and boa[a]!=" ":
            return boa[a]
    if " " not in boa:
        return "draw"

def checkinput():
    while True:
        try:
            choice=int(input("Enter your choice: "))
            if choice>=1 and choice<=9 and boa[choice-1] ==" ":
                return choice-1
        except:
            print("enter valid input")

def optionsleft(options):
    for i in range(0,9):
        if boa[i]==" ":
            options.append(i)


def minimax(boa,depth,is_maximizing):
    result=checkwin()
    if result=="X":
        return 1
    elif result=="O":
        return -1
    elif result=="draw":
        return 0
    
    if is_maximizing:
        best_score=-999
        for i in range(0,9):
            if boa[i]==" ":
                boa[i]="X"
                score=minimax(boa,depth+1,False)
                boa[i]=" "
                best_score=max(score,best_score)
        return best_score
    
    else:
        best_score=999
        for i in range(0,9):
            if boa[i]==" ":
                boa[i]="O"
                score=minimax(boa,depth+1,True)
                boa[i]=" "
                best_score=min(score,best_score)
        return best_score

def bestmove():
    move=-1
    best_score=-999
    for i in range(0,9):
        if boa[i]==" ":
            boa[i]="X"
            score= minimax(boa,0,False)
            boa[i]=" "
            if score>best_score:
                best_score=score
                move=i
    return move

end=False
print("WELCOME TO TIC-TAC-TOE")
dis()
for k in range(1,10):
    options=[]
    optionsleft(options)
    print(options)
    if k%2==0:
        print("player X AI turn")
        valid=bestmove()
        boa[valid]="X"
        dis()
        end=checkwin()
        if end=="X":
            print("X wins")
            break

    else:
        print("player O ")
        valid=checkinput()
        boa[valid]="O"
        dis()
        end=checkwin()
        if end=="O":
            print("O wins")
            break

    if end=="draw":
        print("draw")
        break