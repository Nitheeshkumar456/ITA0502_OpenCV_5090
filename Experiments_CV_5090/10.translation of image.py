import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\OpenCv\Pictures\images (1).jpeg")

if image is None:
    print("Image not found!")
    exit()

# Get image dimensions
rows, cols = image.shape[:2]

# Translation values
tx = 100   # Move 100 pixels to the right
ty = 50    # Move 50 pixels downward

# Translation Matrix
M = np.float32([[1, 0, tx],
                [0, 1, ty]])

# Apply Translation
translated = cv2.warpAffine(image, M, (cols, rows))

# Display Images
cv2.imshow("Original Image", image)
cv2.imshow("Translated Image", translated)

cv2.waitKey(0)
cv2.destroyAllWindows()
