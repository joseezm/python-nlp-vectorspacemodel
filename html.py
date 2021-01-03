# -- coding: utf-8 --
"""
Created on Wed Dec 11 09:20:44 2019

@author: josec
"""


import math
import cx_Oracle
import collections
from flask import Flask, request, render_template
app = Flask(__name__)

dsn_tns = cx_Oracle.makedsn('LAPTOP-IPLREP3V', '1521', service_name='XE')
conn = cx_Oracle.connect(user=r'system', password='admin', dsn=dsn_tns, encoding = "UTF-8", nencoding = "UTF-8")
cur = conn.cursor()
p1 = conn.cursor()
p2 = conn.cursor()
v = conn.cursor()

@app.route('/')
def index():

    return render_template('hola.html')


@app.route('/', methods=['GET','POST'])
def my_comp_post():
    text = request.form['p1']
    #return dbf.rank(text)
    colect = collections.OrderedDict()
    #inicio=time.time()
    colect = hallarVector(text)
    aRetornar = '<table cellspacing="10" cellpadding="10" border="3" style="font-family:verdana;" >'
    for i in colect.keys():
        aRetornar += '<tr>'
        aRetornar += '<td>'
        aRetornar += i
        aRetornar += '</td>'
        aRetornar += '<td>'
        aRetornar += str(colect[i])
        aRetornar += '</td>'
        aRetornar += '</tr>'
        
    #print(aRetornar)
    aRetornar += '</table>'
    
    #final=time.time()
    #tiempo=round(final-inicio,0)
    #print("TIEMPO :   " + str(tiempo))
    return aRetornar


def cosenito(col1, col2):
    
    
    numerador=0
    raiz1=0
    raiz2=0
    resultado=0
    
    for i in col1.keys():
        numerador += col1[i] * col2[i]
        raiz1 += pow(col1[i],2)
        raiz2 += pow(col2[i],2)
        
    raiz1= math.sqrt(raiz1)
    raiz2= math.sqrt(raiz2)
    
    
    
    resultado = numerador/(raiz1*raiz2)
    
    return resultado
    
        

def hallarVector(palabra):
    coleccion1 = collections.OrderedDict()
    coleccion2 = collections.OrderedDict()
    coleccion1_aux = collections.OrderedDict()
    coleccion2_aux = collections.OrderedDict()
    resultado = collections.OrderedDict()
    print('I')
    p2.execute('SELECT palabra2, valor from corpus_15_31 where palabra1 = :p' , {'p': (palabra)})
    for row in p2:
        try:
            coleccion1[row[0]] += row[1]
        except KeyError:
            coleccion1[row[0]] = row[1]
    #print(coleccion1)
    
    
    coleccion1_aux=coleccion1.copy()
    
    
    coleccion2 = coleccion1_aux.copy()
    for i in coleccion2.keys():
        coleccion2[i]=0;
        
    coleccion2_aux=coleccion2.copy()
    
    
    
    count = 0
    p1.execute('SELECT palabra1 from corpus_15_31 group by (palabra1)')
    
    #hola = 'lion'
    #p1.execute('SELECT palabra1 from corpus_15_31  group by (palabra1) having palabra1 = :p', {'p': hola})
    for row in p1:
        coleccion2=coleccion2_aux.copy()
        coleccion1=coleccion1_aux.copy()
        
        p2.execute('SELECT palabra2, valor from corpus_15_31 where palabra1 = :p' , {'p': (row[0])})
        for raw in p2:
            try:
                coleccion2[raw[0]] += raw[1]
            except KeyError:
                coleccion2[raw[0]] = raw[1]
                coleccion1[raw[0]] = 0
                
        res=cosenito(coleccion1,coleccion2)
        v.execute('INSERT INTO corpus_aux VALUES(:p1, :p2, :v)', {'p1':(palabra), 'p2': (row[0]), 'v':(res)})
        conn.commit()

        ##resultado[row] = cosenito(coleccion1,coleccion2)

        if(count%1000==0):
            print(count)
        
        count +=1
        
        ##print(resultado)
        
    print('F')
    v.execute('select * from corpus_aux order by valor desc')
    contador = 0
    for r in v:
        if(contador <= 1000):
            resultado[r[1]] = r[2]
            contador += 1
                
    v.execute('delete from corpus_aux')
    conn.commit()
    #print(resultado)
    return resultado.copy()
   
    
    
    
    
if __name__ == "__main__":
    app.run(debug=False)