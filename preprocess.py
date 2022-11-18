from const import MAX_LEN_PAGES, SAMPLE_LEN
import numpy as np
import string
import re

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('omw-1.4')

stop_words = stopwords.words("english")

lemmatizer = WordNetLemmatizer()

def build_corpus(doc, doc_len):
    random_pages = list(range(doc_len))
    if doc_len > MAX_LEN_PAGES:
        random_pages = np.random.choice(list(range(doc_len)), MAX_LEN_PAGES-10, replace=False)
    corpus = ""
    for page_number in random_pages:
        page = doc[int(page_number)]
        page_text = page.get_text("text")
        corpus = f"{corpus} {page_text}"
    return corpus


def preproces_corpus(corpus):
    #to lower case
    corpus = corpus.lower()
    #tokenize corpus
    tokens = word_tokenize(corpus)
    #remove puinctuations
    tokens = list(filter(lambda token: token not in string.punctuation, tokens))
    #remove stop words
    tokens = [word for word in tokens if word not in stop_words]
    #extract only letters
    tokens = [re.sub(r'[^a-zA-Z]', '', words) for words in tokens]
    #lemmatize tokens
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    #remove one letters tokens
    tokens = [word for word in tokens if len(word)>1]
    return tokens

def get_sample(tokens):
    if len(tokens)>SAMPLE_LEN:
        return np.random.choice(tokens, SAMPLE_LEN, replace=False)
    return tokens