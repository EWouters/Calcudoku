class Solver(object):
    def __init__(self, n, rules, groups):
        self.cellText = [['' for j in range(n)] for i in range(n)]
        self.n = n
        self.rules = rules
        self.groups = groups
        self.attempt = 0    # counts the number of backtracking
        self.field = 0      # counts the resolved fields of the calcudoku grid
        
    def solve(self, start): # recursive backtracking solution
        while True:         # find first available position
            if start >= self.n*self.n:
                start = 0
            if self.cellText[start//self.n][start%self.n] == '':    # if position empty
                break       # found start
            start += 1      # else try next position
        i, j = start//self.n, start%self.n
        # print(f'solve {start}, {i,j}, attempt {self.attempt}, field {self.field}')
        v = 0               # first value to try
        while True:
            v += 1          # increment current value v
            # print(f'value {v} {self.cellText}')
            if v > self.n:  # if no valid value could be used
                self.attempt += 1
                return False
            if self.__check(v, i, j):   # if value at current cell is acceptable
                self.cellText[i][j] = v # store value
                # print(f'{i,j}, {self.cellText}')
                self.field += 1 # indicate another solved field
                if (self.field >= self.n*self.n):   # if all grid fields solved
                    print(f'Solution found in {self.attempt} attempts.')
                    return True
                q = self.solve(start + 1)   # call solve() with the next index    
                if q is False:  # if solve() failed: backtrack
                    self.cellText[i][j] = ''    # clear the current field
                    self.field -= 1 # remove one solved field and continue
                else:       # if success
                    return True # return True

    def __check(self, v, i, j):
        # Check row
        if v in self.cellText[i]:
            # print('Failed row')
            return False
        # Check column
        for r in range(self.n):
            if v == self.cellText[r][j]:
                # print('Failed col')
                return False
        # Check rules
        rule = 0
        for n_rule,g in enumerate(self.groups):
            if (i, j) in g:
                rule = n_rule
                break
        result = int(self.rules[rule][:-1])
        operator = self.rules[rule][-1]
        if operator == '+':
            s = 0
            empty = 0
            for c in self.groups[rule]:
                # print(f'c {c}, {self.cellText}')
                cv = self.cellText[c[0]][c[1]]
                if isinstance(cv, int):
                    s += cv
                else:
                    empty += 1
                # print(f'{i,j}, v: {v}, cv: {cv}, s: {s}, empty: {empty}')
            if empty > 1:
                if s + v >= result:
                    # print(f'Failed empty + ({self.rules[rule]})')
                    return False
            else:
                if s + v != result:
                    # print(f'Failed full + ({self.rules[rule]})')
                    return False
        if operator == '*':
            p = 1
            empty = 0
            for c in self.groups[rule]:
                cv = self.cellText[c[0]][c[1]]
                if isinstance(cv, int):
                    p *= cv
                else:
                    empty += 1
                # print(f'{i,j}, v: {v}, cv: {cv}, p: {p}, empty: {empty}')
            if empty > 1:
                if p * v > result:
                    # print(f'Failed empty * ({self.rules[rule]})')
                    return False
            else:
                if p * v != result:
                    # print(f'Failed full * ({self.rules[rule]})')
                    return False
        if operator == '-':
            if len(self.groups[rule]) != 2:
                raise(NotImplementedError)
            a = 0
            empty = 0
            for c in self.groups[rule]:
                cv = self.cellText[c[0]][c[1]]
                if isinstance (cv, int):
                    a = cv
                else:
                    empty += 1
            if not 0 < empty <= 2 and a - v != result and v - a != result:
                # print(f'Failed - ({self.rules[rule]})')
                return False
        if operator == '/':
            if len(self.groups[rule]) != 2:
                raise(NotImplementedError)
            a = 0
            empty = 0
            for c in self.groups[rule]:
                cv = self.cellText[c[0]][c[1]]
                if isinstance (cv, int):
                    a = cv
                else:
                    empty += 1
            if not 0 < empty <= 2 and a / v != result and v / a != result:
                # print(f'Failed / ({self.rules[rule]})')
                return False
        # print('check True')
        return True

if __name__ == '__main__':
    n = 3
    rules = ['6+', '6*', '2-', '3+']
    groups = [[(0, 0), (1, 0), (2, 0)], [(0, 1), (0, 2)], [(1, 1), (2, 1)], [(1, 2), (2, 2)]]
    solver = Solver(n, rules, groups)
    if solver.solve(0):
        print(f'attempts: {solver.attempt}, fields: {solver.field}')
        print(solver.cellText)