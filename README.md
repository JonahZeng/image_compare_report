# python 30行代码实现beyond compare图片比较报告功能

-----------------------
最近换了工作，满满的坑，正如签名，留下是坚韧，也可能是贱人；

## 目的

我现在的工作每天都要批量仿真图片，就是拿同一批raw进行在PC上仿真ISP，看看算法改动有没有效果啥的，问题来了，每跑一次大概300张的样子，手动一张一张的用beyond compare或者fast stone之类的看图工具去比，不仅效率低，还容易漏看(其实是主要是累^_^)；于是，为什么不动手写个脚本啥的让PC告诉我哪些图片差异大？

废话不多说了，上代码：

```python
#! /usr/local/bin/python3
# _*_ encoding=utf-8 _*_

import cv2 as cv
import numpy as np

#用opencv读取两张要对比的图片
img1 = cv.imread('1.jpg')
img2 = cv.imread('3.jpg')

#ndarray类型转换，为什么？因为两个ndarray相减可能有负数元素
img1 = np.asarray(img1, dtype=np.int16)
img2 = np.asarray(img2, dtype=np.int16)
#新建一个结果图，用来显示差异，红色代表差异大，黑色代表相同，蓝色代表小差异
img_diff = np.full_like(img1, 0, dtype=np.uint8)
#ndarray相减，元素逐个相减
diff = img1 - img2
#相减后对r/g/b元素求绝对值
diff = np.absolute(diff, casting='no')
#r/g/b差求和
diff = diff.sum(axis=2)
#大于27，认为是重要差异，小于5定义为相同，这个地方看压缩情况，压缩率低的话，不用5这么大
import_cord = diff>27
same_cord = diff<=5
improtant_diff_cnt = np.sum(import_cord)
print('重要差异：', improtant_diff_cnt)
same_cnt = np.sum(same_cord)
print('相同：', same_cnt)

print('不重要差异：', diff.size-improtant_diff_cnt-same_cnt)
#先填充蓝色，然后在相同的坐标位置填充白色，重要差异坐标填红色，注意B/G/R顺序
img_diff[:, :, 0]=255
img_diff[same_cord,:]=0,0,0
img_diff[import_cord,:]=0,0,255
#有时候仅仅是想粗略看一下差异，就没有必要保存全尺寸的结果图，缩小4倍保存即可
scale_diff = cv.resize(img_diff, (img_diff.shape[1]//2, img_diff.shape[0]//2))

cv.imwrite('img_diff.jpg', img_diff)
cv.imwrite('scale_diff.jpg', scale_diff)
```
