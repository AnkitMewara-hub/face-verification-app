import cv2
import numpy as np
import face_recognition
import os

def verify_face():
    known_face_encodings = []
    known_face_names = []

    faces_path = "known_faces"
    for filename in os.listdir(faces_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            path = os.path.join(faces_path, filename)
            image = face_recognition.load_image_file(path)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_face_encodings.append(encodings[0])
                known_face_names.append(os.path.splitext(filename)[0])

    video_capture = cv2.VideoCapture(0)
    verified_name = None
    result = False

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_encodings = face_recognition.face_encodings(rgb_small_frame)
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                verified_name = known_face_names[best_match_index]
                result = True
                break

        if result:
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return result, verified_name
