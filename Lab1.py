from matplotlib import pyplot as plt
import numpy as np
import math


# делаем полином Лагранжа покуда
# https://ru.wikipedia.org/wiki/%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BF%D0%BE%D0%BB%D1%8F%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9_%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE%D1%87%D0%BB%D0%B5%D0%BD_%D0%9B%D0%B0%D0%B3%D1%80%D0%B0%D0%BD%D0%B6%D0%B0
def f(i, x, j):
    result = (i - j) / (x - j)
    return result


def LPoly(t, x, y):
    y_end = []
    for i in t:
        result = [1] * len(x)
        for j in x:
            result = [(result[a] * f(i, x[a], j)) if j != x[a] else result[a] for a in range(len(x))]
        for j in range(len(x)):
            result[j] = y(x[j]) * result[j]
        y_end.append((sum(result)))
    return y_end


plt.figure("График нумеро 1")
plt.title("Оригинальный и интреполированные графики")
x_orig = np.arange(0, 10, 0.01)
x_orig_ps = np.arange(-1, 11, 0.01)
# y_orig = lambda x: np.e ** np.sin(x)
# y_orig = lambda x: np.sin(x)
# y_orig = lambda x: x ** 2
y_orig = lambda x: abs((x - 5))
y = list(map(y_orig, x_orig))
n = int(input("Введите количество узлов интерполяции: "))
xn = np.arange(0, 10, 10 / n)
plt.plot(x_orig, y_orig(x_orig), "g", lw=2, label="Оригинальный график")
y_int = LPoly(x_orig_ps, xn, y_orig)
plt.plot(x_orig_ps, y_int, "b", alpha=0.75, label="Интерполяция по равномерно распределенным точкам")
x_cheb = []

for i in range(1, n + 1):
    x_cheb.append(5 * np.cos(((2 * i - 1) / (2 * n)) * np.pi) + 5)
y_int_cheb = LPoly(x_orig_ps, x_cheb, y_orig)
plt.plot(x_orig_ps, y_int_cheb, "r", alpha=0.75, label="Интерполяция по узлам Чебышева")
plt.ylim(min(y) - 1, max(y) + 1)
plt.legend()

plt.figure("График нумеро 2")
plt.title("Графики абсолютных погрешностей")
xd1 = LPoly(x_orig, xn, y_orig)
xd2 = LPoly(x_orig, x_cheb, y_orig)
pogr_int = [abs(xd1[i] - y_orig(x_orig[i])) for i in range(len(x_orig))]
pogr_int_cheb = [abs(xd2[i] - y_orig(x_orig[i])) for i in range(len(x_orig))]
plt.plot(x_orig, pogr_int, "b", label="Абсолютная погрешность для равномерно распределенных узлов")
plt.plot(x_orig, pogr_int_cheb, "r", label="Абсолютная погрешность для узлов Чебышева")
plt.legend()

plt.figure("График нумеро 3")
plt.title("Графики относительных погрешностей")
xd1 = LPoly(x_orig, xn, y_orig)
xd2 = LPoly(x_orig, x_cheb, y_orig)
pogr_int = [(abs((xd1[i] - y_orig(x_orig[i])) / y_orig(x_orig[i]))) for i in range(len(x_orig))]
pogr_int_cheb = [(abs((xd2[i] - y_orig(x_orig[i])) / y_orig(x_orig[i]))) for i in range(len(x_orig))]
plt.plot(x_orig, pogr_int, "b", label="Относительная погрешность для равномерно распределенных узлов")
plt.plot(x_orig, pogr_int_cheb, "r", label="Относительная погрешность для узлов Чебышева")
plt.legend()

plt.show()
