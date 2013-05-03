#!/usr/bin/python3


from path import path
from baytext.classifier import Classificator
from baytext import *
from baytext.util import STOPWORDS
from functools import partial


c = Classificator()

fc = (filter_to_lower, filter_strip(".()[]1234567890!-<>|\\\"§$%&/()=?`+~^`#˝@ł€¶æſðđ»«¢„xvcµ·…€ø¶→←↓˝łđðĸŋ…·"),filter_empty_word)
word_filter = partial(tidy, filter_chain = fc)

def clean(txt):
    ls = map(word_filter, tokenizer(txt, STOPWORDS['de']))
    return ls

for clazz in path('cases').listdir():
    for case in clazz.files("*.txt"):
        print("Train %s for %s" % (case , case))
        c.train(clazz.name, clean(read_document(case)))

c._build()

c._forget()
c.store("classes.db")



#print("words: %d " % len(c.words))
#print(c.words)

# while True:
#     print(">", end=" ")
#     word = input()
#     print(c.words[word])
#     print(c.decide([word]))
#     print(c.score([word]))
