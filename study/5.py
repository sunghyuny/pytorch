import torch
import torch.nn as nn

# 1 입력 → 1 출력 선형 회귀
layer = nn.Linear(1, 1)

# 입력값 x에 대해 예측
x = torch.tensor([[2.0]])
y_pred = layer(x)
print(y_pred)
x = torch.tensor(3.0, requires_grad=True)
y = 3*x ** 3 + 2 * x ** 2 + x

y.backward()

print(x.grad)  # x에 대한 y의 기울기