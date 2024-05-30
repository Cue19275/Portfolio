import os
import numpy as np



        
def Generador_Param(Parametros):
    file = bytes(os.getcwd()+"\param.txt",encoding='utf-8')
    fileflag = os.path.exists(file)
    if(fileflag == True):
        os.remove("param.txt")
    
    with open(os.getcwd()+"\\"+"param.txt", "w") as f:
        for i in Parametros:
            f.write(".param "+i+" "+Parametros[i]+"\n")
    pass

def R1_GEN(knob):
    if (knob == 0):
         R1 = "10k"
    if (knob == 1):
         R1 = "5k"
    if (knob == 2):
         R1 = "2.4k"
    if (knob == 3):
         R1 = "1.6k"
    if (knob == 4):
         R1 = "1k"
    if (knob == 5):
         R1 = "800"
    if (knob == 6):
         R1 = "500"
    if (knob == 7):
         R1 = "400"
    if (knob == 8):
         R1 = "200"
    if (knob == 9):
         R1 = "100" 
    return R1

def R2_GEN(knob2):
    if (knob2 == 0):
         R2 = "10k"
    if (knob2 == 1):
         R2 = "5k"
    if (knob2 == 2):
         R2 = "2.4k"
    if (knob2 == 3):
         R2 = "1.6k"
    if (knob2 == 4):
         R2 = "1k"
    if (knob2 == 5):
         R2 = "800"
    if (knob2 == 6):
         R2 = "500"
    if (knob2 == 7):
         R2 = "400"
    if (knob2 == 8):
         R2 = "200"
    if (knob2 == 9):
         R2 = "100" 
    return R2
def R3_GEN(knob3):
    if (knob3 == 0):
         R3 = "10k"
    if (knob3 == 1):
         R3 = "5k"
    if (knob3 == 2):
         R3 = "2.4k"
    if (knob3 == 3):
         R3 = "1.6k"
    if (knob3 == 4):
         R3 = "1k"
    if (knob3 == 5):
         R3 = "800"
    if (knob3 == 6):
         R3 = "500"
    if (knob3 == 7):
         R3 = "400"
    if (knob3 == 8):
         R3 = "200"
    if (knob3 == 9):
         R3 = "100" 
    return R3
def R4_GEN(knob4):
    if (knob4 == 0):
         R4 = "10k"
    if (knob4 == 1):
         R4 = "5k"
    if (knob4 == 2):
         R4 = "2.4k"
    if (knob4 == 3):
         R4 = "1.6k"
    if (knob4 == 4):
         R4 = "1k"
    if (knob4 == 5):
         R4 = "800"
    if (knob4 == 6):
         R4 = "500"
    if (knob4 == 7):
         R4 = "400"
    if (knob4 == 8):
         R4 = "200"
    if (knob4 == 9):
         R4 = "100" 
    return R4
def R5_GEN(knob5):
    if (knob5 == 0):
         R5 = "10k"
    if (knob5 == 1):
         R5 = "5k"
    if (knob5 == 2):
         R5 = "2.4k"
    if (knob5 == 3):
         R5 = "1.6k"
    if (knob5 == 4):
         R5 = "1k"
    if (knob5 == 5):
         R5 = "800"
    if (knob5 == 6):
         R5 = "500"
    if (knob5 == 7):
         R5 = "400"
    if (knob5 == 8):
         R5 = "200"
    if (knob5 == 9):
         R5 = "100" 
    return R5
def R6_GEN(knob6):
    if (knob6 == 0):
         R6 = "10k"
    if (knob6 == 1):
         R6 = "5k"
    if (knob6 == 2):
         R6 = "2.4k"
    if (knob6 == 3):
         R6 = "1.6k"
    if (knob6 == 4):
         R6 = "1k"
    if (knob6 == 5):
         R6 = "800"
    if (knob6 == 6):
         R6 = "500"
    if (knob6 == 7):
         R6 = "400"
    if (knob6 == 8):
         R6 = "200"
    if (knob6 == 9):
         R6 = "100" 
    return R6
def R7_GEN(knob7):
    if (knob7 == 0):
         R7 = "10k"
    if (knob7 == 1):
         R7 = "5k"
    if (knob7 == 2):
         R7 = "2.4k"
    if (knob7 == 3):
         R7 = "1.6k"
    if (knob7 == 4):
         R7 = "1k"
    if (knob7 == 5):
         R7 = "800"
    if (knob7 == 6):
         R7 = "500"
    if (knob7 == 7):
         R7 = "400"
    if (knob7 == 8):
         R7 = "200"
    if (knob7 == 9):
         R7 = "100" 
    return R7
def R8_GEN(knob8):
    if (knob8 == 0):
         R8 = "25k"
    if (knob8 == 1):
         R8 = "10k"
    if (knob8 == 2):
         R8 = "5k"
    if (knob8 == 3):
         R8 = "2.5k"
    if (knob8 == 4):
         R8 = "1k"
    if (knob8 == 5):
         R8 = "800"
    if (knob8 == 6):
         R8 = "500"
    if (knob8 == 7):
         R8 = "100"
    if (knob8 == 8):
         R8 = "50"
    if (knob8 == 9):
         R8 = "25" 
    return R8
def R9_GEN(knob9):
    if (knob9 == 0):
         R9 = "25k"
    if (knob9 == 1):
         R9 = "10k"
    if (knob9 == 2):
         R9 = "5k"
    if (knob9 == 3):
         R9 = "2.5k"
    if (knob9 == 4):
         R9 = "1k"
    if (knob9 == 5):
         R9 = "800"
    if (knob9 == 6):
         R9 = "500"
    if (knob9 == 7):
         R9 = "100"
    if (knob9 == 8):
         R9 = "50"
    if (knob9 == 9):
         R9 = "25" 
    return R9

        






