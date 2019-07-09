import cv2 as cv
Width = 650
Hight =500
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')


def detect_face(name,original,gray):
    faces = face_cascade.detectMultiScale(gray,scaleFactor= 1.3,minNeighbors= 5)
    for (x,y,w,h) in faces:
        cv.rectangle(original,(x,y),(x+w,y+h),(0,0,255),2)

    cv.imshow("name",original)



def read_image(img_name,ColorScheme):
    img = cv.imread(img_name,ColorScheme)
    resized = cv.resize(img,(Width,Hight))
    gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
    detect_face(img_name,resized,gray)
    cv.waitKey(0)
    cv.destroyAllWindows()


def read_video(name):
    cap = cv.VideoCapture(0)
    # Capture frame-by-frame
    while(True):
        ret, frame = cap.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        detect_face(name,frame,gray)

    # Our operations on the frame come here



        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()

read_image("willy.jpg",1)#name of the image if in the same directory else the location of the image
read_video("myface")
