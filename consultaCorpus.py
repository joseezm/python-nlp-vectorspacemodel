from nltk.stem import WordNetLemmatizer
import cx_Oracle

dsn_tns = cx_Oracle.makedsn('LAPTOP-IPLREP3V', '1521', service_name='XE')
conn = cx_Oracle.connect(user=r'system', password='admin', dsn=dsn_tns)
cur = conn.cursor()

def query(palabra):
    cur.execute('SELECT * from (SELECT palabra2 FROM corpus_00 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3 UNION  SELECT * from (SELECT palabra2 FROM corpus_01 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3 UNION SELECT * from (SELECT palabra2 FROM corpus_02 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3 UNION SELECT * from (SELECT palabra2 FROM corpus_03 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3 UNION SELECT * from (SELECT palabra2 FROM corpus_04 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3 UNION SELECT * from (SELECT palabra2 FROM corpus_05 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3 UNION SELECT * from (SELECT palabra2 FROM corpus_06 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3 UNION SELECT * from (SELECT palabra2 FROM corpus_07 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3 UNION SELECT * from (SELECT palabra2 FROM corpus_08 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3 UNION SELECT * from (SELECT palabra2 FROM corpus_09 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3 UNION SELECT * from (SELECT palabra2 FROM corpus_10 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3 UNION SELECT * from (SELECT palabra2 FROM corpus_11 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3 UNION SELECT * from (SELECT palabra2 FROM corpus_12 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3 UNION SELECT * from (SELECT palabra2 FROM corpus_13 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3 UNION SELECT * from (SELECT palabra2 FROM corpus_14 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    for row in cur:
       print ( palabra + '   ->   ' + row[0])
    
    
def consulta(palabra,tabla):
    if(tabla==0):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_00 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==1):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_01 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==2):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_02 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==3):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_03 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==4):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_04 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==5):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_05 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==6):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_06 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==7):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_07 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==8):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_08 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==9):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_09 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==10):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_10 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==11):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_11 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==12):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_12 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==13):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_13 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==14):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_14 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==15):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_15 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==16):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_16 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==17):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_17 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==18):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_18 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==19):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_19 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==20):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_20 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==21):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_21 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==22):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_22 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==23):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_23 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==24):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_24 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==25):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_25 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==26):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_26 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==27):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_27 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==28):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_28 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==29):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_29 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==31):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_30 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 
    elif(tabla==31):
        cur.execute('SELECT * from (SELECT palabra2 FROM corpus_31 WHERE lower(palabra1) = (:1)  ORDER BY valor DESC) where ROWNUM <= 3', [palabra]) 

    for row in cur:
       print ( palabra + '   ->   ' + row[0])
    

def main():
    palabra = 'miss'
    #consulta(palabra,14)
    query(palabra)


   
    
main()



