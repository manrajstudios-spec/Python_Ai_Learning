# %% 
from transformers import AutoTokenizer,AutoModel,AutoModelForSequenceClassification,AutoModelForSeq2SeqLM,AutoModelForCausalLM
from transformers import pipeline,BartTokenizer,BartForConditionalGeneration

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

# Just embedding 

model = AutoModel.from_pretrained("bert-base-uncased")

# with sentiment analyzer span not spam 

model = AutoModelForSequenceClassification.from_pretrained('bert-base-uncased',
                                           num_labels=2)

# summerisation and translation

model = AutoModelForSeq2SeqLM.from_pretrained('t5-small')

# text gen
model = AutoModelForCausalLM.from_pretrained('gpt2')

# %%

# Pipeline

# sentiment 

clf = pipeline('sentiment-analysis','distilbert-base-uncased-finetuned-sst-2-english')
print(clf('I Love This Movie'))

# %%
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")


# %%
text = "Artificial intelligence has rapidly transformed numerous industries over the past decade, fundamentally changing how businesses operate and how people interact with technology. Machine learning algorithms now power everything from recommendation systems on streaming platforms to fraud detection in banking. Natural language processing has enabled computers to understand and generate human language with remarkable accuracy, leading to the development of sophisticated chatbots and virtual assistants. Computer vision systems can now identify objects, faces, and medical conditions in images with superhuman accuracy in some domains. Despite these remarkable advances, significant challenges remain, including issues of bias in AI systems, the environmental cost of training large models, the need for vast amounts of labeled data, and concerns about job displacement as automation becomes more prevalent. Researchers are actively working on making AI systems more efficient, interpretable, and fair, while policymakers grapple with how to regulate these powerful technologies responsibly. The future of AI holds enormous promise, but realizing that promise while managing the associated risks will require careful collaboration between technologists, ethicists, policymakers, and the public at large."

inputs = tokenizer(text,
                   return_tensors='pt',
                   max_length=1024,
                   truncation=True)

summary_ids = model.generate(inputs['input_ids'],
                             max_length=100,
                             min_length=50,
                             num_beams=4,
                             temperature=0.7,
                             do_sample=True,
                             early_stopping=True)

summary = tokenizer.decode(summary_ids[0],skip_special_tokens=True)
# %%
print(summary)
# %%
