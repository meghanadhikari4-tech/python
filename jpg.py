import os
import cv2

path = r"C:\Users\ASUS\OneDrive\Pictures\Camera Roll\WIN_20260221_17_25_22_Pro.jpg"

print("Exists:", os.path.exists(path))
print("Size:", os.path.getsize(path) if os.path.exists(path) else "Not found")

image = cv2.imread(path)
print("Image:", image)