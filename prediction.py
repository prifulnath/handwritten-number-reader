import joblib
import time
import cv2
import numpy as np
import pyscreenshot as ImageGrab

model = joblib.load('model/digit_recognizer')
image_folder = "img/"

while True:
    image = ImageGrab.grab(bbox=(41,280,938,958))
    image.save(image_folder + "image.png")

    im = cv2.imread(image_folder + "image.png")
    image_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    image_gray  =cv2.GaussianBlur(image_gray, (15,15), 0)
    
    #Threshold the image
    ret, image_threshold = cv2.threshold(image_gray, 100, 255, cv2.THRESH_BINARY)
    reason_of_intrest = cv2.resize(image_threshold, (28,28), interpolation  =cv2.INTER_AREA)
    rows,cols = reason_of_intrest.shape
    
    X = []
    ##  Fill the data array with pixels one by one.
    for i in range(rows):
        for j in range(cols):
            k = reason_of_intrest[i,j]
            k = 1 if k>100 else 0
            X.append(k)

    predictions = model.predict([X])
    print("Prediction:", predictions[0])
    cv2.putText(
        im,
        "Prediction is: " + str(predictions[0]),
        (20,20), 0, 0.8,(0,255,0),2,cv2.LINE_AA
    )
    
    cv2.startWindowThread()
    cv2.namedWindow("Result")
    cv2.imshow("Result",im)
    cv2.waitKey(10000)
    # 27 is the ascii value of esc, 13 is the ascii value of enter
    if cv2.waitKey(1)==13: 
        break
    cv2.destroyAllWindows()
