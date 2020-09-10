#!/usr/bin/python
# -*- coding: utf-8 -*-


# import matplotlib.pylab as plt
import datetime as dt
import config


# funkcja aktualizuje pliki z danymi statystycznymi użytkownika

def check_date():
    def update(cur_day: dt.date, last_day: dt.date, w_file: []):
        dif = (cur_day - last_day).days
        if dif > config.positions:
            w_file.clear()
            for d in range(config.positions):
                new_list = [f'{(cur_day - dt.timedelta(days=d)).isoformat()} 0 0 0 0']
                w_file.extend(new_list)
        else:
            while dif > 0:
                dif -= 1
                new_list = [f'{(cur_day - dt.timedelta(days=dif)).isoformat()} 0 0 0 0']
                w_file = new_list + w_file
            w_file = w_file[:config.positions]
        return w_file

    def create_new(cur_day: dt.date, w_file: []):
        w_file.clear()
        for d in range(config.positions):
            new_list = [f'{(cur_day - dt.timedelta(days=d)).isoformat()} 0 0 0 0']
            w_file.extend(new_list)
        return w_file

    with open(f'statistics\\{config.nick}.txt', 'r', encoding='utf-8') as f:
        user_stats = f.read().split('\n')

    today = dt.date.today()
    if user_stats[0] == '':
        user_stats = create_new(today, user_stats)
    else:
        temp_var = user_stats[0].split(' ')[0].split('-')
        previous = dt.date(int(temp_var[0]), int(temp_var[1]), int(temp_var[2]))
        if previous > today:
            # data ostatniego logowania znajduje się chronologicznie poźniej niż data dzisiejsza (wg systemu)
            print('error occurred due to time travel - check your system time')
        elif previous < today:
            user_stats = update(today, previous, user_stats)

    new_part = ''
    for i in user_stats:
        new_part += f'{i}\n'

    with open(f'statistics\\{config.nick}.txt', 'w', encoding='utf-8') as f:
        f.write(new_part[:-1])
    return


# funkcja wyświetla wykres punktów z ostatnich 7 dni
# dostępna jest opcja dla wersji gry po polsku i po angielsku
#
# def show_plot():
#     with open(f'statistics\\{config.nick}.txt', 'r', encoding='utf-8') as f:
#         src = f.read().split('\n')
#     dates = []
#     pol_cor = []
#     eng_cor = []
#     for e in src[:7]:
#         i = e.split(' ')
#         temp_var = i[0].split('-')
#         temp_date = dt.date(int(temp_var[0]), int(temp_var[1]), int(temp_var[2]))
#         i[0] = temp_date.strftime('%b %d.')
#         dates += [i[0]]
#         pol_cor += [int(i[3])]
#         eng_cor += [int(i[4])]
#     if config.langchoos == 'polish':
#         plt.plot(dates, pol_cor, 'o-', color='green', alpha=0.5)
#         plt.ylim(0)
#         plt.grid(True, alpha=0.2)
#         plt.show()
#     elif config.langchoos == 'english' or 'null':
#         plt.plot(dates, eng_cor, 'o-', color='green', alpha=0.8)
#         plt.ylim(0)
#         plt.grid(True, alpha=0.2)
#         plt.show()
#     else:
#         pass
#     return


# funkcja zwraca zmienną string ze sformatowanym tekstem
# prezentującym dane statystyczne - wystarczy go wyświetlić

def show_stats_full():
    with open(f'statistics\\{config.nick}.txt', 'r', encoding='utf-8') as f:
        user_stats = f.read().split('\n')
    ret_file = 'data'.center(10) + '  ' + 'liczba'.center(10) + ' ' + 'liczba'.center(20) + ' ' +\
               'liczba odgadniętych słów'.center(26) + '\n' + 'rozgrywek'.center(10) + '  ' +\
               'rozgrywek'.center(10) + ' ' + 'wyświetlony słów'.center(20) + ' ' + 'po polsku'.center(12) +\
               '|' + 'po angielsku'.center(14) + '\n\n'
    for i in user_stats:
        temp_var = i.split(' ')
        ret_file += f'{temp_var[0].center(10)}   {temp_var[1].center(10)}' \
                    f'{temp_var[2].center(20)} {temp_var[3].center(13)} {temp_var[4].center(14)}\n'
    # print(ret_file)
    return ret_file


# funkcja aktualizująca statystyki po każdej grze
# 1. argument - liczba sesji (domyślnie 1)
# 2. argument - liczba wyświetlonych par do odgadnięcia
# 3. argument - liczba poprawnie odgadniętych par w trakcie jednej gry w wersji polskiej
# 4. argument - liczba poprawnie odgadniętych par w trakcie jednej gry w wersji angielskiej

def after_session(sessions: int = 1, shown_words: int = 0, pol_correct: int = 0, eng_correct: int = 0):
    with open(f'statistics\\{config.nick}.txt', 'r', encoding='utf-8') as f:
        user_stats = f.read().split('\n', 1)

    temp_var = user_stats[0].split(' ')
    temp_var[1] = f'{sessions + int(temp_var[1])}'
    temp_var[2] = f'{shown_words + int(temp_var[2])}'
    temp_var[3] = f'{pol_correct + int(temp_var[3])}'
    temp_var[4] = f'{eng_correct + int(temp_var[4])}'
    user_stats[0] = f'{temp_var[0]} {temp_var[1]} {temp_var[2]} {temp_var[3]} {temp_var[4]}\n'

    new_part = f'{user_stats[0]}{user_stats[1]}'
    with open(f'statistics\\{config.nick}.txt', 'w', encoding='utf-8') as f:
        f.write(new_part)
    return


# if __name__ == "__main__":
#     pass
