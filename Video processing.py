import cv2
cap = cv2.VideoCapture('video.mp4')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('processed_video.mp4', fourcc, 30, (width, height))

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    edges = cv2.Canny(gray, 100, 200)
    
    out.write(edges)
    
    cv2.imshow('original', frame)
    cv2.imshow('edges', edges)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
