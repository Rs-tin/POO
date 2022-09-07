class Profesores:
  def __init__(self, id, nombre, cur_dic):
    self.id = id
    self.nombre = nombre
    self.cur_dic = cur_dic

  def Parciales(profe, curso, user):
    if user.nombre == profe:
      if user.cur_dic == curso:
        print("Datos confirmados")
        preguntas = []
        print("A continuacion ingrese los datos solicitados")
        name_p = input("Ingrese el nombre del parcial : ")
        por_p = eval(input("Ingrese el porcentaje que tendra el parcial : "))
        num = eval(input("Cuantas preguntas desea agregar al parcial : "))
        for pregunta in range(1,num+1):
          pre_p = input(f"Ingrese la pregunta {pregunta} : ")
          preguntas.append(pre_p)
        
        print(f"Usted ha creado el parcial * {name_p} * que tiene un porcentaje de {por_p}%, este tendra las siguientes preguntas : ")
        for dato in preguntas:
          print(dato)

      else:
        print(f"Usted no dicta el curso de {curso}, por lo que no le corresponde crear el parcial")
    else:
      print("Usted no figura en la base de datos intentelo de nuevo")

p1 = Profesores(1, "Emiliano", "Matematicas")
p2 = Profesores(2, "Sara", "Lengua")

Profesores.Parciales("Emiliano", "Matematicas", p1) 
print("--")
Profesores.Parciales("Sandra", "Ingles", p2) 
print("--")
Profesores.Parciales("Emiliano", "Lengua", p1) 
