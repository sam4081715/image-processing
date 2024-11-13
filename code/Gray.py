#gray value
import numpy as np
import cv2

def gray_self(img):

    h, w, _ = img.shape
    gray = np.zeros([h, w], dtype=int)
    for i in range(h):
        for j in range(w):
            gray[i][j] = 0.114*img[i][j][0] + 0.587*img[i][j][1] + 0.299*img[i][j][2]

    gray = gray.astype(np.uint8)

    return gray

def gray_pack(img):
    #cv2.cvtColor(img, code)
    # img 來源影像
    # code 要轉換的色彩空間名稱
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return gray