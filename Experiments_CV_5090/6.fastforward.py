import cv2

video = cv2.VideoCapture(r"C:\OpenCv\WhatsApp Video 2026-07-15 at 14.52.42.mp4")

while video.isOpened():
    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow("Fast Motion Video", frame)

    # Fast motion
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
