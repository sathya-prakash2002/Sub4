import cv2
import os
capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)

imBackground = cv2.imread('Resources/background.png')

# importing the mode images into a list

folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in folderModePath:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))
    print(len(imgModeList))



while True:
    success, img = capture.read()

    imBackground[162:162 + 480, 55:55 + 640] = img
    # imBackground[44:44 + 633, 808:808 + 414] = imgModeList[0]  # 1,2,0,3


    # cv2.imshow("Webcam",img)
    cv2.imshow("Face Attendance", imBackground)
    cv2.waitKey(1)