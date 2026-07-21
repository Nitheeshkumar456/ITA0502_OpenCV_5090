import cv2

# Read the image
image = cv2.imread(r"C:\OpenCv\Pictures\sample_parrot-image.jpg")

if image is None:
    print("Image not found!")
    exit()

# Scale images
bigger = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Bigger Image", bigger)
cv2.imshow("Smaller Image", smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()
