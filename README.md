# Object Detection System

## Project Overview

This repository contains a real-time object detection project using Ultralytics YOLO and OpenCV.

The core application is `app.py`, a Streamlit web app that:
- loads a YOLO model from `Models/best.pt`
- captures webcam frames via OpenCV
- runs YOLO inference on each frame
- displays annotated frames with bounding boxes and class labels

## Development Pipeline
1. Define project goals and collect dataset requirements from roboflow
2. Prepare dataset file
3. Train the YOLO model and validate results on google COLAB
4. Build the Streamlit app with webcam capture and inference
5. Test the application locally and refine performance
6. Deploy and monitor the object detection system

## Repository Contents

- `app.py` — main Streamlit app for real-time webcam object detection
- `Models/best.pt` — trained YOLO model weights used by the app
- `requirements.txt` — Python dependencies for the project
- `Object_Detection.ipynb` — notebook with project exploration and package installation examples
- `yolo_model.ipynb` — additional notebook for YOLO model work and experimentation

## Things i learned in this project

 + I learned what is YOLO model
 + What is the difference between YOLO and CNN
 + How to train the model on external datasets
 + How different parameter changes affect the training process such as epochs and conf 
 + How to use OpenCV library 
 + How to use Streamlit

## Future functionality 
 + An information card that displays some extra info about the object 
 + Detecion can be used to identify the user of a certain device in order to prevent them opening some restricted folder that only the user can access
 + Can be scaled to a phone detection app for exam surveilence or other places where phones are not allowed

## Difficulty i faced 
 + Choosing the wrong dataset that caused wrong detection such as identifying a banana as an apple
 + Choosing google COLAB to train because of GPU limitations on system 
 + Resolving current dependecies and python version 



