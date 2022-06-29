
class Paciente:
    __Nombre=""
    __Apellido=""
    __Telefono=""
    __Peso=""
    __Altura=""
    def __init__(self, Apellido, Nombre, Telefono, Peso, Altura):
        try:
            self.__Nombre=Nombre
            self.__Apellido=Apellido
            self.__Telefono=Telefono
            self.__Peso=float(Peso)
            self.__Altura=float(Altura)
        except ValueError:
            raise ValueError
    def getNombre(self):
        return self.__Nombre
    def getApellido(self):
        return self.__Apellido
    def getTelefono(self):
        return self.__Telefono
    def getPeso(self):
        return self.__Peso
    def getAltura(self):
        return self.__Altura
    def getIMC(self):
        return(self.__Peso/(self.__Altura/100*self.__Altura/100))
    def getComposicion(self):
        valor=None
        if self.getIMC()<18.5:
            valor=("Peso inferior al Normal")
        elif self.getIMC()<25:
            valor=("Peso Normal")
        elif self.getIMC()<30:
            valor=("Peso superior al Normal")
        else:
            valor=("Obesidad")
        return valor
    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                Nombre=self.__Nombre,
                Apellido=self.__Apellido,
                Telefono=self.__Telefono,
                Peso=self.__Peso,
                Altura=self.__Altura,
                )
            )
        return d