import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# u" + au'+ bu + c = 0
a = lambda x: -x / (4 - x ** 2)
b = lambda x: 1 / (4 - x ** 2)
c = lambda x: 2 * x / (4 - x ** 2)
u0 = 0
u1 = 2
func = lambda x: x + 2 * (1 - x ** 2 / 4) ** 0.5 * np.arcsin(x / 2)
f = lambda x, u0, u1: - (a(x) * u1 + b(x) * u0 + c(x))
h = 0.05
x = np.arange(0, 1.01, h)


def Euler(f, h, u0, u1, x):
    y0 = [u0]
    y1 = [u1]
    for i in range(1, len(x)):
        u1, u0 = u1 + h * f(x[i - 1], u0, u1), u0 + u1 * h
        y0.append(u0)
        y1.append(u1)
    return y0, y1


def RungeKutta(f, h, u0, u1, x):
    y0 = [u0]
    y1 = [u1]
    for i in range(1, len(x)):
        k1 = u1
        q1 = f(x[i - 1], u0, u1)
        k2 = u1 + q1 * h / 2
        q2 = f(x[i - 1] + h / 2, u0 + h / 2 * k1, u1 + h / 2 * q1)
        k3 = u1 + q2 * h / 2
        q3 = f(x[i - 1] + h / 2, u0 + h / 2 * k2, u1 + h / 2 * q2)
        k4 = u1 + q3 * h
        q4 = f(x[i - 1] + h, u0 + k3 * h, u1 + q3 * h)
        u1, u0 = u1 + h / 6 * (q1 + 2 * q2 + 2 * q3 + q4), u0 + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        y0.append(u0)
        y1.append(u1)
    return y0, y1


def Adams(f, h, u0, u1, x):
    y0, y1 = RungeKutta(f, h, u0, u1, x[:3])
    for i in range(2, len(x) - 1):
        aa = y0[i] + h * (23 * y1[i] - 16 * y1[i - 1] + 5 * y1[i - 2]) / 12
        bb = y1[i] + h * (
                23 * f(x[i], y0[i], y1[i]) - 16 * f(x[i - 1], y0[i - 1], y1[i - 1]) + 5 * f(x[i - 2], y0[i - 2],
                                                                                            y1[i - 2])) / 12
        y0.append(aa)
        # дорогой кошька я тебя люблю чего грустишь ??????((((((
        y1.append(bb)
    return y0, y1


def Error(x, y, cy):
    res = []
    func = cy
    for i in range(len(x)):
        res.append(abs(y(x[i]) - func[i]))
    return res


def massError(f, u0, u1, n, y, cy):
    res = []
    for i in range(3, n):
        x = np.arange(0, 1.001, 1 / i)
        res.append(np.mean(Error(x, y, cy(f, 1 / i, u0, u1, x)[0])))
    return list(map(lambda x: 1 / x, range(3, n))), res


plt.figure("Графики полученных функций")
plt.plot(x, func(x), "r--", alpha=0.5)
plt.plot(x, Euler(f, h, u0, u1, x)[0], "b", alpha=0.5)
plt.plot(x, RungeKutta(f, h, u0, u1, x)[0], "g", alpha=0.5)
plt.plot(x, Adams(f, h, u0, u1, x)[0], "k", alpha=0.5)

f1 = Error(x, func, Euler(f, h, u0, u1, x)[0])
f2 = Error(x, func, RungeKutta(f, h, u0, u1, x)[0])
f3 = Error(x, func, Adams(f, h, u0, u1, x)[0])

plt.figure("Графики погрешностей расчитанных функций")
plt.plot(x, f1, "b", alpha=0.5)
plt.plot(x, f2, "g", alpha=0.5)
plt.plot(x, f3, "r", alpha=0.5)

plt.figure("Графики логарифмических погрешностей расчитанных функций")
plt.plot(x, f1, "b", alpha=0.5)
plt.plot(x, f2, "g", alpha=0.5)
plt.plot(x, f3, "r", alpha=0.5)
plt.xscale("log")
plt.yscale("log")

xpol = np.arange(0, 1.01, h * 2)
f1 = Euler(f, h, u0, u1, x)[0]
f2 = Euler(f, h * 2, u0, u1, xpol)[0]
R1 = [abs(func(xpol[i]) - f1[i * 2]) for i in range(len(f2))]  # считаем разницу в каждой точке
R2 = [(f1[i * 2] - f2[i]) / (2 ** 1 - 1) for i in range(len(f2))]  # считаем с помощью h, 2h


def TheCoolerEuler(f2, R2):
    for i in range(len(f2)):
        f2[i] += R2[i]
    return f2
plt.figure("Поправка Ричардсона")
plt.plot(x, f1)
plt.plot(xpol, TheCoolerEuler(f2, R2))
plt.figure("Поправка Ричардсона, погрешность")
plt.plot(x, Error(x, func, f1), "g")
plt.plot(xpol, Error(xpol, func, TheCoolerEuler(f2, R2)), "r")


df = pd.DataFrame(list(zip(R1, R2)), columns=["Вычислить напрямую", 'Два раза воспользоваться методом Рунге'])
print(df, "\n")
plt.figure("Графики методов Рунге")
plt.plot(xpol, R1, "b", alpha=0.5)
plt.plot(xpol, R2, "g", alpha=0.5)

n = 100
plt.figure("Графики логарифмических прямых")
x = massError(f, u0, u1, n, func, Euler)[0][10:-10]
f1 = massError(f, u0, u1, n, func, Euler)[1][10:-10]
f2 = massError(f, u0, u1, n, func, RungeKutta)[1][10:-10]
f3 = massError(f, u0, u1, n, func, Adams)[1][10:-10]
plt.plot(x, f1)
plt.plot(x, f2)
plt.plot(x, f3)
plt.xscale("log")
plt.yscale("log")

print("Точность метода Эйлера:", (np.log(f1[-20]) - np.log(f1[20])) / (np.log(x[-20]) - np.log(x[20])))
print("Точность метода Рунге-Кутта:", (np.log(f2[-20]) - np.log(f2[20])) / (np.log(x[-20]) - np.log(x[20])))
print("Точность метода Адамса:", (np.log(f3[-20]) - np.log(f3[20])) / (np.log(x[-20]) - np.log(x[20])))

plt.show()
