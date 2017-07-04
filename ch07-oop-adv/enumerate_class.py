#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Enumerate class'

__author__ = 'Charles Guo'

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Jan)

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

@unique
class Weekday(Enum):
    Sun, Mon, Tue, Wed, Thu, Fri, Sat = 0, 1, 2, 3, 4, 5, 6

print(Weekday.Mon)
print(Weekday(1))
print(Weekday['Mon'])
print(Weekday.Wed.value)

for name, member in Weekday.__members__.items():
    print(name, '=>', member)