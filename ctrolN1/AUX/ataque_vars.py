#!/usr/bin/python

#Librerias de python
import threading
import os
import errno
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import variablesG

IOdirN1= 'ctrolN1/ctrolN1-IO'
ent = 'entD'

ent3 = IOdirN1 + '/' + ent + repr(3)
ent3FULL = os.path.join(variablesG.G_DIR_BASE, ent3)
print ent3FULL
x = 25 
z = str(x)
with open(os.path.join(variablesG.G_DIR_BASE, ent3), 'w') as f:
     f.write(z)

ent4 = IOdirN1 + '/' + ent + repr(4)
ent4FULL = os.path.join(variablesG.G_DIR_BASE, ent4)
print ent4FULL
x = 12
z = str(x)
with open(os.path.join(variablesG.G_DIR_BASE, ent4), 'w') as f:
     f.write(z)
