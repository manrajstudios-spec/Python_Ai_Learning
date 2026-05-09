# %% 
import numpy 
import torch 
import torch.nn as nn
from torch.utils.data import DataLoader,Dataset
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split

torch.manual_seed(42)
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# %%
X,y = make_blobs(n_samples=10000,n_features=8,random_state=42,shuffle=True)

X_train,X_temp,y_train,y_temp = train_test_split(X,y,test_size=0.3,random_state=42)
X_val,X_test,y_val,y_test = train_test_split(X_temp,y_temp,test_size=0.15,random_state=42)

# %%
X

# %%
class ModleDataset(Dataset):
    def __init__(self,X,y):
        self.X = torch.tensor(X,dtype=torch.float32)
        self.y = torch.tensor(y,dtype=torch.long) 

    def __len__(self):
        return len(self.X)
    
    def __getitem__(self, index):
        return self.X[index],self.y[index]
    
# %%
class MuiltiClass_Clf(nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = nn.Linear(8,64)
        self.l2 = nn.Linear(64,32)
        self.l3 = nn.Linear(32,16)
        self.l4 = nn.Linear(16,8)

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

        return self.l4(X)

# %%

train_loader = DataLoader(dataset=ModleDataset(X_train,y_train),batch_size=64,shuffle=True)
val_loader = DataLoader(dataset=ModleDataset(X_val,y_val),batch_size=64,shuffle=False)
test_loader = DataLoader(dataset=ModleDataset(X_test,y_test),batch_size=64,shuffle=False)

# %%
# Training Setup 
model = MuiltiClass_Clf()

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),lr=0.01)
scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer=optimizer,mode='min',factor=0.1,patience=5)

best_modle = None
accuracy_array = []
train_loss_array = []
val_loss_array = []

min_val_loss = float('inf')


for epoch in range(100):
    train_loss = 0.0

    for batchX,batchY in train_loader:
        preds = model(batchX)
        loss = loss_fn(preds,batchY)
        train_loss += loss

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    correct = 0
    val_loss = 0.0

    with torch.no_grad():
        for batchX,batchY in val_loader:
            preds = model(batchX)
            loss = loss_fn(preds,batchY)
            val_loss += loss
            
            correct += (torch.argmax(preds,dim=1) == batchY).sum().item()
    
    train_loss_array.append(train_loss)
    accuracy_array.append(correct)
    val_loss_array.append(val_loss)

    scheduler.step(val_loss/len(val_loader))

    if val_loss < min_val_loss:
        best_modle = model.state_dict()
        min_val_loss = val_loss
        print(f"epoch --> {epoch} ; lr --> {scheduler.get_last_lr()} \ntrain loss --> {train_loss/len(train_loader)} \nval loss --> {val_loss/len(val_loader)} \naccuracy --> {correct/len(val_loader.dataset)}")


# %%
