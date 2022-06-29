from Paciente import Paciente
from ObjectEncoder import ObjectEncoder
from ManejadorPacientes import ManejadorPacientes
from Paciente import Paciente

class RespositorioPacientes:
    __json=None
    __manejador=None
    def __init__(self, json):
        self.__json = json
        diccionario=self.__json.leerJSONArchivo()
        self.__manejador=self.__json.decodificarDiccionario(diccionario)
        #self.__manejador=ManejadorPacientes()
    def obtenerListaPacientes(self):
        return self.__manejador.getListaPacientes()
    def agregarPaciente(self, pacient):
        self.__manejador.agregarPaciente(pacient)
        return pacient
    def modificarPaciente(self, pacient):
        self.__manejador.updatePaciente(pacient)
        return pacient
    def borrarPaciente(self, pacient):
        self.__manejador.deletePaciente(pacient)
    def grabarDatos(self):
        self.__json.guardarJSONArchivo(self.__manejador.toJSON())

'''json=ObjectEncoder('pacientes.json')
repo=RespositorioPacientes(json)
pacient=Paciente("Juan", "Perez", "264515121", "80", "190")
repo.agregarPaciente(pacient)
repo.grabarDatos()
print("Listo")'''