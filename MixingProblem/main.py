import numpy as np
from scipy.optimize import linprog
import time
import matplotlib.pyplot as plt  # maybe not today
import seaborn as sns  #

def objectiveFunctionPlot():
    x = np.array(["Type 1", "Type 2", "Type 3", "Type 4"])
    fig, (ax1, ax2) = plt.subplots(1, 2)
    objectiveFunction = np.array([7, 4, 6, 8])
    optimalPercentagePerTypePrimal = np.array([0.15, 0.2, 0.3, 0.35])
    optimalPercentagePerTypeDual = np.array([0.25, 0.2, 0.5333, 0.01666])
    ax1.bar(x, optimalPercentagePerTypePrimal, label="Primal Problem")
    ax1.legend()
    ax2.bar(x, optimalPercentagePerTypeDual, label="Dual Problem")
    ax2.legend()
    plt.show()


def MixingProblemPrimal():
    start_time = time.time()
    c = np.array([7, 4, 6, 8])
    A_ub = np.array([[-20, -15, -5, -30], [-10, 0, -20, -5], [10, 0, 20, 5], [40, 65, 35, 40]])
    b_ub = np.array([-18, -8, 13, 50])
    A_eq = np.array([(1, 1, 1, 1)])
    b_eq = np.array([1])
    x1_bounds = (0.1, 0.25)
    x2_bounds = (0, 0.2)
    x3_bounds = (0.3, 1)
    x4_bounds = (0, 1)

    res = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, bounds=[x1_bounds, x2_bounds, x3_bounds, x4_bounds], method="revised simplex")
    # returns 6.45 as cost for new flour
    return res, print(res), print("---%s s Runtime Primal Problem ---" % (time.time() - start_time))


def MixingProblemDual():
    start_time = time.time()
    c = -np.array([-18, -8, 13, 50])
    A_ub = np.array([[-20, -15, -5, -30], [-10, 0, -20, -5], [10, 0, 20, 5], [40, 65, 35, 40]])
    A_transposed = np.transpose(A_ub)
    b_ub = np.array([7, 4, 6, 8])
    A_eq = np.array([(1, 1, 1, 1)])
    b_eq = np.array([1])
    x1_bounds = (0.1, 0.25)
    x2_bounds = (0, 0.2)
    x3_bounds = (0.3, 1)
    x4_bounds = (0, 1)
    res = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_transposed, b_ub=b_ub,
                  bounds=[x1_bounds, x2_bounds, x3_bounds, x4_bounds], method="revised simplex")
    #returns cost of flour 5.585 (if x results are reevaluated with the price)
    return res, print(res), print("---%s s Runtime Dual Problem ---" % (time.time() - start_time))


if __name__ == '__main__':
    MixingProblemPrimal()
    MixingProblemDual()
    objectiveFunctionPlot()
