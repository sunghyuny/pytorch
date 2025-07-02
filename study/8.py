import torch
import torch.nn as nn

# 1. 사용자 정의 모델 클래스
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)  # 입력 1 → 출력 1

    def forward(self, x):
        return self.linear(x)

# 2. 데이터
x = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])

# 3. 모델, 손실 함수, 옵티마이저 정의
model = LinearRegressionModel()
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# 4. 학습
for epoch in range(100):
    y_pred = model(x)  # 여기서 model(x) == model.forward(x)
    loss = criterion(y_pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 20 == 0:
        w = model.linear.weight.item()
        b = model.linear.bias.item()
        print(f"Epoch {epoch:3d} | Loss: {loss.item():.4f} | w: {w:.4f} | b: {b:.4f}")

# 5. 테스트
test_x = torch.tensor([[5.0]])
test_y = model(test_x).item()
print(f"입력 5.0에 대한 예측값: {test_y:.2f}")
