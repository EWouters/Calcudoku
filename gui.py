import numpy as np
import re
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from matplotlib.patches import Rectangle
from matplotlib.widgets import Button, RadioButtons, TextBox

reg = re.compile('([0-9]+[\*\+-/])')

class Gui(object):
    n = 1
    n_rules = 0
    rules = []

    def __init__(self):
        self.cellText = (('',) * self.n,) * self.n
        self.fig = plt.figure()
        self.fig.canvas.mpl_connect('pick_event', self.onpick)

        axsmaller = plt.axes([0.1, 0.875, 0.19, 0.075])
        axbigger = plt.axes([0.3, 0.875, 0.19, 0.075])
        axremove = plt.axes([0.5, 0.875, 0.19, 0.075])
        axadd = plt.axes([0.7, 0.875, 0.19, 0.075])
        self.bbigger = Button(axbigger, 'Bigger')
        self.bbigger.on_clicked(self.bigger)
        self.bsmaller = Button(axsmaller, 'Smaller')
        self.bsmaller.on_clicked(self.smaller)
        self.badd = Button(axadd, 'Add Rule')
        self.badd.on_clicked(self.add)
        self.bremove = Button(axremove, 'Remove Rule')
        self.bremove.on_clicked(self.remove)

        self.rax = plt.axes([0.01, 0.15, 0.165, 0.65])
        self.cmap = get_cmap('Spectral')
        self.add(None)

        self.axbox = plt.axes([0.06, 0.05, 0.115, 0.075])
        self.text_box = TextBox(self.axbox, 'Rule')
        self.text_box.on_submit(self.submit_text)

        self.tax = plt.axes([0.2, 0.2, 0.7, 0.6])
        self.make_table()

        axsolve = plt.axes([0.7, 0.05, 0.19, 0.075])
        self.bsolve = Button(axsolve, 'Solve')

        # axcheck = plt.axes([0.5, 0.05, 0.19, 0.075])
        # self.bcheck = Button(axcheck, 'Check')

    def get_rules(self):
        return self.rules
    def set_rules(self, rules):
        for r in rules:
            m = reg.match(r.strip())
            if m is None:
                print(f"Invalid rule: '{r.strip()}'")
                return
        # print(f'Rules set: {rules}')
        self.rules = rules
        self.n_rules = len(rules)
        self.make_radio()

    def get_cellText(self):
        return self.cellText
    def set_cellText(self, cellText):
        n = len(cellText)
        if n is not len(cellText[0]):
            print('cellText is not a square array')
            return
        for i,row in enumerate(cellText):
            for j,cell in enumerate(row):
                if not (isinstance(cell, int) and cell <= n) and not cell == '':
                    print(f"Invalid cell at ({i},{j}): '{cell}'")
                    return
        groups = None
        if n == self.n:
            groups = self.get_groups()
        self.cellText = cellText
        self.n = n
        self.make_table()
        if groups:
            self.set_groups(groups)

    def get_groups(self):
        l = [[] for n_rule in range(len(self.rules))]
        for n_rule in range(len(self.rules)):
            for i in range(self.n):
                for j in range(self.n):
                    if self.table[i, j].get_facecolor() == self.cmap(n_rule/self.n_rules):
                        l[n_rule].append((i, j))
        return l
    def set_groups(self, groups):
        if len(groups) > self.n_rules:
            self.rules += [' '] * (len(groups) - self.n_rules)
            self.n_rules = len(groups)
        n = max(max(max(groups))) + 1
        if n > self.n:
            self.cellText = (('',) * n,) * n
            self.n = n
            self.make_table()
        for n_group, group in enumerate(groups):
            for i, j in group:
                self.table[i, j].set_facecolor(self.cmap(n_group/self.n_rules))

    def get_r_selected(self):
        if self.n_rules < 2:
            return 0
        return [v.get_facecolor()[0] < .5 for v in self.radio.circles].index(True)
        
    def make_radio(self):
        self.rax.clear()
        self.rax.set_title('Rules')
        self.radio = RadioButtons(self.rax, self.rules, active=self.get_r_selected())
        self.radio.on_clicked(self.submit_radio)
        for i, l in enumerate(self.radio.labels):
            l.set_backgroundcolor(self.cmap(i/self.n_rules))
        plt.draw()

    def make_table(self):
        colWidths = (.05,) * len(self.cellText)
        self.tax.clear()
        self.tax.set_axis_off()
        self.table = self.tax.table(
            cellText=self.cellText,
            colWidths=colWidths,
            loc='center')
        for c in self.table.get_celld().values():
            c.set_picker(True)
        plt.draw()

    def submit_text(self, label):
        r = reg.match(label.strip())
        if r is None:
            print(f"Invalid label: '{label}'")
            return
        self.rules[self.get_r_selected()] = label
        self.make_radio()

    def submit_radio(self, label):
        self.text_box.set_val(label)

    def bigger(self, event):
        self.n += 1
        self.cellText = (('',) * self.n,) * self.n
        self.make_table()
    def smaller(self, event):
        self.n = max(1, self.n - 1)
        self.cellText = (('',) * self.n,) * self.n
        self.make_table()
    def add(self, event):
        self.n_rules += 1
        self.rules.append(' ')
        self.make_radio()
    def remove(self, event):
        self.n_rules = max(1, self.n_rules - 1)
        self.rules = self.rules[:self.n_rules]
        self.make_radio()

    def onpick(self, event):
        if isinstance(event.artist, Rectangle):
            patch = event.artist
            patch.set_facecolor(self.cmap(self.get_r_selected()/self.n_rules))

if __name__ == '__main__':
    gui = Gui()
    plt.show()