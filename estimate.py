from lib2to3.pgen2 import token
import pandas as pd
import numpy as np

def load_data(type):
    if type=='awl':
        data = pd.read_csv('word_lists/awl.csv')
        return data
    else:
        data = pd.read_csv('word_lists/low_freq_list.csv')
        return data

def awl_find(tokens):
    data = load_data('awl')
    awl_ratio = get_ratio(tokens, data)
    return awl_ratio

def low_freq_find(tokens):
    data = load_data('lfwl')
    lfwl_ratio = get_ratio(tokens, data)
    return lfwl_ratio

def get_ratio(tokens, data):
    tokens['checked'] = tokens['tokens'].isin(data['Word'])
    checked = tokens[tokens['checked']==True].shape[0]
    ratio:int = checked/tokens.shape[0]
    ratio = round(ratio*100, 2)   
    return ratio

def process_tokens(tokens):
    tokens = pd.DataFrame(tokens, columns=['tokens'])
    awl_rate = awl_find(tokens)
    lfwl_rate = low_freq_find(tokens)

    return (awl_rate, lfwl_rate)