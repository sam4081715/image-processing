import cv2

#original
img_path = r'D:\vsc_workspace\segment\image.png'
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

#mediam filter 3*3



cv2.imshow('', bin)
cv2.waitKey(0)
cv2.destroyAllWindows()
