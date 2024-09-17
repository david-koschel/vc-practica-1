import cv2

vid = cv2.VideoCapture(0)

while (True):
    # fotograma a fotograma
    ret, frame = vid.read()

    # Hay nuevo fotograma
    if ret:
        # Convertir el fotograma a escala de grises
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Encontrar los píxeles más oscuros y más claros
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(frame_gray)

        # Dibujar un círculo en el píxel más oscuro
        cv2.circle(frame, min_loc, 10, (0, 0, 255), 2)

        # Dibujar un círculo en el píxel más claro
        cv2.circle(frame, max_loc, 10, (255, 0, 0), 2)

        # Muestra fotograma
        cv2.imshow('Vid', frame)

    if cv2.waitKey(20) == 27:
        break

# Libera el objeto de captura
vid.release()
# Destruye ventanas
cv2.destroyAllWindows()