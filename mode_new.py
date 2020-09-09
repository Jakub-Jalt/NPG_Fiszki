#!/usr/bin/python
# -*- coding: utf-8 -*-


import datetime as dt
import mode_stat as mo_s
from os import listdir
from config import *


# funckja sprawdza, czy istnieją pliki dla użytkownika o nazwie zawartej w zmiennej "nick" z pliku "config"
# jeżeli nie ma - tworzy nowe


def check_user():
    files = [f for f in listdir('statistics')]
    for f in files:
        if f == f'{nick}.txt':  # funkcja znalazła pliki użytkownia - jego dane już istnieją
            mo_s.check_date()  # funkcja automatycznie aktualizyje plik ze statystyką przy logowaniu
            return

    today = dt.date.today()
    new_list = ''
    for d in range(positions):
        new_list += f'{(today - dt.timedelta(days=d)).isoformat()} 0 0 0 0\n'
    with open(f'statistics\\{nick}.txt', 'w', encoding='utf-8') as s_txt:
        s_txt.write(new_list[:-1])
    with open(f'user_words\\{nick}.txt', 'w', encoding='utf-8') as w_txt:
        w_txt.write('')
    return


if __name__ == "__main__":
    check_user()
