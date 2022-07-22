#!/bin/python
# -*- coding: utf-8 -*-

import fire

def wynik(amount):
    x = 0
    a = 0
    b = 1
    z = 0

    while x+2 <= amount:
    
        z = dodaj(a, b)
        
        print (z)
        
        a = b
        b = z
        
        x += 1

def dodaj(a, b):
    
    c = a + b
    return c
   



class fibo(object):
    def fi(self, amount):
       
 #       if amount == 0:
 #           return 0
 #       if amount == 1:
 #           return 1
 #       if amount == 2:
 #           return 1
 #       if amount >= 3:

        return wynik(amount)
        
      
#####
if __name__ == '__main__':
    fire.Fire(fibo)