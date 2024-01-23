import cv2
import pafy  # object detection in YouTube videos


def live_capture() -> None:
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()  # read frame from camera
        frame = cv2.flip(frame, flipCode=1)

        text = "Greetings kind stranger :D"
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (85, 40, 0), 3)

        cv2.imshow('Video Capture', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()


def youtube_capture(url: str):
    # TODO: youtube capture functionality
    video = pafy.new(url).streams[-1]
    cap = cv2.VideoCapture(video)


if __name__ == "__main__":
    live_capture()
