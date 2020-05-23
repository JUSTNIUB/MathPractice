#图像操作

from PIL import Image
import numpy as np
import torch

# img = Image.open("pic.jpg")
# img.show()
# img_data = np.array(img)
# print(img_data.shape)
#img_data = img_data.reshape(300*554*3)
# img_data = img_data.transpose(1,0,2)
# print(img_data.shape)
# img = Image.fromarray(img_data)
# img.show()
a = torch.rand(1,2,2,3)

#高阶参数换维? 等于把图片或者特征全部打乱了，如何识别？
print(a)
b = a.permute(0,3,2,1)
print(b.shape)
print(b)