import cv2, time
video=cv2.VideoCapture("highway_traffic.mp4")
a=0
while True:
    a=a+1
    check, frame = video.read()
    print(frame)
    cv2.imshow("capturing", frame)
    key=cv2.waitKey(1)

    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()