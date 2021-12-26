from calc import Solver

def test_sum():
    n = 2
    rules = ['2+', '4+']
    groups = [[(0, 0), (1, 1)], [(0, 1), (1, 0)]]
    solver = Solver(n, rules, groups)
    solver.solve(0)
    assert solver.cellText == [[1, 2], [2, 1]]

def test_product():
    n = 2
    rules = ['1*', '4*']
    groups = [[(0, 0), (1, 1)], [(0, 1), (1, 0)]]
    solver = Solver(n, rules, groups)
    solver.solve(0)
    assert solver.cellText == [[1, 2], [2, 1]]

def test_minus():
    n = 2
    rules = ['0-', '4+']
    groups = [[(0, 0), (1, 1)], [(0, 1), (1, 0)]]
    solver = Solver(n, rules, groups)
    solver.solve(0)
    assert solver.cellText == [[1, 2], [2, 1]]

def test_divide():
    n = 2
    rules = ['1/', '4*']
    groups = [[(0, 0), (1, 1)], [(0, 1), (1, 0)]]
    solver = Solver(n, rules, groups)
    solver.solve(0)
    assert solver.cellText == [[1, 2], [2, 1]]

def test_size_3():
    n = 3
    rules = ['6+', '6*', '2-', '3+']
    groups = [[(0, 0), (1, 0), (2, 0)], [(0, 1), (0, 2)], [(1, 1), (2, 1)], [(1, 2), (2, 2)]]
    solver = Solver(n, rules, groups)
    solver.solve(0)
    assert solver.cellText == [[1, 2, 3], [2, 3, 1], [3, 1, 2]]

def test_size_4():
    n = 4
    rules = ['7+', ' 2-', ' 6+', ' 6+', ' 8+', ' 9+']
    groups = [[(0, 0), (0, 1), (1, 0)], [(0, 2), (0, 3)], [(1, 2), (1, 3)], [(1, 1), (2, 0), (2, 1)], [(3, 0), (3, 1), (3, 2)], [(2, 2), (2, 3), (3, 3)]]
    solver = Solver(n, rules, groups)
    solver.solve(0)
    assert solver.cellText == [[4, 2, 3, 1], [1, 3, 2, 4], [2, 1, 4, 3], [3, 4, 1, 2]]

def test_size_5():
    n = 5
    rules = ['15*', ' 2/', ' 160*', ' 1-', ' 8+', ' 14+', ' 40*', ' 2-']
    groups = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1)], [(2, 0), (3, 0), (4, 0), (4, 1)], [(2, 1), (2, 2)], [(3, 1), (3, 2), (4, 2)], [(0, 3), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4)], [(0, 4), (1, 4), (2, 4)], [(4, 3), (4, 4)]]
    solver = Solver(n, rules, groups)
    solver.solve(0)
    assert solver.cellText == [[3, 1, 5, 2, 4], [1, 2, 3, 4, 5], [5, 3, 4, 1, 2], [4, 5, 2, 3, 1], [2, 4, 1, 5, 3]]

def test_size_6():
    n = 6
    rules = ['5/', ' 288*', ' 12+', ' 18*', ' 3-', ' 12*', ' 72*', ' 8*', ' 16+', ' 22+', ' 10*']
    groups = [[(0, 0), (1, 0)], [(0, 1), (0, 2), (0, 3), (1, 1)], [(0, 4), (0, 5), (1, 5)], [(1, 2), (1, 3), (1, 4), (2, 2), (2, 3)], [(2, 0), (2, 1)], [(3, 0), (3, 1), (3, 2)], [(4, 0), (5, 0), (5, 1)], [(5, 3), (5, 4)], [(3, 3), (4, 3), (4, 4)], [(2, 4), (2, 5), (3, 4), (3, 5), (4, 5), (5, 5)], [(4, 1), (4, 2), (5, 2)]]
    solver = Solver(n, rules, groups)
    solver.solve(0)
    assert solver.cellText == [[1, 4, 6, 2, 3, 5], [5, 6, 2, 3, 1, 4], [2, 5, 3, 1, 4, 6], [3, 1, 4, 5, 6, 2], [4, 2, 1, 6, 5, 3], [6, 3, 5, 4, 2, 1]]