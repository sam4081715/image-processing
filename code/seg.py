import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

#original
img_path = r'D:\vsc_workspace\segment\test_image\image.png'
img  = cv2.imread(img_path)
h, w, _ = img.shape

#gray value
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#binary by average value

count = 0
for i in range(h):
    for j in range(w):
        count += gray[i][j]

thresh = count/(h*w)
ret, bin = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)

#mediam filter 3*3(blur)
gray = np.pad(gray, ((1, 1), (1, 1)), 'constant', constant_values = (0, 0))
gray1 = np.zeros([h, w], dtype=int)

for i in range(h):
    for j in range(w):
        count = 0
        for k in range(3):
            for l in range(3):
                count += gray[i+k][j+l]

        count /= 9
        gray1[i][j] = count

#mediam filter 5*5
gray = np.pad(gray, ((2, 2), (2, 2)), 'constant', constant_values = (0, 0))
out = np.zeros([h, w], dtype=int)

for i in range(h):
    for j in range(w):
        count = 0
        for k in range(5):
            for l in range(5):
                count += gray[i+k][j+l]

        count /= 25
        out[i][j] = count

#GaussianBlur




plt.imshow(out, cmap=plt.get_cmap('gray'))
plt.show()
