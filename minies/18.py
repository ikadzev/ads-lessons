def pol(prompt):
    priority = {'^': (0, False), '*': (1, True), '/': (1, True), '+': (2, True), '-': (2, True), '<<': (3, True),
                '>>': (3, True), '<': (4, True), '<=': (4, True), '>': (4, True), '>=': (4, True), '&': (5, True),
                '|': (6, True), '&&': (7, True), '||': (8, True)}
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
            cnt_brk = cnt_brk[:-1]
        else:
            if stk:
                if cnt_brk and cnt_brk[-1] == 0:
                    stk.append(lex)
                    cnt_brk[-1] += 1
                    continue
                while stk and priority[lex][0] >= priority[stk[-1]][0] and priority[lex][1]:
                    ret.append(stk.pop())
                    if cnt_brk:
                        cnt_brk[-1] -= 1
            stk.append(lex)
            if cnt_brk:
                cnt_brk[-1] += 1
    while stk:
        ret.append(stk.pop())
    return ret


test = '1 + 2 ^ 3 + 4'
print(pol(test))

