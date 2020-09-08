#!/usr/bin/python
# -*- coding: utf-8 -*-


import datetime as dt
from config import *


# funkcja aktualizuje pliki z danymi statystycznymi użytkownika

def check_date():
    def update(cur_day: dt.date, last_day: dt.date, w_file: []):
        dif = (cur_day - last_day).days
        if dif > positions:
            w_file.clear()
            for d in range(positions):
                new_list = [f'{(today - dt.timedelta(days=d)).isoformat()}', '0', '0', '0']
                w_file.extend(new_list)
        else:
            while dif > 0:
                dif -= 1
                new_list = [f'{(today - dt.timedelta(days=dif)).isoformat()}', '0', '0', '0']
                w_file = new_list + w_file
            w_file = w_file[:positions * 4]
        return w_file

    with open(f'statistics\\{nick}.txt', 'r', encoding='utf-8') as f:
        user_stats = f.read().replace('\n', ' ').split(' ')

    today = dt.date.today()
    temp_var = user_stats[0].split('-')
    previous = dt.date(int(temp_var[0]), int(temp_var[1]), int(temp_var[2]))
    if previous > today:
        # data ostatniego logowania znajduje się chronologicznie poźniej niż data dzisiejsza (wg systemu)
        print('error occurred due to time travel - check your system time')
    elif previous < today:
        user_stats = update(today, previous, user_stats)

    new_part = ''
    for i in range(0, positions * 4, 4):
        new_part += f'{user_stats[i]} {user_stats[i + 1]} {user_stats[i + 2]} {user_stats[i + 3]}\n'

    with open(f'statistics\\{nick}.txt', 'w', encoding='utf-8') as f:
        f.write(new_part[:-1])
    return


# funkcja zwraca listę z dany statystycznymi użytkownika
# każda kolejna czwórka elementów listy to jedna pozycja pliku:
# 1 - data dnia rozgrywek
# 2 - liczba łącznie poprawnie odgadniętych słów
# 3 - liczba łącznie wyświetlonych słów
# 4 - liczba sesji

def show_stats():
    with open(f'statistics\\{nick}.txt', 'r', encoding='utf-8') as f:
        user_stats = f.read().replace('\n', ' ').split(' ')
    return user_stats


# funkcja aktualizująca statystyki po każdej grze
# 1. argument - liczba poprawnie odgadniętych w trakcie jednej gry
# 2. argument - liczba wyświetlonych para do odgadnięcia
# 3. argument - liczba sesji (domyślnie 1)

def after_session(co: int = 0, sh: int = 14, se: int = 1):
    with open(f'statistics\\{nick}.txt', 'r', encoding='utf-8') as f:
        user_stats = f.read().split('\n', 1)

    temp_var = user_stats[0].split(' ')
    temp_var[1] = f'{co + int(temp_var[1])}'
    temp_var[2] = f'{sh + int(temp_var[2])}'
    temp_var[3] = f'{se + int(temp_var[3])}'
    user_stats[0] = f'{temp_var[0]} {temp_var[1]} {temp_var[2]} {temp_var[3]}\n'

    new_part = f'{user_stats[0]}{user_stats[1]}'
    with open(f'statistics\\{nick}.txt', 'w', encoding='utf-8') as f:
        f.write(new_part)
    return
