import cv2
import glob

vfiletype = input("\n[+] File Extension(without dot): ")
vwidth = int(input("[+] Width: "))
vheight = int(input("[+] Height: "))

images = glob.glob("*." + vfiletype)

for image in images:
    img = cv2.imread(image,1)
    re = cv2.resize(img,(vwidth,vheight))
    cv2.imshow("Processing", re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image, re)


