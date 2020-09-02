#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# import obsluga_bazy as b_sys


# funkcja dodająca do pliku z fiszkami nowy element
def add_words(p_word: str = '', a_word: str = ''):
    all_words = open('all_words.txt', 'a')
    all_words.write(f'{a_word}-{p_word}/n')
    all_words.close()
    return


# funkcja modyfikująca plik z fiszkami
def edit_words():
    pass

