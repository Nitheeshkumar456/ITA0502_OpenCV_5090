import cv2
import numpy as np

# Read Image
image = cv2.imread(r"C:\OpenCv\Pictures\images (12).jpeg")

if image is None:
    print("Image not found!")
    exit()

# Create Kernel
kernel = np.ones((5, 5), np.uint8)

# Erode
eroded = cv2.erode(image, kernel, iterations=1)

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()
