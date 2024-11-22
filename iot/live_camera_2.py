import cv2
from ultralytics import YOLO
import json
import requests
import time
# Load your trained YOLOv8 model
model = YOLO('./runs/detect/train/weights/best.pt')  # Replace 'best.pt' with the path to your model

# Open the default webcam
cap = cv2.VideoCapture(0)
ignore = 0
picking_object = 0

reset_payload = {"LED": "reset"}

def post_payload(detected_labels, picking_object):
    print(f"Detected labels: {detected_labels}")
    led_payload = reset_payload
    led_url = "http://localhost:1880/LEDPOST"  # Replace with your API URL

    if 'big green cube' in detected_labels:
        led_payload = {"LED": "green"}
        print(led_payload)
    elif 'yellow cube' in detected_labels:
        picking_object = 1
        led_payload = {"LED": "yellow"}
        print(led_payload)

    headers = {
        'Content-Type': 'application/json',  # Specify the content type as JSON
    }
    led_payload = json.dumps(led_payload)

    # Send the POST request
    response = requests.post(led_url, headers=headers, data=led_payload)

    # Check and print the response
    if response.status_code == 200:
        print("Request was successful!")
    else:
        print(f"Request failed with status code {response.status_code}")
    
    if picking_object == 1:
        time.sleep(15)
        led_payload = {"LED": "reset"}
        headers = {
        'Content-Type': 'application/json',  # Specify the content type as JSON
        }
        led_payload = json.dumps(led_payload)
        response = requests.post(led_url, headers=headers, data=led_payload)
        picking_object = 0

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

    # Call the function with the detected labels
#    if cv2.waitKey(1) & 0xFF == ord('a'):
    
    if len(detected_labels)>0 and ignore == 0:
        post_payload(detected_labels, picking_object)
        print("Detected, SLEEPING")
        time.sleep(5)
        ignore = 1
    
    if len(detected_labels)== 0 and ignore == 1:
        ignore = 0

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
