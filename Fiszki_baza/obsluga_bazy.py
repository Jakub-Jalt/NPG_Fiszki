#!/usr/bin/python
# -*- coding: utf-8 -*-

list = open('random_words_ang.txt').read().split()
n_of_words = len(list)
n_of_pairs = n_of_words/2

dict_by_n = {}

i = 0
while i < n_of_pairs:
    v = [list[i], list[i+1]]
    dict_by_n[i] = v
    i += 2


#funkcja zwraca n-tą pare słów jako lista
def get_pair_by_n(n: int):
    return dict_by_n[n]