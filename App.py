import time
import os
import modules.figuras as clase

def main():
    
    os.system("cls")
    print("El programa para crear las figuras geometricas iniciara en 5seg. ")
    time.sleep(5)
        
    os.system("cls")
    print("Primero tomaremos las medidas del rectangulo\n") 
    clase.rectangulo_res()

    os.system("cls")
    print("\nAhora tomaremos el radio del circulo\n")
    clase.circulo_res()
    
    os.system("cls")
    print("\nFinalmente tomaremos la medida de los lados del triangulo\n")
    clase.triangulo_res()
    
    os.system("cls")
    while True:
        try:
            resp =input("Desea generar mas figuras? Si / No ")
        except:
            SyntaxError
        res = resp.upper()
        if res == "SI":
            main()
        elif res == "NO": 
            os.system("cls")  
            print("Fin del programa")
            break
        else:
            print("Opcion no valida") 
            continue  
        
if __name__ == "__main__":
    main()