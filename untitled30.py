# -*- coding: utf-8 -*-
"""Untitled30.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sSRipqwWodgzjRcU4D3OsMk81OHph5GC
"""

import numpy as np
import pandas as pd
data=pd.read_csv('reviews.csv')
print(data.head(10))

data['content']=data['content'].str.lower()
print(data.head(10))

import re
df=pd.DataFrame(data)
def rem(text):
  p=r'https?://\S+'
  return re.sub(p,'',text)
df['content'].dtypes
df['content'] = df['content'].astype(str)
df['content']=df['content'].apply(rem)
print(df)

def remove_next_lines(text):
  return text.replace('\n', '')
df['content'] = df['content'].apply(remove_next_lines)
print(df)

def remove_words_with_numbers(text):
  return ' '.join(word for word in text.split() if not any(c.isdigit() for c in word))
df['c_content'] = df['c_content'].apply(remove_words_with_numbers)
print(df)

def remove_extra_spaces(text):
  return re.sub(r'\s+', ' ', text)
df['content'] = df['content'].apply(remove_extra_spaces)
print(df)

def remove_special_characters(text):
  pattern = r'[^\w\s]'
  return re.sub(pattern, '', text)
df['content'] = df['content'].apply(remove_special_characters)
print(df)

!pip install nltk
nltk.download('punkt')
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = stopwords.words('english')
def remove_stopwords(text):
  words = nltk.word_tokenize(text)
  filtered_words = [word for word in words if word.lower() not in stop_words]
  return ' '.join(filtered_words)
df['content'] = df['content'].apply(remove_stopwords)
print(df)

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
def stem_words(text):
    words = nltk.word_tokenize(text)
    stemmed_words = [stemmer.stem(word) for word in words]
    return ' '.join(stemmed_words)
df['content'] = df['content'].apply(stem_words)
print(df)

!pip install nltk
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
def lemmatize_words(text):
    words = nltk.word_tokenize(text)
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(lemmatized_words)
df['content'] = df['content'].apply(lemmatize_words)
print(df)