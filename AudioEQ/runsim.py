import subprocess
import os
#Librería creada por Carlos Cuellar, en Marzo 2021
#Esta librería esta diseñada para llevar a cabo simulaciones de ltspice

#Está función está diseñada para correr la simulación preparada dentro de su circuito de LTSPICE
#Que tenga como salida la exportación de archivos wav, dado a que el programa correra en batchmode
#Debe de tener LTSPICE instalado en el disco C en la carpeta de program files
def AudioProcessing():
    #Aqui el input debe de incluir tanto el nombre como la terminacion .asc
    name = "Test.asc"
    file = bytes("-Run "+os.getcwd()+"\\"+name+" \n", encoding='utf-8')
    proc = subprocess.Popen('cmd.exe',stdin=subprocess.PIPE)
    proc.stdin.write(b'"C:\\Program Files\\LTC\\LTspiceXVII\\')
    proc.stdin.write(b'XVIIx64.exe" -b '+file)
    proc.stdin.write(b"cd\n")
    proc.stdin.close()
    proc.wait()
    pass


