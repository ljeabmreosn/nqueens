#!/bin/python
# -*- coding: utf-8 -*-
'''
nqueens with numba and numpy
'''
from itertools import permutations
import numpy as np
from colorama import init, Fore

# n = 8


def pp_board(board):
    '''nice printing of the board'''
    print(str(board).replace('[', '').replace(']', '').replace('True', Fore.GREEN + '██')
          .replace('False', Fore.RED + '██').replace(' ', ''))

def put_queen(board, y, x, n):
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
def perms(n):
    s = 0
    def cond(p, i):
        for r in range(i):
            if abs(p[i]-p[r]) == abs(i-r):
                return False
        return True
    def level(p, a, i, n):
        s = 0
        if i >= n:
            board = np.zeros((n, n), dtype=bool)
            for i in range(n):
                put_queen(board, i, p[i]-1, n)
            pp_board(board)
            print('----------------------------')
            s += 1
        else:
            for x in range(len(a)):
                p[i] = a[x]
                if cond(p, i):
                    s += level(p, a[:x]+a[x+1:], i+1, n)
        return s
    return level([0]*n, list(range(1, n+1)), 0, n)
def main():
    '''test functions'''
    init()
    # board = np.zeros((n, n), dtype=bool)
    # put_queen(board, 2, 3)
    # pp_board(board)
    while True:
        print(perms(int(input())))

if __name__ == '__main__':
    main()

