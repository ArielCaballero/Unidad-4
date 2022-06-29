from Paciente import Paciente

class ManejadorPacientes:
    __indice=0
    __pacientes=None
    def __init__(self):
        self.__pacientes=[]
        self.__indice=0
    def agregarPaciente(self, pacient):
        pacient.rowid=self.__indice
        self.__indice+=1
        self.__pacientes.append(pacient)
    def getListaPacientes(self):
        return self.__pacientes
    def deletePaciente(self, pacient):
        indice=self.obtenerIndicePaciente(pacient)
        self.__pacientes.pop(indice)
    def updatePaciente(self, pacient):
        indice=self.obtenerIndicePaciente(pacient)
        self.__pacientes[indice]=pacient
    def obtenerIndicePaciente(self, pacient):
        bandera = False
        i=0
        while not bandera and i < len(self.__pacientes):
            if self.__pacientes[i].rowid == pacient.rowid:
                bandera=True
            else:
                i+=1
        return i
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            pacientes=[paciente.toJSON() for paciente in self.__pacientes]
            )
        return d