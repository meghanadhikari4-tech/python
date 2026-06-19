import cv2
image=cv2.imread(r"C:\Users\ASUS\OneDrive\Pictures\Camera Roll\WIN_20260221_17_25_22_Pro.jpg")
if image is None:
    print("image not loaded")
else:
    print("image loaded successfully")
    pt1=(50,100)
    pt2=(300,100)
    thickness=2
    color=(0,255,0)
    cv2.line(image,pt1,pt2,color,thickness)
    cv2.imshow("line drawing",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()