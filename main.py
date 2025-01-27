productos = [
    ["GTA VI", 79.99, 200],#Nombre, Precio, Cantidad
    ["R6", 19.99, 200],
    ["Minecraft", 14.99, 200],
    ["Call of Duty", 79.99, 200],
    ["FIFA 26", 79.99, 50],
]

#Funcion menu que despliega el nombre de la empresa y las opciones disponibles
def menu():
    print("""
██╗   ██╗██╗██████╗  ██████╗ ███████╗███╗   ██╗    
██║   ██║██║██╔══██╗██╔════╝ ██╔════╝████╗  ██║    
██║   ██║██║██████╔╝██║  ███╗█████╗  ██╔██╗ ██║    
██║   ██║██║██╔═══╝ ██║   ██║██╔══╝  ██║╚██╗██║    
  ╚███ ╔╝██║██║     ╚██████╔╝███████╗██║ ╚████║    
   ╚═══╝ ╚═╝╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                  
""")
    print
    print("=====Menu=====","\n1. Mostrar inventario", "\n2. Añadir Juego", "\n3. Buscar Juego", "\n4. Actualizar Producto", "\n5.Eliminar Producto", "\n6. Salir")
    bucle = True
    while bucle:
        opcion = int(input("\nElige una opcion: "))
        match opcion:
            case 1:
                imprimir_productos(productos)
            case 2:
                nombre = input("Ingrese el nombre del juego: ")
                precio = float(input("Ingrese el precio del juego: "))
                cantidad = int(input("Ingrese la cantidad del juego: "))
                agregar_producto(productos, nombre, precio, cantidad)
            case 3:
                nombre = input("Ingrese el nombre del juego: ")
                buscar_producto(productos, nombre)
            case 4:
                actualizar_producto(productos)
            case 5:
                nombre = input("Ingrese el nombre del juego que desea eliminar: ")
                eliminar_producto(productos, nombre)
            case 6:
                print("Salir")
                bucle = False
            case _:
                print("Opcion invalida")

#Funcion que imprime los productos disponibles en el inventario recorriendo el array productos imprimiendo cada producto por linea con sus respectivos precios y cantidades
def imprimir_productos(productos):
    print("\n===== PRODUCTOS DISPONIBLES =====")
    print("Nombre       Precio    Cantidad")
    print("------------------------------")
    for i in range(len(productos)):
        print(productos[i][0], "/", productos[i][1], "€" ,"/", productos[i][2])
    print("------------------------------")
    

#Funcion que agrega un nuevo producto al inventario
def agregar_producto(productos, nombre, precio, cantidad):
    productos.append([nombre, precio, cantidad])
    

#Duncion que recorre todo el array asta encontrar el producto elegiodo, en caso de encontrarlo imprime su respectiva informacion y en caso de que este producto no se encuentre en la lista de productos mostrara un mensaje de que el producto no se encuentra en la lista
def buscar_producto(productos, nombre):
    for producto in productos:
        if producto[0] == nombre: 
            print(f"""
===============================
✔️  El juego '{nombre}' está disponible en el inventario.
   - Precio: {producto[1]} €
   - Cantidad disponible: {producto[2]}
===============================
            """)
            return
    print(f"""
===============================
❌ El juego '{nombre}' no está en el inventario.
===============================
    """)

#Funcion muy parecida a la anterior con la diferencia que si el producto si se encuentra retornara true y en su defecto false este metodo solo se usa como complementacion de la funcion actualizar_producto
def comprobar_producto(productos, nombre):
    encontrado = False
    for i in range(len(productos)):
        if productos[i][0].lower() == nombre.lower():
            encontrado = True
    return encontrado
        
#Funcion que se encarga de actualizar los datos del producto selecionado con ayuda de la funcion comprobar_producto y en caso de que este no se encuentra lanzara un mensaje de error
def actualizar_producto(productos):
    peticion = input("Indica el producto que quieras actualizar: ")
    if comprobar_producto(productos, peticion):
        peticion2 = int(input("Que quieres cambiar?: \n1.Precio \n2.Cantidad\n"))
        match peticion2:
            case 1:
                precio = float(input("Ingrese el nuevo precio: "))
                if precio >= 0:
                    for i in range(len(productos)):
                        if productos[i][0].lower() == peticion.lower():#lower para que no se tenga problemas con mayusculas y minusculas
                            productos[i][1] = precio
                            #Poner aviso de precio actualizado
                elif precio <= -1:
                    print("Precio invalido")
            case 2:
                cantidad = int(input("Ingrese la nueva cantidad: "))
                if cantidad >= 0:
                    for i in range(len(productos)):
                        if productos[i][0].lower() == peticion.lower():
                            productos[i][2] = cantidad
                            #Poner aviso de cantidad actualizado
                elif cantidad <= -1:
                    print("Cantidad invalida")
            case _:
                print("Opcion invalida")
    else:
        print("Producto no encontrado")

def eliminar_producto(productos, nombre):
    if comprobar_producto(productos, nombre):
        for producto in productos:
            if producto[0] == nombre:
                productos.remove(producto)
                break
    else:
        print("Producto no encontrado")


menu()