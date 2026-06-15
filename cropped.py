import cv2
image=cv2.imread(r"C:\Users\ASUS\OneDrive\Pictures\Camera Roll\WIN_20260221_17_25_22_Pro.jpg")
if image is None:
    print("image not found")
else:
    cropped=image[100:200,50:150]
    cv2.imshow("cropped image",cropped)
    cv2.imshow("original image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()