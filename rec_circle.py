import cv2
image=cv2.imread(r"C:\Users\ASUS\OneDrive\Pictures\Camera Roll\WIN_20260221_17_25_22_Pro.jpg")
if image is None:
    print("image not loaded")
else:
    print("image loaded successfully")
    pt1=(100,100)
    pt2=(200,250)
    thickness=2
    color=(100,230,35)
    cv2.rectangle(image,pt1,pt2,color,thickness)
    cv2.circle(image,(150,150),75,(0,200,0),2)
    cv2.imshow("rectangle and circle",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()