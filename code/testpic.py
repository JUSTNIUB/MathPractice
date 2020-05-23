from PIL import Image
import torch
import numpy

img = Image.open("pic.jpg")
print(img)
a = numpy.array(img)
print(a.shape)


