class Doctor:
    def __init__(self, Nombre, Edad, Especializacion, Universidad):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Especializacion = Especializacion
        self.Universidad = Universidad
        
    def c_sExperiencia(self):
        if(self.Edad > 40):
            return f"{self.Nombre}, usted es un doctor con mucha experiencia"
        else:
            return f"{self.Nombre}, usted aun es un novato"
        
print("********REGISTRO DE DATOS**********")
Nombre = input("Ingrese su nombre: ")
Edad = int(input("Ingrese su edad: "))
Especializacion = input("Ingrese la rama que desempeña: ")
Universidad = input("Ingrese su centro educativo superior de origen:")

        
doctor = Doctor(Nombre, Edad, Especializacion, Universidad)

print(f""" 
      datos del estudiante: \n\n
      Nombre: {doctor.Nombre}\n
      
      Edad: {doctor.Edad}\n
      
      Especializacion: {doctor.Especializacion}\n
      
      Universidad: {doctor.Universidad}\n
      """)

print(doctor.c_sExperiencia())
      
     
        
    
            
        
         
        