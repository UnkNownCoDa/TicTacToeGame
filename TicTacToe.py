#Creating the board
board = [[" "," "," "],[" "," "," "],[" "," "," "]]
count = 0 #Keeps track of how full the board is
def play(player, row, col):
    board[row][col] = player #Places the selection of the player
    for i in board: #Displays the board on the screen
        print(i)
    if board[0][0] == board[1][1] == board[2][2] == player: #checks top left diagonal 
        return player
    if board[2][0] == board[1][1] == board[0][2] == player: #checks top right diagonal
        return player
    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] == player: #checks the rows
            return board[i][1]
        if board[0][i] == board[1][i] == board[2][i] == player: #checks the columns
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

    
