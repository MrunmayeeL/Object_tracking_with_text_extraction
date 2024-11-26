import cv2
import numpy as np
import pytesseract

# Different trackers to choose from
tracker_types = {
    1: 'BOOSTING', 2: 'MIL', 3: 'KCF', 4: 'TLD', 5: 'MEDIANFLOW', 6: 'MOSSE', 7: 'CSRT'
}
print(tracker_types)

n = input("Tracker (Skip for default) : ")

if n == "":
    n = 7
else:
    n = int(n)

tracker_type = tracker_types[n]

# Initialize selected tracker
if tracker_type == 'BOOSTING':
    tracker = cv2.legacy.TrackerBoosting.create()
elif tracker_type == 'MIL':
    tracker = cv2.TrackerMIL.create()
elif tracker_type == 'KCF':
    tracker = cv2.TrackerKCF.create()
elif tracker_type == 'TLD':
    tracker = cv2.legacy.TrackerTLD.create()
elif tracker_type == 'MEDIANFLOW':
    tracker = cv2.legacy.TrackerMedianFlow.create()
elif tracker_type == 'MOSSE':
    tracker = cv2.legacy.TrackerMOSSE.create()
elif tracker_type == 'CSRT':
    tracker = cv2.TrackerCSRT.create()

print("\n\nPress 'a' to toggle draw, and 'q' to quit\n\n")

# Setting up video
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not video.isOpened():
    print("Can't detect camera")
    quit()

width = 1800
height = 1500
video.set(3, width)
video.set(4, height)

ok, frame = video.read()
frame = cv2.flip(frame, 1)

if not ok:
    print("Error")

# Setting up tracker
bbox = cv2.selectROI("detection", frame, False)
tracker.init(frame, bbox)

toggle = 0
art = [[]]
count = 0

# Code for dynamic tracking and drawing on screen
while video.isOpened():
    ok, frame = video.read()
    frame = cv2.flip(frame, 1)
    ok, bbox = tracker.update(frame)
    
    # Extract the coordinates of the bounding box
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

    # Draw the bounding box on the frame
    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2, 1)

    # Extract the region of interest (ROI) where the object is located
    roi = frame[y:y+h, x:x+w]
    
    # Use Tesseract OCR to extract text from the ROI
    text = pytesseract.image_to_string(roi)

    # Display the extracted text
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text.strip(), (x, y - 10), font, 0.7, (0, 255, 0), 2)

    # Toggle drawing of points
    k = cv2.waitKey(25)
    if k & 0xFF == ord('a'):
        if toggle == 1:
            toggle = 0
            count += 1
            art.append([])
        else:
            toggle = 1
    if toggle == 1:
        art[count].append((x + (w / 2), y + (h / 2)))

    for i in art:
        pts = np.array(i, np.int32)
        cv2.polylines(frame, [pts], False, (0, 0, 255), 2)

    # Show the video with the bounding box and text
    cv2.imshow("Video", frame)

    # Quit the loop when 'q' is pressed
    if k & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

# Drawing result
frame = np.full(frame.shape, 255, np.uint8)
for i in art:
    pts = np.array(i, np.int32)
    cv2.polylines(frame, [pts], False, (0, 0, 255), 2)

cv2.imshow("Result", frame)
cv2.waitKey()
cv2.destroyAllWindows()
