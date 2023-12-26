def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

try:
    user_input = int(input("Введите число для вычисления факториала: "))
    if user_input < 0:
        print("Факториал только для неотрицательных чисел.")
    else:
        result = factorial(user_input)
        print(f"Факториал числа {user_input} равен {result}")
except ValueError:
    print("Введите целое число.")