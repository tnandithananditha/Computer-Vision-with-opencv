import cv2
import numpy as np
width = 640
height = 480
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))
for i in range(100):
    frame = np.zeros((height, width, 3), np.uint8)
    cv2.putText(frame, 'Frame ' + str(i), (int(width/2)-50, int(height/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    out.write(frame)
out.release()
cv2.destroyAllWindows()
