# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:45:44 2022

@author: MCH
"""

""" Google Translate Paketi Yüklenmelidir."""
#pip install googletrans==3.1.0a0


#Gerekli paketler eklenir.
import googletrans
from googletrans import Translator
import pandas as pd

#Desteklenen Dil Sayısı
#print(len(googletrans.LANGUAGES))

#Desteklenen Diller
#print(googletrans.LANGUAGES)


translator=Translator()
sentence="Olmak ya da olmamak"
example=translator.translate(sentence)

print(example.src)

print(example.dest)

print(example.origin)

print(example.text)


sentence2="To be or not to be"
example2=translator.translate(sentence2, dest="tr")
print(example2.src)

print(example2.dest)

print(example2.origin)

print(example2.text)


print("**************")

words_tr=["elma","armut","kivi","muz"]

df=pd.DataFrame(columns=["Türkçe","İngilizce","Fransızca","Almanca","Rusça"])

for word in words_tr:
    df=df.append({
        "Türkçe": word,
        "İngilizce":translator.translate(word, dest="en").text,
        "Fransızca":translator.translate(word, dest="fr").text,
        "Almanca": translator.translate(word,dest="de").text,
        "Rusça": translator.translate(word, dest="ru").text
        },ignore_index=True)

print(df.head(1))
print(df.iloc[0])

print(df[{'Türkçe','İngilizce'}])
print(df[{'Türkçe','İngilizce'}].values[0])






