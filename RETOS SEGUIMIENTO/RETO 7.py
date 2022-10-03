class Person:
    def __init__(self, Name:str, Age:int, Size:eval, Hair_Color:str):
        self.Name = Name 
        self.Age = Age
        self.Size = Size 
        self.Hair_Color = Hair_Color
    
    def Walk(self, Distance:eval):
        print(f"Usted {self.Name} ah caminado {Distance} metros de distancia")
    def Eat(self, Food:str):
        print(f"Usted {self.Name} esta comiendo {Food}")
    def Speak(self, Language:str):
        print(f"Usted{self.Name} habla {Language}")

class Student(Person):

    def Study(self, Subject:str):
        print(f"usted {self.Name} esta estudiando {Subject}")

class Teacher(Person):

    def Teach(self, Subject:str):
        print(f"usted {self.Name} esta estudiando {Subject}")

p1 = Person("Orlando", 25, 1.78, "red")
s1 = Student("Gabriel", 15, 1.54, "black")
t1 = Teacher("Clara", 41, 1.60, "blonde") 

t1.Walk(34)
s1.Study("Español")