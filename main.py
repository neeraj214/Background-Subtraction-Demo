import cv2
import numpy as np
import datetime

def motion_detection():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    
    # Initialize Background Subtractor
    # MOG2 is a popular algorithm for background subtraction
    back_sub = cv2.createBackgroundSubtractorMOG2()

    print("Motion Detection started. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Apply background subtraction
        fg_mask = back_sub.apply(frame)

        # Basic noise reduction (optional for skeleton)
        _, fg_mask = cv2.threshold(fg_mask, 250, 255, cv2.THRESH_BINARY)

        # Find contours of moving objects
        contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) < 500:
                continue
            
            # Motion detected!
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Log motion (will be implemented in phase 2)
            # timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # print(f"Motion detected at {timestamp}")

        # Display the result
        cv2.imshow('Motion Detection', frame)
        cv2.imshow('Foreground Mask', fg_mask)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    motion_detection()
