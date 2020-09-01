import matplotlib.pyplot as plt
import numpy
import csv
import sys
import subprocess
import os
listas_agregadas = [] #guarda los nombres de las listas agregadas
rutas_de_listas = [] #guarda las rutas de las listas
sub_ramas = []
listas_que_repiten = []
nombres_canciones_repetidas = [] #canciones que estan repetidas
nombre_artistas_repetidos = []
nombre_duraciones_repetidas = []
fila_reporte_repetidas = []
fila_no_repetidas = []
datos_reporte = []
datos_csv = []
'''A continuacion se muestran las funciones separadas por funciones '''
'''relacionadas a menu, analisis de lista, reporte y graficas'''
'''Se describe luego del codigo como funciona este'''

#Funciones relacionadas a menu o controlar acciones de usuario
                #FUNCIONES DE MENU
def borrar_pantalla():
    subprocess.call('cls', shell=True)
                    #Para borrar lo que esta en pantalla
def titulo():
    titulo_entrada = 'LISTAS DE MÚSICA'
    print(titulo_entrada.center(50, ' '))

                    #PARA IMPRIMIR TITULO CENTRADO

def menu_principal(): #menu que da opciones de acciones para el usuario
    titulo()
    print('1 Agregar una lista de reproducción')
    print('2 Ver listas ya agregadas ')
    print('3 Generar reporte de listas repetidas')
    respuesta = input('Elija una opción para ejecutar o escriba E para terminar el programa: \n')
    if respuesta == 'E':
        sys.exit()
    else:
        if respuesta == '1':
            borrar_pantalla()
            menu_agregar_lista()
        if respuesta == '2':
            opciones_listas_guardadas()
        if respuesta == '3':
            menu_reporte_repetidas()
        else:
            return 'Entrada no válida'

                            #MENU PRINCIPAL QUE PERMITE IR A OTROS MENUS

def menu_agregar_lista(): #permite al usuario modificar el menu de listas agregando listas nuevas
    titulo()
    while True:
        entrada = input('Ingrese la ruta a la lista de reproducción deseada o 0 para terminar \n')
        if entrada == '0':
            borrar_pantalla()
            print('NO SE HA AGREGADO NINGUNA LISTA')
            break
        if os.path.isfile(entrada) == False: #Si la ruta no lleva a ningun archivo, indicarlo
            print('Archivo no existente')
            pass
        else:
            if os.path.splitext(entrada)[1] != '.xml': #Si el archivo no tiene el formato deseado
                print('Archivo en formato no válido ')
            else:
                nombre = os.path.split(entrada)[1]
                confirmacion = input('¿Desea añadir {} al menú? Escriba 1 '
                'para confirmar. \n'.format((nombre))) #Para confirmar por el usuario
                if confirmacion != '1':
                    borrar_pantalla()
                    pass
                if confirmacion == '1':
                    if nombre in listas_agregadas:
                        print('La lista ya ha sido agregada.') #Para no agregador dos veces una lista al menu
                    else:
                        listas_agregadas.append(nombre) #Para guardar el nombre de las listas agregadas
                        rutas_de_listas.append(entrada) #Para guardar las rutas de las listas
                        borrar_pantalla()
                nueva_lista = input('Pulse 1 si desea agregar otra lista o 0 para imprimir el menú final \n')
                if nueva_lista == '1':
                        continue
                if nueva_lista == '0':
                    borrar_pantalla()
                    listas_guardadas()
                    break

                    #PARA QUE EL USUARIO PUEDA AGREGAR UNA NUEVA LISTA

def regresar_a_menu():
    usuario = input('Escriba M para regresar al menú principal.')
    if usuario == 'M':
        borrar_pantalla()
        menu_principal()
    else:
        pass

                 #PERMITE REGRESAR AL MENU PRINCIPAL PARA ELEGIR OTRA OPCION DE ACCION DE LAS DISPONIBLES

def listas_guardadas(): #imprime el menu de listas guardadas
    titulo()
    print('LAS LISTAS AÑADIDAS SON: ')
    for i in listas_agregadas:
        print(listas_agregadas.index(i) + 1, i)
                        #IMPRIME LAS LISTAS GUARDADAS HASTA EL MOMENTO
def menu_reporte_repetidas():
    exportar_lista(filas_tabla)

def opciones_listas_guardadas():
    print('Estas son las listas agregadas hasta el momento: ')
    listas_guardadas()
    input('Escriba 1 para ver las opciones de acciones para las listas \n')
    if input == '1':
        borrar_pantalla()
        print('OPCIONES PARA ACCIONES CON LISTA')
        print('1 Imprimir tabla de datos')
        print('2 Graficar canciones con sus duraciones')
        print('3 Exportar la información de la lista')
        input('Escriba el número de opción que quiere ejecutar o M para regresar al menú principal')
        if input == 'M':
            menu_principal()
        if input == '1':
            impresion_tabla()
        if input == '2':
            graficar(filas_tabla)
        if input == '3':
            exportar_lista()
    else:
        pass
                         #PERMITE AL USUARIO ELEGIR ENTRE LAS ACCIONES DISPONIBLES A HACER PARA UNA LISTA


        '''FUNCIONES RELACIONADAS A OBTENCION DE DATOS DE LISTAS'''
def analizar_lista(): #forma una lista con los datos de cada cancion
    eleccion = int(input(('Escriba el número de la lista que desea analizar o 0 para terminar \n')))
    if eleccion == 0:
        sys.exit()
#archivo sera el xml que el usuario indicara abrir y archivo_convertido, el xml a document object model dom
    else:
        if eleccion not in range(1,len(rutas_de_listas)+1):
            print('Opción no válida. ')
        else:
            borrar_pantalla()
            archivo = open(r'{}'.format(os.path.abspath(rutas_de_listas[eleccion - 1])))
            lista = archivo.readlines()
            for i in lista:
                if i[8:12] == 'Name':
                    filas_tabla.append((i[26:len(i) - 10]))
                if i[8:14] == 'Artist':
                    filas_tabla.append(i[28:len(i) - 10])
                if i[8:18] == 'Total Time':
                    minutos = i[33]
                    segundos = i[35:37]
                    milisegundos = i[37:39]
                    texto_duracion = '{}:{}:{}'.format(minutos, segundos, milisegundos)
                    filas_tabla.append(texto_duracion)

filas_tabla = []
datos_impresion = []
filas_tabla_impresion = []
                         #OBTIENE UNA LISTA CON LA INFORMACION DEL XML DE LA LISTA DE REPRODUCCION
def impresion_tabla(): #imprime la tabla con los datos de una cancion
    for i in range(0,int((len(filas_tabla)/3))):
        datos_impresion.append(filas_tabla[3*i])
        datos_impresion.append(filas_tabla[3*i+1])
        datos_impresion.append(filas_tabla[3*i+2])
    print('CANCIÓN          ARTISTA             DURACIÓN')
    for i in range(0, int((len(filas_tabla) / 3))):
        fila = filas_tabla[3 * i], filas_tabla[3 * i + 1],filas_tabla[3 * i + 2]
        filas_tabla_impresion.append(fila)
    Tabla = """\
+----------------------------------------------------------------------------------------------+
|           Canción                             Artista                             Duración   |
|----------------------------------------------------------------------------------------------|
{}
+---------------------------------------------------------------------------------------------+\
    """
    Tabla = (Tabla.format('\n'.join("| {:<40} {:<40} {:<5} |".format(*fila)
                                    for fila in filas_tabla_impresion)))
    print(Tabla)
    regresar_a_menu()

                #IMPRIME UNA TABLA CON LOS DATOS DE LA LISTA DE REPRODUCCION

def graficar(lista_elegida): #grafica la lista elegida
    tiempo = []
    borrar_pantalla()
    listas_guardadas()
    eleccion = int(input('Indique qué lista quiere graficar o escriba T para graficarlas todas \n'))
    archivo = open(r'{}'.format(os.path.abspath(rutas_de_listas[eleccion - 1])))
    lista = archivo.readlines()
    final = int((len(lista_elegida)/3))
    for i in range(0,final):
        tiempo.append(lista_elegida[2 + 3*i][0])
    a = int(max(tiempo)) + 1
    bins = [i for i in range(0,a+1)]
    plt.hist(tiempo, bins, histtype = 'bar', rwidth = 0.8, color = 'red')
    plt.title('Canciones en lista de reproducción y su duración')
    plt.xlabel('Duración')
    plt.ylabel('Canciones con dicha duración')
    plt.savefig('Gráfica.pdf')
    plt.show()
    for i in lista:
        if i[8:12] == 'Name':
            filas_tabla.append((i[26:len(i) - 10]))
        if i[8:14] == 'Artist':
            filas_tabla.append(i[28:len(i) - 10])
        if i[8:18] == 'Total Time':
            minutos = i[33:35]
            segundos = i[35:37]
            milisegundos = i[37:39]
            texto_duracion = '{}:{}:{}'.format(minutos, segundos, milisegundos)
            filas_tabla.append(texto_duracion)
    regresar_a_menu()
            #GRAFICA LOS DATOS OBTENIDOS EN LA FUNCION ANTERIOR, LA LISTA CON LA INFO DEL XML DE UNA LISTA DADA

                     #FUNCIONES DE REPORTE Y GRAFICAS, GENERAR CONTENIDO Y MOSTRARLO FUERA



            #GENERA EL LISTADO CON LA INFORMACION DE LAS CANCIONES REPETIDAS EN LISTAS

def escribir_reporte_graficas(informacion_a_graficar):
    archivo = open('reporte.tex', 'w')
    archivo_2 = open('encabezado.tex', 'w')
    archivo_3 = open('paquetes.tex', 'w')
    archivo.write('\\input{paquetes.tex} \n')
    archivo.write('\\begin{document} \n')
    archivo.write('\\begin{titlepage} \n')
    archivo.write('\\input{encabezado.tex}\n')
    archivo.write('\\section*{Datos}\n')
    archivo.write('\\begin{longtable}{||c|c|c|p{4cm}||}\n')
    archivo.write('\\hline \n')
    archivo.write('\\hline \n')
    archivo.write('Canción & Artista & Tiempo & Listas de reproduccion en las\
        que aparece \\\\ \n')
    archivo.write('\\hline \n')
    for i in informacion_a_graficar:
        LRep = ''
        for j in i[3]:
            if i != i[3][len(i[3]) - 1]:
                LRep += i + ','
            elif i== i[3][len(i[3]) - 1]:
                LRep += i
        row = '{} & {} & {} & {} \\\\ \n'
        archivo.write(row.format(i[0], i[1], i[2], LRep))
        archivo.write('\\hline \n')
    archivo.write('\\hline \n')
    archivo.write('\\hline \n')
    archivo.write('\\end{longtable}\n')
    archivo.write('\\section*{Grafica} \n')
    archivo.write('\\begin{figure}[H] \n')
    archivo.write('\\centering \n')
    archivo.write('\\includegraphics[scale=0.7]{histograma.pdf} \n')
    archivo.write('\\caption{Estadisticas} \n')
    archivo.write('\\end{figure} \n')
    archivo.write('\\end{titlepage}\n')
    archivo.write('\\end{document}')
    archivo.close()
    subprocess.run('pdfLatex "reporte.tex"', shell=True)
    subprocess.run('del "Graficas.aux"', shell=True)
    subprocess.run('del "Graficas.log"', shell=True)
    subprocess.run('del "Graficas.out"', shell=True)
    borrar_pantalla()
    regresar_a_menu()
                # ESCRIBE UN REPORTE DE LAS LISTAS REPETIDAS

def exportar_lista(lista):
    with open('Lista en CSV.csv', 'w') as csvfile:
        fieldnames = ['Cancion', 'Artista', 'Duracion']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(0, int((len(filas_tabla) / 3))):
            cancion = []
            cancion.append(filas_tabla[3 * i])
            cancion.append(filas_tabla[3 * i + 1])
            cancion.append(filas_tabla[3 * i + 2])
            datos_csv.append(cancion)
        for i in range(0, len(datos_csv)):
            writer.writerow({'Cancion': datos_csv[i][0], 'Artista': datos_csv[i][1], 'Duracion': datos_csv[i][2]})
    regresar_a_menu()
                    #EXPORTA LA LISTA QUE ESTA SIENDO ANALIZADA A FORMATO CSV

def escribir_reporte_repetidas():
    pass

'''def escribir_reporte_repetidas(datos):
    archivo = open("reporte.tex", "w")
    archivo.write("\\documentclass{book}\n")
    archivo.write("\\usepackage[spanish]{babel}\n")
    archivo.write("\\usepackage[utf8]{inputenc}\n")
    archivo.write("\\usepackage[T1]{fontenc}\n")
    archivo.write("\\begin{document}\n")
    archivo.write("\\section*{Reporte de canciones}\n")
    archivo.write("\\begin{tabular}{|c|c|c|p{6cm}|}\n")
    archivo.write("\\hline\n")
    archivo.write("Nombre de la canción & Artista & Duración & Nombres de las listas en las que aparece \\\\ \n")
    archivo.write("\\hline\n")
    for dato in datos:
        listas = ""
        i = 0
        for lista in dato[3]:
            listas += lista
            i += 1
            if i < len(dato[3]):
                listas += ", "
        archivo.write("{} & {} & {} & {} \\\\ \n".format(dato[0], dato[1], dato[2], listas))
        archivo.write("\\hline\n")
    archivo.write("\\end{tabular}\n")
    archivo.write("\\end{document}\n")
    archivo.close()
    subprocess.call(["pdflatex", "reporte.tex"])
    subprocess.call(["rm", "reporte_repetidas.log", "reporte.aux"]) '''


                #ESCRIBE EL REPORTE DE LAS LISTAS REPETIDAS
                #COLOQUE LO ANERIOR COMO COMENTARIO PORQUE NO ACABE ESTA PARTE

def practica():
    menu_agregar_lista()
    analizar_lista()
    impresion_tabla()
    regresar_a_menu()

practica()