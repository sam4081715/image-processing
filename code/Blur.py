#mediam filter 3*3

import numpy as np
import cv2

import Gray

def blur_self(img, ksize):

    h, w = img.shape
    padsize = ksize // 2
    blur = np.pad(img, ((padsize, padsize), (padsize, padsize)), 'constant', constant_values = (0, 0))
    output = np.zeros([h, w], dtype=int)

    for i in range(h):
        for j in range(w):
            count = 0
            for k in range(ksize):
                for l in range(ksize):
                    count += blur[i+k][j+l]
            output[i][j] = count / (ksize**2)
    output = output.astype(np.uint8)

    return output

def blur_pack(img, ksize):
    #cv2.blur(img, ksize)
    # img 來源影像
    # ksize 指定區域單位
    output = cv2.blur(img, (ksize, ksize))

    return output