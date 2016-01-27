#!/bin/python

import sys


n = int(raw_input().strip())

class Triangle:
    def __init__(self, n):
        self.s = ' '*(n-1)

    def recrusion(self,a,b):
        if a == 1:
            
            self.s= self.s[:((b-a))] + '#'
            print self.s
           
        else:
            self.recrusion(a-1, b)
            self.s = self.s[:b-a] + '#' + self.s[(b-a)+1:]
            print self.s
             

cc = Triangle(n)
cc.recrusion(n,n)
