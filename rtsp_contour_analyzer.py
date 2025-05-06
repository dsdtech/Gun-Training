import cv2
import numpy as np
import imutils

# declare variables

framewidth = 1920
frameheight = 1080
RTSP_URL = 'rtsp://xxxxxx:xxxxxxxx@192.168.1.64:554/Streaming/channels/1'
cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)
cap.set(3, framewidth)
cap.set(4, frameheight)
if not cap.isOpened():
    print('Cannot open RTSP stream')
    exit(-1)

# pseudo function

def empty(a):
    pass

# slider

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640,240)
cv2.createTrackbar("Threshold1","Parameters",16,255,empty)
cv2.createTrackbar("Threshold2","Parameters",192,255,empty)
cv2.createTrackbar("Threshold3","Parameters",243,255,empty)
cv2.createTrackbar("Threshold4","Parameters",255,255,empty)

# imagestack

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver



def getContours(imgDil,imgContour):

    contours, hierarchy = cv2.findContours(imgDil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # compute the center of the contour
        M = cv2.moments(cnt)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        # draw the contour and center of the shape on the image

        if area > 5000:
            cv2.drawContours(imgContour, cnt, -1, (255, 0 ,255),3)
            cv2.circle(imgContour, (cX, cY), 7, (255, 0, 255), -1)
            cv2.putText(imgContour, "center", (cX - 20, cY - 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)


while(True):
    success, img = cap.read()
    imgContour = img.copy()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    threshold3 = cv2.getTrackbarPos("Threshold3", "Parameters")
    threshold4 = cv2.getTrackbarPos("Threshold4", "Parameters")
    ret, thresh = cv2.threshold(imgGray,threshold1,threshold2,1)
    imgCanny = cv2.Canny(imgGray,threshold3,threshold4)
    kernel = np.ones((3,3))
    imgDil = cv2.dilate(thresh, kernel, iterations=1)
    getContours(imgDil,imgContour)

    imgStack = stackImages(0.4,([img,imgGray,thresh],[imgCanny,img,imgContour]))

    cv2.imshow('Result',imgStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
