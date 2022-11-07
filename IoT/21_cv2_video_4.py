import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while cap.isOpened() :
    ret, img = cap.read()

    if ret :
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces :
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow("Video Caputre", img)

        key = cv2.waitKey(1) &0xFF
        if key == 27 :
            break

cap.release()
cv2.destroyAllWindows()
