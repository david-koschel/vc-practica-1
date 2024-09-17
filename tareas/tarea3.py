import matplotlib.pyplot as plt
import numpy as np
import cv2

side = 800
black_background = np.zeros((side, side, 3), dtype=np.uint8)
for i in range(0, side, 100):
    start = 0 if i % 200 == 0 else 100
    for j in range(start, side, 200):
        cv2.rectangle(black_background, (i, j), (i + 100, j + 100), (255, 255, 255), -1)
plt.imshow(black_background, cmap='gray')
plt.axis('off')
plt.show()
