# Parking Space Detector

Detects cars in a parking lot image using a pretrained YOLOv8 model.

## Current status
Stage 1 — detects and labels cars in a single static image, saves the annotated output.

Stage 2 - detects if parking space's are occupied in a single static image.

## Planned
- Define parking spot regions and detect occupied vs. empty
- Track spot state and timing over video
- Live camera feed (Arduino) instead of a static image
- SMS notifications when a spot opens up