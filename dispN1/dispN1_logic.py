#!/usr/bin/python

codigo1 = """
print '#################################################################'
print ''
print 'Manejo de excepciones:'
F = time.strftime("%d/%m/%Y")
H = time.strftime("%H:%M:%S")
print F + ' - ' + H

#Lee del bus de entrada
IOdirN1= 'ctrolN1/ctrolN1-IO'
ent1 = IOdirN1 + '/' + sal + repr(1)

# Lee Config. de Comando de ON/OFF remoto
#ent1FULL = os.path.join(variablesG.G_DIR_BASE, ent1)
#print ent1FULL
with open(os.path.join(variablesG.G_DIR_BASE, ent1), 'r') as f:
     UPS_OO_CONFIG = f.readlines()
     UPS_OO_CONFIG = map(int, UPS_OO_CONFIG)
     UPS_OO_CONFIG = UPS_OO_CONFIG[0]
#     print UPS_OO_CONFIG
     if (UPS_OO_CONFIG == TRUE):
       print 'UPS Remote ON/OFF Config OK!: ' + str(UPS_OO_CONFIG)

# Lee Comando de ON/OFF remoto -> APAGA UPS!
ent0 = IOdirN1 + '/' + sal + repr(0)
with open(os.path.join(variablesG.G_DIR_BASE, ent0), 'r') as f:
     UPS_OO_COM = f.readlines()
     UPS_OO_COM = map(int, UPS_OO_COM)
     UPS_OO_COM = UPS_OO_COM[0]

#Recepcion del COMANDO DE OF
     if (UPS_OO_COM == TRUE):
       print 'Exploit exitoso! :) ...'
       print 'UPS Remote ON/OFF Comando: ' + str(UPS_OO_COM) + ' - ' + '(' + F + ' - ' + H + ')'
       print 'Para retomar UPS debe reiniciar ctrolN1'

       #Puesta en cero de salidas 
       IOdirN1= 'dispN1/dispN1-IO'
       sal0 = IOdirN1 + '/' + sal + repr(0)
       with open(os.path.join(variablesG.G_DIR_BASE, sal0), 'w') as f:
     	 f.write('0')	       
       
       sal1 = IOdirN1 + '/' + sal + repr(1)
       with open(os.path.join(variablesG.G_DIR_BASE, sal1), 'w') as f:
         f.write('0')

       sal2 = IOdirN1 + '/' + sal + repr(2)
       with open(os.path.join(variablesG.G_DIR_BASE, sal2), 'w') as f:
         f.write('0')

       sal3 = IOdirN1 + '/' + sal + repr(3)
       with open(os.path.join(variablesG.G_DIR_BASE, sal3), 'w') as f:
         f.write('0')

       #Puesta en cero de entradas ctrolN1 
       IOdirN1= 'ctrolN1/ctrolN1-IO'
       ent0 = IOdirN1 + '/' + ent + repr(0)
       with open(os.path.join(variablesG.G_DIR_BASE, ent0), 'w') as f:
         f.write('0')

       ent1 = IOdirN1 + '/' + ent + repr(1)
       with open(os.path.join(variablesG.G_DIR_BASE, ent1), 'w') as f:
         f.write('0')

       ent2 = IOdirN1 + '/' + ent + repr(2)
       with open(os.path.join(variablesG.G_DIR_BASE, ent2), 'w') as f:
         f.write('0')

       ent3 = IOdirN1 + '/' + ent + repr(3)
       with open(os.path.join(variablesG.G_DIR_BASE, ent3), 'w') as f:
         f.write('0')

       #Registro de COMANDO OFF UPS y APAGADO UPS
       logger_dispN1.critical('Recepcion de Comando de Apagado: ' + str(UPS_OO_COM))
       #Apaga interfaz de UPS
       os.popen("ifconfig eth0:3 down").read()
       #Apaga Servidores *como consecuencia de apagado de UPS
       time.sleep(10)
       os.popen("ifconfig eth0:5 down").read()
       #Mata proceso UPS
       os.system("killall -9 dispN1.py")

"""

codigo2 = """
print ''
print 'Incia logica de control:'
F = time.strftime("%d/%m/%Y") 
H = time.strftime("%H:%M:%S")
print F + ' - ' + H

###################################################
#Inicializa variables de salida

IOdirN1= 'dispN1/dispN1-IO'
sal0 = IOdirN1 + '/' + sal + repr(0)
sal0FULL = os.path.join(variablesG.G_DIR_BASE, sal0)
#print sal0FULL
#x = random.random()
#x = round(x, 2)
#x = x + V_SAL
#x = str(x)
V_SAL = str(V_SAL)
print 'DispN1: estableciendo tension de salida (V): ' + V_SAL
with open(os.path.join(variablesG.G_DIR_BASE, sal0), 'w') as f:
     f.write(V_SAL)

sal1 = IOdirN1 + '/' + sal + repr(1)
#sal1FULL = os.path.join(variablesG.G_DIR_BASE, sal1)
#print sal1FULL
I_SAL = random.randint(I_SAL_MIN, I_SAL_MAX)
I_SAL = str(I_SAL)
print 'DispN1: estableciendo corriente de salida (A): ' + I_SAL
with open(os.path.join(variablesG.G_DIR_BASE, sal1), 'w') as f:
     f.write(I_SAL)

sal2 = IOdirN1 + '/' + sal + repr(2)
#sal2FULL = os.path.join(variablesG.G_DIR_BASE, sal2)
#print sal2FULL
PVA_SAL = int(V_SAL) * int(I_SAL)
PVA_SAL = str(PVA_SAL)
print 'DispN1: estableciendo potencia de salida (VA): ' + PVA_SAL
logger_dispN1.info('Potecia de salida (VA): ' + PVA_SAL)
with open(os.path.join(variablesG.G_DIR_BASE, sal2), 'w') as f:
     f.write(PVA_SAL)

IOdirN1= 'dispN1/dispN1-IO'
sal3 = IOdirN1 + '/' + sal + repr(3)
#sal3FULL = os.path.join(variablesG.G_DIR_BASE, sal3)
#print sal3FULL
TEMP_INT_UPS = random.randint(TEMP_INT_MIN, TEMP_INT_MAX)
TEMP_INT_UPS = str(TEMP_INT_UPS)
print 'DispN1: estableciendo temperatura interna UPS (C): ' + TEMP_INT_UPS
logger_dispN1.info('Temp. Interna UPS: ' + TEMP_INT_UPS)
#print w
with open(os.path.join(variablesG.G_DIR_BASE, sal3), 'w') as f:
     f.write(TEMP_INT_UPS)


################################################################
#Inicializa variables de entrada en otros disp y ctrl

#Escribe parametros en ctrolN1
 
print 'Escribe parametros de entrada en ctrolN1' 
IOdirN1= 'ctrolN1/ctrolN1-IO'

ent0 = IOdirN1 + '/' + ent + repr(0)
#ent0FULL = os.path.join(variablesG.G_DIR_BASE, ent0)
#print 'jmanuel, otra vez x:'
#print x
print 'DispN1: estableciendo tension de salida (V) en ctrolN1-entD0: ' + V_SAL
with open(os.path.join(variablesG.G_DIR_BASE, ent0), 'w') as f:
     f.write(V_SAL)

ent1 = IOdirN1 + '/' + ent + repr(1)
#ent1FULL = os.path.join(variablesG.G_DIR_BASE, ent1)
#print 'jmanuel, otra vez y:'
#print y
print 'DispN1: estableciendo corriente de salida (A) en ctrolN1-entD1: ' + I_SAL
with open(os.path.join(variablesG.G_DIR_BASE, ent1), 'w') as f:
     f.write(I_SAL)

ent2 = IOdirN1 + '/' + ent + repr(2)
#ent2FULL = os.path.join(variablesG.G_DIR_BASE, ent2)
#print 'jmanuel, otra vez z:'
#print z
print 'DispN1: estableciendo potencia de salida (VA) en ctrolN1-entD2: ' + PVA_SAL
with open(os.path.join(variablesG.G_DIR_BASE, ent2), 'w') as f:
     f.write(PVA_SAL)

ent3 = IOdirN1 + '/' + ent + repr(3)
#ent3FULL = os.path.join(variablesG.G_DIR_BASE, ent3)
#print 'jmanuel, otra vez w:'
#print w
print 'DispN1: estableciendo temperatura interna UPS (C) en ctrolN1-entD3: ' + TEMP_INT_UPS
with open(os.path.join(variablesG.G_DIR_BASE, ent3), 'w') as f:
     f.write(TEMP_INT_UPS)

"""
