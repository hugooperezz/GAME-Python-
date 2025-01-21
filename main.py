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
    print("=====Menu=====","\n1. Mostrar inventario", "\n2. Añradir Juego", "\n3. Salir")
    bucle = True
    while bucle:
        opcion = int(input("\nElige una opcion: "))
        match opcion:
            case 1:
                imprimir_productos(productos)
            case 2:
                nombre = input("Ingrese el nombre del juego: ")
                precio = int(input("Ingrese el precio del juego: "))
                cantidad = int(input("Ingrese la cantidad del juego: "))
                agregar_producto(productos, nombre, precio, cantidad)
            case 3:
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
menu()