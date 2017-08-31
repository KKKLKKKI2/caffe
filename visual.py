import cv2
import numpy
import tkinter as tk
from PIL import Image ,ImageTk
a=cv2.imread("C:/Users\D300_ADAS\Desktop\caffe-windows\examples\moth\SingleTest_ID/V01-20150123-001.jpg")
#cv2.namedWindow("Image")
fromCenter = False
showcrosshair = False
r= cv2.selectROI(a,fromCenter,showcrosshair)
im = a[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
cv2.imwrite('123.jpg',im)
cv2.waitKey (5000)
cv2.imwrite('456.jpg',im)
cv2.waitKey (5000)
cv2.imshow("image",im)
cv2.waitKey (0)
#cv2.destroyAllWindows()