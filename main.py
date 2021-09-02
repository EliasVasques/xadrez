import style, peças, xeque_mate
from random import shuffle
# OTIMIZAR FUNÇÕES DE VERIF SE PODE IR, XEQUE E XEQUE-MATE
tabuleiro = [
             ['t1p', 'c1p', 'b1p', 'r0p', 'R0p', 'b2p', 'c2p', 't2p'],
             ['p1p', 'p2p', 'p3p', 'p4p', 'p5p', 'p6p', 'p7p', 'p8p'],
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
             ['p1b', 'p2b', 'p3b', 'p4b', 'p5b', 'p6b', 'p7b', 'p8b'],
             ['t1b', 'c1b', 'b1b', 'r0b', 'R0b', 'b2b', 'c2b', 't2b']
]
vez = True
pode = False
time = 'brancas'
cor = 'b'
jogadores = []     # NOME DOS PLAYERS
jogadores.append(str(input('Jogador 1: ')))
jogadores.append(str(input('Jogador 2: ')))
shuffle(jogadores)                                # ALEATÓRIO, o que ficar no índice 0 vai ser as brancas
while True:
    verifMate = xeque_mate.xeque_mate(tabuleiro, cor)
    if verifMate:
        style.exibir(tabuleiro, jogadores)
        print('Xeque-mate!')
        break
    style.titulo(f'Vez das {time}')
    while True:
        style.exibir(tabuleiro, jogadores)
        encontrado = False      # NOME e COORDENADA
        while True:
            peça = str(input('Qual peça você quer mexer? '))
            peça = peça + cor  # só pode mover peça sua
            for l in range(8):
                for c in range(8):
                    if '   ' != tabuleiro[l][c] == peça:
                        encontrado = True
                        lPeça = l
                        cPeça = c
            if encontrado:
                break
            else:
                print('Digite uma peça válida!')
                print('_' * 32)

        linhas = ['8', '7', '6', '5', '4', '3', '2', '1']  # LER ONDE POR E CONVERTE
        letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        while True:
            posicao = str(input('Pra onde? ')).strip()
            if len(posicao) == 2 and posicao[0] in letras and posicao[1] in linhas:   # ordem em 36 e 37
                lPor = linhas.index(posicao[1])        # digitou 8 quer linha 0...
                cPor = letras.index(posicao[0])
                break
            else:
                print('Digite uma coordenada válida!')
                print('_' * 32)

                # CHAMANDO FUNÇÕES PRA VERIFICAR SE PODE
        if peça[0] == 'R':  # REI
            possibilidades = peças.re(tabuleiro, cor, lPeça, cPeça)
        elif peça[0] == 'p':  # PEÃO
            possibilidades = peças.pe(tabuleiro, cor, lPeça, cPeça)
        elif peça[0] == 'c':  # CAVALO
            possibilidades = peças.ca(tabuleiro, cor, lPeça, cPeça)
        elif peça[0] == 't':  # TORRE
            possibilidades = peças.to(tabuleiro, cor, lPeça, cPeça)
        elif peça[0] == 'b':  # BISPO
            possibilidades = peças.bi(tabuleiro, cor, lPeça, cPeça)
        elif peça[0] == 'r':  # RAINHA
            torre = peças.to(tabuleiro, cor, lPeça, cPeça)
            bispo = peças.bi(tabuleiro, cor, lPeça, cPeça)
            possibilidades = torre + bispo
        print(possibilidades)

        for p in possibilidades:  # p: lista com linha e coluna
            l, c = p[0], p[1]
            if l == lPor and c == cPor:  # uma das opções é onde ele quer por
                pode = True


        if pode:
            pode = False
            tabAux = []
            for lista in tabuleiro:   # SEM LIGAÇÃO ENTRE AS LISTA, [:] e .copy() direto na matriz não funcionava
                tabAux.append(lista.copy())
            for l in range(8):
                for c in range(8):
                    if tabAux[l][c] == peça:  # onde tá a peça fica vazio
                        tabAux[l][c] = '   '
            tabAux[lPor][cPor] = peça  # pondo peça no lugar
            xeque = peças.xeque(tabAux, cor)              # CHEQUE
            if xeque:
                print('Rei em xeque! Proteja-o')
                print('_' * 32)
            else:
                tabuleiro = tabAux
                break
        else:
            print('Não pode mover pra essa posição! Vamos tentar novamente.')
            print('_' * 32)
    vez = not vez                               # MUDANÇA DE VEZ
    if vez:
        time = 'brancas'
        cor = 'b'
    else:
        time = 'pretas'
        cor = 'p'
if cor == 'b':  # AS PRETAS VENCEM: pq as pretas deram cheque, aí trocou de cor
    jogVenc = jogadores[0]
else:           # BRANCAS VENCEM
    jogVenc = jogadores[1]
print(f'Vitória de {jogVenc}')

