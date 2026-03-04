# Night-Time Traffic Monitoring using YOLOv8

## Overview

This project demonstrates a computer vision pipeline for monitoring road traffic during night-time conditions.
The system detects vehicles from a roadside video, tracks them across frames, counts vehicles crossing a virtual line, and generates a traffic heatmap representing vehicle activity over time.

The project is designed as a lightweight traffic monitoring prototype using a short real-world video recorded using a mobile phone.

## Features

* Vehicle detection using **YOLOv8**
* Multi-object tracking across frames
* Vehicle counting using a virtual crossing line
* Traffic density visualization using a **heatmap**
* Annotated output video with bounding boxes and tracking IDs

## Project Pipeline

Video Input
↓
Frame Processing
↓
Vehicle Detection (YOLOv8)
↓
Vehicle Tracking
↓
Vehicle Counting
↓
Traffic Heatmap Generation
↓
Annotated Output Video

## Technologies Used

* Python
* OpenCV
* Ultralytics YOLOv8
* NumPy

## Repository Structure

```
night-traffic-monitoring-yolo
│
├ detect.py                # Vehicle detection script
├ track_count.py           # Vehicle tracking and counting
├ heatmap.py               # Traffic heatmap generation
├ requirements.txt         # Python dependencies
│
├ results
│   ├ output_detection.mp4
│   ├ output_tracking_count.mp4
│   ├ output_heatmap_video.mp4
│   └ traffic_heatmap.png
│
└ README.md
```

## Dataset

The input video was recorded using a mobile phone at night from a roadside location.
The clip contains several vehicles moving on both sides of a road separated by a barrier.

Video duration: **14 seconds**

## Vehicle Classes Detected

The system focuses on common road vehicles:

* Car
* Motorcycle
* Bus
* Truck

Other detected classes such as pedestrians are ignored during traffic analysis.

## Results

The system produces the following outputs:

1. **Detection Video**

   * Vehicles detected with bounding boxes

2. **Tracking and Counting Video**

   * Vehicles tracked across frames
   * Vehicle count displayed on screen

3. **Traffic Heatmap**

   * Visualization of regions where vehicles appear frequently

These results demonstrate how computer vision techniques can be used to analyze traffic patterns even under low-light conditions.

## Limitations

* The input video is short (14 seconds) and contains a limited number of vehicles
* Night-time glare and lighting conditions can affect detection accuracy
* The system uses a pre-trained model and was not fine-tuned for this specific environment

## Future Improvements

Possible improvements include:

* Using longer traffic recordings
* Speed estimation of vehicles
* Lane-based vehicle counting
* Traffic flow analytics (vehicles per minute)
* Deployment on real-time video streams

## How to Run

Install dependencies:

```
pip install -r requirements.txt
```

Run vehicle detection:

```
python detect.py
```

Run tracking and vehicle counting:

```
python track_count.py
```

Generate traffic heatmap:

```
python heatmap.py
```

## Applications

This type of system can be used for:

* Smart city traffic monitoring
* Road safety analysis
* Traffic density estimation
* Surveillance and infrastructure planning

## Author

Computer Vision Portfolio Project
Master of Engineering – Autonomous Driving / AI
