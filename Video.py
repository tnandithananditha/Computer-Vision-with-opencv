import cv2
cap = cv2.VideoCapture(0)  
if not cap.isOpened():
    print("Could not open video capture device")
    exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Video", width, height)
while True:
    ret, frame = cap.read()
    if not ret:
        print("Could not read frame from video capture device")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.rectangle(frame, (100, 100), (200, 200), (0, 0, 255), 2)
    cv2.imshow("Video", frame)
    cv2.imshow("Grayscale", gray)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
