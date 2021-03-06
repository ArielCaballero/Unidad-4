from Provincia import Provincia

class ManejadorProvincias:
    __indice=0
    __provincias=None
    def __init__(self):
        self.__provincias=[]
        self.__indice=0
    def agregarProvincia(self, provincia):
        provincia.rowid=self.__indice
        self.__indice+=1
        self.__provincias.append(provincia)
    def getListaProvincias(self):
        return self.__provincias
    def deleteProvincia(self, provincia):
        indice=self.obtenerIndiceProvincia(provincia)
        self.__provincias.pop(indice)
    def updateProvincia(self, provincia):
        indice=self.obtenerIndiceProvincia(provincia)
        self.__provincias[indice]=provincia
    def obtenerIndicePaciente(self, provincia):
        bandera = False
        i=0
        while not bandera and i < len(self.__provincias):
            if self.__provincias[i].rowid == provincia.rowid:
                bandera=True
            else:
                i+=1
        return i
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            provincias=[provincia.toJSON() for provincia in self.__provincias]
            )
        return d