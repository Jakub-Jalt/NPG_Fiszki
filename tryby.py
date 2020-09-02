#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Callable, Mapping, Optional, List
import obsluga_bazy


max_points: int = 15            #maksymalna liczba punktów do uzyskania w jednej turze gry

def game(mode: int) -> int:
    points: int = 0

    for i in range(0, 15):
        word: List[str] = obsluga_bazy.all_base.get_random_pair()
        if Forro(word) == True:        # Foo - nazwa tymczasowa
            points += 1
    return points




