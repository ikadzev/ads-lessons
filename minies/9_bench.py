from funcs import mult_usual, mult_sht, mult_8, format_table
import time
import numpy as np


def bench(algos: list[tuple], tests: list):
    if not tests:
        print('No tests provided.')
        return
    params = [str(len(tests[i][0])) for i in range(len(tests))]
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


test = []
for i in range(300, 301, 1):
    f = np.arange(1, i ** 2 + 1).reshape(i, i).tolist()
    s = np.arange(i ** 2, 0, -1).reshape(i, i).tolist()
    test.append([f, s])

print(bench([('Usual mult', mult_usual), ("Strassen's mult", mult_sht)], test))
