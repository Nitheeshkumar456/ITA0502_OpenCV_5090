import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\OpenCv\Pictures\images (6).jpeg")

if image is None:
    print("Image not found!")
    exit()

# Get image dimensions
h, w = image.shape[:2]

# Four source points from the original image
src_pts = np.float32([
    [50, 50],
    [w - 50, 50],
    [50, h - 50],
    [w - 50, h - 50]
])

# Corresponding destination points
dst_pts = np.float32([
    [0, 0],
    [w - 100, 50],
    [100, h - 50],
    [w, h]
])

# Compute Homography Matrix
H, status = cv2.findHomography(src_pts, dst_pts)

# Apply Homography Transformation
result = cv2.warpPerspective(image, H, (w, h))

# Display Images
cv2.imshow("Original Image", image)
cv2.imshow("Homography Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
