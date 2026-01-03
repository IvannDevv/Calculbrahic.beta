#Librerias
from alive_progress import alive_bar
import time
#Datos
usuario_correcto = "Ivan"
contraseña_correcta = 1234
#Inicio de programa
user_input = input("Ingresar usuario: ")

#funcion de analisis si el usuario es correcto y existe en la base de datos y se puede ingresar pin
def Analisis_usuario_correcto(name_user, correct_pin, correct_user):
    #Condicionales si usuario es correcto o no
    if name_user == correct_user:
        password_input = int(input("Ingresar pin: "))
        #Condicional contraseña
        intentos_contraseña = 0 #Suma de intentos de contraseñas
        if password_input == correct_pin:
            carga_iniciosesion()
        else:
            while intentos_contraseña <= 2:
                password_input= int(input("Pin incorrecto, ingresar pin de nuevo: "))
                if password_input == correct_pin:
                    carga_iniciosesion()
                    break
                else:
                    intentos_contraseña += 1
    else:
        while True:
            name_user = input("Intenta de nuevo: ")
            if name_user == correct_user:     
                password = int(input("Ingresar pin: "))
                if password == correct_pin:
                    carga_iniciosesion()
                else:
                    while intentos_contraseña <= 2:
                        password = int(input("Pin incorrecto, ingresar pin de nuevo: "))
                        if password == correct_pin:
                            carga_iniciosesion()
                        else:
                            intentos_contraseña += 1
            else:
                print("Incorrecto")

def carga_iniciosesion():
    with alive_bar(100, title="Cargando") as bar:
        for i in range(100):
            time.sleep(0.02)
            bar()
    print(f"Bienvenido a CalculBrahic, {usuario_correcto}")
    inicio_sesion()

def carga_cerrandosesion():
    with alive_bar(100, title="Cargando") as bar:
        for i in range(100):
            time.sleep(0.01)
            bar()
    print(f"Hasta luego {usuario_correcto}!")

def service_Calculbrahic_beta():
    print("Selecciona un numero de que deseas hacer: ")
    while True:
        print("1. Calculos")
        print("2. Conversion de moneda")
        print("3. Salir")

        respuesta_user = int(input())
        #RESPUESTA DE USUARIO DE QUE ACCION QUIERE HACER
        #ACCION 1 DE CALCULOS MATEMATICOS
        if respuesta_user == 0 or respuesta_user > 4:
            print("Error, ingresa un numero de las opciones")
        elif respuesta_user == 1:
            print("¿Que tipo de calculo deseas hacer?:")
            print("1. Multiplicacion")
            print("2 Division")
            print("3. resta")
            print("4. Suma")
            respuesta_user_calculos = int(input("Ingresa el numero de la opcion que deseas: "))
            if respuesta_user_calculos == 0 or respuesta_user_calculos >= 5:
                print("Error, ingresa un numero de las opciones")
            elif respuesta_user_calculos == 1:
                mult_num1 = int(input("Ingresa el primer numero: "))
                mult_num2 = int(input("Ingresa el segundo numero: "))
                mutl_total = mult_num1 * mult_num2
                print(f"La multiplicacion de {mult_num1} x {mult_num2} es {mutl_total}")
            elif respuesta_user_calculos == 2:
                div_num1 = float(input("Ingresa el primer numero: "))
                div_num2 = float(input("Ingresa el segundo numero: "))
                div_total = div_num1 / div_num2 
                print(f"La division de {div_num1} / {div_num2} es {div_total}")
            elif respuesta_user_calculos == 3:
                res_num1 = float(input("Ingresa el primer numero: "))
                res_num2 = float(input("Ingresa el segundo numero: "))
                res_total = res_num1 - res_num2
                print(f"La resta de {res_num1} - {res_num2} es {res_total}")
            elif respuesta_user_calculos == 4:
                sum_num1 = float(input("Ingresa el primer numero: "))
                sum_num2 = float(input("Ingresa el segundo numero: "))
                sum_total = sum_num1 + sum_num2
                print(f"La suma de {sum_num1} + {sum_num2} es {sum_total}")
        elif respuesta_user == 2: #ACCION 2 DE CONVERSION DE MONEDA
            print("Que tipo de cambio de moneda quieres hacer?")
            print("1. Soles a Dolares")
            print("2. Euros a Dolares")
            print("3. Euros a Soles")
            print("4. Soles a Euros")
            respuesta_user_conversiones = int(input("Ingresa el numero de la opcion que deseas: "))
            if respuesta_user_conversiones == 0 or respuesta_user_conversiones >= 5:
                print("Error, ingresa un numero de las opciones que se muestran")
            elif respuesta_user_conversiones == 1:
                monto_s = float(input("Ingresa el monto en Soles para cambiar a Dolares: "))
                cambio_S_D = monto_s * 0.30
                print(f"El cambio de PEN a USD son {cambio_S_D}")
            elif respuesta_user_conversiones == 2:
                monto_e = float(input("Ingresa el monto en Euros para cambiar a Dolares: "))
                cambio_EU_USD = monto_e * 1.17
                print(f"El cambio de EU a USD son {cambio_EU_USD}")
            elif respuesta_user_conversiones == 3:
                monto_e = float(input("Ingresa el monto en EU para cambiarlo a USD: "))
                cambio_EU_PEN = monto_e * 3.94
                print(f"El cambio de EU a PEN es {cambio_EU_PEN}")
            elif respuesta_user_conversiones == 4:
                monto_PEN = float(input("Ingresar el monto en PEN para cambiar a EU: "))
                cambio_PEN_EU = monto_PEN * 0.25
                print(f"El cambio de PEN a EU es {cambio_PEN_EU}")
        elif respuesta_user == 3:
            print(f"Saliendo de CalculBrahic")
            carga_cerrandosesion()
            break
def inicio_sesion():
    service_Calculbrahic_beta()

Analisis_usuario_correcto(user_input, contraseña_correcta, usuario_correcto)