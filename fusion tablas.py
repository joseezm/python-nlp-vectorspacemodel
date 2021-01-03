# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:23:54 2019

@author: Asus
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:13:14 2019

@author: Asus
"""

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
conn = cx_Oracle.connect(user=r'system', password='admin', dsn=dsn_tns, encoding = "UTF-8", nencoding = "UTF-8")
cur = conn.cursor()
   

    
def añadirDato(palabra1, palabra2, valor):
    cur.execute("insert into corpus_0_14 values (:p1, :p2, :v)",{'p1': (palabra1),'p2': (palabra2), 'v': (valor)})
     


    
def fusionar():
    cur = conn.cursor()
    cur.execute('SELECT palabra1, palabra2, valor from corpus14')
    cont = 0
    print('I')
    for row in cur: 
        añadirDato(row[0], row[1], row[2])
        if(cont % 100000 == 0):
            print(cont)
            
        cont=cont+1 
    
    conn.commit()
    print('F')
    
    
    
      
fusionar()

#detectar2()


            
        
   
