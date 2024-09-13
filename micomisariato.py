productos = []  
usuarios = []   

def menu_principal():
    print("\n--- Sistema de Ventas Mi Comisariato ---")
    print("1. Gestión de Productos")
    print("2. Gestión de Usuarios")
    print("3. Generar Factura de Venta")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion 

def gestionar_productos():
    while True:
        print("\n--- Gestión de Productos ---")
        print("1. Añadir Producto")
        print("2. Listar Productos")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            producto = crear_producto()  # Llamada a la función que devuelve un producto
            if producto:  # Validar si el producto fue creado correctamente
                productos.append(producto)
                print(f"Producto '{producto['nombre']}' añadido con éxito.")
        elif opcion == '2':
            listar_productos()  # Esta función no requiere argumentos
        elif opcion == '3':
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

# Función para crear un producto - recibe datos como argumentos y devuelve un diccionario
def crear_producto():
    nombre = input("Ingrese el nombre del producto: ")
    try:
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad en stock: "))
    except ValueError:
        print("Error: Precio o cantidad no válidos.")
        return None  # Retorna None si hay un error de entrada

    # Crea y retorna un diccionario con los datos del producto
    return {
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }

# Función para listar productos
def listar_productos():
    if not productos:
        print("No hay productos registrados.")
    else:
        print("\n--- Lista de Productos ---")
        for i, producto in enumerate(productos):
            print(f"{i + 1}. {producto['nombre']} - Precio: ${producto['precio']} - Cantidad: {producto['cantidad']}")
        
def gestionar_usuarios():
    while True:
        print("\n--- Gestión de Usuarios ---")
        print("1. Registrar Usuario")
        print("2. Listar Usuarios")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            usuario = crear_usuario()  # Llamada a la función que devuelve un usuario
            if usuario:  # Verificar si el usuario fue creado correctamente
                usuarios.append(usuario)
                print(f"Usuario '{usuario['nombre']}' registrado con éxito.")
        elif opcion == '2':
            listar_usuarios()  # Esta función no requiere argumentos
        elif opcion == '3':
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

# Función para crear un usuario - recibe datos y devuelve un diccionario
def crear_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    cedula = input("Ingrese la cédula del usuario: ")
    
    # Validar cédula simple (puede mejorarse)
    if len(cedula) != 10 or not cedula.isdigit():
        print("Cédula no válida.")
        return None  # Retorna None si la cédula es incorrecta

    # Crea y retorna un diccionario con los datos del usuario
    return {
        'nombre': nombre,
        'cedula': cedula
    }

# Función para listar usuarios
def listar_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        print("\n--- Lista de Usuarios ---")
        for i, usuario in enumerate(usuarios):
            print(f"{i + 1}. {usuario['nombre']} - Cédula: {usuario['cedula']}")
            
def generar_factura():
    if not productos:
        print("No hay productos disponibles para la venta.")
        return
    if not usuarios:
        print("No hay usuarios registrados para crear una factura.")
        return

    usuario = seleccionar_usuario()  # Seleccionar un usuario usando una función que retorna un usuario
    if not usuario:
        print("Usuario no válido.")
        return

    total, factura = crear_factura()  # Crear factura y obtener el total y la lista de ítems

    # Mostrar la factura
    print("\n--- Factura de Venta ---")
    print(f"Cliente: {usuario['nombre']} - Cédula: {usuario['cedula']}")
    for item in factura:
        print(f"{item['producto']} - Cantidad: {item['cantidad']} - Subtotal: ${item['subtotal']:.2f}")
    print(f"Total a pagar: ${total:.2f}")

# Función para seleccionar un usuario y devolverlo
def seleccionar_usuario():
    listar_usuarios()
    try:
        usuario_index = int(input("Seleccione el número del usuario para la factura: ")) - 1
        return usuarios[usuario_index] if 0 <= usuario_index < len(usuarios) else None
    except ValueError:
        return None  # Retorna None si la selección es incorrecta

# Función para crear una factura y devolver el total y los ítems
def crear_factura():
    total = 0
    factura = []

    while True:
        listar_productos()
        try:
            producto_index = int(input("Seleccione el número del producto a comprar (0 para finalizar): ")) - 1
            if producto_index == -1:
                break
            if producto_index < 0 or producto_index >= len(productos):
                print("Producto no válido.")
                continue

            producto = productos[producto_index]
            cantidad = int(input(f"Ingrese la cantidad de '{producto['nombre']}' a comprar: "))
            if cantidad > producto['cantidad']:
                print(f"No hay suficiente stock. Disponible: {producto['cantidad']}")
                continue

            producto['cantidad'] -= cantidad
            subtotal = cantidad * producto['precio']
            total += subtotal
            factura.append({'producto': producto['nombre'], 'cantidad': cantidad, 'subtotal': subtotal})
            print(f"{cantidad} unidades de '{producto['nombre']}' añadidas a la factura.")
        except ValueError:
            print("Entrada no válida, intente de nuevo.")

    return total, factura  # Retorna el total y la lista de ítems de la factura

while True:
    opcion = menu_principal()  
    if opcion == '1':
        gestionar_productos()
    elif opcion == '2':
        gestionar_usuarios()
    elif opcion == '3':
        generar_factura()
    elif opcion == '4':
        print("Gracias por usar el sistema de ventas.")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")
        