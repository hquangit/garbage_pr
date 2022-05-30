import matplotlib.pyplot as plt
import cv2
import numpy as np

image_path = "/home/quan/Rikai/3d_box_2/3D-BoundingBox/eval/image_2/000008.png"
labbel_path = "/home/quan/Rikai/3d_box_2/3D-BoundingBox/eval/label_2/000008.txt"

image = cv2.imread(image_path)
image_black = np.zeros((375, 1242, 3),np.uint8)
# print(image.shape)

red = (0,0,255)
blue = (255,0,0)
green = (0,255,0)

# image_black[167, 805]=red
# image_black[328, 995]=blue
image = cv2.line(image, (956, 884), (240,178), green, 9)
# image = cv2.line(image, (402, 240), (192,956), green, 9)
# cv2.imshow('image2',image_black)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# bbox = [(804.79, 167.34), (995.43, 327.94)]
# bbox = [(884.52 178.31), (956.41 240.18)]

# print(bbox[0])