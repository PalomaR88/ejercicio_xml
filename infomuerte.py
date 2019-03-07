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
    resultado=[]
    causa=lista_causas(doc)[numero]
    dato=doc.xpath("/MORTALIDAD/PROVINCIAS/PROVINCIA/MUNICIPIOS/MUNICIPIO/CAUSAS_CCV/CAUSA_CCV[DESC_CAUSA_CCV='%s']/FALLECIDOS_CAUSA_CCV/text()" %(causa))
    for i in dato:
        x=i.strip()
        n_suma=int(x)
        #x=i.strip
        #n_suma=int(i).strip
        resultado.append(n_suma)    
    return sum(resultado)

#función opción 3 (primera parte)
def provincias(doc):
    provincias=[]
    prov=doc.xpath("/MORTALIDAD/PROVINCIAS/PROVINCIA/DESC_PROVINCIA/text()")
    for i in prov:
        i=str(i).strip()
        while 'Ã\x93' in i:
            i=i.replace('Ã\x93','Ó')
        while 'Ã\x8d' in i:
            i=i.replace('Ã\x8d','Í')  
        while 'Ã\x81' in i:
            i=i.replace('Ã\x81','Á')
        while 'Ã\x9a' in i:
            i=i.replace('Ã\x9a','Ú')
        while 'Ã\x89' in i:
            i=i.replace('Ã\x89','É')
        while 'Ã\x91' in i:
            i=i.replace('Ã\x91','Ñ')
        provincias.append(i)
    return provincias

#función opción 3 (segunda parte)
def muertes_provincias(doc, numero):
    provincias=[]
    prov=doc.xpath("/MORTALIDAD/PROVINCIAS/PROVINCIA/DESC_PROVINCIA/text()")
    for i in prov:
        i=str(i)
        provincias.append(i)
    provincia=provincias[numero]
    return provincia

#función opción 3 (tercera parte)
def municipios(doc,numero):
    municipios=[]
    prov=muertes_provincias(doc, numero)
    mun=doc.xpath("/MORTALIDAD/PROVINCIAS/PROVINCIA[DESC_PROVINCIA='%s']/MUNICIPIOS/MUNICIPIO/DESC_MUNICIPIO/text()" %(prov))
    for i in mun:
        i=str(i).strip()
        while 'Ã\x93' in i:
           i=i.replace('Ã\x93','Ó')
        while 'Ã\x8d' in i:
            i=i.replace('Ã\x8d','Í')  
        while 'Ã\x81' in i:
            i=i.replace('Ã\x81','Á')
        while 'Ã\x9a' in i:
            i=i.replace('Ã\x9a','Ú')
        while 'Ã\x89' in i:
            i=i.replace('Ã\x89','É')
        while 'Ã\x91' in i:
            i=i.replace('Ã\x91','Ñ')
        municipios.append(i)
    return municipios


#función opción 3 (cuarta parte)
def muertes_mun(doc, numero, num_mun):
    municipios=[]
    muertes=[]
    prov=muertes_provincias(doc, numero)
    mun=doc.xpath("/MORTALIDAD/PROVINCIAS/PROVINCIA[DESC_PROVINCIA='%s']/MUNICIPIOS/MUNICIPIO/DESC_MUNICIPIO/text()" %(prov))
    for i in mun:
        i=str(i)
        municipios.append(i)
    municipio=municipios[num_mun]
    dato=doc.xpath("//MUNICIPIO[DESC_MUNICIPIO='%s']/FALLECIDOS_MUNICIPIO/text()" %municipio)
    return dato[0].strip()

#función opción 4 (primera parte)
def edad_genero(doc, edad, genero):
    
    listag=[]
    #causas=crear_lista(doc)
    for causa in range(len(lista_causas(doc))):
        listap=[]
        dato_genero=doc.xpath("//CAUSAS_CCV/CAUSA_CCV[DESC_CAUSA_CCV='%s']/GENEROS/GENERO/COD_GENERO/text()" %(lista_causas(doc)[causa]))
        for i in dato_genero:
            gen_i=i.strip()
            if gen_i==genero.upper():
                dato_edad=doc.xpath("//CAUSAS_CCV/CAUSA_CCV[DESC_CAUSA_CCV='%s']/GENEROS/GENERO[COD_GENERO='%s']/EDADES/EDAD/RANGO/text()"%(lista_causas(doc)[causa],i))
                for x in dato_edad:
                    muertes=doc.xpath("//CAUSAS_CCV/CAUSA_CCV[DESC_CAUSA_CCV='%s']/GENEROS/GENERO[COD_GENERO='%s']/EDADES/EDAD[RANGO='%s']/NUM_FALLECIDOS/text()"%(lista_causas(doc)[causa],i,x))
                    for t in muertes:
                        edad_i=x.strip()
                        res_muertes=t.strip()
                        if res_muertes!='0':
                            if edad_i=='> 84':
                                if edad>84:
                                    listap.append(crear_lista(doc)[causa])
                                    lista.append(res_muertes)
                            elif edad_i=='0':
                                if edad==0:
                                    listap.append(crear_lista(doc)[causa])
                                    lista.apend(res_muertes)
                            else:
                                n1=int(edad_i[0:2])
                                n2=int(edad_i[5:7])
                                if n1<=edad and n2>edad:
                                    listap.append(crear_lista(doc)[causa])
                                    lista.append(res_muertes)
                            listag.append(listap)
    return listag

#def nombreprovypob(doc):
#    lista=[]
#    nombre=nombreprovincias(doc)
#    for provincias in doc.xpath('//provincia'):
#        num_loc=provincias.xpath('count(./localidades/localidad)')
#        lista.append(int(num_loc))
#    return zip(nombre,lista)




#menu principal
while True:
    print('''
1.- Listar todas las causas mortales
2.- Contar las muertes por una causa concreta
3.- Filtrar muertes por municipio
4.- Filtrar causas por edad y género
5.- Comparar provincias por causas
0.- Salir''')
    opcion=input("Opción: ")
    print("")
    if opcion=="1":
        for i in range(len(crear_lista(doc))):
            print(i, "-", crear_lista(doc)[i])        
        print("")
        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")

    elif opcion=="2":
        numero=int(input("Introduce el número que corresponde a la causa (opción 1): "))
        print(" ")
        print("Causa: ", buscar_causa(doc, numero))
        print("Resultado: ", sumar(doc, numero))
        print(" ")
        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")

    elif opcion=="3":
        print("")
        print("Provincias disponibles: ")
        for i in range(len(provincias(doc))):
            print(i, "-", provincias(doc)[i])
        numero=int(input("Introduce el número que corresponde a la provincia: "))
        print("")
        print("Municipios disponibles: ")
        for i in range(len(municipios(doc, numero))):
            print(i, "-", municipios(doc, numero)[i])
        num_mun=int(input("Introcuduce el número que corresponde al municipio: "))
        print("Resultado ->",muertes_mun(doc, numero, num_mun))
        print("")
        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")

    elif opcion=="4":
        edad=int(input("Introduce la edad: "))
        while True:
            genero=str(input("Introduce el género (M: mujer/H: hombre): "))
            if genero.upper()!="M" and genero.upper()!="H":
                print("ERROR. Debe indicar M o H")
            else:
                break           
        print(edad_genero(doc, edad, genero))
        print("")
        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")

    elif opcion=="5":
        print("")
        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")

    elif opcion=="0":
        print("Adios")
        break
    else:
        print("Lo siento, no hay ninguna opción disponible")
        print(" ")
        tecla= input("PRESIONA UNA INTRO PARA CONTINUAR")

#strip() para espacios
