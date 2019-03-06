#importar xml
from lxml import etree
doc= etree.parse('xml_muertes.xml')

#función para opción 1 (primera parte)
def crear_lista(doc):
    lista=[]
    for i in lista_causas(doc):
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

#función para opción 1 (segunda parte)
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

#función para opción 2 (primera parte)
def buscar_causa(doc, numero):
    causa=crear_lista(doc)[numero]
    return causa

#funcion para opción 2(segunda parte)
def sumar(doc, numero):
    x=[]
    causa=crear_lista(doc)[numero]
    suma=doc.xpath("/MORATLIDAD/PROVINCIAS/PROVINCIA/MUNICIPIOS/MUNICIPIO/CAUSAS_CCV/CAUSA_CCV[/DESC_CAUSA_CCV/text()='%s']/GENEROS/GENERO/FALLECIDOS_GENERO/text()" %(causa))
    for i in suma:
        x.append(i)    
    return x

    #suma=doc.xpath("/MORATLIDAD/PROVINCIAS/PROVINCIA/MUNICIPIOS/MUNICIPIO/CAUSAS_CCV/CAUSA_CCV[DESC_CAUSA_CCV='%s']/GENEROS/GENERO/FALLECIDOS_GENERO/text()"%(causa))
    #return suma




#menu principal
while True:
    print('''1.- Listar todas las causas mortales
2.- Contar las muertes por una causa concreta
3.- Filtrar muertes por provincia
4.- Filtrar causas por edad y género
5.- Comparar provincias por causas
0.- Salir''')
    opcion=input("Opción: ")
    print("")
    if opcion=="1":
        for i in range(len(crear_lista(doc))):
            print(i, "-", crear_lista(doc)[i])
        print("")
    elif opcion=="2":
        numero=int(input("Introduce el número que corresponde a la causa (opción 1): "))
        print("")
        print(buscar_causa(doc, numero))
        print("")
        print(sumar(doc, numero))

    elif opcion=="3":
        print("")

    elif opcion=="4":
        print("")

    elif opcion=="5":
        print("")

    elif opcion=="0":
        print("Adios")
        break
    else:
        print("Lo siento, no hay ninguna opción disponible")
        print(" ")

#strip() para espacios
