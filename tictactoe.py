import random

board = ['-', '-', '-', 
         '-', '-', '-', 
         '-', '-', '-']
current_player = "X"
game_running = True
winner = None

def tablero(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#tablero(board)

def playerMove(board):
    entrada = int(input("Inserte un numero del 1-9: "))
    if entrada >= 1 and entrada <= 9 and board[entrada-1] == '-':
        board[entrada-1] = current_player
    else:
        print("La posicion ya fue seleccionada, ingrese otro")

def switchPlayer():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def computerMove(board):
    while current_player == "O":
        computer = random.randint(0, 8)
        if board[computer] == "-":
            board[computer] = "O"
            switchPlayer()

def chequeoHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "-":
        winner = board[6]
        return True
    
def chequeoVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
def chequeoDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[0]
        return True
    
def tie(board):
    global game_running
    if "-" not in board:
        tablero(board)
        print("Hubo un empate")
        game_running = False

def win():
    global game_running
    if chequeoDiagonal(board) or chequeoHorizontal(board) or chequeoVertical(board):
        print(f"El ganador es {winner}")
        game_running = False

while game_running:
    tablero(board)
    playerMove(board)
    win()
    tie(board)
    switchPlayer()
    computerMove(board)