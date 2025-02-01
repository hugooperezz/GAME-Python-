import tkinter as tk

productos = [
    ["GTA VI", 79.99, 100],#Nombre, Precio, Cantidad
    ["R6", 19.99, 20],
    ["Minecraft", 14.99, 35],
    ["Call of Duty", 79.99, 85],
    ["FIFA 26", 79.99, 50],
]
def inicio():
    print("\n======== Como quieres operar ========\n" + "-" * 22 ,"\n1. Consola\n" + "-" * 22 , "\n2. Interfaz\n" + "-" * 22,"\n======================")
    opcion = int(input("Selecciona una opcion"))
    match opcion:
        case 1:
            menu()
        case 2:
            interfaz()
        case _:
            print("Opcion no valida")

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
    bucle = True
    while bucle:
        print("\n======== Menu ========\n" + "-" * 22 ,"\n1. Mostrar inventario\n" + "-" * 22 , "\n2. Añadir Juego\n" + "-" * 22, "\n3. Buscar Juego\n" + "-" * 22, "\n4. Actualizar Producto\n" + "-" * 22, "\n5. Eliminar Producto\n" + "-" * 22, "\n6. Resumen inventario\n"+ "-" * 22, "\n7. Buscar Juego\n" + "-" * 22,"\n8. Salir\n" + "-" * 22,"\n======================")
        opcion = int(input("\nElige una opcion: "))
        match opcion:
            case 1:
                imprimir_productos()
            case 2:
                nombre = input("Ingrese el nombre del juego: ")
                precio = float(input("Ingrese el precio del juego: "))
                cantidad = int(input("Ingrese la cantidad del juego: "))
                agregar_producto(nombre, precio, cantidad)
            case 3:
                nombre = input("Ingrese el nombre del juego: ")
                buscar_producto(nombre)
            case 4:
                actualizar_producto()
            case 5:
                nombre = input("Ingrese el nombre del juego que desea eliminar: ")
                eliminar_producto(nombre)
            case 6:
                resumen()
            case 7:
                cantidad = int(input("Ingrese una cantidad en especifico para que salgan los productos con dicha cantidad "))
                buscar_cantidad(cantidad)
            case 8:
                print("Salir")
                bucle = False
            case _:
                print("Opcion invalida")

#Funcion que imprime los productos disponibles en el inventario recorriendo el array productos imprimiendo cada producto por linea con sus respectivos precios y cantidades
def imprimir_productos():
    print("\n====== PRODUCTOS DISPONIBLES ======")
    
    # Definimos el ancho de cada columna
    ancho_nombre = 15
    ancho_precio = 10
    ancho_cantidad = 10
    
    # Imprimimos el encabezado
    print("-" * (ancho_nombre + ancho_precio + ancho_cantidad))
    print(
        "Nombre".ljust(ancho_nombre) +
        "Precio".ljust(ancho_precio) +
        "Cantidad".ljust(ancho_cantidad)
    )
    print("-" * (ancho_nombre + ancho_precio + ancho_cantidad))
    
    # Imprimimos cada producto
    for producto in productos:
        nombre = str(producto[0])
        precio = f"{producto[1]}€"
        cantidad = str(producto[2])
        
        print(
            nombre.ljust(ancho_nombre) +
            precio.ljust(ancho_precio) +
            cantidad.ljust(ancho_cantidad)
        )
    
    print("-" * (ancho_nombre + ancho_precio + ancho_cantidad))
    

#Funcion que agrega un nuevo producto al inventario
def agregar_producto(nombre, precio, cantidad):
    productos.append([nombre, precio, cantidad])
    

#Duncion que recorre todo el array asta encontrar el producto elegiodo, en caso de encontrarlo imprime su respectiva informacion y en caso de que este producto no se encuentre en la lista de productos mostrara un mensaje de que el producto no se encuentra en la lista
def buscar_producto(nombre):
    for i in productos:
        if i[0] == nombre: 
            print(f"""
==============================================================
✔️  El juego '{nombre}' está disponible en el inventario.
   - Precio: {i[1]} €
   - Cantidad disponible: {i[2]}
==============================================================
            """)
            return
    print(f"""
==============================================================
❌ El juego '{nombre}' no está en el inventario.
==============================================================
    """)

#Funcion muy parecida a la anterior con la diferencia que si el producto si se encuentra retornara true y en su defecto false este metodo solo se usa como complementacion de la funcion actualizar_producto
def comprobar_producto(nombre):
    encontrado = False
    for i in range(len(productos)):
        if productos[i][0].lower() == nombre.lower():
            encontrado = True
    return encontrado
        
#Funcion que se encarga de actualizar los datos del producto selecionado con ayuda de la funcion comprobar_producto y en caso de que este no se encuentra lanzara un mensaje de error
def actualizar_producto():
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
        
#Metodo que primero comprueba que el producto exista con la ayuda del metodo comprobar_producto, el metodo recorre el array asta encontrar el producto y eliminarlo de la lista
def eliminar_producto(nombre):
    if comprobar_producto(nombre):
        for producto in productos:
            if producto[0] == nombre:
                productos.remove(producto)
                break
    else:
        print("Producto no encontrado")
        
#Metodo que se encarga de recorrer el array identificando el numero de productos que tenemos en la tienda con un contador que por cada producto que tengamos se suma uno
def totalProductos():
    contadorPorductos = 0
    for i in range(len(productos)):
        contadorPorductos +=1
    return contadorPorductos

#Metodo que imprime ordena la lista de mayor a menor con la ayuda del Key=lamba para introducir el parametro del array de 2 dimensiones que quiero que coja el precio y luego le doy la vuelta con el parametro reverse ya que el sorted me lo ordena de menor a mayor
def productoCaroBarato():
    productoCaroBarato = sorted(productos, key=lambda x: x[1], reverse=True)

    # Encabezado
    print(f"{'Producto':<15}{'Precio':>14}")
    print("=" * 40)

    # Imprimir filas con formato
    for i in productoCaroBarato:  
        print(f"{i[0]:<20}{i[1]:>8.2f} €")
    print("=" * 40)
    
    return productoCaroBarato

#Metodo que recorre el array cogiendo el valor y la cantidad de cada producto, multiplicandolos para darnos el valor total de cada producto, almacenandose en una variable que se encuentra fuera del for y siendo redondeada a 2 decimales
def valorTotal():
    total = 0
    for i in productos:
        precioProducto = i[1]
        cantidadProducto = i[2]
        toralProducto = precioProducto * cantidadProducto
        total = total + toralProducto
    totalFinal = round(total, 2)
    return totalFinal

#Metodo que se usa como union de los metodos anteriores para que se impriman de una forma atractiva
def resumen():
    # Mostrar el número total de productos
    print("")
    print("=" * 40) 
    print(f"Total de productos en la tienda: {totalProductos()}")
    print("=" * 40)

    # Mostrar los productos ordenados de mayor a menor precio
    print("Productos más caros a baratos:")
    print("-" * 40)
    productoCaroBarato()
    
    # Mostrar el valor total de los productos
    print(f"Valor total de los productos: {valorTotal()} €")
    print("=" * 40)

#Funcion que se encarga de buscar productos con una cantidad especifica y imprimir los productos menores a esa cantidad
def buscar_cantidad(cantidad):
    productoMenorCantidad = sorted(productos, key=lambda x: x[2], reverse=True)
    print("\nLos productos con una cantidad menor a:", cantidad,"€")
    for i in productoMenorCantidad:
        if i[2] <= cantidad:  
            print(f"""==============================================================
    - El juego '{i[0]}' está disponible en el inventario.
    - Precio: {i[1]} €
    - Cantidad disponible: {i[2]} """)
    print("==============================================================")

#Metodo que se usa como union de los metodos anteriores para que se impriman de una forma atractiva
def resumen_Interfaz(nueva_ventana):
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Resumen de Inventario")
    nueva_ventana.geometry("850x200") 

    tk.Label(nueva_ventana, text="Resumen Inventario", font=("Arial", 12, "bold"), fg="blue").grid(row=0, column=0, columnspan=3, pady=10, sticky="nsew")

    tk.Label(nueva_ventana, text=f"Total de productos en la tienda: {totalProductos()}", font=("Arial", 10), fg="blue").grid(row=1, column=0, columnspan=3, pady=5, sticky="nsew")

    tk.Label(nueva_ventana, text=f"Productos más caros a baratos: {productoCaroBarato()}", font=("Arial", 10), fg="blue").grid(row=2, column=0, columnspan=3, pady=5, sticky="nsew")

    tk.Label(nueva_ventana, text=f"Valor total de los productos: {valorTotal()} €", font=("Arial", 10), fg="blue").grid(row=3, column=0, columnspan=3, pady=5, sticky="nsew")     

#Metodo que primero comprueba que el producto exista con la ayuda del metodo comprobar_producto, el metodo recorre el array asta encontrar el producto y eliminarlo de la lista
def eliminar_producto_Interfaz(nueva_ventana):
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Eliminar Producto")
    nueva_ventana.geometry("850x200")
    
    tk.Label(nueva_ventana, text="Eliminar Producto", font=("Arial", 12, "bold"), fg="blue").grid(row=0, column=0, columnspan=3, pady=10, sticky="nsew") 
    nombre = tk.Entry(nueva_ventana, width=20).lower()
    nombre.grid(row=1, column=0, columnspan=3, pady=5, sticky="nsew")

    boton1 = tk.Button(nueva_ventana, text="Eliminar", bg="red", fg="white", font=("Arial", 10, "bold"), command=lambda:eliminar_producto(nombre.get()))
    boton1.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

    

#Metodo que se usa como union de los metodos anteriores para que se impriman de una forma atractiva
def buscar_cantidad_Interfaz(nueva_ventana):
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Buscar Cantidad")
    nueva_ventana.geometry("850x200")
    
    tk.Label(nueva_ventana, text="buscar Cantidad", font=("Arial", 12, "bold"), fg="blue").grid(row=0, column=0, columnspan=3, pady=10, sticky="nsew") 


#Metodo que primero comprueba que el producto exista con la ayuda del metodo comprobar_producto, el metodo recorre el array asta encontrar el producto y eliminarlo de la lista
def actualizar_producto_Interfaz(nueva_ventana):
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Actualizar Producto")
    nueva_ventana.geometry("850x200")
    
    tk.Label(nueva_ventana, text="Actualizar Producto", font=("Arial", 12, "bold"), fg="blue").grid(row=0, column=0, columnspan=3, pady=10, sticky="nsew") 

def salir_Interfaz(ventana):
    ventana.destroy()
     
    
def interfaz():
    # Crear la ventana
    ventana = tk.Tk()
    ventana.title("VIPGEN")
    
    
    ventana.geometry("900x200")  # Tamaño inicial de la ventana

    # Título centrado
    nombreTitulo = "VIPGEN"
    titulo = tk.Label(ventana, text=nombreTitulo, font=("Courier", 16, "bold"), fg="blue")
    titulo.grid(row=0, column=0, columnspan=7, pady=10) 

    # Botones con estilos y márgenes
    boton1 = tk.Button(ventana, text="Mostrar inventario", bg="lightblue", fg="black", font=("Arial", 10) ,)
    boton1.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

    boton2 = tk.Button(ventana, text="Añadir Juego", bg="lightgreen", fg="black", font=("Arial", 10))
    boton2.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    boton3 = tk.Button(ventana, text="Buscar Juego", bg="lightyellow", fg="black", font=("Arial", 10))
    boton3.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

    boton4 = tk.Button(ventana, text="Actualizar Producto", bg="lightcoral", fg="black", font=("Arial", 10) , command=lambda:actualizar_producto_Interfaz(ventana))
    boton4.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

    boton5 = tk.Button(ventana, text="Eliminar Producto", bg="lightpink", fg="black", font=("Arial", 10), command=lambda:eliminar_producto_Interfaz(ventana))
    boton5.grid(row=1, column=4, padx=5, pady=5, sticky="ew")

    boton6 = tk.Button(ventana, text="Resumen Inventario", bg="lightgray", fg="black", font=("Arial", 10), command=lambda:resumen_Interfaz(ventana))
    boton6.grid(row=1, column=5, padx=5, pady=5, sticky="ew")

    boton7 = tk.Button(ventana, text="Buscar Juego", bg="Black", fg="white", font=("Arial", 10, "bold"), command=lambda:buscar_cantidad_Interfaz(ventana))
    boton7.grid(row=1, column=6, padx=5, pady=5, sticky="ew")
    
    boton8 = tk.Button(ventana, text="Salir  ", bg="red", fg="white", font=("Arial", 10, "bold"), command=lambda:salir_Interfaz(ventana))
    boton8.grid(row=1, column=7, padx=5, pady=5, sticky="ew")
    ventana.mainloop()

inicio()