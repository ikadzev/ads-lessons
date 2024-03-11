from subprocess import run, check_output as ch_out
from os import chdir, system, getcwd as pwd


def checkout(comm, prog, f, s):
    if s - f <= 1:
        return comm[f]
    cent = (s - f) // 2
    if prog:
        system(f'git checkout {comm[cent][:6]}')
        chk = run(prog, capture_output=False).returncode
        system('git checkout -')
    else:
        try:
            chk = int(input(f'Check "{comm[cent]}". Bad (0) or good (1 or else) commit? '))
        except ValueError:
            print('NaN!')
            exit(1)
    if chk:
        s = cent
    else:
        f = cent
    return checkout(lst, auto, f, s)


wd = input('WD: ')
if wd == '':
    wd = pwd()
b = input('Bad commit: ')
g = input('Good commit: ')
auto = True if int(input('Manual (0) or auto (1)? ')) else False
auto = input('Command for auto mode: ') if auto else None
chdir(wd)
if b != '':
    lst = ch_out(['git', 'log', '--oneline', f'{g}..{b}']).decode().splitlines()
else:
    lst = ch_out(['git', 'log', '--oneline']).decode().splitlines()
print(f'{checkout(lst, auto, 0, len(lst))} if bad!')
