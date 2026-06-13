from ultralytics import YOLO
import cv2
import streamlit as st

st.set_page_config(page_title="YOLOv8 Object Detection")
st.title("Real-Time Object Detection")
st.write("Press the button below to start the webcam detection.")

model = YOLO("Models/best.pt")

start = st.button("Start Webcam Detection")

if start:
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    stop = st.button("stop webcam detection")

    frame_placeholder = st.empty()

    while cam.isOpened():


        success , frame = cam.read()

        if not success:
            st.write("Failed to capture video")
            break

        if stop:
            cam.release()
            break

        results = model.predict(frame, conf=0.5)

        annotated_frame= results[0].plot()

        annotated_frame=cv2.cvtColor(
            annotated_frame,
            cv2.COLOR_BGR2RGB
        )

        frame_placeholder.image(
            annotated_frame,
            channels ="RGB",
            use_container_width = True
        )

    cam.release()


