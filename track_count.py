from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO("yolov8n.pt")

input_video = "night_scenario.mp4"
output_video = "output_tracking_count.mp4"

cap = cv2.VideoCapture(input_video)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

# Counting line
line_y = int(height * 0.65)

vehicle_count = 0
counted_ids = set()

VEHICLE_CLASSES = ["car", "motorcycle", "bus", "truck"]

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    results = model.track(frame, persist=True)[0]

    cv2.line(frame, (0, line_y), (width, line_y), (255, 255, 255), 2)

    if results.boxes.id is not None:

        boxes = results.boxes.xyxy.cpu().numpy()
        ids = results.boxes.id.cpu().numpy()
        classes = results.boxes.cls.cpu().numpy()

        for box, track_id, cls in zip(boxes, ids, classes):

            label = model.names[int(cls)]

            if label not in VEHICLE_CLASSES:
                continue

            x1, y1, x2, y2 = map(int, box)

            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

            cv2.putText(frame,
                        f"{label} ID:{int(track_id)}",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0,255,0),
                        2)

            if abs(cy - line_y) < 5 and track_id not in counted_ids:
                vehicle_count += 1
                counted_ids.add(track_id)

    cv2.putText(frame,
                f"Vehicle Count: {vehicle_count}",
                (20,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2)

    out.write(frame)

cap.release()
out.release()

print("Tracking + counting video saved:", output_video)
print("Total vehicles counted:", vehicle_count)