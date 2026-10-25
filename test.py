from utils import *
from datetime import date
from rich.console import Console
#------------sistema------------
print(end='')
quantidade_de_jogadors = pergunta('Quantos jogadores vão jogar?: ')
ranking = Ranking()
for c in range(1,quantidade_de_jogadors+1):
    nome = input(f'Nome do {c}° jogador: ')
    ranking.add_competidores(nome)
a = pergunta('Até quantas vitórias?: ')
while True:
    finalizador = 0
    print('\n'*60)
    Resumo(ranking).lista_votar()
    for c in ranking.retornador():
        for k, v in c.items():
            if v == a:
                finalizador += 1
    if finalizador == 1:
        break
console = Console(record=True)
conteudo = ''
dado = str(date.today()).split('-')[::-1]
for c in dado:
    if dado.index(c) == len(dado)-1:
        conteudo += c
    else:
        conteudo += f'{c}/'
console.print(conteudo, end=' ')
console.log()
console.print(ranking.rank(True), '\n'*5)
console.save_text('texto.txt')
a = str(open('texto.txt', 'r'))
b = open('dados.txt', 'a')
b.write(a)
