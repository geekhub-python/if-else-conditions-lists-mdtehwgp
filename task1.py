#!/usr/bin/env python3

year = int(input('type year: '))

if (year % 4 == 0 and year % 100) or (year % 400 == 0):
    print('YES')
else:
    print('NO')
