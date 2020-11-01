import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_alternating(self) : 
        for i in range(nspins) : 
            if i%2==0 : self.assertEquals( alternating[i], -1, "The alternating microstate is incorrect" )
            else : self.assertEquals( alternating[i], 1, "The alternating microstate is incorrect" )
            
    def test_spinDown(self) :
        for spin in alldown : self.assertEquals( spin, -1, "the all spin down microstate is incorrect" )
        
   def test_spinUp(self) :
       for spin in allup : self.assertEquals( spin, 1, "The all spin up microstate is incorrect" )
