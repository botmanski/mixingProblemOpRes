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
    constraint1 = np.array([-20, -15, -5, -30])
    ax1.bar(x, optimalPercentagePerTypePrimal, label="Grain-type percentage")
    ax1.legend()
    ax1.set_title("Primal LP")
    ax2.bar(x, optimalPercentagePerTypeDual, label="Grain-type percentage")
    ax2.legend()
    ax2.set_title("Dual LP")
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
    return print(res), print("---%s s Runtime Primal Problem ---" % (time.time() - start_time))


def MixingProblemDual():
    start_time = time.time()
    c = -np.array([18, 8, -13, -50, 1])
    A_ub = np.array([[20, 15, 5, 30], [10, 0, 20, 5], [-10, 0, -20, -5], [-40, -65, -35, -40], [1, 1, 1, 1]])
    A_arg = np.transpose(A_ub)
    b_ub = np.array([7, 4, 6, 8])
    y1_bounds = (0.18, 1)
    y2_bounds = (0.08, 0.13)
    y3_bounds = (0.08, 0.13)
    y4_bounds = (0, 0.5)
    y5_bounds = (0, 1)
    res = linprog(c, A_ub=A_arg, b_ub=b_ub,
                  bounds=[y1_bounds, y2_bounds, y3_bounds, y4_bounds, y5_bounds], method="revised simplex")
    return print(res), print("---%s s Runtime Dual Problem ---" % (time.time() - start_time))

def SlacknessTheorem():
    A_ub = np.array([[20, 15, 5, 30], [10, 0, 20, 5], [-10, 0, -20, -5], [-40, -65, -35, -40]])
    x = np.array([0.15, 0.2, 0.3, 0.35])
    y = np.array([0.236111, 0.13, 0.8, 0.008333])
    c = -np.array([18, 8, -13, -50])
    b = np.array([7, 4, 6, 8])
    A_transposed = np.transpose(A_ub)
    yc = y-c
    A = np.matmul(A_transposed, yc)
    APrime = np.matmul(x, A)
    xb = x-b
    B = np.matmul(A_ub, xb)
    BPrime = np.matmul(y, B)
    return print(APrime, BPrime)

if __name__ == '__main__':
    MixingProblemPrimal()
    MixingProblemDual()
    objectiveFunctionPlot()
    SlacknessTheorem()
