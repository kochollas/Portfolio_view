import nltk
import pandas as pd
import numpy
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))
from nltk.stem import PorterStemmer
ps = PorterStemmer()

#load the text for scraping needed words
data = pd.read_csv('raw.txt', sep="\n ", header=None)
data.columns = ["text"]

#load petnames data
pet_names = pd.read_csv('pets.txt', sep ='\n',header = None)
pet_names = pet_names.iloc[1:]
pet_names.columns = ["name"]
pet_list = pet_names['name'].to_list()

# load the possible types available
pet_types = {"dm":["dark matter","dark metter", "dark"],
             "rb":["rainbow"], "gld":["golden","gold","gldn","glden"], "normal":["normal"]}

all_pet_types = []

for key, value in pet_types.items():
    all_pet_types.append(key)
    for val in value:
        all_pet_types.append(val)

print(all_pet_types)

# NER flow
def NER(txt):
    tokenized = sent_tokenize(txt)
    for i in tokenized:
        wordsList = nltk.word_tokenize(i)
        wordsList = [w for w in wordsList if not w in stop_words]
        tagged = nltk.pos_tag(wordsList)
    return tagged
def bids_gen(row):
    amt_pattern_1 = "[\d.]+[a-zA-Z]"
    amt_pattern_2 = "\d+\.\d+\s+\w+"+"|"+"\d+\s+\w+"
    pat = r"\d+[BmbM]"+"|"+"\d+\s+[BmbM]"
    pattern = (amt_pattern_1+"|"+amt_pattern_2)
    row = re.findall(pattern,row)
    amt = []
    for val in row:
        if re.findall(pat, val):
            amt.append(val)

    return amt

def type_gen(row):
    text = row.lower()
    text = re.findall(r"\w+",text)
    sentence = text
    dm_index = []
    global ty
    ty = 'normal'
    if 'rb' in text or 'rainbow' in text:
        ty = 'rainbow'

    elif 'gld' in text or 'golden' in text or 'gold' in text or 'gldn' in text or 'glden' in text:
        ty = 'golden'

    elif 'dm' in sentence or 'dark matter' in sentence or 'dark metter' in sentence or "dark" in sentence:
        for i in range(len(sentence)):
            if sentence[i] == 'dm':
                dm_index.append(i)
        if len(dm_index) == 1:
            if sentence[dm_index[0]+1] != 'me':
                ty = 'dark matter'
            else:
                ty = 'normal'

        elif len(dm_index)>1:
            for val in dm_index:
                if sentence[val+1] != 'me':
                    ty = 'dark matter'
                    break
                else:
                    ty = 'normal'

    return ty

def pet_gen(row):
    text = row.lower()
    text = re.findall(r"\w+",text)
    text = " ".join(text)
    text = NER(text)
    text = [k[0] for k in text if k[1] not in ('CD')]
    text = [k for k in text if  NER(k)[0][1] !='VBG']
    text = [k for k in text if k not in(all_pet_types)]
    text = [k for k in text if NER(ps.stem(k))[0][1] !='VB']
    names = []
    result = []
    for i in range(len(text)):
        for j in range(len(pet_list)):
            row_names = pet_list[j].split(" ")

            for x in row_names:
                if x == text[i]:
                    names.append(x)
                    break

                elif text[i][-1] =='s':
                    if x == text[i][:-1]:
                        names.append(x)
                        break
                elif x[:4] == text[i][:4] and x[-1] == text[i][-1]:
                    names.append(x)


    [result.append(item) for item in names if item not in result]
    return result

print(pet_gen("selling dm dominus alienus for 400m BLOBENSTAIN 13B NEED MANY"))


# some function to handle duplicated amount and pet names

def remove_duplicates(row):
    pn = pet_gen(row)
    text = row.lower()
    text = re.findall(r"\w+",text)
    count = dict()
    for value in pn:
        counter = 0
        for word in text:
            if value in word:
                counter +=1
                count[value] = counter

    bid_amount_occurence = len(bids_gen(row))
    count['bid_amount_count'] = bid_amount_occurence

    if len([value for key, value in count.items() if value ==2])>0:
        flag = 'DELETE'
    else:
        flag ='OKAY'

    return flag

data['bid_amount'] = data.text.apply(bids_gen)
data['type'] = data.text.apply(type_gen)
data['pet_name'] = data.text.apply(pet_gen)
data['quality'] = data.text.apply(remove_duplicates)
data.to_csv('final.csv')
print(data.head(5))
