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
    cur.setinputsizes(14,14,int)
    
    lemmatizer = WordNetLemmatizer()
    
    cont = 0
    a = 0
    ################################################
    ################################################
    ################aqui############################
    f = open("Corpus/14.txt",encoding = "utf8")
    ################################################
    ################################################
    ################################################
    f1 = f.readlines()
    print("S")
    
    for x in f1:
        if(cont >=0):
            w = ''
            y = ''
            z = ''
            for i in x:
                    if a == 0:
                        if i != ' ' and i != '\t' and i !='\n':
                            w = w + i
                        else:
                            w = esPalabra(w)
                            try:
                                g = lemmatizer.lemmatize(w)
                                #primeros_caracteres.append(g)
                                a = 1
                            except:
                                a=0
                                break
                    elif a == 1:
                        if i != ' ' and i != '\t'and i != '\n':
                            y = y + i
                        else:
                            y = esPalabra(y)
                            try:
                                g = lemmatizer.lemmatize(y)
                                a = 2
                                #segundos_caracteres.append(g)                            
                            except:
                                #primeros_caracteres.pop()
                                w = ''
                                a=0
                                break
                    elif a == 2:
                        if i != ' ' and i != '\t'and i != '\n':
                            z = z + i
                        else:
                            a = 0
                            z = int(z)
                            #valores.append(z)
            rows = [(w.encode("utf-8"),y.encode("utf-8"),z)]
            
            ################################################
            ################################################
            ###################################aqui#########
            cur.executemany("insert into corpus_14(palabra1, palabra2, valor) values (:1, :2, :3)", rows)
            ################################################
            ################################################
            ################################################
            
            
            #print("estamos en la posicion ")
            #print(cont)
            #print("w:"+w.encode("utf-8") +"y:"+y.encode("utf-8"))1
            #cont += 1
            if cont % 1000000 == 0:
                print (cont)
                
        cont +=1
    """print("primeros caracteres:")
    for i in primeros_caracteres:
        print(i)
    print("segundos caracteres:")
    for i in segundos_caracteres:
        print(i)
    print("valores:")
    for i in valores:
        print(i)"""
    f.close()
    conn.commit()
    conn.close()
    #for i in primeros_caracteres:
     #  i = lemmatizer.lemmatize(i)
    print("F")
     
    
main()



#c.execute('select * from alumnos') 
#for row in cur:
#    print (row[0], '-', row[1])



