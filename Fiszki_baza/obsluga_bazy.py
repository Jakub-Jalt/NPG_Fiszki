#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

list = open('random_words_ang.txt').read().split() # lista wszystkich elementów pliku bazy
n_of_words = len(list)
n_of_pairs = int(n_of_words/2)

list_only_ang = []      # lista tylko angielskich słow
i = 0
while i < n_of_words:
    if i % 2 == 0:
        list_only_ang.append(list[i])
    i += 1

list_only_pl = []       # lista tylko polskich słow
i = 0
while i < n_of_words:
    if i % 2 == 1:
        list_only_pl.append(list[i])
    i += 1

list_of_pairs_numbered = {}
k = 0
i = 0
while i < n_of_words:
    v = [list[i], list[i+1]]
    list_of_pairs_numbered[k] = v
    i += 2
    k += 1


# funkcja zwraca n-tą pare słów jako lista
def get_pair_by_n(n: int) -> list:
    return list_of_pairs_numbered[n]


# funkcja zwraca losowe angielskie slowo
def get_rand_ang() -> str:
    r = random.randint(0, len(list_only_ang) - 1)
    return list_only_ang[r]


# funkcja zwraca losowe polskie slowo
def get_rand_pl() -> str:
    r = random.randint(0, len(list_only_pl) - 1)
    return list_only_pl[r]


# funkcja zwraca losowa pare slow jako lista 2-elementowa
def get_rand_pair() -> list:
    r = random.randint(0, n_of_pairs - 1)
    return list_of_pairs_numbered[r]


# print(get_rand_pl())
# print(get_rand_ang())
# print(get_rand_pair())