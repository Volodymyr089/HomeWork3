"""
1:

x = int(input("Число 1: "))
y = int(input("Число 2: "))
summ = 0
summch = 0
summ9 = 0

for i in range(x, y):

    if i % 2 != 0:
        summ += i
    if i % 2 == 0:
        summch += i
    if i % 9 == 0:
        summ9 += i
print("Четные", summch)
print("Не четные", summ)
print("Кратные", summ9)
"""

"""
2:

x = input("Введите строку: ")
y = input("Введите символ: ")

for i in x:
    print(y)
"""

"""
3:

x = 0
while x != 7:

    x = int(input("Введите число: "))

    if x > 0:
        print("Number is positive")

    if x < 0:
        print("Number is negative")

    if x == 0:
        print("Number is equal to zero")

print("Good bye!")
"""

"""
4:

x = int(input("Введите число: "))
c = 0
while x != 7:
    c += 1
    if c <= x:
        print(c)

print("Good bye!")
"""
