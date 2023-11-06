import cv2
import numpy as np

binary_image = cv2.imread('image16992479510.png', cv2.IMREAD_GRAYSCALE)

num_labels, labeled_image = cv2.connectedComponents(binary_image)

color_map = np.random.randint(0, 256, (num_labels, 3), dtype=np.uint8)

color_map[0] = [0, 0, 0]

colored_image = color_map[labeled_image]

cv2.imshow('Colored Image', colored_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
