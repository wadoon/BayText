# -*- encoding: utf-8 -*-
"""

https://github.com/jart/redisbayes/blob/master/redisbayes.py
"""

__all__ = ['Classificator', 'tokenizer']

import operator, re, shelve
from functools import reduce

__license__ = "gpl-v3.0"
__author__ = "Alexander Weigl"
__version__ = "0.1"


def incr_key(*l):
    """
    >>> a = {}
    >>> incr_key((a, 1), (a, 1), (a, 2))
    >>> a
    {1: 2, 2: 1}
    """
    for d, key in l:
        try:
            d[key] += 1
        except:
            d[key] = 1

def normalize(d):
    c = float(sum(d.values()))
    return { k: v / c for k, v in list(d.items()) }

def normalize2(wc, card_c):
    return {(w, c) : count / card_c[c] for (w, c), count in list(wc.items())}

def product(iter):
    return reduce(operator.mul, iter)

class Classificator(object):
    """
    >>> c = Classificator()
    >>> c.train('good', ['A'])
    >>> c.train('bad', ['X'])
    >>> c._build()
    
    >>> c.decide( ['A'] )
    'good'
    >>> c.decide( ['X'] )
    'bad'
    """

    def __init__(self):
        self.p = dict()
        self.wordClassCount = dict()
        self.words = dict()
        self.categories = dict()
        self.cardClass = dict()

        self._p_z_x = dict()
        self._p_x = dict()
        self._p_z = dict()
        
        
    def load(self, file):
       db = shelve.open(file)
       attrib = self.__dict__
       attrib.update(db)
       #for k in attrib.keys():
       #    setattr(self, k, db[k])
           
    def store(self, file):
        db = shelve.open(file)
        db.update(self.__dict__)
        db.close()

    def train(self, clazz, words=list()):
        """
        Put the `words` under the category ``clazz`` into the database.
        """
        incr_key((self.categories, clazz))
        list(map(lambda w: incr_key(
             (self.words, w),
             (self.cardClass, clazz),
             (self.wordClassCount, (w, clazz)))
            , words))

    def _forget(self):
        """Deletes the counting tables. You can still classify 
        with ``score`` and ``decide`` but not train anymore. 
        Calling ``_build`` should be avoided."""

    def _build(self):
        self._p_z_x = dict()
        self._p_x = dict()
        self._p_z = dict()

        # x = klasse
        # z = woerter

        self._p_x = normalize(self.categories)
        self._p_z = normalize(self.words)        
        self._p_z_x = normalize2(self.wordClassCount, self.cardClass)


    def score(self, words):
        """Returns the score for every known category"""
        def score_for_cat(cat):            
            # print(cat)
            p_x_z = 1
            hit = False
            for w in words:
                try:
                    _p_zx = self._p_z_x[w, cat]
                    _p_z = self._p_z[w]   
                    # print("\t", w,cat, _p_zx , _p_z)
                    p_x_z = p_x_z * _p_zx / _p_z
                    hit = True
                except KeyError:
                    pass

            if not hit: return 0
            return p_x_z * self._p_x[cat]
                
        scoring = { cat : score_for_cat(cat)
                    for cat in list(self.categories.keys())}
        return scoring
        
    def decide(self, words):
        mx_class = None
        mx_score = 0
        for cl, sc in self.score(words).items():
            if sc > mx_score:
                mx_class = cl
        return mx_class

if __name__ == '__main__':
    import doctest
    doctest.testmod()
