from nltk.stem import WordNetLemmatizer
import cx_Oracle

def esPalabra(input):
    while len(input) < 3:
        input += " "
    return input

def main():
    dsn_tns = cx_Oracle.makedsn('LAPTOP-IPLREP3V', '1521', service_name='XE')
    conn = cx_Oracle.connect(user=r'system', password='admin', dsn=dsn_tns)
    print("connected")
    cur = conn.cursor()
    cur.bindarraysize = 1
    cur.setinputsizes(20)
    
    lemmatizer = WordNetLemmatizer()
    
    cont = 0
    a = 0
    
    f = open("Corpus/stop.txt",encoding = "utf8")
    f1 = f.readlines()
    print("S")
    
    for x in f1:
        print (x)
        if(cont >=0):
            w = ''
            for i in x:
                if i != ' ' and i != '\t' and i !='\n':
                    w = w + i
                else:
                    w = esPalabra(w)
                            
        
        rows = [(w.encode("utf-8"))]
        #cur.executemany("insert into corpus_01(palabra1, palabra2, valor) values (:1, :2, :3)", rows)
        #cur.execute("insert into stopwords(sw) values (:1)", rows)
        
        cur.execute("delete from corpus_01 where palabra2 = (:1)", rows)

        cont +=1


    f.close()
    conn.commit()
    conn.close()
    print("F")
     
    
main()



