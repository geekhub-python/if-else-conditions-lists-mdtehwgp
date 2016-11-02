#!/usr/bin/env python3

num1, num2, num3 = (int(input('type num1: ')),
                    int(input('type num2: ')),
                    int(input('type num3: '))
                    )

if num1 == num2 == num3:
    print(3)
elif num1 != num2 and num2 != num3 and num3 != num1:
    print(0)
else:
    print(2)
