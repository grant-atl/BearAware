# Bear Aware

A physical computing project that uses facial emotion detection to control LED lights in real-time.

## Overview

Bear Aware uses your computer's webcam to detect facial emotions and sends that data to an Arduino, which changes LED colors based on how you're feeling.

## How It Works

1. Webcam captures your face using OpenCV and dlib
2. DeepFace analyzes your facial expression to detect emotion
3. The dominant emotion is sent to Arduino via serial connection
4. LED strip changes color based on emotion:
   - **Angry** → Red
   - **Sad** → Blue
   - **Other emotions** → Warm Yellow

## Hardware

- Arduino board
- NeoPixel LED strip (166 LEDs)
- Speaker (for startup melody)

## Software Dependencies

- Python 3
- OpenCV
- DeepFace
- dlib
- pyserial

## Usage

1. Connect Arduino and upload `bearAware/bearAware.ino`
2. Run `python facevideo.py`
3. Press 'q' to quit
