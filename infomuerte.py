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
    for i in range(len(causas)):
        existe=False
        for x in range(len(lista)):
            if causas[i]==lista[x]:
                existe=True
        if existe==False:
            lista.append(causas[i])
    return lista

#funcion que convalida, introduce el máx y devuelve una nueva opcion
def convalidar(dato, num_max):
    while True:
        numero=int(input("Introduce el número que corresponde %s" %(dato)))
        if numero>num_max:
            print("ERROR. El número debe ser entre 0  y", num_max)
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

#función que con la edad y el genero devuelve todas las muertes y 
def edad_genero(doc, edad, genero):



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
        numero=convalidar("a la provincia: ",len(lista_provincias_imp(doc)))
        print("")
        print("Municipios disponibles: ")
        for i in range(len(lista_municipios_imp(doc, numero))):
            print(i, "-", lista_municipios_imp(doc, numero)[i])
        num_mun=convalidar("al municipio: ",len(lista_municipios_imp(doc,numero)))
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
        numero=convalidar("a la provincia: ",len(lista_provincias_imp(doc)))    
        print(" ")     
        for i in edad_genero(doc, edad, genero):
            for x in range(len(i)):
                if x/2==0:
                    print("Enfermedad ->", i[x])
                else:
                    print("Fallecidos ->", i[x])
                    print("")
        print("")
        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")
#
#    elif opcion=="5":
#        for i in range(len(provincias(doc))):
#            print(i, "-", provincias(doc)[i])
#        numero=int(input("Introduce el número que corresponde a la provincia: "))
#        print("")
#        print("Municipios disponibles: ")
#        for i in range(len(municipios(doc, numero))):
#            print(i, "-", municipios(doc, numero)[i])
#        mun1=int(input("Introcuduce el número que corresponde al primer municipio: "))
#        for i in range(len(provincias(doc))):
#            print(i, "-", provincias(doc)[i])
#        numero=int(input("Introduce el número que corresponde a la provincia: "))
#        print("")
#        print("Municipios disponibles: ")
#        for i in range(len(municipios(doc, numero))):
#            print(i, "-", municipios(doc, numero)[i])
#        mun2=int(input("Introcuduce el número que corresponde al segundo municipio: "))
#       
#        print(comparacion(doc,mun1,mun2))        
#
#
#        print("")
#        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")
#
    elif opcion=="0":
        print("Adios")
        break
    else:
        print("Lo siento, no hay ninguna opción disponible")
        print(" ")
        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")
