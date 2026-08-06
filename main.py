import cv2
from ultralytics import YOLO 


#load model and predict image
model = YOLO("yolov8n.pt")
results = model.predict("lot.jpg")

# Load image
img = cv2.imread("lot.jpg")

# Draw bounding boxes and labels on the image
counter = 0
for box in results[0].boxes:
   if int(box.cls[0])== 2 and box.conf[0] > 0.3: #class 2 is car
    x1,y1,x2,y2 = map(int,box.xyxy[0])
    cv2.rectangle (img,(x1,y1),(x2,y2),(255,0,0),2)
    cv2.putText(img,f"Car {counter} / confidence {box.conf[0]:.2f}",(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)
    counter += 1
print(f"Detected {counter} cars")
cv2.imwrite("output.jpg", img) # Save the output image 


#Define coordinates of parking spaces
spots = [[224.3874, 3865.9597, 2899.6946, 5490.7827], [393, 3038, 1689, 3595], [2519, 3234, 4126, 4347]]

# Check if parking spaces are occupied
for spot in spots:
    occupied = False
    for box in results[0].boxes.xyxy:
        cx = int((box[0] + box[2]) / 2)
        cy = int((box[1] + box[3]) / 2)
        if spot[0] <= cx <= spot[2] and spot[1] < cy < spot[3]:
            occupied = True
            cv2.rectangle(img,(int(spot[0]),int(spot[1])),(int(spot[2]),int(spot[3])),(0,225,0),2)
            break
        else:
            occupied = False
            cv2.rectangle(img,(int(spot[0]),int(spot[1])),(int(spot[2]),int(spot[3])),(0,0,255),2)

#write the output image with parking space occupancy
cv2.imwrite("output_with_parking_spaces.jpg", img)
