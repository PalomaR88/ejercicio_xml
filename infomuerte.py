#importar xml
from lxml import etree
doc= etree.parse('xml_muertes.xml')

#funcion que devuelve una lista (doc) con las tildes y la Ñ
def imprimir_por_pantalla(doc):
    lista=[]
    for i in doc:
        causa=str(i).strip()
        while 'Ã\x93' in causa:
            causa=causa.replace('Ã\x93','Ó')
        while 'Ã\x8d' in causa:
            causa=causa.replace('Ã\x8d','Í')  
        while 'Ã\x81' in causa:
            causa=causa.replace('Ã\x81','Á')
        while 'Ã\x9a' in causa:
            causa=causa.replace('Ã\x9a','Ú')
        while 'Ã\x89' in causa:
            causa=causa.replace('Ã\x89','É')
        while 'Ã\x91' in causa:
            causa=causa.replace('Ã\x91','Ñ')
        lista.append(causa)
    return lista

#función para la opción 1
def opcion1(doc):
    dato=lista_causas(doc)
    dato2=imprimir_por_pantalla(dato)
    return dato2

#función que introduce el doc y devuelve las causas sin repetir
def lista_causas(doc):
    lista=[]
    causas=doc.xpath("/MORTALIDAD/PROVINCIAS/PROVINCIA/MUNICIPIOS/MUNICIPIO/CAUSAS_CCV/CAUSA_CCV/DESC_CAUSA_CCV/text()")
    for i in lista_sin_repetir(causas):
        lista.append(i)
    return lista

#función que introduces una lista y la devuelve sin
#valores repetidos
def lista_sin_repetir(dat_xp):
    lista=[]
    for i in range(len(dat_xp)):
        existe=False
        for x in range(len(lista)):
            if dat_xp[i]==lista[x]:
                existe=True
        if existe==False:
            lista.append(dat_xp[i])
    return lista

#funcion que convalida, introduce el máx y devuelve una nueva opcion
def convalidar(dato, num_max):
    while True:
        numero=int(input("Introduce el número que corresponde %s" %(dato)))
        if numero>(num_max):
            print("ERROR. El número debe ser entre 0  y", (num_max))
        else:
            break
    return numero

#funcion que introduce un numero y devuelve una causa
def buscar_causa(doc, numero):
    causas=[]
    imprimir=[]
    for i in lista_causas(doc):
        causas.append(i)
    for i in imprimir_por_pantalla(causas):
        imprimir.append(i)
    return imprimir[numero]

#funcion que introduces recibe un numero que indica la causa
#y devuelve la suma de todos los fallecidos por esa causa
def sumar(doc, numero):
    resultado=[]
    causa=lista_causas(doc)[numero]
    dato=doc.xpath("/MORTALIDAD/PROVINCIAS/PROVINCIA/MUNICIPIOS/MUNICIPIO/CAUSAS_CCV/CAUSA_CCV[DESC_CAUSA_CCV='%s']/FALLECIDOS_CAUSA_CCV/text()" %(causa))
    for i in dato:
        x=i.strip()
        n_suma=int(x)
        resultado.append(n_suma)    
    return sum(resultado)

#funcion que devuelve la una lista con las provincias para 
# imp
def lista_provincias_imp(doc):
    provincias=[]
    prov=lista_prov(doc)
    prov_imp=imprimir_por_pantalla(prov)
    for i in prov_imp:
        provincias.append(i)
    return provincias

#funcion que devuelve la lista de las provincias, no para
#imprimir por pantalla
def lista_prov(doc):
    provincias=[]
    prov=doc.xpath("/MORTALIDAD/PROVINCIAS/PROVINCIA/DESC_PROVINCIA/text()")
    for i in prov:
        provincias.append(i)
    return provincias    

#funcion que devuelve una lista con los municipios sin
#imprimir por pantalla, eligiendo antes una provincia a 
#través de un numero
def lista_municipios(doc,num):
    municipios=[]
    prov=eleccion_prov(doc,num)
    mun=doc.xpath("/MORTALIDAD/PROVINCIAS/PROVINCIA[DESC_PROVINCIA='%s']/MUNICIPIOS/MUNICIPIO/DESC_MUNICIPIO/text()" %(prov))
    for i in mun:
        municipios.append(i)
    return municipios

#funcion que devuelve una lista con los municipios para 
#imprimir por pantalla, eligiendo antes una provincia a 
#través de un numero
def lista_municipios_imp(doc,num):
    provincias=[]
    prov=lista_municipios(doc,num)
    mun=imprimir_por_pantalla(prov)
    for i in prov:
        provincias.append(i.strip())
    return provincias

#funcion que da un numero y devuelve una provincia no para
#imprimir por pantalla
def eleccion_prov(doc, numero):
    provincias=[]
    prov=lista_prov(doc)
    for i in prov:
        i=str(i)
        provincias.append(i)
    provincia=provincias[numero]
    return provincia

#funcion que con el numero de provincia y municipio
#devuelve las muertes
def muertes_mun(doc, numero, num_mun):
    muertes=[]
    municipio=lista_municipios(doc,numero)[num_mun]
    dato=doc.xpath("//MUNICIPIO[DESC_MUNICIPIO='%s']/FALLECIDOS_MUNICIPIO/text()" %municipio)
    return dato[0]

#función que con la edad y el genero y la provincia devuelve 
# todas las muertes
def edad_genero(doc, edad, genero, numero):
    listag=[]
    prov=lista_prov(doc)[numero]
    causas=lista_causas(doc)
    causas_imp=imprimir_por_pantalla(causas)
    gen=eleccion_gen(doc,genero)
    rango_edad=eleccion_edad(doc,edad)
    for i in range(len(causas)):
        listap=[]
        muertes=doc.xpath("/MORTALIDAD/PROVINCIAS/PROVINCIA[DESC_PROVINCIA='%s']/MUNICIPIOS/MUNICIPIO/CAUSAS_CCV/CAUSA_CCV[DESC_CAUSA_CCV='%s']/GENEROS/GENERO[COD_GENERO='%s']/EDADES/EDAD[RANGO='%s']/NUM_FALLECIDOS/text()"%(prov,causas[i],gen,rango_edad))
        for x in muertes:
            m_imp=int(x.strip())
            if m_imp>0:
                listap.append(causas_imp[i].strip())
                listap.append(m_imp)
                listag.append(listap)
    return listag

#con una letra por teclado devuelve la correspondencia del
#genero en la tabla
def eleccion_gen(doc,genero):
    gen=[]
    dato_genero=doc.xpath("//CAUSAS_CCV/CAUSA_CCV/GENEROS/GENERO/COD_GENERO/text()")
    for i in lista_sin_repetir(dato_genero):
        if i.strip()==genero.upper():
            gen.append(i)
    return gen[0]

#funcion que con una edad devuelve el rango en el xml
def eleccion_edad(doc,edad):
    lista=[]
    lista_edad=[]
    muertes=doc.xpath("//CAUSAS_CCV/CAUSA_CCV/GENEROS/GENERO/EDADES/EDAD/RANGO/text()")
    for i in lista_sin_repetir(muertes):
        n=i.strip()
        if n=='> 84':
            if edad>84:
                lista_edad.append(i)
        elif n=='0':
            if edad==0:
                lista_edad.append(i)
        elif n!='< 84' and n!='0':
            n1=int(n[0:2])
            n2=int(n[5:7])
            if edad>=n1 and edad<n2:
                lista_edad.append(i)
    return lista_edad[0]

#función base para el punto 5
def opcion5(doc,n1, mun1, n2, mun2):
    lista=[]
    m1=lista_municipios(doc,n1)[mun1]
    m2=lista_municipios(doc,n2)[mun2]
    datos=comp_mun(doc,m1,m2)
    return datos
    
#funcion para recuperar los datos de ambos municipios
def comp_mun(doc,m1,m2):
    listag=[]
    causas=lista_causas(doc)
    causas_imp=imprimir_por_pantalla(causas)
    for i in range(len(causas)):
        lista=[]
        muertes_causas1=doc.xpath("//MUNICIPIO[DESC_MUNICIPIO='%s']/CAUSAS_CCV/CAUSA_CCV[DESC_CAUSA_CCV='%s']/FALLECIDOS_CAUSA_CCV/text()"%(m1,causas[i]))
        lista.append(causas_imp[i])
        for x in muertes_causas1:
            muertes_m1=muertes_causas1[0]
        muertes_causas2=doc.xpath("//MUNICIPIO[DESC_MUNICIPIO='%s']/CAUSAS_CCV/CAUSA_CCV[DESC_CAUSA_CCV='%s']/FALLECIDOS_CAUSA_CCV/text()"%(m2,causas[i]))      
        for x in muertes_causas2:
            muertes_m2=muertes_causas2[0]
        numero1=int(muertes_m1.strip())
        numero2=int(muertes_m2.strip()) 
        lista.append(numero1)
        lista.append(numero2)
        listag.append(lista)
    return listag


#menu principal
while True:
    print('''
1.- Listar todas las causas mortales
2.- Contar las muertes por una causa concreta
3.- Filtrar muertes por municipio
4.- Filtrar causas por edad y género
5.- Comparar municipios por causas
0.- Salir''')
    opcion=input("Opción: ")
    print("")
    if opcion=="1":
        for i in range(len(opcion1(doc))):
            print(i, "-", opcion1(doc)[i])        
        print("")
        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")

    elif opcion=="2":
        numero=convalidar("a la causa: ",80)  
        print(" ")
        print("Causa: ", buscar_causa(doc, numero))
        print("Resultado: ", sumar(doc, numero))
        print(" ")
        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")

    elif opcion=="3":
        print("")
        print("Provincias disponibles: ")
        for i in range(len(lista_provincias_imp(doc))):
            print(i, "-", lista_provincias_imp(doc)[i])
        nume=(len(lista_provincias_imp(doc))-1)
        numero=convalidar("a la provincia: ",nume)
        print("")
        print("Municipios disponibles: ")
        for i in range(len(lista_municipios_imp(doc, numero))):
            print(i, "-", lista_municipios_imp(doc, numero)[i])
        nume2=(len(lista_municipios_imp(doc,numero))-1)
        num_mun=convalidar("al municipio: ",nume2)
        print("Resultado ->",muertes_mun(doc, numero, num_mun).strip())
        print("")
        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")

    elif opcion=="4":
        edad=convalidar("a la edad: ", 120)
        while True:
            genero=str(input("Introduce el género (M: mujer/H: hombre): "))
            if genero.upper()!="M" and genero.upper()!="H":
                print("ERROR. Debe indicar M o H")
            else:
                break  
        print("")
        print("Provincias disponibles: ")
        for i in range(len(lista_provincias_imp(doc))):
            print(i, "-", lista_provincias_imp(doc)[i])
        numero=convalidar("a la provincia: ",len(lista_provincias_imp(doc))-1)    
        print(" ")     
        for i in edad_genero(doc, edad, genero,numero):
            for x in range(len(i)):
                if x%2==0:
                    print("Enfermedad ->", i[x])
                else:
                    print("Fallecidos ->", i[x])
                    print("")
        print("")
        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")

    elif opcion=="5":
        for i in range(len(lista_provincias_imp(doc))):
            print(i, "-", lista_provincias_imp(doc)[i])
        n1=convalidar("a la primera provincia: ",len(lista_provincias_imp(doc))-1)
        for i in range(len(lista_municipios_imp(doc, n1))):
            print(i, "-", lista_municipios_imp(doc, n1)[i])
        mun1=convalidar("al municipio: ",len(lista_municipios_imp(doc,n1))-1)
        
        
        for i in range(len(lista_provincias_imp(doc))):
            print(i, "-", lista_provincias_imp(doc)[i])
        n2=convalidar("a la segunda provincia: ",len(lista_provincias_imp(doc))-1)
        for i in range(len(lista_municipios_imp(doc, n2))):
            print(i, "-", lista_municipios_imp(doc, n2)[i])
        mun2=convalidar("al municipio: ",len(lista_municipios_imp(doc,n2))-1)
        municipio1=lista_municipios_imp(doc,n1)[mun1]
        municipio2=lista_municipios_imp(doc,n2)[mun2]
        for i in opcion5(doc,n1, mun1, n2, mun2):
            for x in opcion5(doc,n1, mun1, n2, mun2):
                print("Causa ->",x[0])
                print("         ",municipio1,"->",x[1])
                print("         ",municipio2,"->",x[2])
             
    elif opcion=="0":
        print("Adios")
        break
    else:
        print("Lo siento, no hay ninguna opción disponible")
        print(" ")
