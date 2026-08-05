import random
ids = []
nombres = []
contenidos = []
categorias = []
lineas = []
fechas = []
ubicaciones = []
estados = []
observaciones = []
#-----------------------------------#
#--|menu_principal_archivador_txt|--#
#-----------------------------------#
while True:
    print("menu principal archivador txt")
    print("1) registrar archivo")
    print("2) editar archivo")
    print("3) eliminar archivo")
    print("4) buscar archivo")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #-----------------------#
    #--|registrar_archivo|--#
    #-----------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_archivo = 1
        else:
            id_archivo = ids[-1] + 1
        nombre = input("nombre del archivo (.txt): ")
        contenido = input("contenido: ")
        categoria = input("categoría: ")
        cantidad_lineas = int(input("cantidad de líneas: "))
        fecha = input("fecha de creación: ")
        ubicacion = input("ubicación o carpeta: ")
        estado = input("estado (activo o archivado): ")
        observacion = input("observación: ")
        ids.append(id_archivo)
        nombres.append(nombre)
        contenidos.append(contenido)
        categorias.append(categoria)
        lineas.append(cantidad_lineas)
        fechas.append(fecha)
        ubicaciones.append(ubicacion)
        estados.append(estado)
        observaciones.append(observacion)
        print("archivo txt registrado correctamente.")
        print("id:", id_archivo)
    #--------------------#
    #--|editar_archivo|--#
    #--------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen archivos registrados.")
        else:
            print("editar archivo")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]} | {estados[i]}")
            id_buscar = int(input("ingrese la id del archivo: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {nombres[posicion]} | {categorias[posicion]}")
                nombres[posicion] = input("nuevo nombre: ")
                contenidos[posicion] = input("nuevo contenido: ")
                categorias[posicion] = input("nueva categoría: ")
                lineas[posicion] = int(input("nueva cantidad de líneas: "))
                fechas[posicion] = input("nueva fecha: ")
                ubicaciones[posicion] = input("nueva ubicación: ")
                estados[posicion] = input("nuevo estado: ")
                observaciones[posicion] = input("nueva observación: ")
                print("archivo actualizado correctamente.")
            else:
                print("id no encontrada.")
    #----------------------#
    #--|eliminar_archivo|--#
    #----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen archivos registrados.")
        else:
            print("eliminar archivo")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]} | {estados[i]}")
            id_buscar = int(input("ingrese la id del archivo: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del archivo")
                print(f"{ids[posicion]} | {nombres[posicion]} | {categorias[posicion]}")
                respuesta = input("¿desea eliminar este archivo? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    contenidos.pop(posicion)
                    categorias.pop(posicion)
                    lineas.pop(posicion)
                    fechas.pop(posicion)
                    ubicaciones.pop(posicion)
                    estados.pop(posicion)
                    observaciones.pop(posicion)
                    print("archivo eliminado correctamente.")
                else:
                    print("el archivo no fue eliminado.")
            else:
                print("id no encontrada.")
    #--------------------#
    #--|buscar_archivo|--#
    #--------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen archivos registrados.")
        else:
            print("buscar archivo")
            id_buscar = int(input("ingrese la id del archivo: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("contenido:", contenidos[posicion])
                print("categoría:", categorias[posicion])
                print("cantidad de líneas:", lineas[posicion])
                print("fecha:", fechas[posicion])
                print("ubicación:", ubicaciones[posicion])
                print("estado:", estados[posicion])
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #--------------------#
    #--|lista_de_datos|--#
    #--------------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen archivos registrados.")
        else:
            activos = 0
            archivados = 0
            total_lineas = 0
            programacion = 0
            personal = 0
            universidad = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]} | {lineas[i]} líneas | {estados[i]}")
                total_lineas += lineas[i]
                if estados[i].lower() == "activo":
                    activos += 1
                elif estados[i].lower() == "archivado":
                    archivados += 1
                if categorias[i].lower() == "programación":
                    programacion += 1
                elif categorias[i].lower() == "personal":
                    personal += 1
                elif categorias[i].lower() == "universidad":
                    universidad += 1
            print("estadísticas archivador txt")
            print("cantidad de archivos:", len(ids))
            print("archivos activos:", activos)
            print("archivos archivados:", archivados)
            print("total de líneas almacenadas:", total_lineas)
            print("categoría programación:", programacion)
            print("categoría personal:", personal)
            print("categoría universidad:", universidad)
            posicion = random.randint(0, len(ids) - 1)
            print("archivo txt seleccionado")
            print("id:", ids[posicion])
            print("nombre:", nombres[posicion])
            print("contenido:", contenidos[posicion])
            print("categoría:", categorias[posicion])
            print("cantidad de líneas:", lineas[posicion])
            print("fecha:", fechas[posicion])
            print("ubicación:", ubicaciones[posicion])
            print("estado:", estados[posicion])
            print("observación:", observaciones[posicion])
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el archivador txt.")
        break
    else:
        print("opción no válida.")