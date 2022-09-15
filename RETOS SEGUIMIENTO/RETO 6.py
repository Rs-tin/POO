# LOS SABORES DE MAGOLA

class Chefs:
    def __init__(self, cargo:str, id:int, nombre:str):
        self.cargo = cargo 
        self.id = id
        self.nombre = nombre

class Cliente:
    def __init__(self, id:int, nombre:str, plato_select:str):
        self.id = id 
        self.nombre = nombre
        self.plato_select = plato_select

class Menu:
    def __init__(self, id:int, nombre:str, ingredientes:list):
        self.id = id 
        self.nombre = nombre
        self.ingredientes = []

class Productos_Despensa:
    def __init__(self, nombre:str, cantidad:int):
        self.nombre = nombre
        self.cantidad = cantidad

cp1 = Chefs("Chef Principal", 1, "Gustou")
sc1 = Chefs("Subchef", 1, "Carla")
sc2 = Chefs("Subchef", 2, "linguini")

c1 = Cliente(1,"Luis", "Arroz")
c2 = Cliente(2,"Laura", "Tortas")
c3 = Cliente(3,"Camilo", "Jugo en leche")

m1 = Menu(1, "Arroz", ["arroz", "sal", "aceite"])
m2 = Menu(2, "Tortas", ["harina", "aceite", "sal"])
m3 = Menu(3, "Jugo en leche", ["Leche", "azucar"])

d1 = Productos_Despensa("arroz", 8)
d2 = Productos_Despensa("sal", 2)
d3 = Productos_Despensa("aceite", 5)
d4 = Productos_Despensa("harina", 3)
d5 = Productos_Despensa("arroz", 8)
d6 = Productos_Despensa("azucar", 0)