# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# %%

path = "C:/Users/manra_reeinmj/OneDrive/Desktop/Python_Ai_Learning/Learning/MachineLearning/Hour_Score.csv"
# %%
df = pd.read_csv(path)


# %%
df
# %%

X = df.Hours
y = df.Scores

# %%

def Loss(m,c):
    predictions = (m * X +c)

    return ((y - predictions)**2).mean() 


# %%
def Gradient(m_now,c_now,L):
    prediction = m_now * X + c_now
    error = prediction-y

    grad_m = (2/len(df)) * (X @ error)
    grad_c = (2/len(df)) * error.sum()

    m = m_now - L * grad_m
    c = c_now - L * grad_c
    return m , c


# %%

def Train(L,epochs):
    m,c=0,0

    for i in range(epochs):
        m , c = Gradient(m,c,L)
        print(f"Loss {Loss(m,c)}")

        if i % 50 == 0:print(f"{i,m,c}")
    print(m,c)
# %%
Train(0.0001,1000)
# %%
# %%
