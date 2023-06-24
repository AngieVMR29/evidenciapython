from Persona import *
class Empleado(Persona):
    cargo=""
    valorhora=0
    horastrabajadas=0
    departamento=""
   
    def pedirDatos(self):
        self.cargo=input("Ingrese el cargo que tiene: ")
        self.valorhora=float(input("Ingrese el valor que le pagan por hora: "))
        self.horastrabajadas=float(input("Ingrese la cantidad de horas trabajadas: "))
        return super().pedirDatos()
    def calcularhonorarios(self,valorhora,horastrabajadas):
        valorT=valorhora*horastrabajadas
        valorT1= valorT-0.966
        print("El valor de sus honorarios es",valorT1)

    def mostrarpersona(self):
        print("Su cargo es ",self.cargo," sus horas trabajadas son",self.horastrabajadas," el valor de la h hora trabajada es",self.valorhora," y el depertamento al que pertenece es ",self.departamento)