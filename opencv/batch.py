import cv2
import os

sourcepath = 'resources/large/'
destinationpath = 'resources/small/'

images = os.listdir(sourcepath)

for image in images:
    img = cv2.imread(sourcepath+image, 0)
    try:
        resized_img = cv2.resize(img, (100, 100))
        cv2.imwrite(destinationpath+"small_"+image, resized_img)
    except cv2.error:
        print("oups couldn't resize image file")
