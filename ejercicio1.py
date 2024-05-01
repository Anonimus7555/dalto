class Estudiante:
    def __init__(self, Nombre, Edad, Grado):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Grado = Grado
        
    def estudiar(self):
        print(f"El estudiante {self.Nombre} esta estudiando") 
        

        
Nombre = input("Ingrese su nombre: ")
Edad = int(input("Ingrese su edad: "))
Grado = int(input("Ingrese su grado: "))

estudiante = Estudiante(Nombre, Edad, Grado)
        
    
print(f""" 
      datos del estudiante: \n\n
      Nombre: {estudiante.Nombre}\n
      
      Edad: {estudiante.Edad}\n
      
      Grado: {estudiante.Grado}\n
      """)
     
estudiante.estudiar()
      