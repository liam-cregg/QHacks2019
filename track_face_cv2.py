import cv2

def track_faces():
    faceCascade = cv2.CascadeClassifier('C:\\Users\\Liam\\PycharmProjects\\QHacks2019\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

    video_capture = cv2.VideoCapture(0)
    centre_face = []

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            centre_face = [(x + w/2), (y+(w/2))]
            print(centre_face)
            return centre_face

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    track_faces()