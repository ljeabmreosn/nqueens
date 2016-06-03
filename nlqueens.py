'''trying to do nqueens without recursion'''
import numpy as np

class NRnQueens():
    '''non-recursive nqueens'''
    def __init__(self, n):
        self.i = 0
        self.arr = np.arange(n)
        self.count = 0

    def find_next_bigger(self):
        '''if it exists, swaps arr[j] and arr[i] where arr[j] is less than arr[i] for j > i'''
        cur = self.arr[self.i]
        n = len(self.arr)
        cur_min = n
        cur_min_index = 0
        for j in range(self.i+1, n):
            if self.arr[j] > cur and self.arr[j] < cur_min:
                cur_min = self.arr[j]
                cur_min_index = j
        if cur_min != n:    #found number in possible section that is larger than current
            self.arr[self.i], self.arr[cur_min_index] = self.arr[cur_min_index], self.arr[self.i]
            return True
        else:
            return False

    def find_next(self):
        '''finds the smallest value after i and increments i'''
        n = len(self.arr)
        cur_min = n
        cur_min_index = 0
        for j in range(self.i+1, n):
            if self.arr[j] < cur_min:
                cur_min = self.arr[j]
                cur_min_index = j
        self.arr[self.i+1], self.arr[cur_min_index] = self.arr[cur_min_index], self.arr[self.i+1]
        self.i += 1

    def backtrack(self):
        '''goes back until there is a valid swap'''

        if self.find_next_bigger():
            return True

        cur = self.arr[self.i]

        cur_min = len(self.arr)
        cur_min_index = 0

        for j in range(self.i - 1, -1, -1):
            if self.arr[j] < cur:
                self.arr[j], self.arr[self.i] = self.arr[self.i], self.arr[j]
                self.i = j
                return False
            if self.arr[j] < cur_min:
                cur_min = self.arr[j]
                cur_min_index = j

        self.arr[cur_min_index], self.arr[self.i] = self.arr[self.i], self.arr[cur_min_index]

    def is_valid(self):
        '''checks to see if self.arr[:i] is a valid configuration'''
        for level in range(self.i):
            if abs(self.arr[self.i] - self.arr[level]) == self.i-level:
                return False
        return True

    def do_next(self):
        '''testing function'''
        if self.i == len(self.arr) - 1:
            if self.is_valid():
                self.count += 1
                print('VALID, solution {}'.format(self.count))
            self.backtrack()
        else:
            if self.is_valid():
                print('valid, finding next')
                self.find_next()
            else:
                if self.backtrack():
                    print('not valid, backtracking in place')
                else:
                    print('not valid, backtracking down')
        print('{} {}'.format(self.arr, self.i))

if __name__ == '__main__':
    nq = NRnQueens(5)
    for _ in range(200):
        nq.do_next()
