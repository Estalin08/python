
nombre_pasajeros=[]
apellido_pasajeros=[]
id_pasajeros=[]
ciudad_pasajeros=[]
departamentos_pasajeros=[]

tupla_nombre_pasajeros=()
tupla_apellido_pasajeros=()
tupla_id_pasajeros=()
tupla_ciudad_pasajeros=()
tupla_departamento_pasajeros=()


print(" ")
print("BIENVENIDO A VUELOS S.A.S")
print(" ")
print("DIGITE 1: PARA AGREGAR PASAJEROS A LA LISTA DE VUELOS \nDIGITE 2: PARA AGREGAR CIUDADES \nDIGITE 3: PARA CONSULTAR A QUE CIUDAD VIAJA ALGUN PASAJERO \nDIGITE 4: PARA CONSULTAR LA CANTIDAD DE PASAJEROS POR CIUDAD \nDIGITE 5: PARA CONSULTAR LA CANTIDAD DE PASAJEROS POR DEPARTAMENTOS \nDIGITE 6: PARA CONSULTAR LOS PASAJEROS QUUE VIAJAN POR DEPARTAMENTO \nDIGITE 7: PARA SALIR")
print(" ")
opcion=(input("RTA: "))
print(" ")

while opcion!= "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion!= "6" and opcion != "7":
    print("ERROR OPCION INCORRECTA")
    print(" ")
    print("DIGITE 1: PARA AGREGAR PASAJEROS A LA LISTA DE VUELOS \nDIGITE 2: PARA CONSULTAR A QUE CIUDAD VIAJA ALGUN PASAJERO \nDIGITE 3: PARA CONSULTAR LA CANTIDAD DE PASAJEROS POR CIUDAD \nDIGITE 4: PARA CONSULTAR LA CANTIDAD DE PASAJEROS POR DEPARTAMENTOS \nDIGITE 5: PARA CONSULTAR LOS PASAJEROS QUUE VIAJAN POR DEPARTAMENTO \nDIGITE 6: PARA SALIR")
    print(" ")
    opcion=(input("RTA: "))



if opcion=="1":

    print("INGRESE LOS DATOS DEL PASAJERO")

    nombre=str(input("Nombre: ")).lower()

    for i in range(1,100) :
        if  nombre.isalpha()==False : 
            print("Ingrese el nombre sin numero y sin espacios")
            nombre=str(input("Nombre: ")).lower()

    nombre_pasajeros.append(nombre) 



    print(nombre_pasajeros)     
    
    tupla_nombre_pasajeros= tuple (nombre_pasajeros)

    print(tupla_nombre_pasajeros)





    apellido=str(input("Apellido: ")).lower()

    for i in range(1,100) :
        if  apellido.isalpha()==False : 
            print("Ingrese el apellido sin numero y sin espacios")
            apellido=str(input("Apellido: ")).lower()

    apellido_pasajeros.append(apellido) 
      


    print(apellido_pasajeros)   

    tupla_apellido_pasajeros= tuple (apellido_pasajeros)

    print(tupla_apellido_pasajeros)






    id=str(input("id: "))

    for i in range(1,100) :
        if  id.isdigit() == False: 
            print("Error ingrese el id correctamente")
            id=str(input("id: "))
    
    id_pasajeros.append(apellido)


    print(id_pasajeros)

    tupla_id_pasajeros= tuple (id_pasajeros)
    print(tupla_id_pasajeros)




    ciudad=str(input("Ingrese la ciudad de destino: ")).lower()

    for i in range(1,100) :
        if  ciudad.isalpha()==False : 
            print("Ingrese el nombre de la ciudad sin espacios o numeros")
            ciudad=str(input("Ciudad: ")).lower()

    
    ciudad_pasajeros.append(ciudad)
    print(ciudad_pasajeros)

    tupla_ciudad_pasajeros= tuple(ciudad_pasajeros)
    print(tupla_ciudad_pasajeros)


    
    departamento= str(input("departamento: ")).lower()

    for i in range(1,100) :
        if  departamento.isalpha()==False : 
            print("Ingrese el nombre de la ciudad sin espacios o numeros")
            departamento=str(input("Ciudad: ")).lower()

    
    departamentos_pasajeros.append(departamento)
    print(departamentos_pasajeros)

    tupla_departamento_pasajeros= tuple(departamentos_pasajeros)

    print(tupla_departamento_pasajeros)


    print("¡Usuario registrado con exito!")


#aaa

