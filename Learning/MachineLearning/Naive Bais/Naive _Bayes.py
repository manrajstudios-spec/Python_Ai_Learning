# %%
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,accuracy_score

# %%
class GaussingNB:
    def fit(self,X,y):

        X,y = np.asarray(X),np.asarray(y) 
        self.classes = np.unique(y) # TYPES OF OUTCOMES
        n_classes = len(self.classes) # HOW MANY DIFFRENT OUTCOMES ARE THERE 
        n_features = X.shape[1] # HOW MANY FEATURES ARE THERE 

        self.means = np.zeros((n_classes , n_features))
        self.variences = np.zeros((n_classes , n_features))
        self.priors = np.zeros(n_classes)

        for i , k in enumerate(self.classes):

            Xk = X[y==k]
            self.means[i] = Xk.mean(axis=0)
            self.variences[i] = Xk.var(axis=0)
            self.priors[i] = Xk.shape[0] / X.shape[0]

        return self
    
    def log_gaussian(self,X):
        num = -0.5 * (X[:,None,:] - self.means) ** 2 / self.variences
        log_prob = num - 0.5 * np.log(2*np.pi * self.variences)
        return log_prob.sum(axis=2)
    
    def predict(self,X):
        X = np.asarray(X)

        log_likelihood = self.log_gaussian(X)

        log_prior = np.log(self.priors)

        return self.classes[np.argmax(log_likelihood + log_prior , axis = 1)]



# %%

X,y = load_breast_cancer(return_X_y=True)
df = load_breast_cancer(as_frame=True).frame

X_train,X_test , y_train,y_test = train_test_split(X,y,test_size=0.2)

clf = GaussingNB().fit(X_train,y_train)

y_pred = clf.predict(X_test)

print(classification_report(y_test,y_pred))
print(accuracy_score(y_test,y_pred))

# %%
