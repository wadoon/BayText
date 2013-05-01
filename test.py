#!/usr/bin/python3

import unittest as u
import baytext
from baytext.classifier import Classificator


class ClassifierTest(u.TestCase):
    def test_store_and_load(self):
        c = Classificator()
        c.train("A", (1,2,3))
        c.train("B", (3,4,5))
        c._build()                
        c.store("test.db")
        
        d = Classificator()
        d.load("test.db")
        
        self.assertEqual(c.__dict__, d.__dict__, "not the same classificators")
        
u.main()        




