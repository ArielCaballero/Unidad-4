from API import Weather

class Provincia:
    __Nombre=""
    __Capital=""
    __Cantidadhabitantes=""
    __Departamentos=""
    __api=""
    def __init__(self, Nombre, Capital, Cantidadhabitantes, Departamentos):
        try:
            self.__Nombre=Nombre
            self.__Capital=Capital
            self.__Cantidadhabitantes=Cantidadhabitantes
            self.__Departamentos=Departamentos
            self.__api=Weather()
            url='https://api.openweathermap.org/data/2.5/weather?q='+self.__Capital.replace(" ","+")+'&units=metric&&ang=es&appid=1b8c228fc6543b78c36fc685ad504ad6'
            self.__api.run(url)
        except ValueError:
            raise ValueError
    def getNombre(self):
        return self.__Nombre
    def getCapital(self):
        return self.__Capital
    def getHabitantes(self):
        return self.__Cantidadhabitantes
    def getDepartamentos(self):
        return self.__Departamentos
    def getTemperatura(self):
        return str(self.__api.getResultado()['main']['temp'])
    def getSensacion(self):
        return str(self.__api.getResultado()['main']['feels_like'])
    def getHumedad(self):
        return str(self.__api.getResultado()['main']['humidity'])
    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                Nombre=self.__Nombre,
                Capital=self.__Capital,
                Cantidadhabitantes=self.__Cantidadhabitantes,
                Departamentos=self.__Departamentos,
                )
            )
        return d