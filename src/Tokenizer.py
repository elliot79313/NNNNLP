# -*- coding: utf-8 -*-


import re
import nltk


def tokenize(raw): 
    sub_tokens =  re.findall(ur'([\u4e00-\u9fff]|[\uff00-\uffef]|[a-zA-Z]+|\s+)', unicode(raw,'utf-8'))
    print sub_tokens



