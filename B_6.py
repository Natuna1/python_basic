"""
N面サイコロをM回振ったときの結果を表示してください
N, M は正の整数とします
N, M はユーザーからの入力を利用すること
[例]
サイコロの面の数は?: 8
何回振りますか?: 20
[6, 6, 8, 5, 1, 6, 4, 4, 3, 4, 7, 5, 7, 1, 4, 2, 5, 7, 1, 7]
"""

import random

men = int(input("サイコロの面の数は?:"))
torai = int(input("何回振りますか?: "))

numbers_list = list()

for r in range(0, torai):

    dice = random.randint(1, men)
    numbers_list.append(dice)

print(numbers_list)
