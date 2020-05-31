import torch
#矩阵操作 转置
a = torch.tensor([[1.,2.],[3.,4.]])
print(torch.eig(a,eigenvectors=True))#求特征值和特征向量
print(a.det())#求行列式
print(torch.norm(a,p=2))#求二范数
