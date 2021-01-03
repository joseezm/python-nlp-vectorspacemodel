# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 09:06:49 2019

@author: Asus
"""

from nltk.corpus import words as nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import re,string

import cx_Oracle

dsn_tns = cx_Oracle.makedsn('LAPTOP-IPLREP3V', '1521', service_name='XE')
conn = cx_Oracle.connect(user=r'system', password='admin', dsn=dsn_tns)
cur = conn.cursor()

dictionary=dict.fromkeys(nltk.words(),None)


def delete_emp(n_empno):
    cur = conn.cursor()
    cur.execute("Delete from corpus_13 where palabra1 = :n_empno",{'n_empno': (n_empno)})
    cur.close()
    conn.commit()
    

    

def ver_english(word):
    try:
        x=dictionary[word]
        return True
    except KeyError:
        return False

    
def detectar():
    cur = conn.cursor()
    cur.execute('SELECT palabra1 from corpus_13 group by(palabra1) ')
    cont = 0
    print('I')
    for row in cur:     
        if(ver_english(row[0]) == False):
            print ('- ' + row[0])
            #delete_emp(row[0])

            
        print(cont)
            
        cont=cont+1 
    
    print('F')
    
    
    
      
detectar()

#detectar2()


            
        
   
