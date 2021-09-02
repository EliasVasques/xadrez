def titulo(msg):
    print('-'*32)
    print(msg.center(32))
    print('-'*32)


def exibir(tabuleiro, jog):
    casa = True
    cont = 8
    print('  |', jog[0], ' |')
    for l in tabuleiro:
        print(f'{cont} ', end='')
        for c in l:
            # fundo
            if casa:
                print('\033[1;47m', end='')   # cinza claro
            else:
                print('\033[1;100m', end='')  # cinza escuro
            # cor
            if c[2] == 'p':
                print(f'{c[0:2]:^4}\033[m', end='')        # sem modificar
            else:
                print(f'\033[1;97m{c[0:2]:^4}\033[m', end='') # cor branca
            casa = not casa
        print()
        cont -= 1
        casa = not casa                                         # alternar cor
    # printando as letras
    print('  ', end='')
    vogal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for v in vogal:
        print(f'{v:^4}', end='')
    print('\n  |', jog[1], ' |')

