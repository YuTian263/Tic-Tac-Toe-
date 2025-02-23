board = ['-','-','-',
         '-','-','-',
         '-','-','-']
winner = None 

def display(): 
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def play_game(): 
    display()  # display initial board 
    won = False 
    count = 0 
    while count < 9 and not won: 
        handle_turn(count)
        count += 1 
        if check_win(board):
            won = True 
    if won: 
        return winner + ' has won the game!'
    else: 
        return 'draw'
     
def handle_turn(count):
    position = int(input("Enter board position from 1-9: "))
    if board[position - 1] != '-':
        print("Position already taken. Try again.")
        handle_turn(count)
    else: 
        if count % 2 == 0: 
            board[position - 1] = "X"
        else: 
            board[position - 1] = "O"  # Changed from '0' (zero) to 'O' (letter) for clarity.
        display()
    
def check_win(board):
    global winner 
    # Check horizontal rows (previously named check_vertical)
    def check_rows(): 
        global winner 
        for i in range(0, 9, 3): 
            if board[i] != '-' and board[i] == board[i+1] == board[i+2]: 
                winner = board[i]  # Fixed: previously set to [i] (a list), now correctly set to the winning symbol.
                return True 
        return False     
    # Check diagonal lines
    def check_diagonals():
        global winner
        if board[0] != '-' and board[0] == board[4] == board[8]:
            winner = board[0]
            return True
        if board[2] != '-' and board[2] == board[4] == board[6]:
            winner = board[2]
            return True
        return False
    # Check vertical columns (previously named check_horizontal)
    def check_columns(): 
        global winner 
        for i in range(3): 
            if board[i] != '-' and board[i] == board[i+3] == board[i+6]: 
                winner = board[i]
                return True 
        return False 

    if check_rows() or check_columns() or check_diagonals():
        return True 
    return False

n = play_game() 
print(n)
