import cv2
from matplotlib import pyplot as plt

import Gray
import Binary
import Median
import Blur

#original
img_path = r'D:\vsc_workspace\segment\test_image\image.png'
img  = cv2.imread(img_path)
h, w, _ = img.shape

#gray value
gray = Gray.gray_pack(img)

#binary with average value
bin = Binary.bin_pack(gray)

#mediam filter 3*3
med = Median.median_pack(gray, 3)

#blur 3*3
blur = Blur.blur_pack(gray, 3)

cv2.imshow('', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
