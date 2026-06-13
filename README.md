# Object Detection System

## Project Overview

This repository contains a real-time object detection project using Ultralytics YOLO and OpenCV.

The core application is `app.py`, a Streamlit web app that:
- loads a YOLO model from `Models/best.pt`
- captures webcam frames via OpenCV
- runs YOLO inference on each frame
- displays annotated frames with bounding boxes and class labels

## Repository Contents

- `app.py` — main Streamlit app for real-time webcam object detection
- `Models/best.pt` — trained YOLO model weights used by the app
- `requirements.txt` — Python dependencies for the project
- `Object_Detection.ipynb` — notebook with project exploration and package installation examples
- `yolo_model.ipynb` — additional notebook for YOLO model work and experimentation
- `.vscode/settings.json` — local VS Code settings to configure the workspace Python interpreter

## Requirements

Install the required packages in the same virtual environment used to run the app.

```bash
pip install -r requirements.txt
```

Key dependencies include:
- `ultralytics`
- `opencv-python`
- `streamlit`
- `torch`
- `torchvision`

## Running the App

From the repository root, start the Streamlit app:

```bash
python -m streamlit run app.py
```

Open the local URL shown in the terminal to use the app.

## Notes

- The app expects the model weights file at `Models/best.pt`.
- If `ultralytics` or `cv2` are underlined in VS Code, the editor may be using a different Python interpreter than the terminal.
- Make sure the active interpreter points to the project virtual environment and that `requirements.txt` packages are installed there.
- If needed, reload VS Code or restart the Python language server after selecting the correct interpreter.
