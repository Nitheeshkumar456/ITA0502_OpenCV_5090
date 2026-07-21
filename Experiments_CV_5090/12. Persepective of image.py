import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\OpenCv\Pictures\images (5).jpeg")

if image is None:
    print("Image not found!")
    exit()

# Get image dimensions
rows, cols = image.shape[:2]

# Four points from the original image
pts1 = np.float32([[50, 50],
                   [300, 50],
                   [50, 300],
                   [300, 300]])

# Corresponding points in the output image
pts2 = np.float32([[0, 0],
                   [300, 0],
                   [100, 300],
                   [250, 300]])

# Create Perspective Transformation Matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

# Apply Perspective Transformation
perspective = cv2.warpPerspective(image, M, (cols, rows))

# Display Images
cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformation", perspective)

cv2.waitKey(0)
cv2.destroyAllWindows()
