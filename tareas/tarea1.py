import matplotlib.pyplot as plt
import numpy as np

side = 800
black_background = np.zeros((side, side, 1), dtype=np.uint8)
for i in range(0, side, 100):
    start = 0 if i % 200 == 0 else 100
    for j in range(start, side, 200):
        black_background[i:i + 100, j:j + 100, 0] = 255
plt.imshow(black_background, cmap='gray')
plt.axis('off')
plt.show()
