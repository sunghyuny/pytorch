import torch
import torch.nn as nn

# 1. 데이터 준비
x = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])

# 2. 모델 정의 (1입력 → 1출력)
model = nn.Linear(1, 1)

# 3. 손실 함수 & 옵티마이저 설정
criterion = nn.MSELoss()               # 평균 제곱 오차
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 4. 학습 루프
for epoch in range(100):
    # (1) 예측
    y_pred = model(x)

    # (2) 손실 계산
    loss = criterion(y_pred, y)

    # (3) 역전파 & 업데이트
    optimizer.zero_grad()  # 기울기 초기화
    loss.backward()        # 역전파
    optimizer.step()       # 파라미터 업데이트

    if epoch % 10 == 0:
        print(f"Epoch {epoch}: Loss={loss.item():.4f}, w={model.weight.item():.4f}, b={model.bias.item():.4f}")

# 5. 예측 테스트
test = torch.tensor([[5.0]])
pred = model(test)
print(f"입력 5.0에 대한 예측값: {pred.item():.2f}")
