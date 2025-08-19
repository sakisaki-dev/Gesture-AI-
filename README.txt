Gesture-Controlled AI Mouse
This project is a real-time, gesture-based mouse controller that allows you to use hand movements to interact with your computer's cursor. It uses a combination of computer vision and AI to track your hand and translate its movements into mouse actions.

🚀 Features
Real-Time Mouse Control: Move the cursor by moving your hand in front of the camera.

Clicking Functionality: Perform a left-click by pinching your index finger and thumb together.

Multi-Platform: Works on any system with a webcam and the necessary dependencies.

Web-Based Video Feed: Streams the camera's output with real-time hand tracking and annotations directly to a web browser.

⚙️ Getting Started
Prerequisites
Python 3.x

A webcam

Installation
Clone this repository to your local machine:

git clone [Your-Repository-URL-Here]
cd [your-project-directory]

Install the required Python packages using the provided requirements.txt file:

pip install -r requirements.txt

Running the Application
Make sure your webcam is connected and not in use by another application.

Run the Flask application from your terminal:

python your_app_name.py

(Note: Replace your_app_name.py with the actual name of your Python file.)

🧠 How It Works
The application utilizes the MediaPipe Hands solution to detect and track hand landmarks in real-time. It processes each frame from the webcam  OpenCV and then uses the coordinates of specific landmarks (e.g., the tip of the index finger) to control the pyautogui library, which moves the computer's mouse. The click action is triggered by detecting the distance between the index finger tip and the thumb tip, simulating a pinch gesture.

requirements.txt
Flask
Flask-Cors
opencv-python
mediapipe
pyautogui
numpy
