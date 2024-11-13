#mediam filter 3*3

import numpy as np
import cv2

import Gray

def median_self(img, ksize):

    h, w = img.shape
    padsize = ksize // 2
    med = np.pad(img, ((padsize, padsize), (padsize, padsize)), 'constant', constant_values = (0, 0))
    output = np.zeros([h, w], dtype=int)

    for i in range(h):
        for j in range(w):
            count = []
            for k in range(ksize):
                for l in range(ksize):
                    count.append(med[i+k][j+l])

            n = len(count)
            for k in range(n):
                for l in range(n-k-1):
                    if count[l] > count[l+1]:
                        count[l], count[l+1] = count[l+1], count[l]

            median = n//2 + 1 if n%2 > 0 else n//2
            output[i][j] = count[median-1]
            #print(count, count[median-1])
    output = output.astype(np.uint8)

    return output

def median_pack(img, ksize):
    #cv2.medianBlur(img, ksize)
    # img 來源影像
    # ksize 模糊程度 ( 必須是大於 1 的奇數 )
    
    output = cv2.medianBlur(img, ksize)

    return output