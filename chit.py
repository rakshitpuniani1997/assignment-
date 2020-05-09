import pymongo
from pymongo import MongoClient
import re
import pandas as pd
import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string
corpus = []

# reading data
cluster = MongoClient("mongodb+srv://Rak123:Rak123@cluster0-kyilz.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["cltweets"]
collection = db["tweets"]
data = pd.DataFrame(list(collection.find({},{"body":1,"_id":0})))

# Data Cleaning
for i in range(len(data)):
    cleaned_data = re.sub('[r'\d+'],'', data[i])
    cleaned_data = data["body"][i].translate(string.maketrans("",""),string.punctuation)
    cleaned_data = cleaned_data.strip()
    stop_words = set(stopwords.words('english'))tokens = word_token
    cleaned_data = cleaned_data.lower()
    cleaned_data = cleaned_data.split()

    ps = PorterStemmer()
    cleaned_data = [ps.stem(word) for word in cleaned_data if not word in set(stopwords.words('english'))]
    corpus.append(cleaned_data)
    df2['clean'] = ','.join(cleaned_data)

df = pd.DataFrame()
df["body"] = corpus
df2.to_csv(r'/Users/rakshit/Downloads/Datacuratedtask_1.txt.', encoding='utf-8', index=False)

# # Mapper
# import sys
# for line in sys.stdin:
#     line = line.strip()
#     words = line.split()
#     for word in words:
#         print '%s\t%s' % (word, "1")
#
# # Reducer
# import sys
# word_count = {}
# for line in sys.stdin:
#     line = line.strip()
#     word, count = line.split('\t', 1)
#     try:
#         count = int(count)
#     except ValueError:
#         continue
#
#     try:
#         word_count[word] = word_count[word] + count
#     except:
#         word_count[word] = count
#
#
# for word in word_count.keys():
#     print '%s\t%s' % (word, word_count[word])


