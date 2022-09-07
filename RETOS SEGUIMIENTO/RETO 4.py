from datetime import date
import seaborn as sns

class User:
  def __init__(self, id:int, user_name:str, balance:float):
    self.id = id 
    self.user_name = user_name
    self.balance = balance
    self.order_list = []
    self.car = []

  def add_product_to_car(self, prod):
    self.car.append(prod) 

  def consolidate_order(self):
    total = 0
    for prod in self.car:
      total = total + prod.price 
    if total <= self.balance:
      print("Orden aceptada")
      o1 = Order(1, self.car, date.today(), total, True)
      self.order_list.append(o1)
      self.car = []

    else:
      print("su dinero no alcanza")
      self.add_to_balance()
      self.consolidate_order()

  def add_to_balance(self):
    question = input("Desea añadir dinero : ")
    if question == "si":
      cuanto = eval(input("Ingrese el valor que desea agregar : "))
      self.balance = cuanto
    else:
      print("Orden rechazada")
    
  def plot_order_history(self):
    fechas = []
    precios = []
    print("Entre")
    for dato in self.order_list:  
      fechas.append(dato.date)
      precios.append(dato.total)
    sns.lineplot(x=fechas, y=precios)

class Order: 
  def __init__(self, id:int, product_list:list, date:date, total:float, status:bool):
    self.id = id 
    self.product_list = product_list 
    self.date = date
    self.total = total 
    self.status = status

class Product:
  def __init__(self, id:int, name:str, price:float):
    self.id = id 
    self.name = name 
    self.price = price 
    self.price_history = {date.today():price}

  def update_price(self, date, new_price):
    self.price = new_price
    self.price_history[date] = new_price

u1 = User(1, "Carlos", 1000)
u2 = User(2, "Mariana", 2000) 

p1 = Product(1, "Mango", 300)  
p2 = Product(2, "Uvas", 200)  

p1.update_price(date(2022, 5, 13), 250)

u1.add_product_to_car(p1)
u1.add_product_to_car(p2) 

u1.consolidate_order()
u1.plot_order_history()