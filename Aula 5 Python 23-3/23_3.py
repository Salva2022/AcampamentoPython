# -*- coding: utf-8 -*-
"""23-3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GHx_tmT-oZknbu9yGcJ7l5UmZsKcAHmx
"""

from random import randint
quantidade = int(input('Quantas dezenas você deseja jogar?: '))
resultado = []
cont = 0
print(f'Foram gerados os seguintes números:')
while cont < quantidade:
    n = randint(1, 60)
    if n not in resultado:
        cont += 1
        resultado.append(n)
    else:
        n = randint(1, 60)
print(*(sorted(resultado)), sep=' - ')