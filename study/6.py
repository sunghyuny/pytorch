import torch

# 1. 학습 데이터 준비 (공부시간 → 점수)
x = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[7.0], [4.0], [6.0], [8.0]])

# 2. 학습 파라미터 초기화 (기울기 w, 절편 b)
w = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)

# 3. 학습률 설정
lr = 0.01

# 4. 100번 반복 학습
for epoch in range(100):
    # (1) 예측값 계산
    y_pred = x * w + b

    # (2) 손실 함수 (MSE)
    loss = ((y_pred - y) ** 2).mean()

    # (3) 역전파
    loss.backward()

    # (4) 경사하강법으로 파라미터 갱신
    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad

        # (5) 기울기 초기화
        w.grad.zero_()
        b.grad.zero_()

    if epoch % 1 == 0:
        print(f"Epoch {epoch}: Loss={loss.item():.4f}, w={w.item():.4f}, b={b.item():.4f}")

# 5. 테스트
test = torch.tensor([[9.0]])
pred = test * w + b
print(f"입력 5.0일 때 예측 값: {pred.item():.2f}")
