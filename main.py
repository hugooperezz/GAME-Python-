productos = [
    ["GTA VI", 79.99, 200],#Nombre, Precio, Cantidad
    ["R6", 19.99, 200],
    ["Minecraft", 14.99, 200],
    ["Call of Duty", 79.99, 200],
    ["FIFA 26", 79.99, 50],
]

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
    print("=====Menu=====","\n1. Mostrar inventario", "\n2. Añadir Juego", "\n3. Buscar Juego", "\n4. Actualizar Producto" "\n5. Salir")
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
                print("Salir")
                bucle = False
            case _:
                print("Opcion invalida")
                
def imprimir_productos(productos):
    print("\n===== PRODUCTOS DISPONIBLES =====")
    print("Nombre       Precio    Cantidad")
    print("------------------------------")
    for i in range(len(productos)):
        print(productos[i][0], "/", productos[i][1], "€" ,"/", productos[i][2])
    print("------------------------------")
    

def agregar_producto(productos, nombre, precio, cantidad):
    productos.append([nombre, precio, cantidad])
    

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

def comprobar_producto(productos, nombre):
    encontrado = False
    for i in range(len(productos)):
        if productos[i][0].lower() == nombre.lower():
            encontrado = True
    return encontrado
        

def actualizar_producto(productos):
    peticion = input("Indica el producto que quieras actualizar: ")
    if comprobar_producto(productos, peticion):
        peticion2 = int(input("Que quieres cambiar?: \n1.Precio \n2.Cantidad\n"))
        match peticion2:
            case 1:
                precio = float(input("Ingrese el nuevo precio: "))
                if precio >= 0:
                    for i in range(len(productos)):
                        if productos[i][0].lower() == peticion.lower():
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
                

  

menu()