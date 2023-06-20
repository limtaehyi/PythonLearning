import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms

# 데이터 전처리
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

# 데이터 로드
train_dataset = datasets.MNIST('./data', train=True, download=True, transform=transform)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)

# MLP 모델 정의
class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):
        x = x.view(-1, 28 * 28)
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# 모델, 손실 함수, 최적화 함수 초기화
model = MLP()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

# 훈련 루프
for epoch in range(10):  # 10 에폭 반복
    for batch_idx, (X, y) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(X)             
        loss = criterion(output, y)  
        loss.backward()               
        optimizer.step()              

        # 로그 출력
        if batch_idx % 100 == 0:
            print(f"Epoch: {epoch} | Loss: {loss.item()}")
