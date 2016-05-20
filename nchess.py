#!/bin/python
# -*- coding: utf-8 -*-
'''
nqueens with numba and numpy
'''
import numpy as np
from colorama import init, Fore
import copy

n = 8

def pp_board(board):
    '''nice printing of the board'''
    print(str(board).replace('[', '').replace(']', '').replace('True', Fore.GREEN + '██')
          .replace('False', Fore.RED + '██').replace(' ', ''))

def put_queen(board, y, x):
    '''uses some numpy functions to put a queen on the board'''
    board[y] = np.ones(n, dtype=bool)
    board[:, x] = np.ones(n, dtype=bool)
    off1 = y - x
    off2 = n - y - x
    if off1 > 0:
        d1ar1 = np.arange(n-off1) + off1
        d1ar2 = np.arange(n-off1)
        len1 = n-off1
    else:
        d1ar1 = np.arange(n+off1)
        d1ar2 = np.arange(n+off1) - off1
        len1 = n+off1
    if off2 > 0:
        d2ar1 = np.arange(n-off2, -1, -1)
        d2ar2 = np.arange(n-off2 + 1)
        len2 = n-off2 + 1
    else:
        d2ar1 = np.arange(n+off2 - 2, -1, -1) - off2 + 1
        d2ar2 = np.arange(n+off2 - 1) - off2 + 1
        len2 = n+off2 - 1
    board[d1ar1, d1ar2] = np.ones(len1, dtype=bool)
    board[d2ar1, d2ar2] = np.ones(len2, dtype=bool)
    board[y][x] = False

def main():
    '''test functions'''
    init()
    board = np.zeros((n, n), dtype=bool)
    print(perm_op1(board, level=0))
    #print(perm_all())

def perm_op1(board, level=0):
    '''basic permutation with optimization'''
    count = 0
    for i in range(len(board)):
        board_temp = board.copy()
        if not board_temp[i][level]:
            put_queen(board_temp, i, level)
            #print()
            #pp_board(board_temp)
            if level < n-1:
                count += perm_op1(board_temp, level=level+1)
            else:
                #print()
                #pp_board(board_temp)
                return count + 1
    return count

def perm_all():
    from itertools import permutations
    perms = permutations(range(n))
    count = 0
    for perm in perms:
        board = np.zeros((n, n), dtype=bool)
        for x, y in enumerate(perm):
            #print('{} {}'.format(x, y))
            if not board[y][x]:
                put_queen(board, y, x)
                if x == n-1:
                    #print()
                    #pp_board(board)
                    count += 1
            else:
                break
    return count


if __name__ == '__main__':
    main()

