
# coding: utf-8

# In[1]:


import re
import nltk
import string
import csv
from nltk.corpus import stopwords
text="My name is Hao-Wei. Nice to meet you!"
#tokens_with_punctuation=text.split(" ")
#print tokens_with_punctuation
def tokenize(text):
    pattern=r'[a-zA-Z]+[a-zA-Z\.\-]'
    tokens=nltk.regexp_tokenize(text, pattern)
#print tokens
    return tokens

def sentiment_analysis(text):
    textlist=tokenize(text)
    lower_textlist=[x.lower() for x in textlist]
    stop_words = stopwords.words('english')
    filtered_tokens={word for word in lower_textlist if word not in stop_words}
    positive_words=[]
    negative_words=[]
    with open("positive-words.txt",'r') as f:
        for line in f:
            positive_words.append(line.strip())
    with open("negative-words.txt",'r') as f:
        for line in f:
            negative_words.append(line.strip()) 
    
    positive_num=0
    negative_num=0
    for token in filtered_tokens:
        if token in positive_words:
            positive_num=positive_num+1
        if token in negative_words:
            negative_num=negative_num+1    
    if positive_num > negative_num:
        return "positive"
    elif positive_num < negative_num:
        return "negative"
    else:
        return "neutral"
        
def evaluation_accuracy(csv_file):
    with open(csv_file, "rb") as f:
        movie_review=csv.reader(f, delimiter=',')
        total=0
        correct=0
        for row in movie_review:
            total=total+1
            if sentiment_analysis(row[0])==row[1]:
                correct=correct+1
        return  correct*100/total*0.01 
        
print tokenize(text)
print sentiment_analysis(text)
print evaluation_accuracy("finding_dory_reivew.csv")
    

