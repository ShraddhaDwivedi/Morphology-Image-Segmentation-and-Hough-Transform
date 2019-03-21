from cv2 import imread, imwrite
import numpy as np
import math as math
from Utilities import sharpen, blur, edgeDetector

#BLACK = 0
#WHITE = 256


def writeImage(img, outputFileName):
	imwrite('output/Task3_Sol1_'+outputFileName+'.jpg', img)
	return 1

img = imread("./test.jpg", 0)
print(img[50,50])