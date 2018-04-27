import dlib
from skimage.io import imread,imsave
import cv2
from matplotlib import pyplot as plt
detector=dlib.get_frontal_face_detector()

path="putin.jpeg"
img=imread(path)

dets=detector(img)

print("nums,",len(dets))

for d in dets:
	left=d.left()
	right=d.right()
	top=d.top()
	bottom=d.bottom()
	cv2.rectangle(img,(left,top),(right,bottom),(255,0,0),2)

plt.imshow(img)
plt.show()

imsave("dlib.png",img)
