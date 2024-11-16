import streamlit as st
from PIL import Image
import numpy as np
import cv2
from ultralytics import YOLO

# Load trained YOLOv8 model
model = YOLO('./test_model/best-example.pt')  # Replace with your model's path

#relabel = {0: 'Big Cube', 1: 'Hole', 2: 'Cylinder', 3: 'Cube'}

def main():
    st.title("Cube Detection App")
    st.write("Upload an image and the model will detect cubes.")

    # Image upload
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Open the image file
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        st.write("")
        st.write("Detecting cubes...")

        # Convert PIL Image to numpy array
        image_np = np.array(image)

        # Run the model
        results = model(image_np)

        # Draw bounding boxes on the image
        #results[0].names = relabel
        annotated_image = results[0].plot()
        st.image(annotated_image, caption='Processed Image', use_column_width=True)

        # Check if cubes were detected
        if results[0].boxes is not None and len(results[0].boxes) > 0:
            # Get class names from model

            class_names = model.names  # {class_index: class_name}
            #class_names = relabel
            # Get detected class indices
            detected_class_indices = results[0].boxes.cls.cpu().numpy().astype(int)
            #print(results[0].boxes.cls.cpu().numpy().astype(int))
            # Map indices to class names
            detected_class_names = [class_names[idx] for idx in detected_class_indices]
            print(detected_class_names)
            if "Cube" in detected_class_names:
                st.success("Cubes detected in the image!")
            else:
                st.info("Cubes not found using current model")
        else:
            st.info("Process done")

if __name__ == '__main__':
    main()
