def pol(prompt):
    priority = {'^': 0, '*': 1, '/': 1, '+': 2, '-': 2, '<<': 3, '>>': 3, '<': 4, '<=': 4, '>': 4, '>=': 4, '&': 5,
                '|': 6, '&&': 7, '||': 8}
    ret = []
    cnt_brk = []
    stk = []
    prompt = prompt.split()
    for lex in prompt:
        if lex.isnumeric():
            ret.append(lex)
        elif lex == '(':
            cnt_brk.append(0)
        elif lex == ')':
            while cnt_brk[-1] != 0:
                ret.append(stk.pop())
                cnt_brk[-1] -= 1
            cnt_brk = cnt_brk[-1]
        else:
            if stk:
                if cnt_brk and cnt_brk[-1] == 0:
                    stk.append(lex)
                    cnt_brk[-1] += 1
                    continue
                while priority[lex] > priority[stk[-1]]:
                    ret.append(stk.pop())
                    if cnt_brk:
                        cnt_brk[-1] -= 1
            stk.append(lex)
            if cnt_brk:
                cnt_brk[-1] += 1
    while stk:
        ret.append(stk.pop())
    return ret


inp = input('Введите пример через пробелы: ')
# inp = '1 + 3 * ( 5 ^ 2 )'
print(*pol(inp), sep=' ')
