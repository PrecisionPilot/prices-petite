from cloud import detect_objects, detect_text
import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 13: # return key
        cv2.imwrite('capture.jpg', frame)
        detect_objects("capture.jpg")
    elif key == 27: # exit on ESC
        break

vc.release()
cv2.destroyWindow("preview")