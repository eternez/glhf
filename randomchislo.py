from random import random
import random
chislo = int(input("Введи первое число"))
chislo1 = int(input("Введи второе число"))
randomnoechislo = int(random() * (chislo1 - chislo + 1)) + chislo
print(randomnoechislo)

