from modules import figuras
import matplotlib.pyplot as plt
import numpy as np

def crea_triangulo():
   
    # Longitudes de los lados
    a = figuras.get_arista1() # longitud del lado AB
    b = figuras.get_arista2()  # longitud del lado BC
    c = figuras.get_arista3()  # longitud del lado CA

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
    plt.plot([Ax, Bx], [Ay, By], 'k-')  # Lado AB
    plt.plot([Bx, Cx], [By, Cy], 'k-')  # Lado BC
    plt.plot([Cx, Ax], [Cy, Ay], 'k-')  # Lado CA

    # Dibujar los puntos de los vértices
    plt.plot([Ax, Bx, Cx], [Ay, By, Cy], 'ro')  # Vértices

    # Configurar la escala de los ejes y mostrar la cuadrícula
    plt.axis('equal')


    # Mostrar la gráfica
    plt.show()

    def graf_triangulo(self):
    
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        pp0 = plt.Polygon([[self.get_arista1(),1],[self.get_arista2(),self.get_arista1()],[1,self.get_arista1()]],color="black")

        ax.add_patch(pp0)

        plt.ylim(0,self.get_arista1()+1)
        plt.xlim(0,self.get_arista2()+1)

        plt.title("Triangulo")
        plt.show()
        
    
    
    
def operar(self):
        
        while True:    
            try:
                oper = int(input("Que operacion desea realizar ? 1.Area  2.Perimetro:  "))
                break
            except ValueError:
                print("el valor debe ser numerico")
        while True:
            if oper== 1:
                    area = self.get_base() * self.get_altura()
                    print("El area del rectangulo es: ",area)
                break
            elif oper == 2:
                perimetro = (self.get_altura()*2)+(self.get_base()*2)
                print("El perimetro es de: ", perimetro)
                break
            else:
                print("No hay mas funciones")
                try:
                    oper = int(input("Que operacion desea realizar ? 1.Area  2.Perimetro:  "))                    
                except ValueError:
                    print("el valor debe ser numerico")
                continue