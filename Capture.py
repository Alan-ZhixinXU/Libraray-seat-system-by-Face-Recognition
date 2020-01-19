import cv2
capture = cv2.VideoCapture(0)
while True:
    ref, frame = capture.read()
    cv2.imshow('Capturing',frame)

    c = cv2.waitKey(1)
    if  c  == ord('s'): #s 键保存并退出
        cv2.imwrite('Face_picture.jpg', frame)
        cv2.destroyAllWindows()
        break

    elif c == 20:
        #20s未拍摄，按Esc退出摄像
        cv2.destroyAllWindows()
        break
    
capture.release()



