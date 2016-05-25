#!/bin/python
# -*- coding: utf-8 -*-
'''
nqueens with numba and numpy
'''
import timeit
from sys import argv
import numpy as np
from colorama import init, Fore

PRINT_BOARD = False

def pp_board(board):
    '''nice printing of the board'''
    print(str(board).replace('[', '').replace(']', '').replace('True', Fore.GREEN + '██')
          .replace('False', Fore.RED + '██').replace(' ', '')+'\n'+Fore.RESET)

def put_queen(board, y, x, n):
    '''uses some numpy functions to put a queen on the board'''
    #board[y] = np.full(n, True, dtype=bool)
    #board[:, x] = np.full(n, True, dtype=bool)
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
    board[d1ar1, d1ar2] = np.full(len1, True, dtype=bool)
    board[d2ar1, d2ar2] = np.full(len2, True, dtype=bool)
    board[y][x] = False

def main():
    '''test functions'''
    init()
    if len(argv) > 1:
        n = int(argv[1])
    else:
        print('nchess.py, usage:\nn print repeat functions')
        return
    if len(argv) > 2:
        global PRINT_BOARD
        PRINT_BOARD = bool(int(argv[2]))

    functions = [perm_all, perm_op1, perm_op2, perm_op3, perm_op4]
    if len(argv) > 3:
        repeats = int(argv[3])
    else:
        repeats = 100
    if len(argv) > 4:
        for func in argv[4:]:
            print()
            funcstr = str(functions[int(func)]).split(' ')[1]
            print(funcstr)
            print(min(timeit.repeat('print('+funcstr+'({}))'.format(n),
                                    setup='from __main__ import '+funcstr,
                                    repeat=repeats, number=1)))
    else:
        print(function(n) for function in functions[1:])

def prof():
    '''alternate main using cProfile instead of timeit'''
    import cProfile
    init()
    if len(argv) > 1:
        n = int(argv[1])
    else:
        print('nchess.py, usage:\nn print repeat functions')
        return
    if len(argv) > 2:
        global PRINT_BOARD
        PRINT_BOARD = bool(int(argv[2]))

    functions = [perm_all, perm_op1, perm_op2, perm_op3, perm_op4]
    if len(argv) > 4:
        for func in argv[4:]:
            print()
            funcstr = str(functions[int(func)]).split(' ')[1]
            print(funcstr)
            #cProfile.runctx('print('+funcstr + '({}))'.format(n), globals(), locals(),
            #                filename='nchess.prof', sort='time')
            cProfile.run(funcstr+'({})'.format(n), sort='time')
    else:
        print(function(n) for function in functions[1:])

def perm_op3(n):
    '''perm_david with more sane naming'''
    def cond(queens, i):
        '''checks board validity'''
        for level in range(i):
            if abs(queens[i]-queens[level]) == abs(i-level):
                return False
        return True
    def level(queens, possible, i, n):
        '''places queens'''
        count = 0
        if i >= n:
            if PRINT_BOARD:
                board = np.full((n, n), False, dtype=bool)
                for i in range(n):
                    put_queen(board, i, queens[i]-1, n)
                    pp_board(board)
            count += 1
        else:
            for index, val in enumerate(possible):
                queens[i] = val
                if cond(queens, i):
                    count += level(queens, possible[:index]+possible[index+1:], i+1, n)
        return count
    return level([0]*n, tuple(range(1, n+1)), 0, n)

def perm_op4(n):
    '''perm_david with more sane naming'''
    def cond(queens, i):
        '''checks board validity'''
        to_abs = np.empty((i, 2), np.uint8)
        for level in range(i):
            to_abs[level][0] = queens[i] - queens[level]
            to_abs[level][1] = i - level
        to_comp = np.abs(to_abs)
        print(to_comp)
        for level in to_comp:
            if level[0] != level[1]:
                return False
        return True
    def level(queens, possible, i, n):
        '''places queens'''
        count = 0
        if i >= n:
            if PRINT_BOARD:
                board = np.full((n, n), False, dtype=bool)
                for i in range(n):
                    put_queen(board, i, queens[i]-1, n)
                    pp_board(board)
            count += 1
        else:
            for index, val in enumerate(possible):
                queens[i] = val
                if cond(queens, i):
                    count += level(queens, possible[:index]+possible[index+1:], i+1, n)
        return count
    return level([0]*n, tuple(range(1, n+1)), 0, n)

def perm_op1(n, board=None, level=0):
    '''basic permutation with optimization'''
    count = 0
    if board is None:
        board = np.full((n, n), False, dtype=bool)
    for i in range(n):
        board_temp = board.copy()
        if not board_temp[i][level]:
            put_queen(board_temp, i, level, n)
            if level < n-1:
                count += perm_op1(n, board_temp, level=level+1)
            else:
                if PRINT_BOARD:
                    pp_board(board_temp)
                return count + 1
    return count

def perm_op2(n, board=None, level=0, possible=None):
    '''permutation with possible values'''
    count = 0
    if board is None:
        board = np.full((n, n), False, dtype=bool)
    if possible is None:
        possible = list(range(n))
    for i in possible:
        board_temp = board.copy()
        if not board_temp[i][level]:
            put_queen(board_temp, i, level, n)
            possible_temp = [val for val in possible if val != i]
            if level < n-1:
                count += perm_op2(n, board_temp, level=level+1, possible=possible_temp)
            else:
                if PRINT_BOARD:
                    pp_board(board_temp)
                return count + 1
    return count

def perm_all(n):
    '''terrible function, tests every possible combination'''
    from itertools import permutations
    perms = permutations(range(n))
    count = 0
    for perm in perms:
        board = np.full((n, n), False, dtype=bool)
        for x, y in enumerate(perm):
            #print('{} {}'.format(x, y))
            if not board[y][x]:
                put_queen(board, y, x, n)
                if x == n-1:
                    if PRINT_BOARD:
                        pp_board(board)
                    count += 1
            else:
                break
    return count


if __name__ == '__main__':
    #main()
    prof()

