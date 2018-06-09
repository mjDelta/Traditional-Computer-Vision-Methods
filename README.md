# Traditional-Computer-Vision-Methods
some examples of PIL,opencv in traditional computer vision filed</br>

## 1.<a href="https://github.com/mjDelta/Traditional-Computer-Vision-Methods/blob/master/contours.py">Contour</a></br>
For contour drawing method, applying ```color image graying method``` is essential, because of threshold.</br>
For ```skimage.measure.find_contours```, it only takes 0-1 valued mask image as input. So use it to visualize the segmentation results.</br>
![image](https://github.com/mjDelta/Traditional-Computer-Vision-Methods/blob/master/img/contours.png)</br>

## 2.<a href="https://github.com/mjDelta/Traditional-Computer-Vision-Methods/blob/master/hist.py">Hist</a></br>
For ```skimage.measure.equalize_adapthist```, it makes the image contrast more obvious. It maybe helpful in preprocessing.</br>
![image](https://github.com/mjDelta/Traditional-Computer-Vision-Methods/blob/master/img/hist.png)</br>

## 3.<a href="https://github.com/mjDelta/Traditional-Computer-Vision-Methods/blob/master/morphology.py">Morphology</a></br>
For ```skimage.measure.morphology```, it can do dilation, erosion, opening, closing etc. But first turn the image into gray scale.</br>
In this image, dilation help remove some confusing edges of the nucleus. Erosion expand the edges of the nucleus.</br> 
![image](https://github.com/mjDelta/Traditional-Computer-Vision-Methods/blob/master/img/morphology.png)</br>

## 4.<a href="https://github.com/mjDelta/Traditional-Computer-Vision-Methods/blob/master/connected_component_labeling.py">connected_component_labeling</a></br>
For ```skimage.measure.label```, it can find the connected component objects. But first turn the image into gray scale.</br>
![image](https://github.com/mjDelta/Traditional-Computer-Vision-Methods/blob/master/img/label.png)</br>


## 5.<a href="https://github.com/mjDelta/Traditional-Computer-Vision-Methods/blob/master/remove_small_objects.py">remove_small_objects</a></br>
For ```skimage.morphology.remove_small_objects```, it can remove the small objects by counting how many pixels the connected components should at least have. But first turn the image into gray scale.</br>
![image](https://github.com/mjDelta/Traditional-Computer-Vision-Methods/blob/master/img/remove_small_objects.png)</br>

## 6.<a href="https://github.com/mjDelta/Traditional-Computer-Vision-Methods/blob/master/dlib_detect_face.py">dlib_detect_face</a></br>
For ```dlib.get_frontal_face_detector```, it can detect people faces quickly.It implements the algorithm in </br>
> One Millisecond Face Alignment with an Ensemble of Regression Trees
<img width="500" height="300" src="https://github.com/mjDelta/Traditional-Computer-Vision-Methods/blob/master/img/dlib.png"/>
