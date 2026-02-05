class Human:
    def __init__(self, name, age, country):
        self.name = name
        self.__age = age          # інкапсуляція (приватний атрибут)
        self.country = country

    # getter
    def get_age(self):
        return self.__age

    # setter з перевіркою
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Вік повинен бути додатнім!")

    def info(self):
        return f"Ім'я: {self.name}, Вік: {self.__age}, Країна: {self.country}"

# Наслідування
class Student(Human):
    def __init__(self, name, age, country, university, course):
        super().__init__(name, age, country)
        self.university = university
        self.course = course

    # Поліморфізм (перевизначення методу)
    def info(self):
        return (f"Ім'я: {self.name}, Вік: {self.get_age()}, Країна: {self.country}, "
                f"Університет: {self.university}, Курс: {self.course}")

# Ввід даних
name = input("Введіть ім'я: ")
age = int(input("Введіть вік: "))
country = input("Введіть країну: ")
university = input("Введіть університет: ")
course = int(input("Введіть курс: "))

# Створення об'єкта
student = Student(name, age, country, university, course)

print("\nІнформація про студента:")
print(student.info())
