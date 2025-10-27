import time

def retry_on_error(retries=3):
    """
    Декоратор, який повторює виконання функції задану кількість разів,
    якщо під час виконання виникла помилка.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Помилка: {e}. Спроба {attempts} з {retries}.")
                    time.sleep(1)
            return f"Функція не виконалася після {retries} спроб."
        return wrapper
    return decorator
