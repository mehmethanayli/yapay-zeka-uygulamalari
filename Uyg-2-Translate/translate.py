# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 17:43:03 2022

@author: MCH
"""
"""Google Translate Apı"""
#pip install googletrans==3.1.0a0

import googletrans
from googletrans import Translator
import pandas as pd

#Kaç dil arasında çalışabileceğini gösterir.
#print(len(googletrans.LANGUAGES))

#Dil kısaltmaları ve isimlerini verir.
#print(googletrans.LANGUAGES)

#Önce dil sonra kısaltma ismini verir.
#print(googletrans.LANGCODES)


translator=Translator()
sentence="Olmak ya da olmamak.Gül verince mutluluktan güler."
example=translator.translate(sentence)

#Nesne tipini verir.
print(type(example))

#Kaynak cümle dilini verir.
print(example.src)

#Hedef cümle dilini verir.
print(example.dest)

#Orijinal cümleyi verir.
print(example.origin)

#Çevirilmiş cümleyi verir.
print(example.text)



print("******************")
sentence2="To be or not to be. When he gives a rose, he laughs happily."

example2=translator.translate(sentence2, dest="tr")

print(example2.src)
print(example2.dest)
print(example2.origin)
print(example2.text)

print("******************")

word_tr=["elma", "armut", "araba","mikrofon","kapı","lastik", "bilgisayar"]

df=pd.DataFrame(columns=["Türkçe","İngilizce","Fransızca","Rusça"])

#print(df)
for word in word_tr:
    df=df.append({
        "Türkçe": word,
        "İngilizce": translator.translate(word, dest="en").text,
        "Fransızca": translator.translate(word, dest="fr").text,
        "Rusça": translator.translate(word, dest="ru").text
        },ignore_index=True)
    
print(df)   
print("******************")
 
print(df.head(2))
print("******************")

print(df.iloc[0])
print("******************")

print(df[{"Türkçe","İngilizce"}])
print("******************")

print(df[{"Türkçe","İngilizce"}].values[2])








