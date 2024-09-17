from copy import deepcopy

import cv2
import numpy as np

camera_video = cv2.VideoCapture(0)

while True:
    # fotograma a fotograma
    ret, frame = camera_video.read()

    if ret:
        # Separamos canales
        b = frame[:, :, 0]
        g = frame[:, :, 1]
        r = frame[:, :, 2]

        h, w, c = frame.shape
        image1 = deepcopy(frame)
        image2 = deepcopy(frame)
        image3 = deepcopy(frame)
        image4 = deepcopy(frame)

        image1[:, :, 0] = b * 255
        image1[:, :, 1] = g * 255
        image1[:, :, 2] = r * 5

        image2[:, :, 0] = b * 255
        image2[:, :, 1] = g * 5
        image2[:, :, 2] = r * 255

        image3[:, :, 0] = b * 5
        image3[:, :, 1] = g * 255
        image3[:, :, 2] = r * 255

        image4[:, :, 0] = b * 5
        image4[:, :, 1] = g * 5
        image4[:, :, 2] = r * 5

        collage_up = np.hstack((image2, image1))
        collage_down = np.hstack((image3, image4))
        collage = np.vstack((collage_up, collage_down))

        cv2.circle(collage, (w, h), 20, (0, 0, 0), 8)

        cv2.imshow('ESC to leave', cv2.resize(collage, (w, h), cv2.INTER_NEAREST))

    # Detenemos pulsado ESC
    if cv2.waitKey(20) == 27:
        break

# Libera el objeto de captura
camera_video.release()
# Destruye ventanas
cv2.destroyAllWindows()
