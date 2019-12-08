import numpy as np
import matplotlib.pyplot as plt

s = input()

size = 25 * 6
layer_count = len(s) // size

layer_lst = [list(map(int, s[size * i:size * (i + 1)]))
             for i in range(layer_count)]

image = [[-1 for j in range(25)] for i in range(6)]

for i in range(6):
    for j in range(25):
        k = 0
        px = layer_lst[k][i * 25 + j]
        while(px == 2):
            k += 1
            px = layer_lst[k][i * 25 + j]
        image[i][j] = px

for row in image:
    print(*row, sep='')

im = np.array(image)

plt.imshow(im, cmap='gray')
plt.tight_layout()
plt.axis('off')
plt.show()
