import cv2
image=cv2.imread(r"C:\Users\ASUS\OneDrive\Pictures\Camera Roll\WIN_20260221_17_25_22_Pro.jpg")
print(image)
if image is None:
    print("image not found")
else:
    (h,w)=image.shape[:2]
    center=(w//2,h//2)
    m=cv2.getRotationMatrix2D(center,90,1.0)
    rotated=cv2.warpAffine(image,m,(w,h))
    cv2.imshow("original image",image)
    cv2.imshow("rotated image",rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()