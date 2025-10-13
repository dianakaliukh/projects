# Лабораторна робота №5
# Тема: Робота з бібліотеками Python

# Імпорт 10 бібліотек
import math
import random
import datetime
import os
import time
import json
import sys
import statistics
import calendar
import string

#  math — математичні функції
try:
    num = 16
    print(f"Квадратний корінь з {num} =", math.sqrt(num))
except Exception as e:
    print("Помилка в блоці math:", e)

#  random — генерація випадкових чисел
try:
    nums = [random.randint(1, 10) for _ in range(5)]
    print("Випадкові числа:", nums)
except Exception as e:
    print("Помилка в блоці random:", e)

#  datetime — робота з датою і часом
try:
    now = datetime.datetime.now()
    print("Поточна дата і час:", now.strftime("%Y-%m-%d %H:%M:%S"))
except Exception as e:
    print("Помилка в блоці datetime:", e)

#  os — робота з файловою системою
try:
    current = os.getcwd()
    print("Поточна директорія:", current)
except Exception as e:
    print("Помилка в блоці os:", e)

#  string — робота з рядками
try:
    letters = string.ascii_lowercase
    random_word = ''.join(random.choice(letters) for _ in range(6))
    print("Випадкове слово:", random_word)
except Exception as e:
    print("Помилка в блоці string:", e)

print("\n✅ Програма виконана успішно!")
