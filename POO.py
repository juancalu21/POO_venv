import modules.Class as clase

def main():

    Aprendiz1 = clase.Aprendiz('','','','')

    documento = input("Digite su documento: ")
    Aprendiz1.set_documento(documento)
    #print("Documento del aprendiz: ", Aprendiz1.get_documento())

    nombre = input("Digite su nombre: ")
    Aprendiz1.set_nombre(nombre)
    #print("Nombre del aprendiz: ", Aprendiz1.get_nombre())

    ficha = input("Digite su ficha: ")
    Aprendiz1.set_ficha(ficha)
    #print("Ficha del aprendiz: ", Aprendiz1.get_ficha())

    evaluacion = input("Digite su evaluacion: ")
    Aprendiz1.set_evaluacion(evaluacion)
    #print("Evaluacion del aprendiz: ", Aprendiz1.get_evaluacion())

    Aprendiz1.info_aprendiz()

if __name__=="__main__":
    main()