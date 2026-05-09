# %%
import torch
import torch.nn as nn 

# %%
a = torch.tensor([1.0,2.0,3.0])

layer = nn.Linear(3,1)

print(layer(a))

print(a)
print(a.shape)
print(a.ndim)

# %% 
                    # batch_size , channels , height , width
images = torch.zeros(8,3,64,64)

print(images)
print(images.shape)
print(images.ndim)

# %%

x = torch.tensor([[1.0,2.0,3.0],
                 [4.0,5.0,6.0]])

print(x.shape)
y = x.reshape(3,2)
print(y)
print(y.shape)

z = x.reshape(6)
print(z)
print(z.shape)

# %%

x = torch.tensor(3.0,requires_grad=True)

y = x **2

print(y)

y.backward()

print(x.grad)
# %%
x = torch.tensor(2.,requires_grad=True)

y = 3*x**3 + 2 * x **2 + x

y.backward(retain_graph=True)
print(x.grad)
y.backward()
print(x.grad)

# %%

modle = nn.Linear(2,1)

print(modle.weight)
print(modle.bias)

x = torch.tensor([1.0,2.0])
out = modle(x)
print(out)
print(out.shape)


