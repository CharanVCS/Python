# printing board 
def printboard(board):
    p =[(board[i] if board[i]!=' ' else i+1) for i in range (9)]
    print(f" {p[0]} | {p[1]} | {p[2]}")
    print(f"---|---|---")
    print(f" {p[3]} | {p[4]} | {p[5]}")
    print(f"---|---|---")
    print(f" {p[6]} | {p[7]} | {p[8]}")
# checking winner
def wincheck(board):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for pos in wins:
        if board[pos[0]]==board[pos[1]]==board[pos[2]]== 'X' :
            print("X player Won the match")
            return 1
        elif board[pos[0]]==board[pos[1]]==board[pos[2]]== 'O':
            print("O player Won the match")
            return 1
    if ' ' not in board:
        print('Match is Draw')
        return 1

if __name__=="__main__":
    board=[' ' for i in range(9)]
    print('Welcome to tic tac toe Game')
    turn=1
    while True:
        printboard(board)
        if wincheck(board):
            end=input('Press enter to exit')
            break

        if turn == 1 :
            print("X's Chance")
            pos=int(input('Enter position:'))
            if board[pos-1]==' ':
                board[pos-1]='X'
                turn =0
        else :
            print("O's Chance")
            pos=int(input('Enter position:'))
            if board[pos-1]==' ':
                board[pos-1]='O'
                turn =1