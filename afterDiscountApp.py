#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 08:31:25 2020

@author: dooriq
"""

totalBuyer = int(input("Masukan banyaknya orang yang membeli: "))
totalPurchase = int(input("Masukan total biaya yang dibayarkan : "))

buyerDic = {}
for i in range(totalBuyer):
    print("Orang Ke-",i+1)
    buyerName = input("masukan nama orang: ")
    buyerPurchase = input("masukan jumlah harga :")
    buyerDic.__setitem__(buyerName,buyerPurchase)
    print("=======================================")
    
print()
print("Hasil :")

totalCost = 0
for key in buyerDic.items():
    totalCost += int(key[1])
    
    
for key in buyerDic.items():
    persentage = int(key[1])/totalCost
    buyerDic[key[0]] = round(persentage*totalPurchase,-3)
    
    
for key in buyerDic.items():
    print(key[0]," membayar tagihan sebesar ", int(key[1]))
    print()
