#! /usr/local/bin/python3
# _*_ encoding=utf-8 _*_

import cv2 as cv
import numpy as np


img1 = cv.imread('1.jpg')
img2 = cv.imread('2.jpg')

img1 = np.asarray(img1, dtype=np.int16)
img2 = np.asarray(img2, dtype=np.int16)

diff = img1 - img2
diff = np.absolute(diff, casting='no')
print(diff.dtype)

diff = diff.sum(axis=2)
improtant_diff_cnt = np.sum(diff>50)
print('重要差异：', improtant_diff_cnt)
same_cnt = np.sum(diff==0)
print('相同：', same_cnt)

print('不重要差异：', diff.size-improtant_diff_cnt-same_cnt)