# Лабораторна робота №5
# Стандартні (вже є в Python, не потребують встановлення)
import math
import random
import datetime
import os
# Зовнішні (потрібно встановити через pip)
from colorama import Fore, Style # кольоровий текст
import pandas as pd      # для роботи з таблицями (даними)
import numpy as np       # для обчислень з масивами
import matplotlib.pyplot as plt  # для побудови графіків
from faker import Faker  # для генерації фейкових даних
import emoji             #емодзі

# 1. math
try:
    num = 25
    print("Квадратний корінь з", num, "=", math.sqrt(num))
except Exception as e:
    print("Помилка math:", e)

# 2. random
try:
    print("Випадкове число від 1 до 10:", random.randint(1, 10))
except Exception as e:
    print("Помилка random:", e)

# 3. emoji
try:
    print("Python — це класно!", emoji.emojize(":snake: :sparkles:"))
except Exception as e:
    print("Помилка emoji:", e)

# 4. colorama
try:
    print(Fore.GREEN + "Цей текст зелений!" + Style.RESET_ALL)
except Exception as e:
    print("Помилка colorama:", e)

# 5. matplotlib
try:
    x = [1, 2, 3, 4, 5]
    y = [n**2 for n in x]
    plt.plot(x, y)
    plt.title("Графік y = x²")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
except Exception as e:
    print("Помилка matplotlib:", e)
