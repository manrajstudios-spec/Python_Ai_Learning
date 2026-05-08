# %% 
import torch
from sklearn.datasets import make_moons

device = 'cuda' if torch.cuda.is_available() else 'cpu'

# %%
"""
torch.manual_seed(42)

X = torch.randn(100,2)
y = (X[:,0] + X[:,1] > 0).float().unsqueeze(1) 

X_train, X_test = X[:80], X[80:]
y_train, y_test = y[:80], y[80:]
"""
# %%

X_np,y_np = make_moons(n_samples=10000,shuffle=True,noise=0.2,random_state=42)

X = torch.tensor(X_np,dtype=torch.float32)
y = torch.tensor(y_np,dtype=torch.float32).unsqueeze(1)

X_train, X_test = X[:8000], X[8000:]
y_train, y_test = y[:8000], y[8000:]

X_train = X_train.to(device)
y_train = y_train.to(device)
X_test = X_test.to(device)
y_test = y_test.to(device) 

# %%
class BinaryClassifier(torch.nn.Module): # nn.module makes it a nn type of class so we can use neural network meathods 
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(2,16) # (input size (must match cols of input), Hidden Layer Size (can be any))
        self.fc2 = torch.nn.Linear(16,8)
        self.fc3 = torch.nn.Linear(8,1)
        self.relu = torch.nn.ReLU()
        self.sigmoid = torch.nn.Sigmoid()
        self.dropout = torch.nn.Dropout(p=0.3)
    def forward(self,x):
        x = self.relu(self.fc1(x))
        # x = self.dropout(x)
        x = self.relu(self.fc2(x))
        # x = self.dropout(x)
        return self.fc3(x)
    
torch.manual_seed(42)
modle = BinaryClassifier().to(device)
print(modle)

loss_fn = torch.nn.BCEWithLogitsLoss() # Built in sigmoid so we dont need sigmoid in for fc3
optimizer = torch.optim.Adam(modle.parameters(),lr=0.01)

for epochs in range(100):

    preds = modle(X_train)

    loss = loss_fn(preds,y_train)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    if epochs % 10 == 0:
        print(f" epochs -> {epochs} loss -> {loss}")

with torch.no_grad():
    preds = modle(X_test)
    probs = torch.sigmoid(preds)
    predicted = (probs > 0.5).float()
    accuracy = (predicted == y_test).float().mean()
    print(accuracy.item())  


# %%