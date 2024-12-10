import streamlit as st
import cv2
import numpy as np
import os

st.title("Live Video Stream and Recording from Web Camera")

# Function to get video stream from webcam and record it
def video_stream(record=False, output_path="output.avi"):
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture video")
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame, channels="RGB")

        if record:
            out.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    cap.release()
    out.release()

# Placeholder for video frames
frame_placeholder = st.empty()

# Checkbox to start/stop recording
record = st.checkbox("Record Video")

# Input for output file path
output_path = st.text_input("Enter output file path", "output.avi")

# Start video stream
video_stream(record=record, output_path=output_path)
