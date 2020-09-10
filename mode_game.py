#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List
import database
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


    config.word: List[str] = database.all_base.get_random_pair()
    f = open("users_words\\" + config.nick + ".txt", "r", encoding="utf-8")
    while str(config.word) in f.readlines():
        config.word = database.all_base.get_random_pair()
    f.close()

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

        if received_word == config.word[1]:
            config.pol_in_session += 1
            f = open("users_words\\" + config.nick + ".txt", "a", encoding="utf-8")
            f.write(str(config.word) + " \n")
            f.close()
        return config.word[1]
    elif config.langchoos == "english":

        if received_word == config.word[0]:
            config.eng_in_session += 1
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




