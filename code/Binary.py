#binary by average value

import cv2
import numpy as np

def get_thresh(img):
    count = 0
    h, w = img.shape
    for i in range(h):
        for j in range(w):
            count += img[i][j]
    thresh = count/(h*w)

    return thresh
    

def bin_self(img):

    h, w = img.shape
    thresh = get_thresh(img)
    maxvalue = 255

    bin = np.zeros([h, w], dtype=int)
    for i in range(h):
        for j in range(w):
            if img[i][j] > thresh:
                bin[i][j] = maxvalue
            else:
                bin[i][j] = 0

    bin = bin.astype(np.uint8)
    return bin

def bin_pack(img):
    
    #ret, output = cv2.threshold(img, thresh, maxval, type)
    # ret 是否成功轉換，成功會顯示閾值
    # output 轉換後的影像
    # img 來源影像
    # thresh 閾值，通常設定 127
    # maxval 最大灰度，通常設定 255
    # type 轉換方式
    
    thresh = get_thresh(img)
    maxvalue = 255
    ret, bin = cv2.threshold(img, thresh, maxvalue, cv2.THRESH_BINARY)

    return bin