import re
import numpy as np
import pandas as pd
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://Rak123:Rak123@cluster0-kyilz.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["cltweets"]
collection = db["tweets"]
data = collection.find({"gnip.profileLocations.address.country":"Australia"},{"_id":0,"actor.twitterTimeZone":1})
data_for_curation = list(data)
df = pd.DataFrame(data_for_curation)
# for i in data_for_curation:
#     print(data_for_curation)
# stopWords = set(stopwords.words('english'))

body = []
for i in range(len(data_for_curation)):
    body_try = data_for_curation[i]
    body.append(body_try)

def cl