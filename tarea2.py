import matplotlib.pyplot as plt
import numpy as np

alto = 800
ancho = 800

mondrian = np.zeros((alto, ancho, 3), dtype=np.uint8)

mondrian[0:200, 0:400, 0] = 255
mondrian[0:400, 420:600, 0:3] = 255
mondrian[0:100, 620:, 0:2] = 255
mondrian[120:450, 620:, 2] = 255
mondrian[220:400, 0:200, 0:3] = 255
mondrian[220:400, 220:400, 0:3] = 255
mondrian[420:500, 0:200, 0] = 255
mondrian[520:600, 0:200, 0] = 255
mondrian[420:450, 220:600, 0:2] = 255
mondrian[620:800, 0:500, 2] = 255
mondrian[470:800, 520:800, 0] = 255

plt.axis('off')
plt.imshow(mondrian)
plt.show()
