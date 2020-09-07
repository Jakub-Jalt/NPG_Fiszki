#!/usr/bin/python
# -*- coding: utf-8 -*-


import datetime as dt


class Steve:

    def __init__(self, stat_list: str):
        self.stat_list = stat_list.replace('\n', ' ').split(' ')
        if self.stat_list[-1] == '':
            self.stat_list = self.stat_list[:-1]

    def check_day(self):

        def update(cur_day: dt.date, last_day: dt.date):
            dif = (cur_day - last_day).days
            if dif > 30:
                self.stat_list.clear()
                for d in range(30):
                    new_list = [f'{(today - dt.timedelta(days=d)).isoformat()}', '0']
                    self.stat_list.extend(new_list)
            else:
                while dif > 0:
                    new_list = [f'{(today - dt.timedelta(days=dif)).isoformat()}', '0']
                    self.stat_list = new_list + self.stat_list
                    dif -= 1
                self.stat_list = self.stat_list[:30]
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
        temp_var = ''
        for p in range(0, 2 * 30, 2):
            temp_var += f'{self.stat_list[p]} : {self.stat_list[p+1]}\n'
        print(temp_var)
        return

    def ret_stat(self):
        temp_var = ''
        for i in range(0, 2 * 30, 2):
            temp_var += f'{self.stat_list[i]} {self.stat_list[i+1]}\n'
        temp_var = temp_var[:-1]
        return temp_var


if __name__ == "__main__":
    user = input('enter user name: ')
    with open(f'statistics\\{user}_o.txt', 'r', encoding='utf-8') as user_stats:
        new = Steve(user_stats.read())
    new.check_day()
    new.show()
    with open(f'statistics\\{user}_o.txt', 'w', encoding='utf-8') as user_stats:
        user_stats.write(new.ret_stat())
