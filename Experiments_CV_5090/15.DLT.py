import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\OpenCv\Pictures\images (7).jpeg")

if image is None:
    print("Image not found!")
    exit()

# Get image dimensions
h, w = image.shape[:2]

# Source points
src_pts = np.float32([
    [50, 50],
    [w - 50, 50],
    [50, h - 50],
    [w - 50, h - 50]
])

# Destination points
dst_pts = np.float32([
    [0, 0],
    [w - 100, 50],
    [100, h - 50],
    [w, h]
])

# Compute Homography using Direct Linear Transformation (DLT)
H, status = cv2.findHomography(src_pts, dst_pts, 0)

# Apply the transformation
result = cv2.warpPerspective(image, H, (w, h))

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("DLT Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
