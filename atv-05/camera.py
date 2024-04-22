import cv2 as cv

camera = cv.VideoCapture(0)

while True:
    status, frame = camera.read()
    key = cv.waitKey(1) & 0xff
    if not status or key == ord('q'):
        break
    cv.imshow("webcam", frame)
    if key == ord('s'):
        cv.imwrite("foto_salva.jpg", frame)
camera.release()
cv.destroyAllWindows()
