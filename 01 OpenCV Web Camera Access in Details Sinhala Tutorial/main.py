import cv2

#use the web

cap = cv2.VideoCapture(0)


while True:
    _, frame = cap.read()


    cv2.imshow('my window', frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        print("q was pressed -> exiting the loop")
        break



cv2.destroyAllWindows()
cap.release()



