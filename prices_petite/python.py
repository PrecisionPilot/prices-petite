from cloud import detect_objects, detect_text
import cv2

def capture():
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    keyword = ""

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 13: # return key   --- Capture ---
            cv2.imwrite('capture.jpg', frame)
            if "lay's" in detect_text("capture.jpg"):
                keyword = "Lay's chips"
            else:
                keyword = detect_objects("capture.jpg")
            break
        elif key == 27: # exit on ESC
            break

    vc.release()
    cv2.destroyWindow("preview")

    return keyword

if __name__ == "__main__":
    print(capture())