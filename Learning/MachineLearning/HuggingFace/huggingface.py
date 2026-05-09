# %% 
from transformers import AutoTokenizer

# %%
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# %%

text = 'i love ABC'
tokens = tokenizer(text,)

# %%
tokens
# %%

lst = ['i Love Ai Ml','i Hate Ai ml']

tokens = tokenizer(lst,
                   padding = True,
                   truncation=True,
                   max_lenght=128,
                   return_tensors='pt')
# %%
print(tokens['input_ids'])
print(tokens['input_ids'].shape)
print(tokens['attention_mask'])
print(tokens['attention_mask'].shape)

# -----------------------------------------Auto Modle---------------------------------------

# %%

