# %% 
import torch
import torch.nn as nn
from sklearn.datasets import make_moons
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# %%

X_mm ,y_mm= make_moons(n_samples=10000,shuffle=True,random_state=42,noise=0.2)
torch.manual_seed(42)


X = torch.tensor(X_mm,dtype=torch.float32)
y = torch.tensor(y_mm,dtype=torch.float32).unsqueeze(1)

X_train, X_test = X[:8000], X[8000:]
y_train, y_test = y[:8000], y[8000:]

X_train = X_train.to(device)
y_train = y_train.to(device)
X_test = X_test.to(device)
y_test = y_test.to(device) 

# %%

modle = nn.Sequential(
    nn.Linear(2,16),
    nn.ReLU(),
    nn.Linear(16,8),
    nn.ReLU(),
    nn.Linear(8,1)
).to(device)
loss_fn = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(modle.parameters(),lr=0.01)

modle.train()
for epochs in range(100):
    preds = modle(X_train)
    loss = loss_fn(preds,y_train)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if epochs % 10 == 0:
        print(f" epochs -> {epochs} loss -> {loss}")
modle.eval()
with torch.no_grad():
    preds = modle(X_test)
    probs = torch.sigmoid(preds)
    predicted = (probs > 0.5).float()
    accuracy = (predicted == y_test).float().mean()
    print(accuracy.item())
