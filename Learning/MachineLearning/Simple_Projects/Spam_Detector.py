# %% 

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report,accuracy_score

# %%

df = pd.read_csv("/home/manraj_studios/Python/Python_Ai_Learning/Learning/MachineLearning/Simple_Projects/spam_or_not_spam.csv")


# %%
df
# %%

X = df.email.fillna('')
y = df.label

# %%

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

vectorizer = TfidfVectorizer()

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# %%

clf = LogisticRegression()

clf.fit((X_train),(y_train))
# %%
y_pred = clf.predict(X_test)
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test,y_pred))
# %%
