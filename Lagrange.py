import numpy as np

def divided_differences(f ,X):
    """
        Return the tablle of divided differences of the function f with respect to points 
        X = [x0,x1,...,xn] as defined in Chapter 2 1.3 of ANED (Demailly)


        Inputs:
        - f -> function  R to R
        - X -> X = [x0,x1,...,xn]

        Output:
        - TAB such that TAB[i] = f[x0,...,xi]
    """

    TAB = [0 for _ in range(len(X))]
    TAB_previous = f(X)
    TAB[0] = TAB_previous[0]

    for step in range(1,len(X)):
        for index in range(step,len(X)):
            TAB[index] = (TAB_previous[index] - TAB_previous[index - 1]) / (X[index] - X[index - step])

        TAB_previous = TAB[:]

    return TAB


def evaluate_lagrange_polynomial(X, div_diff, x):
    """
        Evaluate on the set x of points x the lagrange polynomial associated with the divided differences tab provided
        as input associated with the references point X.

        Inputs:
        - X : reference points
        - div_diff : divided differences tab
        - x : evaluation points

        Outputs:
        - evaluations:  evaluations of points x by the associated lagrange polynomial
    """

    evaluations = div_diff[-1] * np.ones(len(x)).flatten()

    index = len(X) - 2

    while index >= 0:
        evaluations =  div_diff[index] + (x - X[index])*evaluations
        index -= 1
    return evaluations
