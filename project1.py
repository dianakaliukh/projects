# Лабораторна робота №1
# Створення змінних
name = 'Diana'                              #тип даних str
age = 16                                    #тип даних int
height = 1.72                               #тип даних float
student = True                              #тип даних bool
hobbies = ['guitar', 'sport']               #тип даних list
friends = {'Anna, Vera'}                    #тип даних set
grades = (12, 11, 10)                       #тип даних tuple
info =  {'city': 'Lutsk'}                   #тип даних dict

#виведення кожної змінної та її типу

print('name', type(name),':', name)
print('age', type(age),':', age)
print('height', type(height),':', height)
print('student', type(student),':', student)
print('hobbies', type(hobbies),':', hobbies)
print('friends', type(friends),':', friends)
print('grades', type(grades),':', grades)
print('info', type(info),':', info)

a = 12
b = 3

c = a + b                #додавання
print(c)

d = a - b                #віднімання
print(d)

i = a * b                 #множення
print(i)

f = a / b                 #діленння (результат завжди float)
print(f)

g = a // b                #ділення без остачі
print(g)

j = a % b                 #остача від ділення
print(j)

k = a ** b                #піднесення до степення
print(k)