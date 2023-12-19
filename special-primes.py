# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:04:55 2018

@author: Sempai
"""

def desc(n):
    """
    este mÃ³dulo prueba iterativamente desde 2 distintos valores de divisor para ver si dividen a n
    
    si se encuentra un divisor se aÃ±ade a la lista y se divide n entre Ã©l
    
    la descomposiciÃ³n acaba evidentemente cuando n ya no se puede descomponer mÃ¡s, esto es n=1
    """
    lista=[]
    while n!=1:
        divisor=2        
        while n%divisor!=0:
            divisor = divisor + 1    
        lista.append(divisor)
        n=n/divisor    
    return (lista)


def javo(j):
    i=1
    n=3
    while i<j:
        if len(desc(n))==1:
            i+=1
            print (n)
        n+=2
    return n,i