import numpy as np
import cv2
#from matplotlib import pyplot as plt

# Remember to use the virtualenv (>> mkvirtualenv (name) -p python2) 
#  >> workon py2env
# and when finished
#  >> deactivate

# see: http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
cap3 = cv2.VideoCapture(3)

#w = 1280
#h = 360
#cap1.set(cv2.CAP_PROP_FRAME_WIDTH,w)
#cap1.set(cv2.CAP_PROP_FRAME_HEIGHT,h)
#cap2.set(cv2.CAP_PROP_FRAME_WIDTH,w)
#cap2.set(cv2.CAP_PROP_FRAME_HEIGHT,h)
#cap3.set(cv2.CAP_PROP_FRAME_WIDTH,w)
#cap3.set(cv2.CAP_PROP_FRAME_HEIGHT,h)

#stereo = cv2.StereoBM_create(numDisparities=64,blockSize=15)

#cv2.startWindowThread()
cv2.namedWindow("Frame A",cv2.WINDOW_NORMAL)
cv2.namedWindow("Frame B",cv2.WINDOW_NORMAL)
cv2.namedWindow("Frame C",cv2.WINDOW_NORMAL)
#cv2.namedWindow("Frame D",cv2.WINDOW_NORMAL)
#cv2.namedWindow("Result",cv2.WINDOW_NORMAL)

i=0
while(True):
    i=i+1

    # Capture frame-by-frame
    pf1 = cap1.grab()
    pf2 = cap2.grab()
    pf3 = cap3.grab()
    ret1, frame1 = cap1.retrieve()
    ret2, frame2 = cap2.retrieve()
    ret3, frame3 = cap3.retrieve()
    #ret1, frame1 = cap1.read()
    #ret2, frame2 = cap2.read()
    #ret3, frame3 = cap3.read()

    #print("got raw frame")
    #frame1, frame2 = np.hsplit(framec1,2)
    #frame3, frame4 = np.hsplit(framec2,2)
    #print("Split in half")

    # Our operations on the frame come here
    #gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    #gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    #disparity = stereo.compute(gray1,gray2)

    if (ret1 and ret2 and ret3):
        frame1l, frame1r = np.hsplit(frame1,2)
        cv2.imwrite("data/camera1/left/camera1_left_" + str(i).zfill(6) + ".jpg", frame1l)
        cv2.imwrite("data/camera1/right/camera1_right_" + str(i).zfill(6) + ".jpg", frame1r)

        frame2l, frame2r = np.hsplit(frame2,2)
        cv2.imwrite("data/camera2/left/camera2_left_" + str(i).zfill(6) + ".jpg", frame2l)
        cv2.imwrite("data/camera2/right/camera2_right_" + str(i).zfill(6) + ".jpg", frame2r)

        frame3l, frame3r = np.hsplit(frame3,2)
        cv2.imwrite("data/camera3/left/camera3_left_" + str(i).zfill(6) + ".jpg", frame3l)
        cv2.imwrite("data/camera3/right/camera3_right_" + str(i).zfill(6) + ".jpg", frame3r)

    # Display the resulting frame
    if ret1:
        cv2.imshow("Frame A",frame1)
    if ret2:
        cv2.imshow("Frame B",frame2)
    if ret3: 
        cv2.imshow("Frame C",frame3)
    #cv2.imshow("Result",disparity/256)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap1.release()
cap2.release()
cap3.release()
cv2.destroyAllWindows()
