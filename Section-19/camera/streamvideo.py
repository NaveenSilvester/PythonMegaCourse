import streamlit as st
import cv2
import numpy as np

st.title("Live Video Stream from Web Camera")

# Function to get video stream from webcam
def video_stream():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture video")
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame, channels="RGB")
    cap.release()

# Placeholder for video frames
frame_placeholder = st.empty()

# Start video stream
video_stream()
