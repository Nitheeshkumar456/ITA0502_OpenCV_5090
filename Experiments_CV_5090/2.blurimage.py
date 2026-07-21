import cv2

# Read Image
image = cv2.imread(r"C:\OpenCv\Pictures\images (9).jpeg")

if image is None:
    print("Image not found!")
    exit()

# Gaussian Blur
blur = cv2.GaussianBlur(image, (7, 7), 0)

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Blur", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
