import os
import sys

#funcion para borrar la pantalla
def borrarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
     os.system ("cls")
#variables
#para validar que escirbe un numero en el input
validacion = False
validacion_1 = False
repetir = True
#para no repetir las mismas preguntas/seccion 1
num1_1 = True
num1_2 = True
num1_3 = True
#nombre para no repetir tanto
nombre = "Christiane Nüsslein-Volhard"

#titulo
while 1:
    print("x"*54)
    print(" "*13  + nombre) 
    print("x"*54)
    #secciones
    print("1- Biografía")
    print("2- Premios")
    print("3- Publicaciones")
    print(" ")
    print(" ")
    print("Elige la sección que quieras informarte sobre Christiane Nüsslein-Volhard.")
    #elejir la seccion
    repetir = True #repetir true para cada vez que vuelva al menu principal le salga el texto de biografia

    numero_seccion = int(input("Sección: "))
    borrarPantalla()
    
    if numero_seccion == 99:
        sys.exit()
       

    if numero_seccion == 1:
        while True:    
            #preguntas de biografia
            if repetir == True:
                print("--------BIOGRAFÍA--------")
                print("1-¿QUIÉN ES " + nombre.upper() + "?")
                print("2-¿CUANDÓ Y DÓNDE NACIÓ?")
                print("3-¿DÓNDE ESTUDIO?")
            num_info_1 = int(input("Que quieres saber sobre " + nombre + ": "))
            print( 40*"~")
            if num_info_1 == 1:   
                if num1_1 == True: 
                    print(nombre + "es una de las mujeres cinetíficas más famosas debido a que consiguió en 1988 un nobel de Fisiología o Medicina.")
                    num1_1 = False 
                    repetir = False                      
                elif num1_1 == False:
                    print("Esta pregunta ya la has hecho antes, busca arriba la respuesta")
            elif  num_info_1 ==2:
                if num1_2 == True:
                    print(nombre + " nació el 20 de octubre de 1942 en Magdeburg, Alemania")
                    num1_2 = False
                    repetir = False 
                elif num1_2 == False:
                    print("Esta pregunta ya la has hecho antes, busca arriba la respuesta")
                    repetir = False 
            elif num_info_1 ==3:
                if num1_3 == True:
                    print( nombre + " estudió inicialmente Biología en Fráncfort, luego cambió a Física y posteriormente a Bioquímica.")
                    print("Desde 1985 dirige la división de genética del Instituto Max Planck de Biología del desarrollo en Tubinga, Alemania.")
                    num1_3 = False
                    repetir = False 
                elif num1_3 == False:
                    print("Esta pregunta ya la has hecho antes, busca arriba la respuesta")
                    repetir = False 
            elif num_info_1 == 99:
                    borrarPantalla()
                    break
                    
            else:
                print("No hay ninguna categoria con ese número, prueba a intentarlo con otro")
    if numero_seccion == 2:
        print("---------PREMIOS---------")
        print("Estoss son sus premios:")
        print("Premio Gottfried Wilhelm Leibniz 1986")
        print("Premio Albert Lasker por Investigación Médica Básica 1991")
        print("Premio Louisa Gross Horwitz 1992")
        print("Louis-Jeantet Prize for Medicine 1992")
        print("Otto Warburg Medal 1992")
        print("Sir Hans Krebs Medal 1993")
        print("Ernst Schering Prize 1993")
        print("Premio Nobel de Fisiología o Medicina 1995")
        print("Condecoración Austriaca de las Ciencias y las Artes 2009")
        salir = int(input("Salir: "))
        if salir == 99:
            borrarPantalla()

    if numero_seccion == 3:
        print("------PULICACIONES------")
        print("Algunas de sus publicaciones son:")
        print("Gradienten als Organisatoren der Embryonalentwicklung, 1996")
        print("Wann ist ein Mensch ein Mensch? C. F. Müller, 2003")
        print("Von Genen und Embryonen.2004,")
        print("Mein Kochbuch: Einfaches für besondere Anlässe, 2006")
        print("Coming to life: how genes drive development, Kales Press, USA 2006")
        salir1 = int(input("Salir: "))
        if salir1 == 99:
            borrarPantalla()
