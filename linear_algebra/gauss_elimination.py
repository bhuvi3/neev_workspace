#!/usr/bin/env python

"""
Unit 1 assignment - Gauss Elimination
Assignment 1

Implement the Gauss elimination algorithm for computing the solution to a linear system of equations Ax = b
Requirements

    1. The program should take as argument a single file name. The file will contain the pickle'd numpy matrix A and vector b. (Changed to augmented matrix - [A b])
    2. You need to implement the algorithm from scratch, not use a numpy routine
    3. The output should be a numpy array containing the solution x
    4. Your code should detect whether the system of equations is consistent or not
    5. In case multiple solutions are possible, any one should be returned.
    6. In case no solutions are possible, an error should be thrown

Assignment submission

The assignment should be submitted as a link to a directory in github. The directory should contain a README.md file which will have a description of the program usage and any other comments.

The submission type is set to Online Text. Simply paste the github URL to your program directory here.
"""

import argparse
import numpy as np
import pickle
import copy

def get_args():
    """
    Parse the command line arguments.

    """
    parser = argparse.ArgumentParser(description="Gauss elimination algorithm for computing the solution to a "
                                                 "linear system of equations Ax = b.")
    parser.add_argument('--input_file',
                        help='Specify the path to the pickle file containing the augmented matrix [A b]')
    parser.add_argument('--output_file',
                        default=None,
                        help='Specify the path to the which the solution vector x needs to saved. '
                             'Default: Saves the output in the current directory.')
    args = parser.parse_args()
    return args

def _get_row_echelon_form(A):
    """
    Convert to row echelon form for the augmented matrix.
    Args:
        A: Augmented matrix [A b]

    """
    A = copy.deepcopy(A)
    m, n = A.shape
    # n - 1 because we don't need to consider the augmented column b.
    for k in range(min(m, n - 1)):
        # Find the pivot and swap rows.
        i_max = k + np.argmax(np.abs(A[k:, k]))
        # This catches divide by zero.
        if A[i_max, k] == 0:
            continue
            """
            print "The highest pivot is 0."
            if A[i_max, n - 1] == 0:
                print "The corresponding b is also 0. Hence, the system could still be consistent."
                continue
            else:
                raise ValueError("Inconsistent system of equations: The sub-matrix is singular.")
            """

        # Swap axes with the pivot i_max row.
        A[[i_max, k]] = A[[k, i_max]]

        # For all rows below pivot.
        for i in range(k + 1, m):
            f = A[i, k] / A[k, k]

            # For all elements in the current row.
            for j in range(k, n):
                A[i, j] = A[i, j] - A[k, j] * f

    return A

def _back_substitution(T):
    """
    Perform back substitution on augmented matrix.
    Here it is assumed that the size of the array is (m, m +1).

    """
    m, n = T.shape
    if n != m + 1:
        raise ValueError("Backsubstituion must get array of shape : m, m +1")

    x = np.zeros(m)
    for i in reversed(range(m)):
        k = np.dot(x, T[i,:-1])
        # v = T[i, n - 1] / T[i, i]
        x[i] = (T[i, n - 1] - k) / T[i, i]

    return x


def gauss_elimination(Ab):
    """
    The Gauss Elimination algorithm to find solution to the system of linear equation Ax = b.
    Args:
        Ab: The augmented matrix [A b]
    Returns:
        The solution vector x.

    """
    # Copy to keep the function immutable.
    Ab = copy.deepcopy(Ab)
    Ab = Ab.astype(np.float64)

    R = _get_row_echelon_form(Ab)
    print "Row echelon augmented matrix: \n%s\n" % R

    # Determine if the system of equations are inconsistent.
    m, n = R.shape
    x_len = n - 1
    for free_i in reversed(range(m)):
        if R[free_i, n - 1 - 1] != 0:
            break

        if R[free_i, n - 1] != 0:
            raise ValueError("Inconsistent system of equations: no solutions exist.")

    # Slice out the free variable rows.
    # This reduces the computation for back substitution.
    T = R[:free_i + 1, :]
    print "Row echelon free variables sliced augmented matrix: \n%s\n" % T
    #print free_i

    # Slice out the columns on the right.
    # This reduces the computation for back substitution.
    S = T[:, :free_i + 1]
    b_row = T[:, n - 1]
    b_row1 = b_row.reshape((len(b_row), 1))
    S = np.hstack((S, b_row1))
    print "Row echelon free variables sliced, square converted augmented matrix: \n%s\n" % S

    # Back substitution.
    x_unique = _back_substitution(S)
    x = np.pad(x_unique, (0, x_len - len(x_unique)), 'constant')
    return x


if __name__ == "__main__":
    args = get_args()
    Ab = pickle.load(open(args.input_file))
    x = gauss_elimination(Ab)
    print "The solution is: %s" % x
    if not args.outout_file:
        args.outout_file = "./x.pickle"
    pickle.dump(x, open(args.outout_file, "w"))
