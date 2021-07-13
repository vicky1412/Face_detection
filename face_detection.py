import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("randeep.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=5)

for x,y,z,w in faces:
    rec = cv2.rectangle(img,(x,y),(x+z,y+w),(0,255,0),thickness=5)
print(rec)



cv2.imshow("randeep",img)
cv2.waitKey()