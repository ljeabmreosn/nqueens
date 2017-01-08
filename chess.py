import sys
n = int(sys.argv[1])

def put_rook(attack_board, r, c):
    # up
    for i in range(0, c):
        attack_board[r][i] += 1
    # down
    for i in range(c+1, n):
        attack_board[r][i] += 1
    # left
    for i in range(0, r):
        attack_board[i][c] += 1
    # right
    for i in range(r+1, n):
        attack_board[i][c] += 1
    return attack_board

def put_bishop(attack_board, r, c):
    # up_left
    for i in range(1, min(r+1,c+1)):
        attack_board[r-i][c-i] += 1
    # down_right
    for i in range(1, min(n-r,n-c)):
        attack_board[r+i][c+i] += 1
    # up_right
    for i in range(1, min(r+1,n-c)):
        attack_board[r-i][c+i] += 1
    # down_left
    for i in range(1, min(n-r,c+1)):
        attack_board[r+i][c-i] += 1
    return attack_board

def put_queen(attack_board, r, c):
    return put_rook(put_bishop(attack_board, r, c), r, c)

def put(piece_board, attack_board, piece, position):
    position = position.strip()
    piece = piece.strip().lower()
    r = int(position[1:])-1
    c = ord(position[0].lower()) - 97
    # print(r, c)
    pieces = ['p', 'n', 'b', 'r', 'q', 'k']
    if piece not in pieces or c < 0 or c > 7 and r < 0 and r > 7:
        print('out of range')
        return (piece_board, attack_board)
    ##########################################
    piece_board[r][c] = piece
    if piece == 'p':
        return piece_board, put_pawn(attack_board, r, c)
    if piece == 'n':
        return piece_board, put_knight(attack_board, r, c)
    if piece == 'b':
        return piece_board, put_bishop(attack_board, r, c)
    if piece == 'r':
        return piece_board, put_rook(attack_board, r, c)
    if piece == 'q':
        return piece_board, put_queen(attack_board, r, c)
    if piece == 'k':
        print('k')
        return piece_board, put_king(attack_board, r, c)
    else:
        print('other error')
        return piece_board, attack_board
        
def empty_attack_board():
    return [[0]*n for i in range(n)]
def empty_piece_board():
    return [["=="]*n for i in range(n)]
def display(board):
    for r in board:
        for e in r:
            print(e, end='\t')
        print()
    print('\n')

import sys
from itertools import permutations
a = list(permutations(list(range(1,n+1))))
# while True:
#     # display(piece_board)
#     # display(attack_board)
#     move = ''
#     try:
#         move = input('> ')
#         move = move.split()
#         if move[0] == 'put':
#             piece_board, attack_board = put(piece_board, attack_board, move[2], move[1])
#     except:
#         break
ans = 0
for i in a:
    piece_board = empty_piece_board()
    attack_board = empty_attack_board()
    for j in range(len(i)):
        piece_board, attack_board = put(piece_board, attack_board, 'q', chr(97+j)+str(i[j]))
    noo = 0
    for x in range(n):
        for y in range(n):
            if attack_board[x][y] == 0:
                noo += 1
    if noo >= n:
        # display(piece_board)
        # display(attack_board)
        # dummy = input()
        ans += 1
print(ans)
    
