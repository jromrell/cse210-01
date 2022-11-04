def main():
    spots = {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5', 
          6 : '6', 7 : '7',  8 : '8', 9 : '9'}
    playing = True
    complete = False
    turn = 0
 # Game Loop
    while playing:
     #blank line
     print()
     # Draw the current Game Board
     make_board(spots)
     #blank line
     print()
     #tell players who's turn it is
     print(str((turn % 2) +1 ) + "'s turn to choose a square (1-9):")

     # Get input and make sure it's valid
     choice = input()
     # The game has ended, 
     if str.isdigit(choice) and int(choice) in spots:
       # Check if the spot is already taken.
       if not spots[int(choice)] in {"X", "O"}:
         # If not, update board and increment the turn
         turn += 1
         spots[int(choice)] = check_turn(turn)

     # Check if the game has ended (and if someone won)
     if check_for_win(spots): playing, complete = False, True
     if turn > 8: playing = False

    make_board(spots)
 # If there was a winner, say who won
    if complete:
        if check_turn(turn) == 'X': print("Player 1 Wins!")
        else: print("Player 2 Wins!")
    else: 
   # Tie Game
        print("No Winner")

    print("Good game. Thanks for playing!") 

def make_board(spots):
    board = (f"{spots[1]}|{spots[2]}|{spots[3]}\n-+-+- \n"
              f"{spots[4]}|{spots[5]}|{spots[6]}\n-+-+- \n"
              f"{spots[7]}|{spots[8]}|{spots[9]}")
    print(board)

def check_turn(turn):
    if turn % 2 == 0: 
        return 'O'
        
    else: 
        return 'X'

def check_for_win(spots):
   # Handle Horizontal Cases
   if   (spots[1] == spots[2] == spots[3]) \
     or (spots[4] == spots[5] == spots[6]) \
     or (spots[7] == spots[8] == spots[9]):
     return True
   # Handle Vertical Cases
   elif   (spots[1] == spots[4] == spots[7]) \
     or (spots[2] == spots[5] == spots[8]) \
     or (spots[3] == spots[6] == spots[9]):
     return True
   # Diagonal Cases
   elif (spots[1] == spots[5] == spots[9]) \
     or (spots[3] == spots[5] == spots[7]):
     return True

   else: return False

if __name__ == "__main__":
    main()

