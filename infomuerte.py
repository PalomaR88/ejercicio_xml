#importar xml
from lxml import etree
doc= etree.parse('xml_muertes.xml')

#función para opción 1
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
        print(lista_causas(doc))
            #print(causa[50])
        print("")
    elif opcion=="2":
        print("")

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


