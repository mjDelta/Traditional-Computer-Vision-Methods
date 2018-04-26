import numpy as np
import scipy.ndimage as ndi
from skimage import measure,color
import matplotlib.pyplot as plt


def microstructure(l=256):
    n = 5
    x, y = np.ogrid[0:l, 0:l]  
    mask = np.zeros((l, l))
    generator = np.random.RandomState(1)  
    points = l * generator.rand(2, n**2)
    mask[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
    mask = ndi.gaussian_filter(mask, sigma=l/(4.*n))
    return mask > mask.mean()

data = microstructure(l=128)*1 

labels=measure.label(data,connectivity=2)  
dst=color.label2rgb(labels)  
print('regions number:',labels.max()+1)  

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(data, plt.cm.gray, interpolation='nearest')
ax1.axis('off')
ax2.imshow(dst,interpolation='nearest')
ax2.axis('off')

fig.tight_layout()
plt.show()
