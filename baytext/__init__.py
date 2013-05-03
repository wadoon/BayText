# -*- encoding: utf-8 -*-

from .functionguard import guard
import os
import shutil
import re

###############################################################################
## read document section

@guard
def read_document(file):
    return read_document_txt(file)


def endswith(sfx):
    return lambda x: x.endswith(sfx)

read_document.register_predicate(endswith, prefix="")


@read_document.endswith("txt")
def read_document_txt(file): 
    with open(file) as f:
        return f.read()


@read_document.endswith("pdf")
def read_document_pdf(file):
    cmd = "pdftotext " 
    args = ['-eol unix',
            '-enc UTF-8', file]

    a = os.system(cmd + " ".join(args))
    return read_document(file.replace('pdf', 'txt'))


@read_document.endswith("html")
def read_document_html(file):
    from HTMLParser import HTMLParser

    class MLStripper(HTMLParser):
        def __init__(self):
            self.reset()
            self.fed = []

        def handle_data(self, d):
            self.fed.append(d)

        def get_data(self):
            return ''.join(self.fed)

    def strip_tags(html):
        s = MLStripper()
        s.feed(html)
        return s.get_data()

    return strip_tags(read_document_txt(file))


###############################################################################
def filter_to_lower(word):
    return word.lower()


def filter_empty_word(word):
    ""
    if word == "":
        return None
    return word


def filter_remove(regex):
    ""
    def froc(word):
        return re.sub(regex, ' ', word, re.UNICODE)
    return froc


def filter_strip(chars):
    ""
    def fs(word):
        return word.strip(chars)
    return fs


def tidy(text, filter_chain=[]):
    ""
    if not isinstance(text, str):
        text = str(text)
    if not isinstance(text, str):
        text = text.decode('utf8')

    for f in filter_chain:
        text = f(text)
    return text


def tokenizer(text, stopwords=set()):
    """
    >>> tokenizer("i love my car")
    ['love', 'car']

    >>> tokenizer("ich mag mein auto", german_ignore)
    ['mag', 'auto']
    """
    words = text.split()
    return [w for w in words if len(w) > 2 and w not in stopwords]
