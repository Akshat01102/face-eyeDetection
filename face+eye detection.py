import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)


while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces and eyes
    faces = face_cascade.detectMultiScale(gray, 1.05,12)
    eyes = eye_cascade.detectMultiScale(gray, 2,12)
    # Draw the rectangle around each face and circle around eyes
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 3)
    for (x1, y1, w1, h1) in eyes:
        cv2.circle(img, (int((2*x1+w1)/2), int((2*y1+h1)/2)), 40, (255, 255, 255), 1)
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()