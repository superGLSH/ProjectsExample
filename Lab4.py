import numpy as np
import matplotlib.pyplot as plt


def dihotomiya(f, a, b, eps):
    nn = int(np.log2((b - a) / (2*eps))) + 1
    n = 0
    while (b - a) >= eps:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        else:
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
        n += 1
    print(nn)
    return [round(c, int(np.log10(1 / eps))), n]


def NewtonMethod(f, fp, a, eps):
    x0 = a + 1
    x1 = x0 - f(x0) / fp(x0)
    n = 1
    while abs(x1 - x0) >= eps:
        x0, x1 = x1, x1 - f(x1) / fp(x1)
        n += 1
    return [round(x1, int(np.log10(1 / eps))), n]


def velocity(f, fp, a, eps):
    resh = 1.26930347151271
    x0 = a + 1
    x1 = x0 - f(x0) / fp(x0)
    n = 1
    sp1 = []
    sp2 = []
    while abs(x1 - x0) >= eps:
        x0, x1 = x1, x1 - f(x1) / fp(x1)
        n += 1
        sp1.append(abs(x1 - resh))
        sp2.append(abs(resh - x0))
    plt.plot(sp1, sp2)
    plt.xscale("log")
    plt.yscale("log")
    plt.show()
    return (np.log(sp1[-2]) - np.log(sp1[0])) / (np.log(sp2[-2]) - np.log(sp2[0]))


f = lambda x: x ** 5 - 3 * x ** 2 + 2 * x - 1
fp = lambda x: 5 * x ** 4 - 6 * x + 2
min_ = 0
max_ = 10
eps1 = 10 ** (-3)
eps2 = 10 ** (-6)
eps3 = 10 ** (-9)
print("Значение, полученное с помощью метода дихотомии: {}, количество итераций: {}".format(
    *dihotomiya(f, min_, max_, eps1)))
print("Значение, полученное с помощью метода дихотомии: {}, количество итераций: {}".format(
    *dihotomiya(f, min_, max_, eps2)))
print("Значение, полученное с помощью метода дихотомии: {}, количество итераций: {}".format(
    *dihotomiya(f, min_, max_, eps3)))
print("Значение, полученное с помощью метода Ньютона: {}, количество итераций: {}".format(
    *NewtonMethod(f, fp, min_, eps1)))
print("Значение, полученное с помощью метода Ньютона: {}, количество итераций: {}".format(
    *NewtonMethod(f, fp, min_, eps2)))
print("Значение, полученное с помощью метода Ньютона: {}, количество итераций: {}".format(
    *NewtonMethod(f, fp, min_, eps3)))
print(velocity(f, fp, min_, eps1))
print(velocity(f, fp, min_, eps2))
print(velocity(f, fp, min_, eps3))
