#!/usr/bin/env python3

# l = input('type list numbers: ')
l = [1, -2, 3, -4, 5, 6]

for i, n in enumerate(l):
    if (l[i] * l[i+1]) > 0:
        print(l[i], l[i+1])
        break
    else:
        pass


# TODO Fix temporary crutches
