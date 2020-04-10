import cv2

# 1 : color
# 0 : black & white
# -1 : transparency capability
img = cv2.imread("resources/galaxy.jpg", 0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)  # is 2

# img_color = cv2.imread("resources/galaxy.jpg", 1)
# print(img_color.ndim)  # is 3

resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_img)
cv2.imwrite("resources/galaxy_medium.jpg", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
