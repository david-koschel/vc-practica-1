# PRÁCTICA 1. VISIÓN POR COMPUTADOR

> Trabajo realizado por:
> - David Koschel Henríquez
> - Pablo Nicolás Santana Hernández

## Tareas realizadas durante la práctica

- [x] **TAREA 1.** Crear una imagen con la textura de un tablero de ajedrez
- [x] **TAREA 2.** Crear una imagen estilo Mondrian como por ejemplo la mostrada a continuación:
- [X] **TAREA 3.** Hacer uso de las funciones de dibujo de OpenCV
- [X] **TAREA 4.** Modificar un plano de la imagen
- [X] **TAREA 5.** Destacar tanto el píxel con el color más claro como con el color más oscuro de una imagen
- [X] **TAREA 6.** Hacer una propuesta pop art con la entrada de la cámara web o vídeo

***

### TAREA 1

Para crear el tablero de ajedrez se crea un fondo negro de tamaño 800. Posteriormente, se va recorriendo cada fila y
se va pintando un cuadrado de negro cada dos columnas. Dependiendo si la columna impar o par, se empieza pintando
la primera o segunda columna.

### TAREA 2

Para crear el Mondrian se genera un fondo negro y luego se crean cuadros de distintos tamaños y colores en rangos
definidos. Los colores usados son:

- Azul
- Rojo
- Amarillo
- Blanco
- Negro

### TAREA 3

Se reutilizó el código creado en la resolución de la tarea 1, el tablero de ajedrez,
pero en lugar de modificar los píxeles del fondo, se crean cuadrados de color blanco con OpenCV.

### TAREA 4

Para esta tarea, se realizaron modificaciones en los planos azul y verde de la imagen, ajustándolos para que se
mostraran en blanco y negro. Además, se creó una máscara destinada a detectar los píxeles con menor intensidad en la
capa roja, para luego transformarlos también a blanco y negro. El objetivo de este proceso fue resaltar únicamente los
objetos de color rojo en la imagen. Las pruebas se llevaron a cabo con dos webcams distintas, en una de ellas el efecto
se logró con éxito, mientras que en la otra los resultados no fueron tan satisfactorios.

### TAREA 5

Para poder pintar círculos en los píxeles más claros y oscuros, en el código se convierte el frame recibido por cámara a
escala de grises para poder utilizar la función ***minMaxLoc()*** y luego usar *cv2.circle()* alrededor de estos
píxeles.

El frame en escala de grises solo se utiliza para la obtención de los píxeles comentados anteriormente y los círculos se
pintan sobre el frame sin modificación.

### TAREA 6

Para la última tarea, se copió la imagen 4 veces y a cada una se le modificaron ciertos canales, dando un resultado
estilo _Pop Art_.