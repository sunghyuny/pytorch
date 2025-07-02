import torch
import torch.nn as nn

class MLPClassifier(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),  # 입력 → 은닉층
            nn.ReLU(),                         # 활성화 함수
            nn.Linear(hidden_dim, output_dim)  # 은닉층 → 출력층
        )
    
    def forward(self, x):
        return self.model(x)
# 예: 입력 10차원 → 은닉층 32 → 출력 2개 클래스 (예: 긍/부정)
model = MLPClassifier(input_dim=10, hidden_dim=32, output_dim=2)

# 가짜 입력 (배치 3개, 특성 10개)
x = torch.randn(3, 10)

# 예측
output = model(x)
print("출력:", output)
print("예측 클래스:", torch.argmax(output, dim=1))