import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sig

def read_series(filenames,n):
  print('reading:',filenames%0)
  img=plt.imread(filenames%0)
  s=img.shape
  imgstack=np.zeros([*s[:2],n])
  imgstack[:,:,0]=img
  for i in range(1,n):
    print('reading:',filenames%i)
    imgstack[:,:,i]=plt.imread(filenames%i)
  return imgstack

def display_image_series(f,imgstack,cols=6):
  s=imgstack.shape
  for i in range(s[2]):
    ax=f.add_subplot(s[2]//cols,cols,i+1)
    ax.set_axis_off()
    plt.imshow(imgstack[:,:,i],cmap='gray')
 
def show_series():
  f=plt.figure(figsize=(12,4))
  imgstack=read_series('fseries(%i).png',18)
  display_image_series(f,imgstack,9)
  #plt.savefig('focusseries.png', facecolor=(130./256,126./256,120./256),dpi=160) 
  plt.show()

show_series()
