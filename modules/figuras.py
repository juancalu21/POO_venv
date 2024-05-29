import math
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import numpy as np


class Rectangulo:
    
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def set_base(self, value):
        self.__base = value

    def get_base(self):
        return self.__base

    def set_altura(self, value):
        self.__altura = value

    def get_altura(self):
        return self.__altura

    def operar(self):
        area = self.get_base() * self.get_altura()
        print("El area del rectangulo es: ",area)
        
        perimetro = (self.get_altura()*2)+(self.get_base()*2)
        print("El perimetro es de: ", perimetro)       
        
            
    def graf_rectangulo(self):
    
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        pp0 = plt.Rectangle((1,1),self.get_base(), self.get_altura(),  color="black")

        ax.add_patch(pp0)

        plt.ylim(0,self.get_altura()+2)
        plt.xlim(0,self.get_base()+2)

        plt.title("Rectangulo")
        plt.show()


def rectangulo_res():   
    
    rectangulo1= Rectangulo(0,0)
    

    while True:    
        try:
            base = int(input("Digite su base: "))
            rectangulo1.set_base(base)
            break
        except ValueError:
            print("el valor debe ser numerico")

    while True: 
        try:
            altura = int(input("Digite su altura: "))
            rectangulo1.set_altura(altura)
            break
        except ValueError:
            print("el valor debe ser numerico")

    rectangulo1.operar()
    rectangulo1.graf_rectangulo()


class Circulo:

    def __init__(self, radio ):
        self.__radio = radio


    def set_radio(self, value):
        self.__radio = value

    def get_radio(self):
        return self.__radio
   
    
    def operar(self):
    
        area = math.pi* (self.get_radio()**2)
        print("El area del circulo es: ",round(area))

        perimetro = (2 * math.pi* self.get_radio())
        print("El perimetro es de: ", round(perimetro))
        
    

    def graf_circulo(self):
        
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        pp0 = plt.Circle((self.get_radio()+1,self.get_radio()+1), radius=self.get_radio(), color="black")

        ax.add_patch(pp0)

        plt.ylim(0,self.get_radio()*2+2)
        plt.xlim(0,self.get_radio()*2+2)

        plt.title("Circulo")
        plt.show()



def circulo_res():

    circulo1= Circulo(0)

    while True:    
        try:
            radio = int(input("Digite su Radio: "))
            circulo1.set_radio(radio)
            break
        except ValueError:
            print("el valor debe ser numerico")
    
    circulo1.operar()
    circulo1.graf_circulo()



class Triangulo:

    def __init__(self, arista1, arista2, arista3):
        self.__arista1 = arista1
        self.__arista2 = arista2
        self.__arista3 = arista3

    def set_arista1(self, value):
        self.__arista1 = value

    def get_arista1(self):
        return self.__arista1

    def set_arista2(self, value):
        self.__arista2 = value

    def get_arista2(self):
        return self.__arista2

    def set_arista3(self, value):
        self.__arista3 = value

    def get_arista3(self):
        return self.__arista3

    def validar(self):
  
        return self.get_arista1() + self.get_arista2()> self.get_arista3() and self.get_arista1() + self.get_arista3()> self.get_arista2() and self.get_arista3() + self.get_arista2()> self.get_arista1()

    def operar(self):
        
        while True:   
            if  not Triangulo.validar(self): 
                print("Valores invalidos")
                triangulo_res()
                continue
            else:
                
                op = (self.get_arista1() + self.get_arista2()+ self.get_arista3()) /2
                area =(op * (op - self.get_arista1()) * (op - self.get_arista2()) * (op - self.get_arista3())) **0.5
                print("El area del triangulo es de: ", round(area))
                
                perimetro = (self.get_arista1()+self.get_arista2()+self.get_arista3())
                print("El perimetro es de: ", round(perimetro))
                
                

            break
    def crea_triangulo(self):
   
        # Longitudes de los lados
        a = self.get_arista1() # longitud del lado AB
        b = self.get_arista2()  # longitud del lado BC
        c = self.get_arista3()  # longitud del lado CA

        # Calcular el área usando la fórmula de Herón
        s = (a + b + c) / 2  # semiperímetro
        area = np.sqrt(s * (s - a) * (s - b) * (s - c))

        # Calcular la altura
        h = (2 * area) / a

        # Coordenadas de los vértices
        Ax, Ay = 0, 0  # Vértice A
        Bx, By = a, 0  # Vértice B
        Cx = (b**2 - c**2 + a**2) / (2 * a)  # Coordenada x del vértice C
        Cy = np.sqrt(b**2 - Cx**2)  # Coordenada y del vértice C

        # Crear la figura
        plt.figure()

        # Dibujar los lados del triángulo
        plt.plot([Ax, Bx], [Ay, By], 'black')  # Lado AB
        plt.plot([Bx, Cx], [By, Cy], 'black')  # Lado BC
        plt.plot([Cx, Ax], [Cy, Ay], 'black')  # Lado CA

        # Dibujar los puntos de los vértices
        plt.plot([Ax, Bx, Cx], [Ay, By, Cy], )  # Vértices

        # Configurar la escala de los ejes y mostrar la cuadrícula
        plt.axis('equal')


        # Mostrar la gráfica
        plt.show()    
        
def triangulo_res():

    triangulo1= Triangulo(0, 0, 0)
    

    while True:    
        try:
            ar1 = int(input("Digite la medida de la primera Arista: "))
            triangulo1.set_arista1(ar1)
            break
        except ValueError:
            print("el valor debe ser numerico")

    while True:    
        try:
            ar2 = int(input("Digite la medida de la Segunda Arista: "))
            triangulo1.set_arista2(ar2)
            break
        except ValueError:
            print("el valor debe ser numerico")

    while True:    
        try:
            ar3 = int(input("Digite la medida de la Segunda Arista: "))
            triangulo1.set_arista3(ar3)
            break
        except ValueError:
            print("el valor debe ser numerico")
            
    triangulo1.operar()
    triangulo1.crea_triangulo()
   