import random
from PIL import Image


dict_ = {}
max_i = 0
max_j = 0

# фильтр анархия


def image_filter(pixels, i, j):
    global dict_, max_i, max_j
    if max_i == 0:
        for b in range(0, 1000000):
            try:
                pixels[b, j]
            except IndexError:
                max_i = b - 1
                break
    if max_j == 0:
        for b in range(0, 1000000):
            try:
                pixels[i, b]
            except IndexError:
                max_j = b - 1
                break
    if (i, j) not in dict_.keys():
        a = random.randint(0, max_i), random.randint(0, max_j)
        random_pix = pixels[a]
        dict_[a] = pixels[i, j]
    else:
        random_pix = dict_[i, j]
    if i == max_i and j == max_j:
        max_i = 0
        max_j = 0
        # print(dict_)
        dict_ = {}
    return random_pix



im = Image.open("tgh.jpg")
pixels = im.load()
x, y = im.size
for i in range(x):
    for j in range(y):
        pixels[i, j] = image_filter(pixels, i, j)
im.save("ujk.jpg")

