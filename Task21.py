# Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

from fractions import Fraction
MD = 11
used = set()

for i in range(1, MD):
    for j in range(1, MD + 1):
        if i < j and i//j != i/j and (n := Fraction):
            print(n)
            used.add(n)