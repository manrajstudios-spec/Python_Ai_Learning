# %%
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import OrdinalEncoder


# %%
df = fetch_openml('car',as_frame=True).frame

# %%
df

# %%
# TO ENCODE 
columns_to_encode = ['lug_boot','safety']

encoder = OrdinalEncoder(categories=[['small','med','big'],
                                     ['low','med','high']])

df[columns_to_encode] = encoder.fit_transform(df[columns_to_encode])
# %%
df

# %%
# TO REVERSE ENCODE

df[columns_to_encode] = encoder.inverse_transform(df[columns_to_encode])
df

# %%

# TO ENCODE DATA WHICH HAVE MUTIPLE VALUES LIKE more than 3 4 so converting each into some int is not ideal

# WE USE ONE HOT ENCODER

df = fetch_openml('adult',as_frame=True).frame

# %%
df
# %%

from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(handle_unknown='ignore',sparse_output=False)

en = encoder.fit_transform(df[['occupation','race']])
new_cols = encoder.get_feature_names_out(['occupation','race'])

# %%
import pandas as pd
encoded_df = pd.DataFrame(en,columns=new_cols)
df = df.drop(['occupation','race'],axis=1)

df = pd.concat([df,encoded_df],axis=1)

df


# %%
