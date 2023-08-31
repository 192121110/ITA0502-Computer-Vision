import cv2
path="C:/Users/gnana/Downloads/download.jfif"
img = cv2.imread(path)
img = cv2.resize(img,(600,600))
cv2.imshow(img)
cv2.waitKey(0)
