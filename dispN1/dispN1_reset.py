#!/usr/bin/python
#print 'Este es el codigo de logica'
import threading
import os
import errno
import sys
import time
#Importa Objetos del Sistema de Control Industrial (SCI)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import variablesG

ent = 'entD'

print ' ' 
print 'Reincia valores de entrada de dispN1 para que arranque:'
F = time.strftime("%d/%m/%Y")
H = time.strftime("%H:%M:%S")
print F + ' - ' + H

IOdirN1= 'dispN1/dispN1-IO'
ent0 = IOdirN1 + '/' + ent + repr(0)
ent0FULL = os.path.join(variablesG.G_DIR_BASE, ent0)
print 'Comando UPS_OO_CONFIG: ' + ent0FULL + ' -> 0'
with open(os.path.join(variablesG.G_DIR_BASE, ent0), 'w') as f:
     f.write('0')

ent1 = IOdirN1 + '/' + ent + repr(1)
ent1FULL = os.path.join(variablesG.G_DIR_BASE, ent1)
print 'Comando UPS_OO_COM: ' + ent1FULL + ' -> 1'
with open(os.path.join(variablesG.G_DIR_BASE, ent1), 'w') as f:
     f.write('1')

#Enciende interfaz de UPS
os.popen("ifconfig eth0:3 up").read()
#Enciende Servidores *como consecuencia de apagado de UPS
time.sleep(3)
os.popen("ifconfig eth0:5 up").read()

time.sleep(3)
os.popen("/etc/init.d/networking restart").read()

