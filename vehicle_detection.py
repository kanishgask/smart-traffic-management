import cv2

car_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_car.xml'
)

def detect_vehicles(frame):

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(
        gray,
        1.1,
        3
    )

    count = len(cars)

    for(x,y,w,h) in cars:
        cv2.rectangle(
            frame,
            (x,y),
            (x+w,y+h),
            (255,0,0),
            2
        )

    cv2.putText(
        frame,
        f"Vehicles:{count}",
        (50,100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,0,255),
        2
    )

    return count, frame
