import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound

# Función para convertir texto a voz
def speech(text):
    print(text)
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)
    
    # Guarda el archivo de audio generado
    output.save("./sounds/output.mp3")
    # Reproduce el archivo de audio generado
    playsound("./sounds/output.mp3")

# Inicializa la captura de video desde la cámara (índice 0)
video = cv2.VideoCapture(0)
labels = []

while True:
    # Lee un cuadro (frame) del video
    ret, frame = video.read()
    
    # La biblioteca cvlib ha aprendido algunos objetos básicos usando aprendizaje de objetos
    # Generalmente, se necesitan alrededor de 800 imágenes para que aprenda qué es un teléfono.
    bbox, label, conf = cv.detect_common_objects(frame, model='yolov4-tiny')
    
    # Dibuja las cajas delimitadoras en la imagen
    output_image = draw_bbox(frame, bbox, label, conf)
    
    # Muestra la imagen con detección de objetos
    cv2.imshow("Detection", output_image)
    
    # Agrega etiquetas detectadas a la lista si no están ya presentes
    for item in label:
        if item in labels:
            pass
        else:
            labels.append(item)
    
    # Si se presiona la tecla "q", sale del bucle
    if cv2.waitKey(1) & 0xFF == ord("q"):
        video.release()
        cv2.destroyAllWindows()
        break

# Genera una frase con las etiquetas detectadas
i = 0
new_sentence = []
for label in labels:
    if i == 0:
        new_sentence.append(f"I found a {label} ")
    else:
        new_sentence.append(f", a {label},")
    i += 1
new_sentence.append(f", And that concludes my findings ")

# Convierte la frase a voz y la reproduce
speech(" ".join(new_sentence))
# Imprime las etiquetas detectadas
print(labels)

