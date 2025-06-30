d={
    1:"n",2:"n",3:"n",
    4:"n",5:"n",6:"n",
    7:"n",8:"n",9:"n"
}

def dis():
    for i in range(1,10,3):
        for j in range(i,i+3):
            print(f"| {d[j]} |",end="")
        
        print("")
        print("_"*15)
        print("")

def check():
    if ((d[1] == "X" and d[2] == "X" and d[3] == "X") or
        (d[4] == "X" and d[5] == "X" and d[6] == "X") or
        (d[7] == "X" and d[8] == "X" and d[9] == "X") or
        (d[1] == "X" and d[4] == "X" and d[7] == "X") or
        (d[2] == "X" and d[5] == "X" and d[8] == "X") or
        (d[3] == "X" and d[6] == "X" and d[9] == "X") or
        (d[1] == "X" and d[5] == "X" and d[9] == "X") or
        (d[3] == "X" and d[5] == "X" and d[7] == "X")):
        print("X wins")
        end=1
    elif ((d[1] == "O" and d[2] == "O" and d[3] == "O") or
        (d[4] == "O" and d[5] == "O" and d[6] == "O") or
        (d[7] == "O" and d[8] == "O" and d[9] == "O") or
        (d[1] == "O" and d[4] == "O" and d[7] == "O") or
        (d[2] == "O" and d[5] == "O" and d[8] == "O") or
        (d[3] == "O" and d[6] == "O" and d[9] == "O") or
        (d[1] == "O" and d[5] == "O" and d[9] == "O") or
        (d[3] == "O" and d[5] == "O" and d[7] == "O")):
        print("O wins")
        end=1

end=0
for i in range(1,10):
    if i%2==0:
        choice=int(input("player 2 enter your choice :"))
        d[choice]="O"
    else :
        choice=int(input("player 1 enter your choice :"))
        d[choice]="X"
    dis()
    check()
    if end==1:
        break