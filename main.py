import cv2
import numpy as np

# QUESTION 1
image = cv2.imread("data\dental_xray.tif", cv2.IMREAD_COLOR)

row, col = np.where(image[:, :, 0] >= 230)

# Set those pixels to red color
image[row, col] = [0, 0, 255]  # BGR color format, set red to [0, 0, 255]

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# QUESTION 2

