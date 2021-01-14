import cv2
import winsound
cam = cv2.VideoCapture(0)

while cam.isOpened():
    #ret-retrive
    #to read the
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    #taken two frame to see the differnece
    diff = cv2.absdiff(frame1, frame2)
    #convert colour full image to gray colour to get the accurate diffrence between the two image
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    #make the image blur
    blur = cv2.GaussianBlur(gray,(5,5), 0)
    #threshold:-getting read of nises and unwanted things
    _,thres = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated= cv2.dilate(thres, None, iterations=3)
    #contours are the borderof the detected things
    contours, _ = cv2.findContours(dilated,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1, contours, -1, (0,255,0), 2)
    for c in contours:
        if cv2.contourArea(c)<5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        # winsound.Beep(500,200)
        winsound.PlaySound('alert.mp3', winsound.SND_ASYNC)
    #press q to close the camera
    if cv2.waitKey(10) == ord('q'):
        break;
    #to show in your computer(camera open in your  computer)
    cv2.imshow('Security Cam',frame1) 