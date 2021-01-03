
from nltk.corpus import words as nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import re,string
import math
import cx_Oracle

dsn_tns = cx_Oracle.makedsn('LAPTOP-IPLREP3V', '1521', service_name='XE')
conn = cx_Oracle.connect(user=r'system', password='admin', dsn=dsn_tns, encoding = "UTF-8", nencoding = "UTF-8")
cur = conn.cursor()
p1 = conn.cursor()
p2 = con.cursor()
v = con.cursor()

   
def repetido(lista, palabra):
    for x in len(lista):
        if (lista[x] == palabra):
            return x
        
    return -1


def hallarVector(lista1, lista2):
    num=0
    raiz1=0
    raiz2=0
    for x in len(lista1):
        num = num +(lista1[x]*lista2[x])
        raiz1= raiz1 + (lista1[x]*lista1[x])
        raiz2= raiz2 + (lista2[x]*lista2[x])

    val=(num)/ (math.sqrt(raiz1) * math.sqrt(raiz2))
    
    return val



def vectores(palabra):
    relaciones = []
    valores1 = []
    valores2 = []
    relaciones1 = []
    valores1aux = []
    valores2aux = []
    
    p2.excute('SELECT palabra2, valor from corpus where palabra1 = :p' , {'p': (palabra)})
    
    for row in p2:
        pos=repetido(relaciones1,row[0])
        if(pos==-1):
            relaciones1.append(row[0])
            valores1aux.append(row[1])
            valores2aux.append(0)    
        else:
            valores1aux[pos] = valores1aux[pos] + row[1]

        
        
    p1.execute('SELECT palabra1 from corpus group by (palabra1)')
    for p1row in p1:
        relaciones = relaciones1.copy()
        valores1 = valores1aux.copy()
        valores2 = valores2aux.copy()
        
        p2.excute('SELECT palabra2, valor from corpus where palabra1 = :p' , {'p': (p1row[0])})
        for p2row in p2:
            pos = repetido(relaciones,p2row[0])
            if(pos == -1):
                relaciones.append(p2row[0])
                valores1.append(0)
                valores2.append(p2row[1])
                
            else:
                valores2[pos] = valores2[pos]+p2row[1]
                
        print (len(relaciones))
        print (len(valores1))
        print (len(valores2))
        
        vec = hallarVector(valores1,valores2)
        
        cur.execute('insert into vectores (:p1,:p2, :val)', {'p1':(palabra), 'p2':(p2row[0]), 'val':(vec)})
        
        print (vec)
        
        
        
def vectores2(palabra,palabra2):
    relaciones = []
    valores1 = []
    valores2 = []
    relaciones1 = []
    valores1aux = []
    valores2aux = []
    
    p2.excute('SELECT palabra2, valor from corpus where palabra1 = :p' , {'p': (palabra)})
    
    for row in p2:
        pos=repetido(relaciones1,row[0])
        if(pos==-1):
            relaciones1.append(row[0])
            valores1aux.append(row[1])
            valores2aux.append(0)    
        else:
            valores1aux[pos] = valores1aux[pos] + row[1]

        
        
    p1.execute('SELECT palabra1 from corpus group by (palabra1) where palabra1 = :p', {'p':palabra2})
    for p1row in p1:
        relaciones = relaciones1.copy()
        valores1 = valores1aux.copy()
        valores2 = valores2aux.copy()
        
        p2.excute('SELECT palabra2, valor from corpus where palabra1 = :p' , {'p': (p1row[0])})
        for p2row in p2:
            pos = repetido(relaciones,p2row[0])
            if(pos == -1):
                relaciones.append(p2row[0])
                valores1.append(0)
                valores2.append(p2row[1])
                
            else:
                valores2[pos] = valores2[pos]+p2row[1]
                
        print (len(relaciones))
        print (len(valores1))
        print (len(valores2))
        
        vec = hallarVector(valores1,valores2)
        
        #cur.execute('insert into vectores (:p1,:p2, :val)', {'p1':(palabra), 'p2':(p2row[0]), 'val':(vec)})
        
        print ( palabra1 + '  ' + palabra2 + '  ' vec)
        
                
    
def consulta(palabra):
    cur.execute('select * from (select valor from vectores where palabra1 = :p) where ROWNUM <= 10', {'p':palabra})
    for row in cur:
        print (row[0])
    
      



            
        
   
