import cv2

# Video captute
# 0 or 1 based on the type and the number of your cameras
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()      # We don't want ret in this
    cv2.imshow("Frame", frame) # Show the current frame

    key = cv2.waitKey(1)
    if key==27: # If you press Esc then the frame window will close (and the program also)
        break
    elif key==ord('p'): # If you press p/P key on your keyboard
        cv2.imwrite("pic.jpg", frame) # Save current frame as picture with name pic.jpg

cap.release()
cv2.destroyAllWindows()