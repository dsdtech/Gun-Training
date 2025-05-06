# Gun-Training
Smart Target Scoring System for Military Gun Training -  This project is a real-time image processing and shot detection system tailored for military gun training. It connects to an RTSP-enabled IP camera, analyzes the live video stream, and performs bullet impact detection on a circular target using computer vision. The system calculates the score of each shot based on its distance from the target center and displays the result visually.

---

## 🎯 Project Objective

- Detect and score gunshots on a target during live military shooting exercises.
- Calculate shot accuracy based on proximity to the target center.
- Display real-time visual feedback including contours, shot center, and score.
- Allow dynamic threshold control for optimal performance in various lighting conditions.

---

## 🔧 Features

- ✅ RTSP stream acquisition from IP camera (CCTV, surveillance, etc.)
- ✅ Grayscale conversion and edge detection (Canny)
- ✅ Adjustable image thresholds using interactive OpenCV trackbars
- ✅ Contour detection and area filtering to identify bullet impacts
- ✅ Real-time display of all image processing stages in a stacked view
- ✅ Marking of shot centers with coordinate annotations
- ✅ Extensible for scoring system and result logging

---

## 📁 Script Overview

**Filename**: `rtsp_contour_analyzer.py`

### 🛠️ Major Components:

| Component        | Purpose                                                                 |
|------------------|-------------------------------------------------------------------------|
| `RTSP_URL`       | Connects to a live RTSP stream from a target-viewing camera             |
| `cv2.VideoCapture()` | Reads frames in real time using FFMPEG backend                      |
| `stackImages()`  | Custom utility to stack multiple image views into a single window       |
| `cv2.createTrackbar()` | Allows real-time adjustment of threshold values through GUI      |
| `getContours()`  | Detects contours and highlights valid ones with area > 5000 pixels      |
| `cv2.drawContours()` | Visually marks bullet hits with contour and central crosshair      |

---

## 📸 Live View Composition

- **Top Left**: Original color feed
- **Top Middle**: Grayscale version
- **Top Right**: Binary thresholded image (adjusted via `Threshold1` and `Threshold2`)
- **Bottom Left**: Canny edge detection (`Threshold3` and `Threshold4`)
- **Bottom Middle**: Duplicate of original (placeholder for development)
- **Bottom Right**: Final contour detection with center points

---

## 🔃 Control Parameters

Adjust via the "Parameters" window sliders:

| Slider Name  | Range | Description                           |
|--------------|-------|---------------------------------------|
| Threshold1   | 0–255 | Lower bound for binary threshold      |
| Threshold2   | 0–255 | Upper bound for binary threshold      |
| Threshold3   | 0–255 | Lower bound for Canny edge detection  |
| Threshold4   | 0–255 | Upper bound for Canny edge detection  |

---

## 🚀 How to Run

### 📦 Install Dependencies

```bash
pip install opencv-python numpy imutils

## ▶️ Run the Script

 1. Dont forget to modify the RTSP stream URL:RTSP_URL = 'rtsp://user:pass@192.168.1.64:554/Streaming/channels/1'

2.  Then run:python rtsp_contour_analyzer.py. The script will display a window with the video feed and processing steps. It will also open a window with trackbars.

3.  Use the trackbars to adjust the image processing parameters to accurately detect bullet impacts. Press q to quit.

Code Explanation

The Python script (your\_script\_name.py) performs the following:

* Imports Libraries: Imports cv2, numpy, and imutils.
* Sets up Video Capture: Opens the RTSP stream using cv2.VideoCapture.
* Defines Functions:
    * stackImages(): Stacks multiple images for display.
    * getContours(): Detects and filters contours.
* Creates Trackbars: Creates trackbars to adjust threshold values.
* Main Loop:
    * Reads frames from the video stream.
    * Processes the frames (grayscale, threshold, Canny, contours).
    * Detects bullet impacts (using contour properties).
    * Calculates shot scores (this part needs to be implemented).
    * Displays the results.
* Cleanup: Releases the video capture and closes windows.

Troubleshooting

* Cannot open RTSP stream: Double-check the RTSP\_URL.
* No video display: Check camera connection and network.
* Inaccurate detection: Adjust trackbar values.
* Performance issues: Reduce video resolution.
