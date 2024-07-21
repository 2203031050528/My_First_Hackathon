from flask import Flask, Response, render_template
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

app = Flask(__name__)

height = 480
width = 1280

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)

detector = HandDetector(detectionCon=0.8, maxHands=1)

# Annotation variables
annotation = [[]]
annotationStart = False
annotationNumber = -1
shapeName = ""

def shapeClassification(contour):
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)

    if len(approx) == 3:
        return "Triangle"
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w) / h
        if 0.95 <= aspectRatio <= 1.05:
            return "Square"
        else:
            return "Rectangle"
    elif len(approx) == 5:
        return "Pentagon"
    else:
        return "Circle"

def generate_frames():
    global annotationStart, annotationNumber, annotation, shapeName

    while True:
        success, img = cap.read()
        if not success:
            break

        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img)

        if hands:
            hand = hands[0]
            fingers = detector.fingersUp(hand)
            lmList = hand['lmList']

            yVal = int(np.interp(lmList[8][1], [100, height - 100], [0, height]))
            indexFinger = lmList[8][0], yVal

            if fingers == [0, 1, 1, 0, 0]:
                cv2.circle(img, indexFinger, 12, (0, 0, 255), cv2.FILLED)

            if fingers == [0, 1, 0, 0, 0]:
                if annotationStart is False:
                    annotationStart = True
                    annotationNumber += 1
                    annotation.append([])

                cv2.circle(img, indexFinger, 12, (0, 0, 255), cv2.FILLED)
                annotation[annotationNumber].append(indexFinger)
            else:
                if annotationStart:
                    annotationStart = False
                    if len(annotation[annotationNumber]) > 2:
                        contour = np.array(annotation[annotationNumber], dtype=np.int32)
                        cv2.drawContours(img, [contour], 0, (0, 255, 0), 2)
                        shapeName = shapeClassification(contour)

                if fingers == [0, 1, 1, 1, 0]:
                    if annotation:
                        annotation.pop(-1)
                        annotationNumber -= 1
                        shapeName = ""

        for i in range(len(annotation)):
            for j in range(len(annotation[i])):
                if j != 0:
                    cv2.line(img, annotation[i][j - 1], annotation[i][j], (0, 0, 255), 12)

        if shapeName:
            cv2.putText(img, shapeName, (380, 360), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

        ret, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
