from gui import Gui
from calc import Solver
import matplotlib.pyplot as plt

if __name__ == '__main__':
    gui = Gui()
    def solve(event):
        print(f'n: {gui.n}')
        print(f'rules: {gui.get_rules()}')
        print(f'groups: {gui.get_groups()}')
        solver = Solver(gui.n, gui.get_rules(), gui.get_groups())
        if solver.solve(0):
            print(f'cellText: {solver.cellText}')
            gui.set_cellText(solver.cellText)
    gui.bsolve.on_clicked(solve)
    plt.show()