import numpy as np
from scipy.optimize import linprog

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def MixingProblem(name):
    c = np.array([700, 400, 600, 800])

    return np.linalg.solve(name, c)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name = np.array([
        [20, 15, 5, 30, -1, 0, 0, 0, 0, 0, 0, 0, 18],
        [10, 0, 20, 5, 0, 1, 0, 0, 0, 0, 0, 0, 13],
        [10,0,20,5,0,0,-1,0,0,0,0,0,8],
        [40,65,35,40,0,0,0,1,0,0,0,0,50],
        [1,0,0,0,0,0,0,0,1,0,0,0,25],
        [1,0,0,0,0,0,0,0,0,-1,0,0,10],
        [0,1,0,0,0,0,0,0,0,0,1,0,20],
        [0,0,1,0,0,0,0,0,0,0,0,-1,30],
    ])
    MixingProblem(name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
