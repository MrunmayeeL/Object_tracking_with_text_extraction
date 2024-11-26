Overview

This program allows you to track objects in a live webcam feed and extract any visible text from the tracked object using Tesseract OCR. It provides the option to choose from various trackers (like CSRT, KCF, and others) and displays the detected text on the object in real-time. You can also toggle the drawing of the object’s path.
Features

    Choose from different object tracking algorithms (e.g., CSRT, KCF, MOSSE).
    Select the object to track by drawing a bounding box on it.
    Extract and display text from the object using Tesseract OCR.
    Toggle drawing of points to visualize the object’s movement.
    Exit the program by pressing 'q'.

Requirements

    OpenCV:
        pip install opencv-python
    Tesseract OCR:
        Install Tesseract following instructions for your platform.
        pip install pytesseract

How to Use

    Run the script:

    python object_tracking_with_text_extraction.py

    Select a Tracker:
        Choose the tracker you want to use (default is CSRT).

    Select Object to Track:
        Click and drag to draw a box around the object you want to track.

    Text Display:
        The text detected on the object will be displayed above it in real-time.

    Toggle Path Drawing:
        Press a to toggle drawing points showing the object’s movement.

    Exit:
        Press q to quit the program.

Notes

    The program uses the webcam to capture video and tracks the selected object.
    The text displayed on the object is extracted using Tesseract OCR, so it might not work well if the text is too blurry