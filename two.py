boa = [" " for i in range(9)]  # 0-based indexing

def dis():
    for i in range(0, 7, 3):
        for j in range(i, i + 3):
            print(f" {boa[j]} ", end="")
            if j != i + 2:
                print("|", end="")
        print()
        if i < 6:
            print("---|---|---")

def checkwin():
    answer = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for a, b, c in answer:
        if boa[a] == boa[b] == boa[c] and boa[a] != " ":
            return boa[a]  # Return 'X' or 'O'
    return None

def checkinput():
    while True:
        try:
            choice = int(input("Enter your choice (1-9): "))
            if 1 <= choice <= 9 and boa[choice - 1] == " ":
                return choice - 1
            else:
                print("Invalid move. Try again.")
        except:
            print("Enter a valid number.")

print("WELCOME TO TIC-TAC-TOE")
dis()

for k in range(9):
    if k % 2 == 0:
        print("Player O's turn.")
        valid = checkinput()
        boa[valid] = "O"
    else:
        print("Player X's turn.")
        valid = checkinput()
        boa[valid] = "X"

    dis()
    winner = checkwin()
    if winner:
        print(f"Player {winner} wins!")
        break
else:
    print("It's a draw!")
