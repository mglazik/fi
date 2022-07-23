#!/bin/python
# -*- coding: utf-8 -*-

import fire


def fibonacci(a,b,i):
    c = a+b
    print(c)
    i=i-1
    if i == 0:
        pass
    else:
        return fibonacci(b,c,i)
    
         
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
    
    def reku(self, ilosc):
        if ilosc < 0:
            print("wybierz liczbę większą od zera")
        if ilosc == 0:
            print("0")
            pass
        if ilosc == 1:
            print("0")
            print("1")
            pass
        if ilosc >= 2:
            print("0")
            print("1")
            fibonacci (0,1,ilosc-1)
      
#####
if __name__ == '__main__':
    fire.Fire(fibo)