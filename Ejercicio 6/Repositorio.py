from ObjectEncoder import ObjectEncoder
from ManejadorProvincias import ManejadorProvincias
from Provincia import Provincia

class RespositorioProvincias:
    __json=None
    __manejador=None
    def __init__(self, json):
        self.__json = json
        diccionario=self.__json.leerJSONArchivo()
        self.__manejador=self.__json.decodificarDiccionario(diccionario)
        #self.__manejador=ManejadorProvincias()
    def obtenerListaProvincias(self):
        return self.__manejador.getListaProvincias()
    def agregarProvincia(self, provincia):
        self.__manejador.agregarProvincia(provincia)
        return provincia
    def modificarProvincia(self, provincia):
        self.__manejador.updateProvincia(provincia)
        return provincia
    def borrarProvincia(self, provincia):
        self.__manejador.deleteProvincia(provincia)
    def grabarDatos(self):
        self.__json.guardarJSONArchivo(self.__manejador.toJSON())

'''json=ObjectEncoder('pacientes.json')
repo=RespositorioPacientes(json)
pacient=Paciente("Juan", "Perez", "264515121", "80", "190")
repo.agregarPaciente(pacient)
repo.grabarDatos()
print("Listo")'''