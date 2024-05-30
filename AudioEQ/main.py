import runsim 
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import numpy as np
import subprocess
import ValueGenerator
from layout import *

class SKETCH (QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ejecutar_push)
        self.dial.valueChanged.connect(self.dial_barra)
        self.dial_4.valueChanged.connect(self.dial_barra2)
        self.dial_2.valueChanged.connect(self.dial_barra3)
        self.dial_5.valueChanged.connect(self.dial_barra4)
        self.dial_6.valueChanged.connect(self.dial_barra5)
        self.dial_7.valueChanged.connect(self.dial_barra6)
        self.dial_3.valueChanged.connect(self.dial_barra7)
        self.sp1.valueChanged.connect(self.sliderfun)
        self.genr.currentIndexChanged.connect(self.preset)
        self.update()
    def preset(self):
        if (self.genr.currentIndex() == 0):
            self.dial.setValue(0)
            self.dial_4.setValue(0)
            self.dial_2.setValue(0)
            self.dial_5.setValue(0)
            self.dial_6.setValue(0)
            self.dial_7.setValue(0)
            self.dial_3.setValue(0)
        elif (self.genr.currentIndex() == 1):
            self.dial.setValue(8)
            self.dial_4.setValue(8)
            self.dial_2.setValue(5)
            self.dial_5.setValue(5)
            self.dial_6.setValue(3)
            self.dial_7.setValue(6)
            self.dial_3.setValue(5)
        elif (self.genr.currentIndex() == 2):
            self.dial.setValue(7)
            self.dial_4.setValue(7)
            self.dial_2.setValue(6)
            self.dial_5.setValue(4)
            self.dial_6.setValue(4)
            self.dial_7.setValue(7)
            self.dial_3.setValue(7)
        elif (self.genr.currentIndex() == 3):
            self.dial.setValue(4)
            self.dial_4.setValue(4)
            self.dial_2.setValue(5)
            self.dial_5.setValue(7)
            self.dial_6.setValue(7)
            self.dial_7.setValue(5)
            self.dial_3.setValue(4)
            
        pass
    
        
    def sliderfun(self):
        print(self.sp1.value())
        pass
    
    
    def dial_barra(self):
        self.progressBar.setProperty("value", self.dial.value())
        d1 = self.dial.value()
        if (d1 == 0):
            self.db1.setText("-20db")
        elif (d1 == 1):
            self.db1.setText("-14db")
        elif (d1 == 2):
            self.db1.setText("-7.6db")
        elif (d1 == 3):
            self.db1.setText("-4db")
        elif (d1 == 4):
            self.db1.setText("0db")
        elif (d1 == 5):
            self.db1.setText("2db")
        elif (d1 == 6):
            self.db1.setText("6db")
        elif (d1 == 7):
            self.db1.setText("8db")
        elif (d1 == 8):
            self.db1.setText("14db")
        elif (d1 == 9):
            self.db1.setText("20db")
        
    def dial_barra2(self):
        self.progressBar_2.setProperty("value", self.dial_4.value())
        d2 = self.dial_4.value()
        if (d2 == 0):
            self.db2.setText("-20db")
        elif (d2 == 1):
            self.db2.setText("-14db")
        elif (d2 == 2):
            self.db2.setText("-7.6db")
        elif (d2 == 3):
            self.db2.setText("-4db")
        elif (d2 == 4):
            self.db2.setText("0db")
        elif (d2 == 5):
            self.db2.setText("2db")
        elif (d2 == 6):
            self.db2.setText("6db")
        elif (d2 == 7):
            self.db2.setText("8db")
        elif (d2 == 8):
            self.db2.setText("14db")
        elif (d2 == 9):
            self.db2.setText("20db")
        
    def dial_barra3(self):
        self.progressBar_4.setProperty("value", self.dial_2.value())
        d3 = self.dial_2.value()
        if (d3 == 0):
            self.db3.setText("-20db")
        elif (d3 == 1):
            self.db3.setText("-14db")
        elif (d3 == 2):
            self.db3.setText("-7.6db")
        elif (d3 == 3):
            self.db3.setText("-4db")
        elif (d3 == 4):
            self.db3.setText("0db")
        elif (d3 == 5):
            self.db3.setText("2db")
        elif (d3 == 6):
            self.db3.setText("6db")
        elif (d3 == 7):
            self.db3.setText("8db")
        elif (d3 == 8):
            self.db3.setText("14db")
        elif (d3 == 9):
            self.db3.setText("20db")
    def dial_barra4(self):
        self.progressBar_3.setProperty("value", self.dial_5.value())
        d4 = self.dial_5.value()
        if (d4 == 0):
            self.db4.setText("-20db")
        elif (d4 == 1):
            self.db4.setText("-14db")
        elif (d4 == 2):
            self.db4.setText("-7.6db")
        elif (d4 == 3):
            self.db4.setText("-4db")
        elif (d4 == 4):
            self.db4.setText("0db")
        elif (d4 == 5):
            self.db4.setText("2db")
        elif (d4 == 6):
            self.db4.setText("6db")
        elif (d4 == 7):
            self.db4.setText("8db")
        elif (d4 == 8):
            self.db4.setText("14db")
        elif (d4 == 9):
            self.db4.setText("20db")
    def dial_barra5(self):
        self.progressBar_7.setProperty("value", self.dial_6.value())
        d5 = self.dial_6.value()
        if (d5 == 0):
            self.db5.setText("-20db")
        elif (d5 == 1):
            self.db5.setText("-14db")
        elif (d5 == 2):
            self.db5.setText("-7.6db")
        elif (d5 == 3):
            self.db5.setText("-4db")
        elif (d5 == 4):
            self.db5.setText("0db")
        elif (d5 == 5):
            self.db5.setText("2db")
        elif (d5 == 6):
            self.db5.setText("6db")
        elif (d5 == 7):
            self.db5.setText("8db")
        elif (d5 == 8):
            self.db5.setText("14db")
        elif (d5 == 9):
            self.db5.setText("20db")
    def dial_barra6(self):
        self.progressBar_5.setProperty("value", self.dial_7.value())
        d6 = self.dial_7.value()
        if (d6 == 0):
            self.db6.setText("-20db")
        elif (d6 == 1):
            self.db6.setText("-14db")
        elif (d6 == 2):
            self.db6.setText("-7.6db")
        elif (d6 == 3):
            self.db6.setText("-4db")
        elif (d6 == 4):
            self.db6.setText("0db")
        elif (d6 == 5):
            self.db6.setText("2db")
        elif (d6 == 6):
            self.db6.setText("6db")
        elif (d6 == 7):
            self.db6.setText("8db")
        elif (d6 == 8):
            self.db6.setText("14db")
        elif (d6 == 9):
            self.db6.setText("20db")
    def dial_barra7(self):
        self.progressBar_6.setProperty("value", self.dial_3.value())
        d7 = self.dial_3.value()
        if (d7 == 0):
            self.db7.setText("-20db")
        elif (d7 == 1):
            self.db7.setText("-14db")
        elif (d7 == 2):
            self.db7.setText("-7.6db")
        elif (d7 == 3):
            self.db7.setText("-4db")
        elif (d7 == 4):
            self.db7.setText("0db")
        elif (d7 == 5):
            self.db7.setText("2db")
        elif (d7 == 6):
            self.db7.setText("6db")
        elif (d7 == 7):
            self.db7.setText("8db")
        elif (d7 == 8):
            self.db7.setText("14db")
        elif (d7 == 9):
            self.db7.setText("20db")
    
    def ejecutar_push(self):
        print("fase 1")
        knob = self.dial.value() #9
        knob2 = self.dial_4.value()
        knob3 = self.dial_2.value()
        knob4 = self.dial_5.value()
        knob5 = self.dial_6.value()
        knob6 = self.dial_7.value()
        knob7 = self.dial_3.value()
        knob8 = self.sp1.value()
        knob9 = self.sp2.value()
        if (self.Distorsion.isChecked() == False):
           print("NoCheque")
           R10 = "1k"
           R11 =  "100Meg"
           
        else:
            print("Cheque")
            R10 = "100Meg"
            R11 =  "1K"
        print("fase 2")
        R1 = ValueGenerator.R1_GEN(knob)
        print("!")
        R2 = ValueGenerator.R2_GEN(knob2)
        print("!")
        R3 = ValueGenerator.R3_GEN(knob3)
        print("!")
        R4 = ValueGenerator.R4_GEN(knob4)
        print("!")
        R5 = ValueGenerator.R5_GEN(knob5)
        print("!")
        R6 = ValueGenerator.R6_GEN(knob6)
        print("!")
        R7 = ValueGenerator.R7_GEN(knob7)
        print("!")
        R8 = ValueGenerator.R8_GEN(knob8)
        print("finish")
        R9 = ValueGenerator.R9_GEN(knob9)
        print("fase 3")
        ParaX = {
            "R1" : R1,
            "R2" : R2,
            "R3" : R3,
            "R4" : R4,
            "R5" : R5,
            "R6" : R6,
            "R7" : R7,
            "R8" : R8,
            "R9" : R9,
            "R10" : R10,
            "R11" : R11,
            "time" : "10"
        }
        print("fase 4")
        ValueGenerator.Generador_Param(ParaX)
        print(ParaX)
        runsim.AudioProcessing()
    
aplication = QtWidgets.QApplication([])
ventanamain=SKETCH()
ventanamain.show()
aplication.exec_()
