import cv2


cap=cv2.VideoCapture(0)


while True:
    
    work,frame=cap.read()
    flipframe=cv2.flip(frame, 0)
  
    cv2.imshow("my ugly face",flipframe)
    
    cv2.imshow("another my ugly face",frame)
    
    if cv2.waitKey(1)&0xff==ord("q"):
        break