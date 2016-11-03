#!/usr/bin/env python3

l = list(input('type list numbers: '))

count = 0
for pair in l:
    if l.count(pair) >= 2:
        pair = 1
        count += pair

print(count // 2)
