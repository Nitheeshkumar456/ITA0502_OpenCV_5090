import cv2
import numpy as np

# Open the video
cap = cv2.VideoCapture(r"C:\OpenCv\WhatsApp Video 2026-07-15 at 14.52.42.mp4")

if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Get frame dimensions
    h, w = frame.shape[:2]

    # Source points (Original)
    pts1 = np.float32([
        [50, 50],
        [w - 50, 50],
        [50, h - 50],
        [w - 50, h - 50]
    ])

    # Destination points (Perspective Changed)
    pts2 = np.float32([
        [0, 0],
        [w, 50],
        [100, h],
        [w - 100, h - 50]
    ])

    # Perspective Transformation Matrix
    M = cv2.getPerspectiveTransform(pts1, pts2)

    # Apply Perspective Transformation
    transformed = cv2.warpPerspective(frame, M, (w, h))

    # Display
    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Transformed Video", transformed)

    # Press Q to Exit
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
