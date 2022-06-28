class Fraccion:
    __denominador=None
    __numerador=None
    def __init__(self, num, den):
        if (type(num)==int and type(den)==int):
            if den!=0:
                self.__numerador=num
                self.__denominador=den
    def simplificar(self):
        aux = 0
        a=self.__numerador
        b=self.__denominador
        while b != 0:
            aux = b
            b = a % b
            a = aux
        self.__numerador//=a
        self.__denominador//=a
        return self
    def __add__(self, otro):
        if type(self)==type(otro):
            denominador=self.__denominador*otro.__denominador
            numerador=self.__numerador*otro.__denominador+otro.__numerador*self.__denominador
            return Fraccion(numerador, denominador).simplificar()
    def __sub__(self, otro):
        if type(self)==type(otro):
            denominador=self.__denominador*otro.__denominador
            numerador=self.__numerador*otro.__denominador-otro.__numerador*self.__denominador
            return Fraccion(numerador, denominador).simplificar()
    def __mul__(self, otro):
        if type(self)==type(otro):
            denominador=self.__denominador*otro.__denominador
            numerador=self.__numerador*otro.__numerador
            return Fraccion(numerador, denominador).simplificar()
    def __mod__(self, otro):
        if type(self)==type(otro):
            denominador=self.__denominador*otro.__numerador
            numerador=self.__numerador*otro.__denominador
            return Fraccion(numerador, denominador).simplificar()
    def getnumerador(self):
        return self.__numerador
    def getdenominador(self):
        return self.__denominador
    def __str__(self):
        return ("{}/{}".format(self.__numerador, self.__denominador))