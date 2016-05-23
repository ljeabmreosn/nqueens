#!/bin/python
# -*- coding: utf-8 -*-
'''
nqueens with numba and numpy
'''
from timeit import timeit
from sys import argv
import numpy as np
from colorama import init, Fore

# n = 8

def pp_board(board):
    '''nice printing of the board'''
    print(str(board).replace('[', '').replace(']', '').replace('True', Fore.GREEN + '██')
          .replace('False', Fore.RED + '██').replace(' ', '')+'\n'+Fore.RESET)

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

def main():
    '''test functions'''
    init()
    # board = np.zeros((n, n), dtype=bool)
    # put_queen(board, 2, 3)
    # pp_board(board)
    n = int(argv[1])
    global print_board
    if len(argv) > 2:
        print_board = bool(int(argv[2]))
    else:
        print_board = True

    functions = [perm_all, perm_david, perm_op1]
    if len(argv) >  3:
        for func in argv[3:]:
            print()
            funcstr = str(functions[int(func)]).split(' ')[1]
            print(funcstr)
            print(timeit(funcstr+'({})'.format(n), setup='from __main__ import '+funcstr, number=10))
            print(functions[int(func)](n))
    else:
        print(functions[-1](n))

def perm_david(n):
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
            if print_board:
                pp_board(board)
            s += 1
        else:
            for x in range(len(a)):
                p[i] = a[x]
                if cond(p, i):
                    s += level(p, a[:x]+a[x+1:], i+1, n)
        return s
    return level([0]*n, list(range(1, n+1)), 0, n)

def perm_op1(n, board=None, level=0):
    '''basic permutation with optimization'''
    count = 0
    if board is None:
        board = np.zeros((n, n), dtype=bool)
    for i in range(n):
        board_temp = board.copy()
        if not board_temp[i][level]:
            put_queen(board_temp, i, level, n)
            if level < n-1:
                count += perm_op1(n, board_temp, level=level+1)
            else:
                if print_board:
                    pp_board(board_temp)
                return count + 1
    return count

def perm_all(n):
    from itertools import permutations
    perms = permutations(range(n))
    count = 0
    for perm in perms:
        board = np.zeros((n, n), dtype=bool)
        for x, y in enumerate(perm):
            #print('{} {}'.format(x, y))
            if not board[y][x]:
                put_queen(board, y, x, n)
                if x == n-1:
                    if print_board:
                        pp_board(board)
                    count += 1
            else:
                break
    return count


if __name__ == '__main__':
    main()

