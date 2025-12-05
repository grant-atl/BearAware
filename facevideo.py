import cv2
from deepface import DeepFace
import dlib
from collections import Counter
import time
import serial


ser = serial.Serial('/dev/cu.usbmodem1101', 9600)

faceCascade = dlib.get_frontal_face_detector()

frame_rate = 10

image_size = (640, 480)


def open_camera():
    camera_index = 0
    while True:
        cap = cv2.VideoCapture(camera_index)
        if cap.isOpened():
            print(f"Camera opened at index {camera_index}")
            return cap
        else:
            print(f"Cannot open camera at index {camera_index}")
            camera_index += 1
            if camera_index > 10:
                raise IOError("Cannot open any camera")


cap = open_camera()
emotions = []
start_time = time.time()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: No frame captured")
        continue

    frame = cv2.resize(frame, image_size)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade(gray)

    if len(faces) > 0:
        result = DeepFace.analyze(frame, actions=['emotion'])
        emotions.append(result[0]['dominant_emotion'])
    else:
        emotions.append('No face found')

    if time.time() - start_time >= 1:
        counter = Counter(emotions)
        dominant_emotion, _ = counter.most_common(1)[0]
        ser.write(dominant_emotion.encode())

        emotions = []
        start_time = time.time()
    else:
        continue

    for rect in faces:
        x, y, w, h = rect.left(), rect.top(), rect.width(), rect.height()
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(frame,
                dominant_emotion,
                (50, 50),
                font, 3,
                (0, 0, 255),
                2,
                cv2.LINE_4)
    cv2.imshow('Video', frame)

    if cv2.waitKey(int(1000 / frame_rate)) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
