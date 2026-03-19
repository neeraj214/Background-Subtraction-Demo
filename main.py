import cv2
import sys

def main():
    # 1. Initialize VideoCapture with camera index 0
    cap = cv2.VideoCapture(0)

    # 2. Error check to see if camera opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam at index 0.")
        sys.exit()

    print("Live Feed started. Press 'q' to exit.")

    # 3. Start a while loop to read frames continuously
    while True:
        # 4. Read one frame from the camera
        # ret is a boolean (True if frame read successfully), frame is the image array
        ret, frame = cap.read()

        # 5. Check if frame was captured successfully
        if not ret:
            print("Error: Could not read frame from camera.")
            break

        # 6. Display the live frame in a window titled "Live Feed"
        cv2.imshow("Live Feed", frame)

        # 7. Wait for 30ms and check if 'q' is pressed to exit
        # waitKey(30) allows the window to refresh and handles keyboard input
        if cv2.waitKey(30) & 0xFF == ord('q'):
            print("Exiting...")
            break

    # 8. Clean exit: Release camera resource and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
    print("Webcam closed cleanly.")

if __name__ == "__main__":
    main()
