import cv2
from ultralytics import YOLO
import json
import requests
import time

# Load your trained YOLOv8 model
model = YOLO('./runs/detect/train/weights/best.pt')  # Replace 'best.pt' with the path to your model

# Open the default webcam
cap = cv2.VideoCapture(0)

reset_payload = {"LED": "reset"}

# Dictionary to store the detection time for each label
detection_timers = {}

def post_payload(label):
    print(f"Sending payload for: {label}")
    led_payload = reset_payload
    led_url = "http://localhost:1880/LEDPOST"  # Replace with your API URL

    if label == "green":
        led_payload = {"LED": "false"}
    elif label == "yellow":
        led_payload = {"LED": "true"}

    headers = {
        'Content-Type': 'application/json',
    }
    led_payload = json.dumps(led_payload)

    # Send the POST request
    response = requests.post(led_url, headers=headers, data=led_payload)

    # Check and print the response
    if response.status_code == 200:
        print("Request was successful!")
    else:
        print(f"Request failed with status code {response.status_code}")

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Run YOLOv8 inference on the frame
    results = model(frame)

    # Extract detected labels from results
    detected_labels = set()
    for result in results:
        for box in result.boxes.data:
            label_index = int(box[5])  # Assuming box[5] contains the class index
            label = model.names[label_index]  # Map index to class label
            detected_labels.add(label)

    # Process detected labels
    current_time = time.time()
    for label in detected_labels:
        if label in detection_timers:
            elapsed_time = current_time - detection_timers[label]
            if label == "green" and elapsed_time >= 10:  # 5 seconds + 5 more seconds for green
                post_payload(label)
                detection_timers.pop(label)  # Reset the timer after sending the payload
            elif label == "yellow" and elapsed_time >= 65:  # 5 seconds + 1 minute for yellow
                post_payload(label)
                detection_timers.pop(label)  # Reset the timer after sending the payload
        else:
            # Start the timer for a new detection
            detection_timers[label] = current_time

    # Remove labels no longer in the scene from the timers
    detection_timers = {k: v for k, v in detection_timers.items() if k in detected_labels}

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Display the resulting frame
    cv2.imshow('YOLOv8 Live Detection', annotated_frame)

    # Press 'q' to exit the webcam
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture and close windows
cap.release()
cv2.destroyAllWindows()
