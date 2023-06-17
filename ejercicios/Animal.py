class Animal:
    nombre=""
    edad=0

    def __init__(self,n,e):
        self.nombre=n
        self.edad=e

    def registrarAnimal(self):
        self.nombre=input("Ingrese nombre del animal: \n")
        self.edad=int(input("Ingrese edad del animal: \n"))


    def mostrarAnimal(self):
        print("El nombre del animal es ",self.nombre," y la edad es ",self.edad)
        
    def duplicarEdadAnimal(self, edad):
        edad2= edad*2
        print("La edad del animal duplicada es ",edad2)
        return edad2 
    def cambiarNombre(self):
        self.nombre=input("Ingrese el nuevo nombre: \n")

    






# tigre= Animal()
# tigre.edad=5
# tigre.nombre="Tony"

# print("El nombre del animal es ",tigre.nombre," y se edad es ",tigre.edad)




