from funcs import mult_usual, mult_sht, mult_8, format_table
import time
import numpy as np


def bench(algos: list[tuple], tests: list):
    if not tests:
        print('No tests provided.')
        return
    params = [f'Test {i + 1}' for i in range(len(tests))]
    if not algos:
        print('No algorithms provided.')
        return
    algos_names = [i[0] for i in algos]
    res = [[] for _ in algos]
    for i in range(len(algos)):
        for test in tests:
            start = time.time()
            _ = algos[i][1](test[0], test[1])
            res[i].append(time.time() - start)
    return format_table(algos_names, params, res)

f = np.arange(1, 37).reshape(6, 6).tolist()
s = np.arange(36, 0, -1).reshape(6, 6).tolist()
tests = [[f, s]]
# f = np.arange(1, 22501).reshape(150, 150).tolist()
# s = np.arange(22500, 0, -1).reshape(150, 150).tolist()
f = np.arange(1, 10001).reshape(100, 100).tolist()
s = np.arange(10000, 0, -1).reshape(100, 100).tolist()
tests.append([f, s])
print(bench([('Usual mult', mult_usual), ("Mult by 8 rec's", mult_8), ("Strassen's mult", mult_sht)], tests))
