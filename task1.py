# 1 Вычислить число π c заданной точностью d

# *Пример:* 

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# https://completerepair.ru/kak-vychislit-chislo-pi

from math import pi
i = int(input("Enter the number of decimal places: "))
h = 0
b = list()
for x in str(pi):
    h += 1
    b.append(x)
    if h == i+2:
        break

h = ''.join(b)
print(h)

