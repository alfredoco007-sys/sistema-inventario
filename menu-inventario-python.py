array=[]
opcion=input("ingreasa el producto y su precio para finalizar escribe listo")
while opcion>5:
    print("selecciona una opcion: ")
    print("1.-agregar uno o mas productos: ")
    print("2.-mostrar inventario: ")
    print("3.-actualizar y buscar producto: ")
    print("4.-eliminar producto:")
    print("5.-salir de la lista")
    opcion=int(input("INGRESA LA OPCION DESEADA:"))
    opcion=input("ingresa el producto y su precio para finalizar escribe listo")

    if opcion==1:
        producto=input("ingresa tus productos requeridos:")
        array.append(producto)
        print("¿deseas agregar mas productos?")

    elif opcion==2:
        print(f"productos en el inventario {producto}")    

    elif opcion==3:
        producto=input("producto a buscar")
        encontrado=False

        for i in array:
            if i ==producto:
                encontrado=True

        if encontrado:
            print("El producto si esta en la lista")
        else:
            print("el producto no esta en la lista")        

        producto=input("modificar precio: ")
        
    elif opcion==4:
         nombre = input("nombre a eliminar:")
         eliminado=False

         for i in array:
             if i== producto:
                 array.remove(producto)
                 eliminado=True 
                 break
             
         if eliminado:
             print("el producto fue eliminado")

         else:
             print("producto no encontrado")

    elif opcion==5:
         print("Saliendo...  ")
         exit(0)