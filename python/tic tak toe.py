theboard={'7':' ','8':' ','9':' ',
        '4':' ','5':' ','6':' ',
        '1':' ','2':' ','3':' '}

boardkeys=[]
print('Numbers positions are in the format\n7|8|9\n4|5|6\n1|2|3')

for key in theboard:
    boardkeys.append(key)


def printBoard(board):
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print('-------')
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('-------')
    print(board['1']+'|'+board['2']+'|'+board['3'])


def game():
    turn='X'
    count=0


    for i in range(10):
        printBoard(theboard)

        print(f'It is turn of {turn}, Specify the place you want to go')
        
        move=input()

        if theboard[move]==' ':
            theboard[move]=turn
            count=count+1
        else:
            print('sorry this location is filled, please hoose another one')
            continue

        if count>=5:
            if theboard['7']==theboard['8']==theboard['9']!='':
                printBoard(theboard)
                print('\nGame Over\n')
                print(f'Player {turn} won the game')
                break

            elif theboard['4']==theboard['5']==theboard['6']!='':
                printBoard(theboard)
                print('\nGame Over\n')
                print(f'Player {turn} won the game')
                break

            elif theboard['1']==theboard['2']==theboard['3']!='':
                printBoard(theboard)
                print('\nGame Over\n')
                print(f'Player {turn} won the game')
                break

            elif theboard['1']==theboard['4']==theboard['7']!='':
                printBoard(theboard)
                print('\nGame Over\n')
                print(f'Player {turn} won the game')
                break

            elif theboard['2']==theboard['5']==theboard['8']!='':
                printBoard(theboard)
                print('\nGame Over\n')
                print(f'Player {turn} won the game')
                break

            elif theboard['3']==theboard['6']==theboard['9']!='':
                printBoard(theboard)
                print('\nGame Over\n')
                print(f'Player {turn} won the game') 
                break
            elif theboard['3']==theboard['6']==theboard['9']!='':
                printBoard(theboard)
                print('\nGame Over\n')
                print(f'Player {turn} won the game') 
                break
            elif theboard['7']==theboard['5']==theboard['3']!='':
                printBoard(theboard)
                print('\nGame Over\n')
                print(f'Player {turn} won the game') 
                break
            elif theboard['1']==theboard['5']==theboard['9']!='':
                printBoard(theboard)
                print('\nGame Over\n')
                print(f'Player {turn} won the game') 
                break

        if count==9:
            print('\nGame Over\nThe Game is tie')

        if turn=='X':
            turn='O'
        else:
            turn='X'

    restart=input('Do you want to restart the game?(y/n)')

    if restart=='y' or restart=='Y':
        for key in boardkeys:
            theboard[key]=' '
        game()


if __name__=='__main__':
    game()