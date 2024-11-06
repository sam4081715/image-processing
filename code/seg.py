import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

#original
img_path = r'D:\vsc_workspace\segment\test_image\image.png'
img  = cv2.imread(img_path)
h, w, _ = img.shape

#gray value
gray1 = np.zeros([h, w], dtype=int)
for i in range(h):
    for j in range(w):
        gray1[i][j] = 0.114*img[i][j][0] + 0.587*img[i][j][1] + 0.299*img[i][j][2]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#print(gray)
#print(gray1)

#binary by average value

count = 0
for i in range(h):
    for j in range(w):
        count += gray[i][j]
thresh = count/(h*w)

maxvalue = 255

bin1 = np.zeros([h, w], dtype=int)
for i in range(h):
    for j in range(w):
        if gray[i][j] > thresh:
            bin1[i][j] = maxvalue
        else:
            bin1[i][j] = 0

ret, bin = cv2.threshold(gray, thresh, maxvalue, cv2.THRESH_BINARY)

#print(bin1)
#print(bin)

#for i in range(h):
#    for j in range(w):
#        if bin1[i][j] != bin[i][j]:
#            print(bin1[i][j], bin[i][j])

#mediam filter 3*3
gray = np.pad(gray, ((1, 1), (1, 1)), 'constant', constant_values = (0, 0))
gray1 = np.zeros([h, w], dtype=int)

for i in range(h):
    for j in range(w):
        count = []
        for k in range(3):
            for l in range(3):
                count.append(gray[i+k][j+l])

        n = len(count)
        for o in range(n):
            for p in range(n-o-1):
                if count[p] > count[p+1]:
                    count[p], count[p+1] = count[p+1], count[p]

        median = n//2 + 1 if n%2 > 0 else n//2
        
        gray1[i][j] = median

#mediam filter 5*5
gray = np.pad(gray, ((2, 2), (2, 2)), 'constant', constant_values = (0, 0))
gray1 = np.zeros([h, w], dtype=int)

for i in range(h):
    for j in range(w):
        count = []
        for k in range(5):
            for l in range(5):
                count.append(gray[i+k][j+l])

        n = len(count)
        for o in range(n):
            for p in range(n-o-1):
                if count[p] > count[p+1]:
                    count[p], count[p+1] = count[p+1], count[p]

        median = n//2 + 1 if n%2 > 0 else n//2
        
        gray1[i][j] = median

#blur

#plt.imshow(out, cmap=plt.get_cmap('gray'))
#plt.show()
