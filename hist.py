# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:29:41 2018

@author: ZMJ
"""
from matplotlib import pyplot as plt
from skimage.io import imread
from skimage.exposure import equalize_adapthist as ea
img_path="img/00ae65c1c6631ae6f2be1a449902976e6eb8483bf6b0740d00530220832c6d3e/"
test_img=img_path+"images/00ae65c1c6631ae6f2be1a449902976e6eb8483bf6b0740d00530220832c6d3e.png"

img=imread(test_img)
fig=plt.figure(figsize=(8,4))
fig.add_subplot(121)
plt.imshow(img)
fig.add_subplot(122)
plt.imshow(ea(img))
plt.show()