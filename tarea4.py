import cv2

camera_video = cv2.VideoCapture(0)
while True:
    ret, frame = camera_video.read()

    if ret:
        # Separamos canales
        b = frame[:, :, 0]
        g = frame[:, :, 1]
        r = frame[:, :, 2]
        h, w, c = frame.shape

        #Calculamos el canal blanco y negro
        b_and_w = 0.299 * b + 0.587 * g + 0.114 * r

        image = frame.copy()
        image[:, :, 0] = b_and_w
        image[:, :, 1] = b_and_w

        #Creamos una máscara que detecta los píxeles menos intensos
        not_enough_red_mask = (r / 2 < g) & (r / 1.5 < b)
        image[:, :, 2][not_enough_red_mask] = b_and_w[not_enough_red_mask]

        cv2.imshow('ESC to leave', image)

    # Detenemos pulsado ESC
    if cv2.waitKey(20) == 27:
        break

camera_video.release()
cv2.destroyAllWindows()
