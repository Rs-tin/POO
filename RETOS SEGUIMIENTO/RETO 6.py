# LOS SABORES DE MAG
class Chefs:
    def __init__(self, cargo:str, id:int, nombre:str):
        self.cargo = cargo 
        self.id = id
        self.nombre = nombre

class Cliente:
    def __init__(self, id:int, nombre:str, codigo_plato:str):
        self.id = id 
        self.nombre = nombre
        self.codigo_plato = codigo_plato 
    
    def Realizar_Pedido(self):
        if Menu.Comprobar(self, self.codigo_plato) == True:
            print("Ingredientes suficientes para el pedido")
        else:
            print("No hay ingredientes para el pedido, desea modificar su eleccion")

class Menu:
    def __init__(self, id:int, nombre:str, ingredientes:list):
        self.id = id 
        self.nombre = nombre
        self.ingredientes = ingredientes
    
    def Comprobar(self, seleccion):
        if isinstance(seleccion, Menu):
            for ingre in seleccion.ingredientes:
                a = Productos_Despensa.comprobar_cantidad(self, ingre)
                if a == True:
                    print(f"si hay {ingre.nombre}")
                    continue
                else: 
                    print(f"no hay {ingre.nombre}")
                    return False
                    Break 
        return True

class Productos_Despensa:
    def __init__(self, nombre:str, cantidad:int):
        self.nombre = nombre
        self.cantidad = cantidad
    
    def comprobar_cantidad(self, ingrediente):
        if ingrediente.cantidad > 0:
            print(ingrediente.cantidad, "antes de restar")
            ingrediente.cantidad -= 1
            print(ingrediente.cantidad, "despues de restar")
            return True
        else:
            return False


cp1 = Chefs("Chef Principal", 1, "Gustou")
sc1 = Chefs("Subchef", 1, "Carla")
sc2 = Chefs("Subchef", 2, "linguini")

arroz = Productos_Despensa("arroz", 8)
sal = Productos_Despensa("sal", 2)
aceite = Productos_Despensa("aceite", 5)
harina = Productos_Despensa("harina", 3)
azucar = Productos_Despensa("azucar", 1)
leche = Productos_Despensa("leche", 3)


m1 = Menu(1, "Arroz", [arroz, sal, aceite])
m2 = Menu(2, "Tortas", [harina, aceite, sal])
m3 = Menu(3, "Jugo en leche", [leche, azucar])


c1 = Cliente(1,"Luis", m1)
c2 = Cliente(2,"Laura", m2)
c3 = Cliente(3,"Camilo", m3)
c3.Realizar_Pedido()
c3.Realizar_Pedido()