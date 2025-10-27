from retry_on_error import retry_on_error

@retry_on_error(retries=3)
def divide(a, b):
    """Функція для ділення двох чисел."""
    return a / b

# Тестування
print(divide(10, 2))   # Виконається успішно
print(divide(10, 0))   # Виникне помилка, декоратор зробить 3 спроби
