import streamlit as st
import numpy as np
from PIL import Image
from ultralytics import YOLO

st.title("Bahrain Currency Detector")

model = YOLO("best.pt")

photo = st.camera_input("Take a picture")

if photo:
    img = np.array(Image.open(photo).convert("RGB"))[..., ::-1]  # RGB -> BGR for YOLO
    results = model(img)
    st.image(results[0].plot(), channels="BGR")
