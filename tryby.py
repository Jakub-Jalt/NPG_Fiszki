#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Callable, Mapping, Optional, List
import datetime
import obsluga_bazy


max_points: int = 15            #maksymalna liczba punktów do uzyskania w jednej turze gry

def game(mode: int) -> None:     # mode: 0 - nic, 1 - ang_pol, 2 - pol_ang
    points: int = 0

    for i in range(0, max_points):
        word: List[str] = obsluga_bazy.all_base.get_random_pair()
        if mode == 1:
            if Foo(word[0]) == word[1]:        # Foo - nazwa tymczasowa
                points += 1
        elif mode == 2:
            if Foo(word[1]) == word[0]:        # Foo - nazwa tymczasowa
                points += 1

    f = open("statistics.txt", "a")
    f.write(str(datetime.datetime.now()) + " - " + str(points) + " \n")           #zapisanie liczby uzyskanych punktów do pliku
    return


def Foo(word: str) -> str:
    print(word)
    return input("")


game(2)
