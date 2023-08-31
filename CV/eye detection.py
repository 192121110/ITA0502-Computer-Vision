import cv2
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
image_path = "C:/Users/gnana/Downloads/125019349.jfif"
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
for (ex, ey, ew, eh) in eyes:
    cv2.rectangle(image, (ex, ey), (ex + ew, ey + eh), (0, 0, 0), 2) 
cv2.imshow('Eye Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()



