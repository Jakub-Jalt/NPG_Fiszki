#!/usr/bin/python
# -*- coding: utf-8 -*-

# funkcja "update" nie jest jeszcze gotowa


import datetime as dt


class Steve:

    def __init__(self, stat_list: str):
        self.stat_list = stat_list.replace('\n', ' ').split(' ')

    def check_day(self):

        def update(cur_day: dt.date, last_day: dt.date):  # funkcja nie jest jeszcze gotowa !!!
            dif = (cur_day - last_day).days
            if dif > 30:
                pass
            while dif > 0:
                dif -= 1
            return

        today = dt.date.today()
        temp_var = self.stat_list[0].split('-')
        previous = dt.date(int(temp_var[0]), int(temp_var[1]), int(temp_var[2]))
        if previous > today:
            print('error occurred due to time travel - check your system time')
        elif previous < today:
            update(today, previous)
        return

    def ret_stat(self):
        temp_var = ''
        for i in range(0, 2 * 30, 2):
            temp_var += f'{self.stat_list[i]} {self.stat_list[i+1]}\n'
        temp_var = temp_var[:-1]
        return temp_var


if __name__ == "__main__":
    user = input('enter user name: ')
    with open(f'statistics\\{user}.txt', 'r', encoding='utf-8') as user_stats:
        new = Steve(user_stats.read())
    new.check_day()
    with open(f'statistics\\{user}.txt', 'w', encoding='utf-8') as user_stats:
        user_stats.write(new.ret_stat())
