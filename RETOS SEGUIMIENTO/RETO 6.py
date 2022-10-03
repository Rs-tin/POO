class Chefs:
    def __init__(self, cargo:str, id:int, nombre:str):
        self.cargo = cargo 
        self.id = id
        self.nombre = nombre

    def Entregar_Pedido(self, eleccion):
        print(eleccion.nombre, self.nombre)
        a = Chefs.E_Chef(self)
        print(f"{a.nombre} a entregado su pedido ")
        self.pedidos_completados.append(eleccion.nombre)
        print(self.pedidos_completados)

    def E_Chef(self):
        return c2

class Cliente:
    def __init__(self, id:int, nombre:str):
        self.id = id 
        self.nombre = nombre
        self.pedidos_completados = []

    def Realizar_Pedido(self, eleccion):
        
        if isinstance(eleccion, Menu):
            Menu.Enviar_Ingredientes(self, eleccion) 
            a = Productos_Despensa.Comprobar(self, eleccion.ingredientes)
            if a == True:
                print("Voy a preparar su pedido y se lo enviare")
                Chefs.Entregar_Pedido(self, eleccion)

            else:
                a = input("no hay suficientes ingredientes para preparar su eleccion, desea modificar su eleccion y[si] N[no] : ")
                if a == "y":
                    self.Realizar_Pedido(eval(input("Que desea ordenar : ")))
                else:
                    print("Cancelaremos su pedido")

        else:
            print("No tenemos eso en nuestro menu, cambie su eleccion")
            self.Realizar_Pedido(eval(input("Que desea ordenar : ")))

class Menu:
    def __init__(self, id:int, nombre:str, ingredientes:list):
        self.id = id 
        self.nombre = nombre
        self.ingredientes = ingredientes
    
    def Enviar_Ingredientes(self, eleccion):
        return eleccion.ingredientes

class Productos_Despensa:
    def __init__(self, nombre:str, cantidad:int):
        self.nombre = nombre
        self.cantidad = cantidad 
    
    def Comprobar(self, ingredientes):
        n = len(ingredientes)
        total = 0
        for ingre in ingredientes:
            a = eval(ingre)
            if a.cantidad > 0:
                total += 1 
        
        if n == total:
            for ingre in ingredientes:
                a = eval(ingre)
                a.cantidad -= 1 
            return True

c1 = Chefs("Subchef", 1, "Gustou")
c2 = Chefs("Subchef", 2, "Aladin")
c3 = Chefs("Chef", 1, "Carla")

cl1 = Cliente(1, "Santiago")
cl2 = Cliente(2, "Alexa")
cl3 = Cliente(3, "Restrepo")

m1 = Menu(1, "Salchipapas", ["papa", "salchicha", "platano"])
m2 = Menu(2, "Sopa", ["papa", "lentejas"])

papa = Productos_Despensa("papa", 1)
salchicha = Productos_Despensa("salchicha", 1)
platano = Productos_Despensa("platano", 1)
lentejas = Productos_Despensa("lentejas", 1)

cl1.Realizar_Pedido(eval(input("Que desea ordenar 1 : ")))
cl2.Realizar_Pedido(eval(input("Que desea ordenar 2 : ")))
cl3.Realizar_Pedido(eval(input("Que desea ordenar 3 : ")))
cl2.Realizar_Pedido(eval(input("Que desea ordenar 2 : ")))
cl1.Realizar_Pedido(eval(input("Que desea ordenar 1 : ")))
cl1.Realizar_Pedido(eval(input("Que desea ordenar 1 : ")))
cl3.Realizar_Pedido(eval(input("Que desea ordenar 3 : ")))