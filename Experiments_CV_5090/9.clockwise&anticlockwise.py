import cv2

# Read the image
image = cv2.imread(r"C:\OpenCv\Pictures\images.jpeg")

if image is None:
    print("Image not found!")
    exit()

# Rotate 90° Clockwise
clockwise = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Rotate 90° Counter Clockwise
counter_clockwise = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Display Images
cv2.imshow("Original Image", image)
cv2.imshow("Clockwise Rotation", clockwise)
cv2.imshow("Counter Clockwise Rotation", counter_clockwise)

cv2.waitKey(0)
cv2.destroyAllWindows()
