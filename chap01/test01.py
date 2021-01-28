import cv2                                                     #导入OpenCV模块
img_lena1 = cv2.imread(r'..\OImage\lena.jpg')                    #将图片分别读入img1,img2,img3中
img_lena2 = cv2.imread(r'..\OImage\lena.jpg', cv2.IMREAD_GRAYSCALE)
img_lena3 = cv2.imread(r'..\OImage\lena.bmp')
img_lena4 = cv2.imread(r'..\OImage\lena.bmp', cv2.IMREAD_GRAYSCALE)
print(type(img_lena1), type(img_lena2), type(img_lena3), type(img_lena4))
