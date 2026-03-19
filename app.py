from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Video streaming route (will be implemented in phase 2)
@app.route('/video_feed')
def video_feed():
    # This will eventually yield camera frames for streaming
    return "Video feed skeleton"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
