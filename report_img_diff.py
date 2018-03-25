#! /usr/local/bin/python3
# _*_ encoding=utf-8 _*_

import cv2 as cv
import numpy as np


img1 = cv.imread('1.jpg')
img2 = cv.imread('3.jpg')

img1 = np.asarray(img1, dtype=np.int16)
img2 = np.asarray(img2, dtype=np.int16)
img_diff = np.full_like(img1, 0, dtype=np.uint8)

diff = img1 - img2
diff = np.absolute(diff, casting='no')
print(diff.dtype)

diff = diff.sum(axis=2)
import_cord = diff>27
same_cord = diff<=5
improtant_diff_cnt = np.sum(import_cord)
print('重要差异：', improtant_diff_cnt)
same_cnt = np.sum(same_cord)
print('相同：', same_cnt)

print('不重要差异：', diff.size-improtant_diff_cnt-same_cnt)

img_diff[:, :, 0]=255
img_diff[same_cord,:]=0,0,0
img_diff[import_cord,:]=0,0,255

scale_diff = cv.resize(img_diff, (img_diff.shape[1]//2, img_diff.shape[0]//2))

cv.imwrite('img_diff.jpg', img_diff)
cv.imwrite('scale_diff.jpg', scale_diff)