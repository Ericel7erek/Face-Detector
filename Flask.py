from flask import Flask, render_template, request, Response
import cv2

app = Flask(__name__)

# Initialize video capture object (for webcam)
video_capture = cv2.VideoCapture(0)  # Use 0 for webcam, or specify the path to the video file

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/video_feed')
def video_feed():
    return Response(detect_faces(), mimetype='multipart/x-mixed-replace; boundary=frame')

def detect_faces():
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Perform facial detection (replace this with your actual facial detection code)
        # For demonstration purposes, let's draw a rectangle around the center of the frame
        height, width, _ = frame.shape
        center_x = width // 2
        center_y = height // 2
        cv2.rectangle(frame, (center_x - 50, center_y - 50), (center_x + 50, center_y + 50), (0, 255, 0), 2)

        ret, jpeg = cv2.imencode('.jpg', frame)
        frame_bytes = jpeg.tobytes()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
