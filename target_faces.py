import cv2

# Change based on hardware to optimize aiming calculation
BASE_HEIGHT = 40
FOV = 78
RANGE = [50, 600]
SCREEN_CENTRE = (RANGE[0] + RANGE[1]) / 2
SCALE = 78 / (RANGE[1] - RANGE[0])


def target_faces():
    # faceCascade = cv2.CascadeClassifier(
    #     "C:\\Users\\Liam\\PycharmProjects\\QHacks2019\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
    # )
    faceCascade = cv2.CascadeClassifier(
        "C:\\Users\\Bryan\\OneDrive\\Documents\\Personal Programming\\GitHub Repos\\QHacks2019\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
    )
    video_capture = cv2.VideoCapture(1)
    face_centre = []
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE,
        )
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            adjust_power(distance_ratio=h / BASE_HEIGHT)
            turn_catapult(hor_target_pos=x + w / 2)
        # Display the resulting frame
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()


def adjust_power(distance_ratio):
    print("Distanceratio = " + str(distance_ratio))


def turn_catapult(hor_target_pos):
    offset = hor_target_pos - SCREEN_CENTRE
    turn_degree = abs(offset * SCALE)
    if offset > 0:
        # Call the turn right function
        direction = "right"
    else:
        # Call the turn left function
        direction = "left"


def main():
    target_faces()


if __name__ == "__main__":
    main()
    print("Finished target practice.")
