#!/usr/bin/env python3

n, m, k = (int(input('type n: ')),
           int(input('type m: ')),
           int(input('type k: '))
           )

if (n * m > k) and (k % n == 0 or k % m == 0):
    print('YES')
else:
    print('NO')
