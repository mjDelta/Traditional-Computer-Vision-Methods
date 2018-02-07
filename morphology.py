# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 16:41:10 2018

@author: ZMJ
"""
import skimage.morphology as sm
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.image as mpimg
 
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
img_path="img/00ae65c1c6631ae6f2be1a449902976e6eb8483bf6b0740d00530220832c6d3e/"
test_img=img_path+"images/00ae65c1c6631ae6f2be1a449902976e6eb8483bf6b0740d00530220832c6d3e.png" 
img = mpimg.imread(test_img)     
gray = rgb2gray(img)    
dilat=sm.dilation(gray)
ersion=sm.erosion(gray)
opening=sm.opening(gray)
closing=sm.closing(gray)
fig=plt.figure(figsize=(20,4))
fig.add_subplot(151)
plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.title("Image")
fig.add_subplot(152)
plt.imshow(dilat, cmap = plt.get_cmap('gray'))
plt.title("Dilation Image")
fig.add_subplot(153)
plt.imshow(ersion, cmap = plt.get_cmap('gray'))
plt.title("Erosion Image")
fig.add_subplot(154)
plt.imshow(opening, cmap = plt.get_cmap('gray'))
plt.title("Opening Image")
fig.add_subplot(155)
plt.imshow(closing, cmap = plt.get_cmap('gray'))
plt.title("Closing Image")
plt.show()