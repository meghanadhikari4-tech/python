#gaussianblur
import cv2
image=cv2.imread(r"C:\Users\ASUS\OneDrive\Pictures\Camera Roll\WIN_20260221_17_25_22_Pro.jpg")
blurred=cv2.GaussianBlur(image,(3,3),0)
cv2.imshow("original image",image)
cv2.imshow("blurred image",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
#median blur
blur=cv2.medianBlur(image,11)
cv2.imshow("blurred",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()