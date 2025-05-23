
## Read Image

import cv2

# LOAD AN IMAGE USING 'IMREAD'
#img = cv2.imread("Resources/Vaish.jpg")
# DISPLAY
#cv2.imshow("Vaishnavi Kukkala",img)
#cv2.waitKey(0)



## Read Video

# import cv2
#
# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture("Resources/test_ video.mp4")
# while True:
#     success, img = cap.read()
#     img = cv2.resize(img, (frameWidth, frameHeight))
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# Read Webcam
import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)
cap.set(10,100)

while True:
    success, img = cap.read()
    cv2.imshow("My Cam", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break