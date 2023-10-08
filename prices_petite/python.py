from cloud import detect_objects, detect_text
import cv2


def capture():
    cv2.namedWindow("Capture")
    vc = cv2.VideoCapture(0)

    keyword = ""

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        cv2.imshow("Capture", frame)
        rval, frame = vc.read()
        frame_notext = frame.copy()
        cv2.putText(frame, "Press Enter to Capture", (120, 30), cv2.FONT_HERSHEY_PLAIN, 2, (200, 128, 0), 2)
        key = cv2.waitKey(20)

        if key == 13: # return key   --- Capture ---
            cv2.imwrite('capture.jpg', frame_notext)
            if "lay's" in detect_text("capture.jpg"):
                keyword = "Lay's chips"
            else:
                keyword = detect_objects("capture.jpg")
            break            
        elif key == 27: # exit on ESC
            break

    vc.release()
    cv2.destroyWindow("Capture")

    return keyword

if __name__ == "__main__":
    print(capture())