import cv2
image=cv2.imread(r"C:\Users\ASUS\OneDrive\Pictures\Camera Roll\WIN_20260221_17_25_22_Pro.jpg")
if image is None:
    print("no image found")
else:
    print("choose an option")
    print("1-save")
    print("2-show")
    choice=input("enter 1 or 2:")
    if choice=="1":
        save_path=(r"C:\Users\ASUS\OneDrive\Pictures\Camera Roll\WIN_20260221_17_25_22_Pro.jpg")
        cv2.imwrite(save_path,image)
        print("saved successfully")
    elif choice=="2":
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        cv2.imshow("grayscale image",gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
