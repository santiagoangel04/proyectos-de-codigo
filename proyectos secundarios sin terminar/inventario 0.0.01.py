#replicaremos nuestro programa llamado inventario donde organizaremos
#de mejor forma nuestro progrma con su funciones

productos_inventario={}

#funcion de mostrar el menu 
def mostrar_menu():
    """
    Muestra el menú de las operaciones disponibles.
    """
    print('1. Registrar nuevo producto')
    print('2. Vender un producto')
    print('3. Buscar un producto por su código')
    print('0. Salir')
    opcion=int(input("--> ")) 
    while True:
        if opcion == 1:
            registrar_producto()
        elif opcion == 2:
            vender_producto()
        elif opcion == 3:
            buscar_producto()
        elif opcion == 0:
            break



#registro de productos
def registrar_producto():    
    print("en desarrollo")

#lista de producto para vender 
def vender_producto():
    print("en desarrollo")

#busca el producto
def buscar_producto():
    print("en desarrollo")

#verifica la cantidad de productos del inventario
def cantidad_producto_inventario():
    print("en desarrollo")

#compra el producto para llenar el inventario
#si un producto no se encuentra este imediatamente debe decirle al dueño que es necesario
def comprar_producto():
    print("en desarrollo")

#nuestra funcion principal sera la de run en la cual correra todo el programa
def run():
    mostrar_menu()
    





#declaramos la condicion principal la cual evaluara si este el archivo principal
if __name__ == "__main__":
    run()