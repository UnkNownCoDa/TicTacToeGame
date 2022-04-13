board = [[" "," "," "],[" "," "," "],[" "," "," "]]
count = 0
def play(player, row, col):
    board[row][col] = player
    for i in board:
        print(i)
    if board[0][0] == board[1][1] == board[2][2] == player:
        return player
    if board[2][0] == board[1][1] == board[0][2] == player:
        return player
    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return board[i][1]
        if board[0][i] == board[1][i] == board[2][i] == player:
            return board[0][i]
    return "none" 
player = 'X'
win = 'none'
while win == 'none' and count < 9:
    player = "X" if player == "O" else "O"
    print(f"Player {player}'s turn!")
    row, col = map(int, input("Enter row col: ").split())
    win = play(player, row, col)
    count += 1

if win == "none":
    print("Tie!!!")
else:
    winner = "Player 1" if win == "O" else "Player 2"
    print(f"{winner} has won!!!")

    
