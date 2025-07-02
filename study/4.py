import torch

# 1. 1차원 텐서 생성
a = torch.tensor([1.0,2.0])
print("a",a)
# 2. 2차원
b = torch.tensor([[1.0,2.0],[3.0,4.0]])
print(b)

# 텐서 크기
print("a 크기:", b.shape)


x = torch.arange(0,15)
print(x)

x2d = x.view(5,3) # 0, 
print("x2d:",x2d.shape)
x2 = x.reshape(5,3)
print("x2:",x2.shape)
print("reshape",x.unsqueeze(0).shape)
print(x.unsqueeze(0).squeeze().shape)