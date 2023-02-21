# Michael Scott
# COT4500 Assigment 2

import numpy as np
np.set_printoptions(precision=7, suppress=True, linewidth=100)

def neville():
    # [[x0, x1, x2], [f(x0), f(x1), f(x2)]]
    vals = [[3.6, 3.8, 3.9], [1.675, 1.436, 1.318]]
    x_to_approx = 3.7

    sol_arr = np.empty((len(vals[0]),len(vals[0])))
    for i in range(0, len(vals[0])):
        sol_arr[i][0] = vals[1][i]

    for i in range(1, len(vals[0])):
        for j in range(1, i + 1):
            term1 = (x_to_approx - vals[0][i - j]) * sol_arr[i][j - 1]
            term2 = (x_to_approx - vals[0][i]) * sol_arr[i - 1][j - 1]

            sol_arr[i][j] = (term1 - term2) / (vals[0][i] - vals[0][i-j])

    print(sol_arr[len(vals[0]) - 1][len(vals[0]) - 1], '\n')

def newton_forward(approx=0):
    # [[x0, x1, ...][f(x0), f(x1), ...]]
    vals = [[7.2, 7.4, 7.5, 7.6], [23.5492, 25.3913, 26.8224, 27.4589]]

    num_vals = len(vals[0])
    diffs = np.empty((num_vals, num_vals))

    for i in range(0, num_vals):
        diffs[i][0] = vals[1][i]

    for i in range(1, num_vals):
        for j in range(1, i + 1):
            diffs[i][j] = (diffs[i][j-1] - diffs[i-1][j-1]) / (vals[0][i] - vals[0][i-j])

    print(f"[{diffs[1][1]}, {diffs[2][2]}, {diffs[3][3]}]")

    # Question 3
    if (approx != 0):
        print()
        firstTerm = diffs[0][0]
        secondTerm = diffs[1][1] * (approx - vals[0][0])
        thirdTerm = diffs[2][2] * (approx - vals[0][0]) * (approx - vals[0][1])
        fourthTerm = diffs[3][3] * (approx - vals[0][0]) * (approx - vals[0][1]) * (approx - vals[0][2])

        solution = firstTerm + secondTerm + thirdTerm + fourthTerm
        print(solution)

def divided_difference():
    # [[x], [f(x)], [f'(x)]]
    vals = [[3.6, 3.8, 3.9], [1.675, 1.436, 1.318], [-1.195, -1.188, -1.182]]

    diffs = np.array(
            [[3.6, 1.675,  0.,  0.,  0.,  0.],
             [3.6, 1.675, -1.195, 0., 0., 0.],
             [3.8, 1.436,  0.,  0.,  0.,  0.],
             [3.8, 1.436, -1.188, 0., 0., 0.],
             [3.9, 1.318,  0.,  0.,  0.,  0.],
             [3.9, 1.318, -1.182, 0., 0., 0.]])

    # ????????
    for i in range(2, len(vals[0]) * 2, 2):
        diffs[i][2] = (diffs[i][1] - diffs[i-1][1]) / (diffs[i][0] - diffs[i-2][0])

    for i in range(2, len(vals[0]) * 2):
        for j in range(3, min(i + 2, len(vals[0] * 2))):
            diffs[i][j] = (diffs[i][j-1] - diffs[i-1][j-1]) / (diffs[i][0] - diffs[i-2][0])

    print()
    print(diffs)

def cubic_spline():
    # [[x], [f(x)]]
    vals = [[2, 5, 8, 10], [3, 5, 7, 9]]

    a = vals[1]
    h = []
    for i in range(0, len(vals[0]) - 1):
        h.append(vals[0][i+1] - vals[0][i])

    A = np.zeros((len(vals[0]), len(vals[0])))
    for i in range(0, len(vals[0])):

        if (i - int(len(h) / 2) < 0 or i + int(len(h) / 2) >= len(vals[0])):
            A[i][i] = 1.
            continue

        A[i][i-1] = h[i-1]
        A[i][i] = 2 * (h[i-1] + h[i])
        A[i][i+1] = h[i]

    b = np.zeros(4)
    for i in range(1, len(vals[0]) - 1):
        b[i] = (3 / h[i]) * (a[i+1] - a[i]) - (3 / h[i-1]) * (a[i] - a[i-1])

    x = np.linalg.solve(A, b)

    print()
    print(A)
    print()
    print(b)
    print()
    print(x)

if __name__ == "__main__":
    # Question 1
    neville()

    # Question 2 - 3
    newton_forward(7.3)

    # Question 4
    divided_difference()

    # Question 5
    cubic_spline()