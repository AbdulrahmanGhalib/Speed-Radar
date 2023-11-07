import cv2
from tracker import *
import numpy as np

try :
                
    mydb = mc.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "traffic_record"
    )
    mycursor = mydb.cursor()
    query = "DELETE FROM cars_information"
    mycursor.execute(query)
    mydb.commit()
except:
    print("connection error")
#Creater Tracker Object instance of  class EuclideanDistTracker in tracker.py
tracker = EuclideanDistTracker()

#cap = cv2.VideoCapture("Resources/traffic3.mp4")
cap = cv2.VideoCapture("Resources/traffic4.mp4")
fps_count=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps_count_persecond=int(cap.get(cv2.CAP_PROP_FPS))

#Object Detection
object_detector = cv2.createBackgroundSubtractorMOG2(history=None,varThreshold=None)
#100,5

#KERNALS
kernalOp = np.ones((3,3),np.uint8)
kernalCl = np.ones((11,11),np.uint8)
fgbg=cv2.createBackgroundSubtractorMOG2(detectShadows=True)
kernal_e = np.ones((5,5),np.uint8)

while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
    height,width,_ = frame.shape
    #print(height,width)
    #540,960


    #Extract ROI
    roi = frame[0:540,100:960]

    #MASKING METHOD 1
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 250, 255, cv2.THRESH_BINARY)

    #DIFFERENT MASKING METHOD 2 -> This is used
    fgmask = fgbg.apply(roi)
    ret, imBin = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
    mask1 = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, kernalOp)
    mask2 = cv2.morphologyEx(mask1, cv2.MORPH_CLOSE, kernalCl)
    e_img = cv2.erode(mask2, kernal_e)





    # cv2.imshow("fgmask",fgmask)
    # cv2.imshow("imBin",imBin)
    # cv2.imshow("mask1",mask1)
    # cv2.imshow("mask2",mask2)
    # cv2.imshow("e_img",e_img)


    contours,_ = cv2.findContours(e_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    detections = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        #THRESHOLD
        if area > 1000:
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(roi,(x,y),(x+w,y+h),(0,255,0),3)
            detections.append([x,y,w,h])

     #Object Tracking
    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
        x,y,w,h,id = box_id


        if(tracker.getsp(id)<tracker.limit()):
            cv2.putText(roi,str(id)+" "+str(tracker.getsp(id)),(x,y-15), cv2.FONT_HERSHEY_PLAIN,1,(255,255,0),2)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
        else:
            cv2.putText(roi,str(id)+ " "+str(tracker.getsp(id)),(x, y-15),cv2.FONT_HERSHEY_PLAIN, 1,(0, 0, 255),2)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 165, 255), 3)

        s = tracker.getsp(id)
        if (tracker.f[id] == 1 and s != 0):
            tracker.capture(roi, x, y, h, w, s, id)

    # DRAW LINES

    cv2.line(roi, (0, 410), (960, 410), (0, 0, 255), 2)
    cv2.line(roi, (0, 430), (960, 430), (0, 0, 255), 2)

    cv2.line(roi, (0, 235), (960, 235), (0, 0, 255), 2)
    cv2.line(roi, (0, 255), (960, 255), (0, 0, 255), 2)


    #DISPLAY
    #cv2.imshow("Mask",mask2)
    #cv2.imshow("Erode", e_img)
    cv2.imshow("ROI", roi)


    if cv2.waitKey(1000//fps_count_persecond) & 0XFF == ord('q'):
        tracker.end()
        break
cap.release()
cv2.destroyAllWindows()