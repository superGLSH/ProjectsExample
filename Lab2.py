from matplotlib import pyplot as plt
import numpy as np


def finite_dif(x, y, mode="right"):  # mode: right, central, left
    x_end = []
    y_end = []
    h = x[1] - x[0]
    if mode == "right":
        for i in range(len(x) - 1):
            x_end.append(x[i])
            y_end.append((y(x[i + 1]) - y(x[i])) / h)
    #    elif mode == "central":
    #        for i in range(1, len(x) - 1):
    #           x_end.append(x[i])
    #           y_end.append((y(x[i + 1]) - y(x[i - 1])) / (2 * h))
    elif mode == "central":
        for i in range(2, len(x)):
            x_end.append(x[i])
            y_end.append((1.5 * y(x[i]) - 2 * y(x[i - 1]) + 0.5*y(x[i-2])) / (h))
    elif mode == "left":
        for i in range(1, len(x)):
            x_end.append(x[i])
            y_end.append((y(x[i]) - y(x[i - 1])) / h)
    return x_end, y_end


def finite_dif_2(x, y, mode=2):
    x_end = []
    y_end = []
    h = x[1] - x[0]
    if mode == 2:
        for i in range(1, len(x) - 1):
            x_end.append(x[i])
            y_end.append((y(x[i + 1]) - 2 * y(x[i]) + y(x[i - 1])) / (h ** 2))
    elif mode == 4:
        x = np.insert(x, 0, x[0] - h)
        x = np.append(x, x[-1] + h)
        for i in range(2, len(x) - 2):
            x_end.append(x[i])
            y_end.append((-1 / 12 * y(x[i - 2]) + 4 / 3 * y(x[i - 1]) - 5 / 2 * y(x[i]) + 4 / 3 * y(
                x[i + 1]) - 1 / 12 * y(x[i + 2])) / (h ** 2))
    return x_end, y_end


def pogr(y, y_dif, a, b, f, mode=None, vid=None):
    array_ = []
    array_2 = []
    for n in range(15, 200):
        x = np.arange(a, b, (b - a) / n)
        array_2.append((b - a) / n)
        x_y, dif = f(x, y, mode)
        array_.append(max(abs(np.array(dif) - np.array(list(map(y_dif, x_y))))))
    plt.plot(array_2, array_, vid)
    return (np.log(array_[60]) - np.log(array_[50])) / (np.log(array_2[60]) - np.log(array_2[50]))


a = -1
b = 1
n = int(input("Ломай меня на промежутки, сколько ты хочешь: "))
x = np.arange(a, b, (b - a) / n)  # задаем

y = lambda x: np.e ** np.cos(x) * (1 + x ** 2)
y1 = lambda x: -(x ** 2 + 1) * np.e ** np.cos(x) * np.sin(x) + 2 * x * np.e ** np.cos(x)
y2 = lambda x: (x ** 2 + 1) * np.e ** np.cos(x) * (np.sin(x)) ** 2 - 4 * x * np.e ** np.cos(x) * np.sin(x) - (
        x ** 2 + 1) * np.e ** np.cos(x) * np.cos(x) + 2 * np.e ** np.cos(x)

plt.figure("Графики производных I степеней")

x_y1, dif1 = finite_dif(x, y)
plt.plot(x_y1, dif1, 'b')

x_y2, dif2 = finite_dif(x, y, mode="central")
plt.plot(x_y2, dif2, "r")

plt.figure("Графики производных II степеней")

x_y3, dif3 = finite_dif_2(x, y)
plt.plot(x_y3, dif3, "r--", alpha=1)

x_y4, dif4 = finite_dif_2(x, y, mode=4)
plt.plot(x_y4, dif4, 'bo', alpha=0.75)

plt.figure("Погрешности I степеней")

pogr(y, y1, a, b, f=finite_dif, mode="right", vid="r--")
pogr(y, y1, a, b, f=finite_dif, mode="central", vid="b--")

plt.figure("Погрешности II степеней")

pogr(y, y2, a, b, f=finite_dif_2, mode=2, vid="r--")
pogr(y, y2, a, b, f=finite_dif_2, mode=4, vid="b--")

plt.figure("Погрешности I степеней в логарифмическом виде")

print(pogr(y, y1, a, b, f=finite_dif, mode="right", vid="r--"))
print(pogr(y, y1, a, b, f=finite_dif, mode="central", vid="b--"))
plt.xscale("log")
plt.yscale("log")

plt.figure("Погрешности II степеней в логарифмическом виде")

print(pogr(y, y2, a, b, f=finite_dif_2, mode=2, vid="r--"))
print(pogr(y, y2, a, b, f=finite_dif_2, mode=4, vid="b--"))
plt.xscale("log")
plt.yscale("log")

plt.show()
