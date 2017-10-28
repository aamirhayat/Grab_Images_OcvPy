import cv2

cam1 = cv2.VideoCapture(1)
cam2 = cv2.VideoCapture(2)

cv2.namedWindow("test")
cv2.namedWindow("test2")

img_counter = 0
#set the width and height, and UNSUCCESSFULLY set the exposure time
cam1.set(3,1280) # For logitech C270 webcam 1280x720
cam1.set(4,720) 
cam2.set(3,1280)  # Other dimension 640x480
cam2.set(4,720 )

while True:
    ret, frame = cam1.read()
    ret2, frame2 = cam2.read()
    cv2.imshow("test", frame)
    cv2.imshow("test2", frame2)

    if not ret and ret2:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "camL{}.png".format(img_counter)
        img_name2 = "camR{}.png".format(img_counter)

        cv2.imwrite(img_name, frame)
        cv2.imwrite(img_name2, frame2)
        print("{} written cam1!".format(img_name))
        #cv2.imwrite(img_name, frame)
        print("{} written cam2!".format(img_name))
        img_counter += 1
        

cam1.release()

cv2.destroyAllWindows()