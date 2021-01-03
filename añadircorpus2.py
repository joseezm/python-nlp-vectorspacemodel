# -- coding: utf-8 --
"""
Editor de Spyder

Este es un archivo temporal.
"""
import cx_Oracle

dsn_tns = cx_Oracle.makedsn('LAPTOP-IPLREP3V', '1521', service_name='XE')
conn = cx_Oracle.connect(user=r'system', password='admin', dsn=dsn_tns, encoding = "UTF-8", nencoding = "UTF-8")
cur = conn.cursor()

def añadirDato(palabra1, palabra2, valor):
    cur.execute("insert into corpus_15_31 values (:p1, :p2, :v)",{'p1': (palabra1),'p2': (palabra2), 'v': (valor)})
     


    
def fusionar():
    cur = conn.cursor()
    cur.execute('SELECT palabra1, palabra2, valor from corpus_0_14')
    cont = 0
    print('I')
    for row in cur: 
        añadirDato(row[0], row[1], row[2])
        if(cont % 100000 == 0):
            print(cont)
        cont=cont+1 
    conn.commit()
    print('F')

def lineas():
    dsn_tns = cx_Oracle.makedsn('LAPTOP-IPLREP3V', '1521', service_name='XE')
    conn = cx_Oracle.connect(user=r'system', password='admin', dsn=dsn_tns, encoding = "UTF-8", nencoding = "UTF-8")
    print("connected")
    cur = conn.cursor()
    cont = 0
    with open('myf.txt',encoding = "utf8") as f:
        for linea in f:
            if((cont % 10000) == 0):
                print(cont)
            cur.execute(linea)
            conn.commit()
            cont = cont + 1
            
            
    conn.close()
    
    
    

def borrar():
    f  = open("corpus_15_31.sql","r")
    z = open("myf.txt","x")
    j = 0
    for linea in f:
        if((j % 10000) == 0):
            print(j)
        siguiente = ""
        for i in linea:
            if(i != ';'):
                siguiente += i
        z = open("myf.txt","a")
        z.write(siguiente)
        z.close()
        j = j + 1
        
        
        
fusionar()


