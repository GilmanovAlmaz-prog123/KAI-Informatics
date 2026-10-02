print("Решаем уравнение |x+a| = b/(c-x)")

a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))

counts_roots = 0

a1 = 1
b1 = a - c
c1 = b - a * c
discriminant_case1 = b1 ** 2 - 4 * a1 * c1

if discriminant_case1 >= 0:
    x_1 = (-b1 + discriminant_case1 ** 0.5) / (2 * a1)
    x_2 = (-b1 - discriminant_case1 ** 0.5) / (2 * a1)

    if x_1 != c and x_1 >= -a:
        left_side = abs(x_1 + a)
        right_side = b / (c - x_1)
        if abs(left_side - right_side) < 1e-7:
            print(f"Корень из случая 1: x = {x_1} (Проверка: {left_side:.4f} = {right_side:.4f} -> Верно)")
            counts_roots = counts_roots + 1
    else:
        print("Корень x_1 не удовлетворяет заданному условию")

    if x_2 != c and x_2 >= -a and round(x_2, 7) != round(x_1, 7):
        left_side = abs(x_2 + a)
        right_side = b / (c - x_2)
        if abs(left_side - right_side) < 1e-7:
            print(f"Корень из случая 1: x = {x_2} (Проверка: {left_side:.4f} = {right_side:.4f} -> Верно)")
            counts_roots = counts_roots + 1
    else:
        print("Корень x_2 не удовлетворяет заданному условию")
else:
    print("В случае 1 нет действительных корней (дискриминант < 0)")

a2 = 1
b2 = a - c
c2 = -b - a * c
discriminant_case2 = b2 ** 2 - 4 * a2 * c2

if discriminant_case2 >= 0:
    x_1_1 = (-b2 + discriminant_case2 ** 0.5) / (2 * a2)
    x_2_2 = (-b2 - discriminant_case2 ** 0.5) / (2 * a2)

    if x_1_1 != c and x_1_1 < -a:
        left_side = abs(x_1_1 + a)
        right_side = b / (c - x_1_1)
        if abs(left_side - right_side) < 1e-7:
            print(f"Корень из случая 2: x = {x_1_1} (Проверка: {left_side:.4f} = {right_side:.4f} -> Верно)")
            counts_roots = counts_roots + 1
    else:
        print("Корень x_1_1 не удовлетворяет заданному условию")

    if x_2_2 != c and x_2_2 < -a and round(x_2_2, 7) != round(x_1_1, 7):
        left_side = abs(x_2_2 + a)
        right_side = b / (c - x_2_2)
        if abs(left_side - right_side) < 1e-7:
            print(f"Корень из случая 2: x = {x_2_2} (Проверка: {left_side:.4f} = {right_side:.4f} -> Верно)")
            counts_roots = counts_roots + 1
    else:
        print("Корень x_2_2 не удовлетворяет заданному условию")
else:
    print("В случае 2 нет действительных корней (дискриминант < 0)")

if counts_roots == 0:
    print('Уравнение не имеет корней вообще')




