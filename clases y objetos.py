class celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    def llamar(self):
        print(f"Estas llamando desde un celular: {self.modelo}")
        
    def cortar(self):
        print(f"Estas cortando la llamada desde un: {self.modelo}")
        
celular1 = celular("Samsumg", "s3", "48fp")
celular2 = celular("Apple", "iphone", "56fp")

print(celular2.marca)
celular1.llamar()