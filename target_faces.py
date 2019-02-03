import cv2
# import SerialInterface as si

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

    # The detection mode based on the xml file
    faceCascade = cv2.CascadeClassifier(
        "C:\\Users\\Bryan\\OneDrive\\Documents\\Personal Programming\\GitHub Repos\\QHacks2019\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
    )
    # Which video device the program will use
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
            adjust_power(distance_ratio=BASE_HEIGHT/h)
            turn_catapult(hor_target_pos=x + w / 2)
        # Display the resulting frame
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()


def turn_catapult(hor_target_pos):
    offset = hor_target_pos - SCREEN_CENTRE
    turn_degree = round(abs(offset * SCALE))
    print("Degree = " + str(turn_degree))
    # if offset > 0:
    #     # Call the turn right function
    #     si.clockwise(turn_degree)
    # else:
    #     # Call the turn left function
    #     si.counterClockwise(turn_degree)


def adjust_power(distance_ratio):
    power = round(distance_ratio * 100)
    if power > 255:
        power = 255
    # si.launch(power)
    # print("Power = " + str(power))


def main():
    target_faces()


if __name__ == "__main__":
    main()
    print("Finished target practice.")
