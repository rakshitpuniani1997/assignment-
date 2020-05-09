import re
import pymongo
from pymongo import MongoClient
import pandas as pd
from pprint import pprint
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

cluster = MongoClient("mongodb+srv://Rak123:Rak123@cluster0-kyilz.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["cltweets"]
collection = db["tweets"]
data = collection.find({}, {"body": 1, "_id": 0})
data_for_curation = list(data)
# for i in data_for_curation:
#     print(data_for_curation)
# stopWords = set(stopwords.words('english'))

body = []
for i in range(len(data_for_curation)):
    body_try = data_for_curation[i]["body"]
    body.append(body_try)


def data_curation(body):
    tokenize = word_tokenize(body)
    cleaned_data = [word for word in tokenize if not word in set(stopwords.words('english'))]
    cleaned_data = [word for word in cleaned_data if not (word.isdigit())]
    cleaned_data = [re.sub(r"http\S+", "", word) for word in cleaned_data]
    cleaned_data = [word.strip('.@#') for word in cleaned_data]
    cleaned_data = [word.strip() for word in cleaned_data if word.strip()]

    # emoji = re.compile("["
    #                    "\U0001F600-\U0001F64F"  # emoticons
    #                    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    #                    "\U0001F680-\U0001F6FF"  # transport & map symbols
    #                    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    #                    "\U00002702-\U000027B0"
    #                    "\U000024C2-\U0001F251"
    #                    "]+", flags=re.UNICODE)
    # cleaned_data = [emoji.sub(r'', word) for word in cleaned_data]
    return cleaned_data


cleaned_body = []
body_final = []
for i in range(len(body)):
    cleaned_body.append(data_curation(body[i]))

# while '' in cleaned_body:
#     cleaned_body.remove('')
# for i in range(len(cleaned_body)):
#     body_finalize = cleaned_body[i]
#     body_final.append(body_finalize)

for i in cleaned_body:
    print(i)
df = pd.DataFrame()
df["body"] = cleaned_body
df.to_csv(r'/Users/rakshit/Downloads/Assignment.txt.', encoding='utf-8', index=False)
