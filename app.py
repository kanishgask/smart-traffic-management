from flask import Flask, render_template, Response
import cv2
from vehicle_detection import detect_vehicles
from traffic_logic import signal_control

app = Flask(__name__)

camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = camera.read()

        if not success:
            break
        else:
            vehicle_count, frame = detect_vehicles(frame)

            signal = signal_control(vehicle_count)

            cv2.putText(
                frame,
                f"Signal: {signal}",
                (50,50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2
            )

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield(b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' +
                  frame +
                  b'\r\n')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/video')
def video():
    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


if __name__=="__main__":
    app.run(debug=True)
