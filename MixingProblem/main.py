import numpy as np
from scipy.optimize import linprog

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def MixingProblem():
    c = np.array([7, 4, 6, 8])
    A_ub = np.array([(-20, -15, -5, -30), (-10, 0, -20, -5), (10, 0, 20, 5), (40, 65, 35, 40)])
    b_ub = np.array([-18, -8, 13, 50])
    A_eq = np.array([(1, 1, 1, 1)])
    b_eq = np.array([1])
    x1_bounds = (0.1, 0.25)
    x2_bounds = (0, 0.2)
    x3_bounds = (0.3, 1)
    x4_bounds = (0, 1)

    res = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, bounds=[x1_bounds, x2_bounds, x3_bounds, x4_bounds])

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MixingProblem()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
