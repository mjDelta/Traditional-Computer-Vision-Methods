# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:20:00 2018

@author: ZMJ
"""
from PIL import Image
from pylab import array,contour,gray
from matplotlib import pyplot as plt

test_img="img/00ae65c1c6631ae6f2be1a449902976e6eb8483bf6b0740d00530220832c6d3e/images/00ae65c1c6631ae6f2be1a449902976e6eb8483bf6b0740d00530220832c6d3e.png"

#Read from path
im=array(Image.open(test_img).convert("L"))##Turn into gray-scale img

fig=plt.figure(figsize=(8,4))
fig.add_subplot(121)
gray()
contour(im,origin="image")
fig.add_subplot(122)
gray()
plt.imshow(im)
plt.show()

