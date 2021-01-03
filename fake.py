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
p2 = conn.cursor()
v = conn.cursor()

   
def repetido(lista, palabra):
    for x in len(lista):
        if (lista[x] == palabra):
            return x
        
    return -1


def hallarVector(l1, l2):
    c=0
    for i in range(len(l1)): 
            c+= l1[i]*l2[i] 
    cosine = c / float((sum(l1)*sum(l2))**0.5)
    return cosine



def vectores(palabra):
    relaciones = []
    valores1 = []
    valores2 = []
    relaciones1 = []
    valores1aux = []
    valores2aux = []
    
    p2.excute('SELECT palabra2, valor from corpus where palabra1 = :p' , {'p': (palabra)})
    
    for row in p2:
        try:
            pos=relaciones1.index(row[0])
        except ValueError:
            pos=-1
            
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
            try:
                pos=relaciones.index(p2row[0])
            except ValueError:
                pos=-1
                
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
    
    p2.excute('SELECT palabra2, valor from corpusG where palabra1 = :p' , {'p': (palabra)})
    
    for row in p2:
        try:
            pos=relaciones1.index(row[0])
        except ValueError:
            pos=-1
            
        if(pos==-1):
            relaciones1.append(row[0])
            valores1aux.append(row[1])
            valores2aux.append(0)    
        else:
            valores1aux[pos] = valores1aux[pos] + row[1]


        
        
    p1.execute('SELECT palabra1 from corpusG  where palabra1 = :p group by (palabra1)', {'p':palabra2})
    for p1row in p1:
        relaciones = relaciones1.copy()
        valores1 = valores1aux.copy()
        valores2 = valores2aux.copy()
        
        p2.excute('SELECT palabra2, valor from corpusG where palabra1 = :p' , {'p': (p1row[0])})
        for p2row in p2:
            try:
                pos=relaciones.index(p2row[0])
            except ValueError:
                pos=-1
                
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
        
        print (vec)
        
                
    
def consulta(palabra):
    cur.execute('select * from (select valor from vectores where palabra1 = :p) where ROWNUM <= 10', {'p':palabra})
    for row in cur:
        print (row[0])
        
        
def main():
    vectores2('cat','tiger')
    
main()
    
      



            
        
   
