from flask import Flask, render_template, Response
import cv2
from flask_cors import CORS
import mediapipe
import pyautogui
import numpy as np
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

app = Flask(__name__)
CORS(app)
camera = cv2.VideoCapture(0)
capture_hands = mediapipe.solutions.hands.Hands()
drawing_utils = mediapipe.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
drawing_option = mediapipe.solutions.drawing_utils

import numpy as np
pyautogui.FAILSAFE = False
def frames():
    while True:
        s, frame = camera.read()
        if not s:
            break
        
        frame = cv2.flip(frame, 1)
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output_hands = capture_hands.process(rgb_image)
        all_hands = output_hands.multi_hand_landmarks

        if all_hands:
            for hand in all_hands:
                drawing_utils.draw_landmarks(frame, hand)
                hand_landmarks = np.array([[lm.x, lm.y] for lm in hand.landmark])
                
                # Extract specific landmarks
                index_finger_tip = hand_landmarks[8]
                thumb_tip = hand_landmarks[4]
                
                
                # Calculate pixel coordinates
                x1, y1 = int(index_finger_tip[0] * frame.shape[1]), int(index_finger_tip[1] * frame.shape[0])
                x2, y2 = int(thumb_tip[0] * frame.shape[1]), int(thumb_tip[1] * frame.shape[0])
                
                # Calculate screen coordinates
                mouse_x = int(screen_width * index_finger_tip[0])
                mouse_y = int(screen_height * index_finger_tip[1])
                
                # Update mouse position if finger moves significantly
                if np.linalg.norm([x2 - x1, y2 - y1]) > 30:
                    pyautogui.moveTo(mouse_x, mouse_y)
                    cv2.circle(frame, (x1, y1), 10, (0, 255, 255), -1)  # Highlight finger tip
                
                    # Simulate a click if fingers are close
                    if np.abs(y2 - y1) <= 50:
                        pyautogui.click()
                        print("click")

        ret, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')




@app.route("/")
def index():
    return render_template("frontend.html")


@app.route("/video")
def video():
    return Response(frames(), mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    app.run(debug=True, port = "8001")

