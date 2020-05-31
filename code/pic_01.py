from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("pic.jpg")
r,g,b = img.split()
img0 = Image.merge('RGB',(r.point(lambda i:i==i*0),g.point(lambda i:i==i*0),b))

img_data = np.array(img)

# plt.imshow(img_data)

a=img_data.transpose(1,0,2)
print(img_data.shape)
plt.imshow(a)#显示图片
plt.show()
# img.show()

