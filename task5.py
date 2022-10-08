# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.


f1 = open("input.txt", "r") 
f2 = open("output.txt", "w")
line = f1.readlines()
x = int(line[1])
y = list(line[0])
print('y =',y,'x =',x)
f1.close()
print(len(y))
for i in range(0, len(y)-3):
    if y[i] == 'x':
        y.pop(i)
        print(i)
print(y)

   