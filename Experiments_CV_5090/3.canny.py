import cv2

# Read Image
image = cv2.imread(r"C:\OpenCv\Pictures\images (10).jpeg")

if image is None:
    print("Image not found!")
    exit()

# Convert to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Canny Edge Detection
edges = cv2.Canny(gray, 100, 200)

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Canny Edge Detection", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
