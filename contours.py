# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:20:00 2018

@author: ZMJ
"""
from PIL import Image
from pylab import array,contour,gray
from matplotlib import pyplot as plt
img_path="img/00ae65c1c6631ae6f2be1a449902976e6eb8483bf6b0740d00530220832c6d3e/"
test_img=img_path+"images/00ae65c1c6631ae6f2be1a449902976e6eb8483bf6b0740d00530220832c6d3e.png"

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

from skimage.measure import find_contours
import os
from skimage.io import imread
img=imread(test_img)
fig=plt.figure(figsize=(8,4))
ax=fig.add_subplot(1,2,1)
ax.imshow(img)
ax=fig.add_subplot(1,2,2)
ax.imshow(img)
for m_path in os.listdir(img_path+"masks/"):
#	print(m_path)
	m=imread(os.path.join(img_path+"masks/",m_path))
	contours=find_contours(m,0.5)
	for contour in contours:
		ax.plot(contour[:,1],contour[:,0],linewidth=0.5,color="blue")
plt.show()		