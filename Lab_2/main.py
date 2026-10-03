import matplotlib.pyplot as plt
print("|x+a| = b/(c-x)")

a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))

x1 = int(input("Введите значение x1:"))
x2 = int(input("Введите значение x2:"))
d = 10
h = (x2-x1)/d
mas1 = []
mas2 = []
mas_x = []
print("="*50)
for step in range (0, d+1):
    x = x1 + step*h
    y_x = x**2 + (a-c)*x - (b-a*c)
    mas1.append(y_x)
    y_x1 = x**2 + (a-c)*x - (b+a*c)
    mas2.append(y_x1)
    mas_x.append(x)
    print(f"{step:^5} | {x:^10.4f} | {y_x:^12.4f} | {y_x1:^12.4f}")
print("="*50)
plt.figure(figsize=(10,10))
plt.plot(mas_x, mas1, label='Случай (+)', color='blue', marker='o')
plt.plot(mas_x, mas2, label='Случай (-)', color='red', marker='s')
plt.axhline(0, color='black', linestyle='--', lw=1)
plt.grid(True)
plt.title('График функций для двух случаев раскрытия модуля')
plt.xlabel('Ось x')
plt.ylabel('Ось y')
plt.legend()
plt.show()

