#!/usr/bin/env python

"""
Unit 1 assignment - Gauss Elimination
Assignment 1

Implement the Gauss elimination algorithm for computing the solution to a linear system of equations Ax = b
Requirements

    1. The program should take as argument a single file name. The file will contain the pickle'd numpy matrix A and vector b
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
import math
import numpy as np
import pickle

def get_args():
    """
    Parse the command line arguments.

    """
    parser = argparse.ArgumentParser(description="Gauss elimination algorithm for computing the solution to a "
                                                 "linear system of equations Ax = b.")
    parser.add_argument('--input_file',
                        help='Specify the path to the pickle file containing a tuple containing matrix A and vector b.')
    parser.add_argument('--output_file',
                        help='Specify the path to the which the solution vector x needs to saved.')
    args = parser.parse_args()
    return args


def gauss_elimination(A, b):
    """
    The Gauss Elimination algorithm to find solution to the system of linear equation Ax = b.
    Returns the solution vector x.

    """
    pass


if __name__ == "__main__":
    args = get_args()
    # b is assumed to be the column vector.
    A, b = pickle.load(open(args.input_file))
    x = gauss_elimination(A, b)
    pickle.dump(x, open(args.outout_file, "w"))
