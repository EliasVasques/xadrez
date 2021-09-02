import peças


                                   # se nenhum movimento que possa salvar deixa de ser xeque, ent xeque-mate
def xeque_mate(tabuleiro, cor):     # chamar quando estiver em cheque pra verificar se é cheque-mate
    xeque = peças.xeque(tabuleiro, cor)   # REI EM XEQUE?
    if not xeque:
        return False
    peça = '   '
    opções = list()
    for linha in range(8):   # LINHAS
        for coluna in range(8):     # CASAS
            if tabuleiro[linha][coluna][2] == cor:    # SÓ PEÇAS ALIADAS
                peça = tabuleiro[linha][coluna]

                if peça[0] == 'R':
                    opções = peças.re(tabuleiro, cor, linha, coluna)  # rainha: bispo e torre
                if peça[0] == 'r':
                    torre = peças.to(tabuleiro, cor, linha, coluna)
                    bispo = peças.bi(tabuleiro, cor, linha, coluna)
                    opções = torre + bispo
                if peça[0] == 't':
                    opções = peças.to(tabuleiro, cor, linha, coluna)  # rainha: bispo e torre
                if peça[0] == 'b':
                    opções = peças.bi(tabuleiro, cor, linha, coluna)  # rainha: bispo e torre
                if peça[0] == 'c':
                    opções = peças.ca(tabuleiro, cor, linha, coluna)  # rainha: bispo e torre
                if peça[0] == 'p':
                    opções = peças.pe(tabuleiro, cor, linha, coluna)  # rainha: bispo e torre
                #print(opções)

                # VERFICANDO
                for opção in opções:        # opção é uma lista com coordenada
                    tabAux = []  # CÓPIA DE TABULEIRO
                    for lista in tabuleiro:  # SEM LIGAÇÃO ENTRE AS LISTA, [:] e .copy() N FUNCIONOU
                        tabAux.append(lista.copy())
                    for lin in range(8):          # FICA VAZIO ONDE TAVA
                        for col in range(8):
                            if tabAux[lin][col] == peça:  # onde tá a peça fica vazio
                                tabAux[lin][col] = '   '
                                break
                    tabAux[opção[0]][opção[1]] = peça
                    xeque = peças.xeque(tabAux, cor)  # teste
                    if not xeque:  # não é cheque mate, ou seja, tem saída nesse movimento
                        return False
                    #style.exibir(tabAux, ['Elias', 'Joana'])
                opções.clear()
    return True