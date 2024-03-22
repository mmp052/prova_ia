# Autor
Mateus Moreira Pereira

## Questão 1
1 - Os estados visitados em uma BL são 1; 2; 3; 4; 5; 6; 7; 8; 9; 10; 11

2 - Os estados visitados em uma BP com m=3 são 1; 2; 4; 8; 9; 5; 10; 11

3 - Os estados visitados em uma A* são 1; 3; 7; 6; 2; 5; 11

## Questão 2
### Parte 1
1 - cada cidade gera entre 1 a 4 successores

2 - a profundidade máxima é profundidade 5

3 - $n^0 + n^1 + n^2 + n^3 + n^4 + n^5$

Onde $n$ é o numero de sucessores do nodo que como dito acima varia de 1 a 4

4 - 
- cidade_atual = cidade onde meu agente está no momento
- km = km pra ir para aquela cidade
- cidade_meta = cidade onde quero chegar
- mapa = um dicionario indicando as possiveis rotas de cada cidade os custos e se é uma cidade estratégica e se é um terminal de carga
- transportando_carga = um boleano indicando se está tranportando carga, já que se está precisa parar em uma cidade terminal de carga antes de ir pra cidade meta
- carga = um boleano indicando se passou pelo terminal de carga
- passar_estrategica = boleano que indica se precisa passar por uma cidade estratégica
- estrategica = boleano que indica se já passou por uma cidade estratégica

### Parte 2
1 -  sair de São Paulo ; ir para Sorocaba ; ir para Campinas ; ir para Piracicaba
131.5

2 - sair de Taubaté ; ir para Ubatuba ; ir para São José dos Campos ; ir para São Paulo ; ir para Jundiaí ; ir para Campinas ; ir para Piracicaba
248.0

3 - sair de Sorocaba ; ir para Campinas ; ir para Piracicaba
79.5

4 - sair de Taubaté ; ir para Ubatuba ; ir para São José dos Campos ; ir para São Paulo ; ir para Sorocaba ; ir para Campinas
260.5

5 - sair de Taubaté ; ir para São José dos Campos ; ir para São Paulo ; ir para Jundiaí ; ir para Campinas
116.5

## Questão 3
Eu faria a distancia em linha reta entre as cidades, ja que pensando em um cenário onde eu possa ir reto eu vou andar menos logo, gastando menos Co2.

A equação seria: 
(x_cidade_meta - x_cidade_atual) + (y_cidade_meta - y_cidade_atual)

O x e o y eu pegaria com a latitude e longitude das cidades
