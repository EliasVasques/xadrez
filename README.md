# Avaliação I da disciplina de testes de software no Senai

Entregar o projeto contendo a resolução dos katas listados abaixo e validando as implementações através de testes automatizados necessários para cada kata.

## Kata OHCE (adaptado)

Criar uma função `ohce()` que receberá uma string e, caso a string seja um palíndromo, retorne a expressão “Gostei da palavra!”. Não sendo um palíndromo, retornar a string invertida. Por exemplo: ohce("casa") deve retornar "asac" e ohce("arara") deve retornar "Gostei da palavra!".

## Kata calculador de string (adaptado)

Implementar uma função `stringCalculator()` que receba uma string com números separados por vírgula e retorne a soma deles. Por exemplo: “1,2,3” deve retornar o número 6.

Deve lançar uma exceção caso algum número passado seja negativo
Números maiores do que 1000 devem ser ignorados. Por exemplo: 5 + 2000 = 5

## Kata de placar de jogo de basquete (adaptado)

Criar um programa que irá entregar o número do placar para um jogo de basquete. Dito isto, deve haver seis botões onde cada time poderá marcar 1, 2 ou 3 pontos.

Escreva uma classe *ScoreKeeper* com os seguintes métodos:

```javascript
void scoreTeamA1()
void scoreTeamA2()
void scoreTeamA3()
void scoreTeamB1()
void scoreTeamB2()
void scoreTeamB3()
String getScore()
```

O método getScore() deve sempre retornar uma string com sete caracteres. Por exemplo: “000:000”

## Passos para executar os testes na aplicação

1. Instalar o NodeJS (<https://nodejs.org/>)
2. Instale as dependências executando o comando `npm install`
3. Por fim, executar o comando `npm test`

O projeto deverá ser entregue até o dia 10/03/2022. Passar o link do repositório para o e-mail **douglas.silva@ba.docente.senai.br** com o título Atividade Avaliativa 1 – Seu Nome (Ex.: Atividade Avaliativa 1 – João Batista)

<!-- markdownlint-disable MD026 -->
## Bom estudo a todos!!!
