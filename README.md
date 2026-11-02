# Bahraini Currency Detection

A simple app that detects Bahraini banknotes from a camera photo using a YOLO model.

**Live app:** https://bahraini-currency-detection.streamlit.app

## How to use
1. Open the app link.
2. Allow camera access.
3. Take a picture of a banknote.
4. The app shows the note with a box and its detected value.

## Files
- `app.py` - the Streamlit app
- `best.pt` - the trained YOLO model
- `requirements.txt` - Python packages

## Run locally
```
pip install -r requirements.txt
streamlit run app.py
```
