import cv2                                                     #导入OpenCV模块
img_lena1 = cv2.imread(r'..\data\lena.jpg')                    #将图片分别读入img1,img2,img3中
img_lena2 = cv2.imread(r'..\data\lena.jpg', cv2.IMREAD_GRAYSCALE)
print(type(img_lena1), type(img_lena2))
