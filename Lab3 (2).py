import numpy as np
import matplotlib.pyplot as plt


class CalcIntegral:
    def __init__(self, a, b, n, y):
        self.x = np.linspace(a, b, n + 1)
        self.y = y

    def output(self):
        return self.integral()


class RightRect(CalcIntegral):
    def integral(self):
        return sum([self.y(self.x[i]) * (self.x[i + 1] - self.x[i]) for i in range(len(self.x) - 1)])


class CenterRect(CalcIntegral):
    def integral(self):
        return sum(
            [self.y((self.x[i] + self.x[i + 1]) / 2) * (self.x[i + 1] - self.x[i]) for i in range(len(self.x) - 1)])


class LeftRect(CalcIntegral):
    def integral(self):
        return sum([self.y(self.x[i]) * (self.x[i] - self.x[i - 1]) for i in range(1, len(self.x))])


class Trapeze(CalcIntegral):
    def integral(self):
        return sum([((self.y(self.x[i]) + self.y(self.x[i + 1])) / 2) * (self.x[i + 1] - self.x[i]) for i in
                    range(len(self.x) - 1)])


class Simpson(CalcIntegral):
    def integral(self):
        h = self.x[1] - self.x[0]
        y = self.y(self.x)
        return h / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]) + y[-1])


class Gauss(CalcIntegral):
    def integral(self):
        area = 0
        for i in range(len(self.x) - 1):
            area += 1 / (self.x[i + 1] - self.x[i]) * ((self.y(1 / (self.x[i + 1] - self.x) + 1 / 3 ** 0.5) + self.y(
                1 / (self.x[i + 1] - self.x) - 1 / 3 ** 0.5)) * (self.x[i + 1] - self.x[i]))
        print(area)
            # метод Гаусса на двух точках


class Error:
    def error(self, y, cy, integr, a, b, step=1):
        fin = [(b - a) / n for n in range(10, 49, step)], [
            abs((integr(b) - integr(a)) - cy(a, b, n, y).output())
            for n in range(10, 49, step)]
        return fin


a, b, n = -1, 1, 100
y = lambda x: (2 ** x) * np.cos(x)
integr = lambda x: ((2 ** x) * (np.sin(x) + np.log(2) * np.cos(x))) / (np.log(2) ** 2 + 1)

print("Оригинальный интеграл:", integr(b) - integr(a))
print("Метод правых квадратов:", RightRect(a, b, n, y).output())
print("Метод левых квадратов:", LeftRect(a, b, n, y).output())
print("Метод центральных квадратов:", CenterRect(a, b, n, y).output())
print("Метод трапеции:", Trapeze(a, b, n, y).output())
print("Метод Симпсона:", Simpson(a, b, n, y).output())

plt.figure("Погрешность метода правых квадратов")
plt.plot(*Error().error(y, RightRect, integr, a, b))
plt.figure("Погрешность метода центральных квадратов")
plt.plot(*Error().error(y, CenterRect, integr, a, b))
plt.figure("Погрешность метода левых квадратов")
plt.plot(*Error().error(y, LeftRect, integr, a, b))
plt.figure("Погрешность метода трапеций")
plt.plot(*Error().error(y, Trapeze, integr, a, b))
plt.figure("Погрешность метода Симпсона")
plt.plot(*Error().error(y, Simpson, integr, a, b, step=2))
plt.figure("Погрешность метода Гаусса на двух точках")
plt.plot(*Error().error(y, Gauss, integr, a, b))

plt.figure("Погрешность метода правых квадратов в логарифмическом виде")
xx, yy = Error().error(y, RightRect, integr, a, b)
plt.plot(xx, yy)
print("Погрешность метода правых квадратов в логарифмическом виде: ",
      (np.log(yy[1]) - np.log(yy[-2])) / (np.log(xx[1]) - np.log(xx[-2])))
plt.xscale("log")
plt.yscale("log")

plt.figure("Погрешность метода левых квадратов в логарифмическом виде")
xx, yy = Error().error(y, LeftRect, integr, a, b)
plt.plot(xx, yy)
print("Погрешность метода левых квадратов в логарифмическом виде: ",
      (np.log(yy[1]) - np.log(yy[-2])) / (np.log(xx[1]) - np.log(xx[-2])))
plt.xscale("log")
plt.yscale("log")

plt.figure("Погрешность метода центральных квадратов в логарифмическом виде")
xx, yy = Error().error(y, CenterRect, integr, a, b)
plt.plot(xx, yy)
print("Погрешность метода центральных квадратов в логарифмическом виде: ",
      (np.log(yy[1]) - np.log(yy[-2])) / (np.log(xx[1]) - np.log(xx[-2])))
plt.xscale("log")
plt.yscale("log")

plt.figure("Погрешность метода трапеций в логарифмическом виде")
xx, yy = Error().error(y, Trapeze, integr, a, b)
plt.plot(xx, yy)
print("Погрешность метода трапеций в логарифмическом виде: ",
      (np.log(yy[1]) - np.log(yy[-2])) / (np.log(xx[1]) - np.log(xx[-2])))
plt.xscale("log")
plt.yscale("log")

plt.figure("Погрешность метода Симпсона в логарифмическом виде")
xx, yy = Error().error(y, Simpson, integr, a, b, step=2)
plt.plot(xx, yy)
print("Погрешность метода Симпсона в логарифмическом виде: ",
      (np.log(yy[2]) - np.log(yy[-2])) / (np.log(xx[2]) - np.log(xx[-2])))
plt.xscale("log")
plt.yscale("log")

plt.figure("много графиков")
xx, yy = Error().error(y, RightRect, integr, a, b)
plt.plot(xx, yy, "m")
xx, yy = Error().error(y, LeftRect, integr, a, b)
plt.plot(xx, yy, "y")
xx, yy = Error().error(y, CenterRect, integr, a, b)
plt.plot(xx, yy, "g")
xx, yy = Error().error(y, Trapeze, integr, a, b)
plt.plot(xx, yy, "b")
xx, yy = Error().error(y, Simpson, integr, a, b, step=2)
plt.plot(xx, yy, "r")
plt.xscale("log")
plt.yscale("log")
plt.show()
