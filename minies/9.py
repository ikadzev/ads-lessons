import copy

import numpy as np


def neg(a: list) -> list:
    negative = np.zeros((len(a), len(a[0])), int).tolist()
    for i in range(len(a)):
        for j in range(len(a[i])):
            negative[i][j] = -a[i][j]
    return negative


def mult_usual(a: list, b: list) -> list:
    """ Multiply matrix's (n^3) """
    res = np.zeros((len(a), len(b[0])), dtype=int).tolist()
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                res[i][j] += a[i][k] * b[k][j]
    # print(res)
    return res


def to_zeros_square(a: list) -> list:
    k = 1
    while k < len(a):
        k *= 2
    zeros = np.zeros((k, k), int).tolist()
    for i in range(len(a)):
        for j in range(len(a[0])):
            zeros[i][j] = a[i][j]
    return zeros


def a_to_h(first, second):
    """Returning n // 2 sections of matrix's (left-upper-first = A, right-upper-first = B...)"""
    assert len(first) == len(first[0]) == len(second) == len(second[0])
    n = len(first) // 2

    a = [p[:n] for p in first[:n]]
    b = [p[n:] for p in first[:n]]
    c = [p[:n] for p in first[n:]]
    d = [p[n:] for p in first[n:]]
    e = [p[:n] for p in second[:n]]
    ff = [p[n:] for p in second[:n]]
    g = [p[:n] for p in second[n:]]
    h = [p[n:] for p in second[n:]]

    return {'A': a, 'B': b, 'C': c, 'D': d, 'E': e, 'F': ff, 'G': g, 'H': h}


def to_quarts(blocks):
    """Returning quarts of matrix's mult (for mult_8)"""
    q = {}

    ae = mult_8(blocks['A'], blocks['E'])
    bg = mult_8(blocks['B'], blocks['G'])
    q[1] = sum_matrix(ae, bg)

    af = mult_8(blocks['A'], blocks['F'])
    bh = mult_8(blocks['B'], blocks['H'])
    q[2] = sum_matrix(af, bh)

    ce = mult_8(blocks['C'], blocks['E'])
    dg = mult_8(blocks['D'], blocks['G'])
    q[3] = sum_matrix(ce, dg)

    cf = mult_8(blocks['C'], blocks['F'])
    dh = mult_8(blocks['D'], blocks['H'])
    q[4] = sum_matrix(cf, dh)

    return q


def sum_matrix(target, matrix, x=0, y=0):
    assert len(target) >= y + len(matrix)
    assert len(target[0]) >= x + len(matrix[0])
    result = copy.deepcopy(target)
    i, j = 0, 0
    for lst in result[y:y + len(matrix)]:
        for index in range(x, x + len(matrix[0])):
            lst[index] += matrix[j][i]
            i += 1
        i = 0
        j += 1
    return result


def mult_8(first: list, second: list) -> list:
    """ Multiply matrix's (n^3, 8 recursions ver.) """
    assert len(first) == len(second)
    assert len(first[0]) == len(second[0])
    if len(first) <= 2:
        assert len(first) == len(first[0]) == len(second) == len(second[0])
        return mult_usual(first, second)
    orig_n = len(first)
    first_zero = to_zeros_square(first)
    second_zero = to_zeros_square(second)
    res = np.zeros((len(first_zero), len(second_zero[0])), dtype=int).tolist()
    blocks = a_to_h(first_zero, second_zero)

    quarts = to_quarts(blocks)
    res = sum_matrix(res, quarts[1])
    res = sum_matrix(res, quarts[2], len(res) // 2)
    res = sum_matrix(res, quarts[3], 0, len(res) // 2)
    res = sum_matrix(res, quarts[4], len(res) // 2, len(res) // 2)

    for i in range(len(res)):
        res[i] = res[i][:orig_n]
    return res[:orig_n]


def to_p(blocks):
    p = [[]] * 7
    p[0] = mult_sht(blocks['A'], sum_matrix(blocks['F'], neg(blocks['H'])))
    p[1] = mult_sht(sum_matrix(blocks['A'], blocks['B']), blocks['H'])
    p[2] = mult_sht(sum_matrix(blocks['C'], blocks['D']), blocks['E'])
    p[3] = mult_sht(blocks['D'], sum_matrix(blocks['G'], neg(blocks['E'])))
    p[4] = mult_sht(sum_matrix(blocks['A'], blocks['D']), sum_matrix(blocks['E'], blocks['H']))
    p[5] = mult_sht(sum_matrix(blocks['B'], neg(blocks['D'])), sum_matrix(blocks['G'], blocks['H']))
    p[6] = mult_sht(sum_matrix(blocks['A'], neg(blocks['C'])), sum_matrix(blocks['E'], blocks['F']))
    return p


def mult_sht(first: list[list[int]], second: list[list[int]]) -> list[list[int]]:
    """ Multiply matrix's (n^2.81, shtrassen ver.) """
    assert len(first) == len(second)
    assert len(first[0]) == len(second[0])
    if len(first) <= 2:
        assert len(first) == len(first[0]) == len(second) == len(second[0])
        return mult_usual(first, second)
    orig_n = len(first)
    first_zero = to_zeros_square(first)
    second_zero = to_zeros_square(second)
    res = np.zeros((len(first_zero), len(second_zero[0])), dtype=int).tolist()
    blocks = a_to_h(first_zero, second_zero)
    pies = to_p(blocks)

    q1 = sum_matrix(pies[4], pies[3])
    q1 = sum_matrix(q1, neg(pies[1]))
    q1 = sum_matrix(q1, pies[5])

    q2 = sum_matrix(pies[0], pies[1])
    q3 = sum_matrix(pies[2], pies[3])

    q4 = sum_matrix(pies[0], pies[4])
    q4 = sum_matrix(q4, neg(pies[2]))
    q4 = sum_matrix(q4, neg(pies[6]))

    res = sum_matrix(res, q1)
    res = sum_matrix(res, q2, len(res) // 2)
    res = sum_matrix(res, q3, 0, len(res) // 2)
    res = sum_matrix(res, q4, len(res) // 2, len(res) // 2)

    for i in range(len(res)):
        res[i] = res[i][:orig_n]
    return res[:orig_n]


f = np.arange(1, 26).reshape(5, 5).tolist()
s = np.arange(25, 0, -1).reshape(5, 5).tolist()
print(*mult_usual(f, s), sep='\n', end='\n' * 2)
print(*mult_8(f, s), sep='\n', end='\n' * 2)
print(*mult_sht(f, s), sep='\n')
