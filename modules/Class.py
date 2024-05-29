class Aprendiz:
    #Metodo constructor :: funcion constructura :: Funciones que instancia objetos
    # DOCUMENTO: es de tipo string con un tamaño minimo de 7 caracteres y maximo de 10 caracteres
    #Self: pronombre del objeto para hablar de si mismo.
    # FICHA :
    
    def __init__(self,documento,nombre,ficha,evaluacion ):
        self.__documento = documento
        self.__nombre = nombre
        self.__ficha = ficha
        self.__evaluacion = evaluacion 
    
    def set_documento(self, value):
        self.__documento = value

    def get_documento(self):
        return self.__documento
    
    def set_nombre(self, value):
        self.__nombre = value

    def get_nombre(self):
        return self.__nombre

    def set_ficha(self, value):
        self.__ficha = value

    def get_ficha(self):
        return self.__ficha

    def set_evaluacion(self, value):
        self.__evaluacion = value

    def get_evaluacion(self):
        return self.__evaluacion

    def info_aprendiz(self):
        print('Mi nombre es: {0} \n''Mi documento es: {1} \n''Mi ficha es: {2} \n''Mi evaluacion es: {3}'.format(self.get_nombre(), self.get_documento(), self.get_ficha(), self.get_evaluacion()))