# implementation of two player tic-tac-toe game in python

theboard = {'7':' ','8':' ','9':' ',
            '4':' ','5':' ','6':' ',
            '1':' ','2':' ','3':' '}

board_keys = []

for keys in theboard:
    board_keys.append(keys)
print(board_keys)

def printBoard(board):
    print(board['7']+ '|' + board['8']+ '|' + board['9'])
    print('-+-+-')
    print(board['4']+ '|' + board['5']+ '|' + board['6'])
    print('-+-+-')
    print(board['1']+ '|' + board['2']+ '|' + board['3'])

def game():
    turn = 'x'
    count = 0

    for i in range(10):
        printBoard(theboard)
        print("it's your turn",turn)
        
        move = input()
        if theboard[move]== ' ':
            theboard[move]= turn
        else:
            print("the place is already filled")
            continue

        if count  >5:
            if theboard['7'] == theboard['8'] == theboard['9']!=' ':
                printBoard(theboard)
                print("game over")
                print(turn,'won')
                break
            elif theboard['4'] == theboard['5'] == theboard['6']!=' ':
                printBoard(theboard)
                print("game over")
                print(turn,'won')
                break
            elif theboard['1'] == theboard['2'] == theboard['3']!=' ':
                printBoard(theboard)
                print("game over")
                print(turn,'won')
                break
            elif theboard['7'] == theboard['5'] == theboard['3']!=' ':
                printBoard(theboard)
                print("game over")
                print(turn,'won')
                break
            elif theboard['9'] == theboard['5'] == theboard['1']!=' ':
                printBoard(theboard)
                print("game over")
                print(turn,'won')
                break
            elif theboard['7'] == theboard['4'] == theboard['1']!=' ':
                printBoard(theboard)
                print("game over")
                print(turn,'won')
                break
            elif theboard['8'] == theboard['5'] == theboard['2']!=' ':
                printBoard(theboard)
                print("game over")
                print(turn,'won')
                break
            elif theboard['9'] == theboard['6'] == theboard['3']!=' ':
                printBoard(theboard)
                print("game over")
                print(turn,'won')
                break

        if count == 9:
            print("game over")
            print("it's a tie")

        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'
    restart = input("do you want to play again ( y / n )")
    if restart.lower()== 'y':
        for key in board_keys:
            board_keys[key]=' '
            game()
if __name__ == "__main__":
    game()