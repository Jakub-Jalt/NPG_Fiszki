#!/usr/bin/python
# -*- coding: utf-8 -*-

import random


class Base:
    def __init__(self, words_lst: list):
        self.words_lst = words_lst

    def n_of_words(self) -> int:
        return len(self.words_lst)

    def get_lst_of_pairs(self) -> list:
        lst_of_pairs = []
        i = 0
        while i < self.n_of_words():
            v = [self.words_lst[i], self.words_lst[i+1]]
            lst_of_pairs.append(v)
            i += 2
        return lst_of_pairs

    def get_random_pair(self) -> list:
        x = random.randint(0, len(self.get_lst_of_pairs()) - 1)
        return self.get_lst_of_pairs()[x]

    def get_all_only_pl(self) -> list:
        only_pl = []
        i = 0
        for elem in self.words_lst:
            if i % 2 == 1:
                only_pl.append(elem)
            i += 1
        return only_pl

    def get_all_only_ang(self) -> list:
        only_ang = []
        i = 0
        for elem in self.words_lst:
            if i % 2 == 0:
                only_ang.append(elem)
            i += 1
        return only_ang

    def get_random_ang(self) -> str:
        all_ang = self.get_all_only_ang()
        x = random.randint(0, len(all_ang))
        return all_ang[x]

    def get_random_pl(self) -> str:
        all_pl = self.get_all_only_pl()
        x = random.randint(0, len(all_pl))
        return all_pl[x]


easy = open('easy_words.txt').read().replace("\n", "-").split("-")
easy_base = Base(easy)
# print(easy_base.get_lst_of_pairs())
# print(easy_base.get_random_pair())
# print(easy_base.get_all_only_pl())
# print(easy_base.get_all_only_ang())
# print(easy_base.get_random_ang())
# print(easy_base.get_random_pl())

all = open('all_words.txt').read().replace("\n", "-").split("-")
all_base = Base(all)

# zeby dostac slowo z duzej litery
print(all_base.get_random_pl().capitalize())
print(all_base.get_random_ang().capitalize())