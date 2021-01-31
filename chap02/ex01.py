import cv2
img_lena = cv2.imread(r"../OImage/lena.bmp")   #读取图像
cv2.imshow("img_lena", img_lena)               #创建窗口，显示图像
cv2.waitKey()                                   #用于等待按键,按任意键继续
cv2.destroyWindow("img_lena")                   #销毁所有窗口
retval = cv2.imwrite(r"D:/lena.bmp", img_lena)  #将图片复制到D盘
print(f'retval对应的值——{retval}')                                   #查看返回值retval
print(f'img_lena对应的数据类型——{type(img_lena)}')                            #查看img_lena的数据类型