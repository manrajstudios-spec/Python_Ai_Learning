# %% 
import torch 
from torch.utils.data import Dataset,DataLoader
import torch.nn as nn
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split 

device = 'cuda' if torch.cuda.is_available() else 'cpu'
torch.manual_seed(42)
# %%

X_mm , y_mm = make_moons(n_samples=10000,shuffle=True,random_state=42,noise=0.2)

X_train,X_temp,y_train,y_temp = train_test_split(X_mm,y_mm,test_size=0.3,random_state=42)

X_val,X_test,y_val,y_test = train_test_split(X_temp,y_temp,test_size=0.15,random_state=42)
# %%

class ModleDataset(Dataset):
    def __init__(self,X,y):
        self.X = torch.tensor(X,dtype=torch.float32)
        self.y = torch.tensor(y,dtype=torch.float32).unsqueeze(1)

    def __len__(self):
        return len(self.X)
    
    def __getitem__(self, index):
        return self.X[index],self.y[index]

# %%

train_loader = DataLoader(dataset=ModleDataset(X_train,y_train),batch_size=64,shuffle=True)
val_loader = DataLoader(dataset=ModleDataset(X_val,y_val),batch_size=64,shuffle=False)
test_loader = DataLoader(dataset=ModleDataset(X_test,y_test),batch_size=64,shuffle=False)
# %%

class Binary_Classfier(nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = nn.Linear(2,32)
        self.l2 = nn.Linear(32,16)
        self.l3 = nn.Linear(16,8)
        self.l4 = nn.Linear(8,1)

        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()
        self.dropout = nn.Dropout(p=0.3)
    
    def forward(self,X):
        X = self.relu(self.l1(X))
        X = self.dropout(X)
        
        X = self.relu(self.l2(X))
        X = self.dropout(X)
        
        X = self.relu(self.l3(X))
        X = self.dropout(X)

        return self.sigmoid(self.l4(X))
    
# %%

model = Binary_Classfier()

loss_fn = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(),lr=0.01)

best_model = None
max_loss = float('inf')

for epoch in range(100):
    correct = 0 
    model.train()
    min_loss = float('inf')
    
    for batch_X,batch_y in train_loader:
        preds = model(batch_X)
        loss = loss_fn(preds,batch_y)
        min_loss = loss.item() if loss.item() < min_loss else min_loss

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if epoch % 10 == 0:
        print(f"epoch: {epoch} ; loss: {min_loss}")

    # validation

    model.eval()

    loss_val = 0.0
    with torch.no_grad():
        for batch_X,batch_y in val_loader:
            preds = model(batch_X) 
            predicted = (preds > 0.5).float()
            correct += (predicted == batch_y).sum().item()
            loss_val += loss_fn(preds,batch_y).item() 
            
    if loss_val/len(val_loader) < max_loss:
        max_loss = loss_val/len(val_loader)
        best_model = model.state_dict()
        print(f"accuracy: {correct/len(val_loader)} ; Loss: {max_loss}")

torch.save(best_model,'model.pth')

# %%
model.eval()


    
            


