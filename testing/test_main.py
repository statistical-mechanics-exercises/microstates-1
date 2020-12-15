import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_alternating(self) : 
        for i in range(nspins) : 
            if i%2==0 : self.assertEqual( alternating[i], -1, "The alternating microstate is incorrect" )
            else : self.assertEqual( alternating[i], 1, "The alternating microstate is incorrect" )
            
    def test_spinDown(self) :
        for spin in alldown : self.assertEqual( spin, -1, "the all spin down microstate is incorrect" )
        
    def test_spinUp(self) :
        for spin in allup : self.assertEqual( spin, 1, "The all spin up microstate is incorrect" )
