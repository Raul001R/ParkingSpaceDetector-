import cv2
from ultralytics import YOLO 


#load model and predict image
model = YOLO("yolov8n.pt")
results = model.predict("image.jpg")

# Load image
img = cv2.imread("image.jpg")

# Draw bounding boxes and labels on the image
counter = 0
for box in results[0].boxes:
   if int(box.cls[0])== 2: #class 2 is car
    x1,y1,x2,y2 = map(int,box.xyxy[0])
    cv2.rectangle (img,(x1,y1),(x2,y2),(0,255,0),2)
    cv2.putText(img,f"Car {counter} / confidence {box.conf[0]:.2f}",(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)
    counter += 1
print(f"Detected {counter} cars")
cv2.imwrite("output.jpg", img) # Save the output image 



