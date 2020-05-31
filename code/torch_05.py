import torch

a = torch.diag(torch.tensor([1,2,3,4]))
print(a)

a = torch.eye(3,3)
print(a)
a = torch.tril(torch.ones(3,3))
print(a)
a = torch.zeros(3,3)
print(a)
