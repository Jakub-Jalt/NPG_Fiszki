#!/usr/bin/python
# -*- coding: utf-8 -*-


import datetime as dt


def main(name: str):
    today = dt.date.today()
    new_list = ' 0' * 30
    with open(f'statistics\\{name}.txt', 'w', encoding='utf-8') as s_txt:
        s_txt.write(f'{today.isoformat()}' + new_list)
    with open(f'user_words\\{name}.txt', 'w', encoding='utf-8') as w_txt:
        w_txt.write('')
    return True


if __name__ == "__main__":
    nick = input('enter your name: ')
    main(nick)
