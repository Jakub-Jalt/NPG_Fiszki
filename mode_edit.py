#!/usr/bin/python
# -*- coding: utf-8 -*-


import config


# funkcja dodaje słowa do pliku "all_words.txt"
# otrzymuje listę ze słowami, gdzie każda pozycja to jedno słowo (typu string)
# w ten sposób jedna para to pozycje o, odpowiednio, parzystym i nieparzystym indeksie (licząc od zera)
# następnie konwertuje do typu string i dodaje na koniec pliku "all_words.txt"


def add_words(words_list: []):
    all_words = open('all_words.txt', 'a', encoding='utf-8')
    lst_len = len(words_list)
    new_part = '\n'
    if config.langchoos == 'polish':  # trub polski - pierwsze zostaje podane słowo po polsku, drugie - po angielsku
        for i in range(0, lst_len, 2):
            new_part += f'{words_list[i + 1]}-{words_list[i]}\n'
    elif config.langchoos == 'english' or 'null':  # trub pangielski - pierwsze zostaje podane słowo po angielsku, drugie - po polsku
        for i in range(0, lst_len, 2):
            new_part += f'{words_list[i]}-{words_list[i + 1]}\n'
    else:
        return
    all_words.write(new_part[:-1])
    all_words.close()
    return


if __name__ == "__main__":
    add_words(['english', 'polish'])
