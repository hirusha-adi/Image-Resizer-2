import cv2
import glob

vwidth = int(input("\n[+] Width: "))
vheight = int(input("[+] Height: "))

images = glob.glob("*.jpeg")

for image in images:
    img = cv2.imread(image,1)
    re = cv2.resize(img,(vwidth,vheight))
    cv2.imshow("Processing", re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image, re)


