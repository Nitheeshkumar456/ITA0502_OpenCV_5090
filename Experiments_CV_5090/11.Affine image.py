import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\OpenCv\Pictures\images (3).jpeg")

if image is None:
    print("Image not found!")
    exit()

# Get image size
rows, cols = image.shape[:2]

# Select three points from the original image
pts1 = np.float32([[50, 50],
                   [200, 50],
                   [50, 200]])

# Corresponding points in the transformed image
pts2 = np.float32([[10, 100],
                   [200, 50],
                   [100, 250]])

# Create Affine Transformation Matrix
M = cv2.getAffineTransform(pts1, pts2)

# Apply Affine Transformation
affine = cv2.warpAffine(image, M, (cols, rows))

# Display Images
cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformation", affine)

cv2.waitKey(0)
cv2.destroyAllWindows()
