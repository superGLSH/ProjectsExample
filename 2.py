import cv2


def f(im, x, y):
    for i in range(-20, 21):
        for j in range(-20, 21):
            try:
                if im[x + i][y + j] != False:
                    return False
            except Exception:
                pass
    return True


image = cv2.imread(input("Введите путь до картинки: "))
maska = [len(image[0]) * [False] for i in range(len(image))]
for i in range(len(image)):
    for j in range(len(image[0])):
        yark = sum(image[i][j])
        if yark > 700:
            if f(maska, i, j):
                maska[i][j] = True
for i in range(len(maska)):
    for j in range(len(maska[0])):
        if maska[i][j]:
            cv2.circle(image, (j, i), 20, [0, 0, 255])
cv2.imshow('', image)
cv2.waitKey(0)
