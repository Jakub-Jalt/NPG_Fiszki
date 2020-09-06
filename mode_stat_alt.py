#!/usr/bin/python
# -*- coding: utf-8 -*-


import datetime as dt


class Steve:

    def __init__(self, stat_list: str):
        self.stat_list = stat_list.split(' ')
        if self.stat_list[-1] == '\n':
            self.stat_list = self.stat_list[:-1]

    def check_day(self):

        def update(cur_day: dt.date, last_day: dt.date):
            dif = (cur_day - last_day).days
            if dif > 30:
                new_list = ['0'] * 30
                self.stat_list = [today.isoformat()] + new_list
            else:
                new_list = ['0'] * dif
                self.stat_list = [today.isoformat()] + new_list + self.stat_list[1:-dif]
            return

        today = dt.date.today()
        temp_var = self.stat_list[0].split('-')
        previous = dt.date(int(temp_var[0]), int(temp_var[1]), int(temp_var[2]))
        if previous > today:
            print('error occurred due to time travel - check your system time')
        elif previous < today:
            update(today, previous)
        return

    def show(self):
        temp_var = f'today\'date: {self.stat_list[0]}\n'
        for p in range(1, 31):
            temp_var += f'{p}: {self.stat_list[p]}\n'
        print(temp_var)
        return

    def ret_stat(self):
        temp_var = ''
        for i in range(31):
            temp_var = temp_var + str(self.stat_list[i]) + ' '
        temp_var = temp_var[:-1]
        return temp_var


if __name__ == "__main__":
    user = input('enter user name: ')
    with open(f'statistics\\{user}.txt', 'r', encoding='utf-8') as user_stats:
        new = Steve(user_stats.read())
    new.check_day()
    new.show()
    with open(f'statistics\\{user}.txt', 'w', encoding='utf-8') as user_stats:
        user_stats.write(new.ret_stat())
