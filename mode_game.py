#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Callable, Mapping, Optional, List
import os
import datetime
import obsluga_bazy
import mode_stat as m_s
import config



def game() -> str:

    f = open("users_words\\" + config.nick + ".txt", "r", encoding="utf-8")
    learned_words: int = len(f.readlines())
    f.close()
    f = open("all_words.txt", "r", encoding="utf-8")
    all_words: int = len(f.readlines())
    f.close()
    if learned_words/all_words > 0.9:
        f = open("users_words\\" + config.nick + ".txt", "w", encoding="utf-8")
        f.write("")
        f.close()


    config.word: List[str] = obsluga_bazy.all_base.get_random_pair()
    f = open("users_words\\" + config.nick + ".txt", "r", encoding="utf-8")
    while str(config.word) in f.readlines():
        config.word = obsluga_bazy.all_base.get_random_pair()
    f.close()






                                      # typechoos = 1 nauka, 2 wpisywanie
    if config.langchoos == "polish":
        return config.word[0]
    elif config.langchoos == "english":
        return config.word[1]

def check1() -> str:
    if config.langchoos == "polish":
        return config.word[1]
    elif config.langchoos == "english":
        return config.word[0]

def check2(received_word: str) -> str:
    global eng_in_session, pol_in_session, words_in_session
    config.words_in_session += 1
    if config.langchoos == "polish":
        config.pol_in_session += 1
        if received_word == config.word[1]:
            f = open("users_words\\" + config.nick + ".txt", "a", encoding="utf-8")
            f.write(str(config.word) + " \n")
            f.close()
        return config.word[1]
    elif config.langchoos == "english":
        config.eng_in_session += 1
        if received_word == config.word[0]:
            f = open("users_words\\" + config.nick + ".txt", "a", encoding="utf-8")
            f.write(str(config.word) + " \n")
            f.close()
        return config.word[0]


def save_session():
    if config.langchoos == "polish":
        m_s.after_session(shown_words = config.words_in_session, pol_correct = config.pol_in_session)
    elif config.langchoos == "english":
        m_s.after_session(shown_words = config.words_in_session, eng_correct = config.eng_in_session)
    config.words_in_session = 0
    config.pol_in_session = 0
    config.eng_in_session = 0






"""

    points: int = 0

    for i in range(0, max_points):                  #Funkcja losuje słowo i sprawdza czy nie powtarza się z niedawno użytym
        word: List[str] =  obsluga_bazy.all_base.get_random_pair()
        f = open("users_words\\" + nick + ".txt" , "r", encoding="utf-8")
        while str(word) in f.readlines():
            print("powtórzone słowo" + str(word))
            word = obsluga_bazy.all_base.get_random_pair()
        #f.close()


        if mode == 1:
            if Foo(word[0]) == word[1]:        # Foo - nazwa tymczasowa
                points += 1
                f = open("users_words\\" + nick + ".txt", "a", encoding="utf-8")
                f.write(str(word) + " \n")
                f.close()
        elif mode == 2:
            if Foo(word[1]) == word[0]:        # Foo - nazwa tymczasowa
                points += 1
                f = open("users_words\\" + nick + ".txt", "a", encoding="utf-8")
                f.write(str(word) + " \n")
                f.close()
        elif mode == 3:
            Foo2(word[0] + " - " + word[1])     # Foo2 - nazwa tymczasowa

    f = open("statistics\\" + nick + ".txt", "a")
    f.write(str(datetime.datetime.now()) + " - " + str(points) + " \n")           #zapisanie liczby uzyskanych punktów do pliku
    f.close()
#---------------------------------------------------------------------------------------------------------------------------------




def Foo(word: str) -> str:                      #Funkcja tymczasowa do testowania kodu
    print(word)
    return input("")
#--------------------------------------------------------------------------------------------------------------------------------





def words_statistics() -> None:                 #Funkcja sterująca statystykami
    print(os.getcwd())
    folders = os.listdir("users_words")
    print(folders)
    for i in folders:
        print(i)
        f = open("users_words\\" + i, 'r', encoding="utf-8")
        lines: List[str] = f.readlines()
        f.close()

"""
