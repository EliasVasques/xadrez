def xeque(tabuleiro, cor):        # o problema tá na cor
    for linha in range(8):
        for coluna in range(8):
            if tabuleiro[linha][coluna][0] == 'R' and tabuleiro[linha][coluna][2] == cor:
                l_rei = linha
                c_rei = coluna

    rei_opções = re(tabuleiro, cor, l_rei, c_rei)  # rainha: bispo e torre
    for casa in rei_opções: # CASAS É UMA LISTA COM LINHA E COLUNA
        l, c = casa[0], casa[1]
        if tabuleiro[l][c][0] == 'R' and tabuleiro[l][c][2] != cor:    # INIMIGOS
            #print(f'l: {l} | c: {c}')
            return True
    peão_opções = pe(tabuleiro, cor, l_rei, c_rei)
    for casa in peão_opções: # CASAS É UMA LISTA COM LINHA E COLUNA
        l, c = casa[0], casa[1]
        if tabuleiro[l][c][0] == 'p' and tabuleiro[l][c][2] != cor:
            #print(f'l: {l} | c: {c}')
            return True
    cavalo_opções = ca(tabuleiro, cor, l_rei, c_rei)
    for casa in cavalo_opções: # CASAS É UMA LISTA COM LINHA E COLUNA
        l, c = casa[0], casa[1]
        if tabuleiro[l][c][0] == 'c' and tabuleiro[l][c][2] != cor:
            #print(f'l: {l} | c: {c}')
            return True
    torre_opções = to(tabuleiro, cor, l_rei, c_rei)
    for casa in torre_opções: # CASAS É UMA LISTA COM LINHA E COLUNA
        l, c = casa[0], casa[1]
        if tabuleiro[l][c][0] == 't' or tabuleiro[l][c][0] == 'r' and tabuleiro[l][c][2] != cor:
            #print(f'l: {l} | c: {c}')
            return True
    bispo_opções = bi(tabuleiro, cor, l_rei, c_rei)
    for casa in bispo_opções: # CASAS É UMA LISTA COM LINHA E COLUNA
        l, c = casa[0], casa[1]
        if tabuleiro[l][c][0] == 'b' or tabuleiro[l][c][0] == 'r' and tabuleiro[l][c][2] != cor:
            #print(f'l: {l} | c: {c}')
            return True
    return False


def pe(tab, cor, linha, coluna):
    opções = []
    if cor == 'b':
        l = linha - 1
    else:
        l = linha + 1
    # COMER
    if coluna != 7:
        c = coluna + 1
        if ' ' != tab[l][c][2] != cor:  # INIMIGO
            opções.append([l, c])
    if coluna != 0:
        c = coluna - 1
        if ' ' != tab[l][c][2] != cor:
            opções.append([l, c])
    # AVANÇAR
    if cor == 'b':
        linha_dois_avancos = 6
    else:
        linha_dois_avancos = 1
    c = coluna
    if tab[l][c][2] == ' ':  # JÁ AVANÇOU UMA LINHA NO INÍCIO DA FUNÇÃO
        opções.append([l, c])
        if linha_dois_avancos == linha:
            if cor == 'b':
                l = l - 1
            else:
                l = l + 1
            if tab[l][c][2] == ' ':
                opções.append([l, c])
    return opções


def ca(tab, cor, linha, coluna):
    opções = []
    for x in range(8):
        if x == 0 or x == 4:  # possíveis opções de sinais
            operador1 = '+'
            operador2 = '-'
        if x == 1 or x == 5:
            operador1 = '-'
            operador2 = '+'
        if x == 2 or x == 6:
            operador1 = '+'
            operador2 = '+'
        if x == 3 or x == 7:
            operador1 = '-'
            operador2 = '-'
        if x <= 3:  # ordem dos números
            n1 = '1'
            n2 = '2'
        else:
            n1 = '2'
            n2 = '1'
        l = eval(str(linha) + operador1 + n1)
        c = eval(str(coluna) + operador2 + n2)
        if 0 <= l <= 7 and 0 <= c <= 7:
            if tab[l][c][2] != cor:  # VAZIO OU INIMIGO
                opções.append([l, c])
    return opções


def to(tab, cor, linha, coluna):
    opções = []
    # BAIXO
    l = linha
    c = coluna
    while True:
        l = l + 1
        if l > 7:  # até aqui foi '+'
            break
        # POSSIBILIDADES
        if tab[l][c][2] == cor:  # MESMO TIME
            break
        elif tab[l][c][2] == ' ':  # VAZIA
            opções.append([l, c])
        else:                      # INIMIGO
            opções.append([l, c])
            break
    # CIMA
    l = linha
    c = coluna
    while True:
        l = l - 1
        if l < 0:  # até aqui foi '+'
            break
        # POSSIBILIDADES
        if tab[l][c][2] == cor:  # MESMO TIME
            break
        elif tab[l][c][2] == ' ':  # VAZIA
            opções.append([l, c])
        else:  # INIMIGO
            opções.append([l, c])
            break
    # DIREITA
    l = linha
    c = coluna
    while True:
        c = c + 1
        if c > 7:  # até aqui foi '+'
            break
        # POSSIBILIDADES
        if tab[l][c][2] == cor:  # MESMO TIME
            break
        elif tab[l][c][2] == ' ':  # VAZIA
            opções.append([l, c])
        else:  # INIMIGO
            opções.append([l, c])
            break
    # ESQUERDA
    l = linha
    c = coluna
    while True:
        c = c - 1
        if c < 0:  # até aqui foi '+'
            break
        # POSSIBILIDADES
        if tab[l][c][2] == cor:  # MESMO TIME
            break
        elif tab[l][c][2] == ' ':  # VAZIA
            opções.append([l, c])
        else:  # INIMIGO
            opções.append([l, c])
            break
    return opções


def bi(tab, cor, linha, coluna):
    # / SUBINDO
    opções = []
    l = linha
    c = coluna
    while True:
        l -= 1
        c += 1
        # POSSIBILIDADES
        if l < 0 or c > 7:
            break
        # POSSIBILIDADES
        if tab[l][c][2] == cor:  # MESMO TIME
            break
        elif tab[l][c][2] == ' ':  # VAZIA
            opções.append([l, c])
        else:  # INIMIGO
            opções.append([l, c])
            break
    # / DESCENDO
    l = linha
    c = coluna
    while True:
        l += 1
        c -= 1
        # POSSIBILIDADES
        if l > 7 or c < 0:
            break
        # POSSIBILIDADES
        if tab[l][c][2] == cor:  # MESMO TIME
            break
        elif tab[l][c][2] == ' ':  # VAZIA
            opções.append([l, c])
        else:  # INIMIGO
            opções.append([l, c])
            break
    # \ SUBINDO
    l = linha
    c = coluna
    while True:
        l -= 1
        c -= 1
        # POSSIBILIDADES
        if l < 0 or c < 0:
            break
        # POSSIBILIDADES
        if tab[l][c][2] == cor:  # MESMO TIME
            break
        elif tab[l][c][2] == ' ':  # VAZIA
            opções.append([l, c])
        else:  # INIMIGO
            opções.append([l, c])
            break
    # \ DESCENDO
    l = linha
    c = coluna
    while True:
        l += 1
        c += 1
        # POSSIBILIDADES
        if l > 7 or c > 7:
            break
        # POSSIBILIDADES
        if tab[l][c][2] == cor:  # MESMO TIME
            break
        elif tab[l][c][2] == ' ':  # VAZIA
            opções.append([l, c])
        else:  # INIMIGO
            opções.append([l, c])
            break
    return opções


def re(tab, cor, linha, coluna):
    opções = []
    l = linha + 1  # BAIXO: 0, 1, 2
    for cont in range(8):
        if 3 <= cont <= 5:  # CIMA: 3, 4, 5
            l = linha - 1
        elif cont > 5:   # MESMA LINHA: 6, 7
            l = linha
        if cont == 0 or cont == 3:
            c = coluna
        elif cont == 1 or cont == 4 or cont == 6:
            c = coluna - 1
        elif cont == 2 or cont == 5 or cont == 7:
            c = coluna + 1
        if 0 <= l <= 7 and 0 <= c <= 7:
            if tab[l][c][2] != cor:    # INIMIGO OU VAZIO
                opções.append([l, c])
    return opções


