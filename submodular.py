# -*- coding: utf-8 -*-
#!/usr/bin/env python

from itertools import permutations, combinations_with_replacement
def get_global_set(num_vars):
    x = []
    _vars = range(1, num_vars)
    perm_string = ''.join(map(str,_vars))
    for _x in _vars:
        # Change this
        x.extend(list(permutations(perm_string, _x)))
    x.append([' '])
    y=[]
    for _y in x:
        if tuple(sorted(_y)) not in y:
            y.append(tuple(sorted(_y)))
    return y

def function(v, vals):
    # v = ['1', '2', '3', ' ']
    x = [0]*len(v)
    for _x in vals:
        idx = v.index(_x)
        x[idx] = 1
    # print vals, x
    # change this equation
    # return  2*x[0] - x[0]*x[1] - 2*x[1]*x[2]  # QPBF for question 1
    # return  2*x[0] - x[0]*x[1] - 2*x[1]*x[2]  # QPBF for question 2
    return -2*x[0] + 3*x[1] + 5*x[2] + 7*x[3] - x[0]*x[1] - 2*x[1]*x[2] - 4*x[0]*x[3] - 5*x[1]*x[3]  # QPBF for question 3

def main():
    v = list('1234 ')
    V = get_global_set(len(v))
    print V

    total_itr = 0
    true_itr = 0
    V_choose = list(combinations_with_replacement(V, 2))
    # print len(V_choose)
    for A, B in V_choose:
        AinB = tuple(set(A).intersection(set(B)))
        AunB = tuple(set(A).union(set(B)))
        total_itr += 1
        # print "\n", A,B, AinB, AunB
        if (function(v, A) + function(v, B)) >= (function(v, AinB) + function(v, AunB)):
            #print A, B, AinB, AunB
            true_itr +=1

    print "Number of Iterations that satisfy the condition: ", true_itr
    print "Total number of iterations: ", total_itr
    if true_itr == total_itr:
        print "Yes, This QPBF is submodular."
    else:
        print "No, This QPBF is not submodular."


if __name__ == '__main__':
    main()