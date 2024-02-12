from subprocess import check_output as ch_out
from os import chdir, system, getcwd as pwd

iwd = pwd()
wd = input('WD: ')
if wd == '':
    wd = iwd
b = input('Bad commit: ')
g = input('Good commit: ')
auto = True if int(input('Manual (0) or auto (1)? ')) else False
a_command = input('Command for auto mode: ') if auto else None
chdir(wd)
lst = ch_out(['git', 'log', '--oneline']).splitlines()
length = len(lst)

while True:
    cent = length // 2
    if auto:
        system(f'git checkout {lst[cent][:6]}')
        chk = system(a_command)
    else:
        try:
            chk = int(input(f'Check {lst[cent]}. Bad (0) or good (1 or else) commit? '))
        except ValueError:
            print('NaN!')
            exit(1)
    if chk:
        lst = lst[:cent]
    else:
        lst = lst[cent:]
    length = len(lst)
    if len(lst) == 1:
        print(f'{lst[0]} is bad!')
        exit(0)
