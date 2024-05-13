import cv2
import os

def capture_images(label, num_images):
    cap = cv2.VideoCapture(0)
    os.makedirs(f'data/{label}', exist_ok=True)
    
    count = 0
    while count < num_images:
        ret, frame = cap.read()
        if not ret:
            continue
        
        cv2.imshow('frame', frame)
        key = cv2.waitKey(1)
        
        if key == ord('c'):  # Press 'c' to capture an image
            cv2.imwrite(f'data/{label}/{count}.png', frame)
            count += 1
            print(f'Captured image {count} for label {label}')
        
        elif key == ord('q'):  # Press 'q' to quit
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Capture images for each gesture
capture_images('Thumbs Up', 10)
capture_images('Thumbs Down', 10)
