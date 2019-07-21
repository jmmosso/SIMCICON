#!/usr/bin/python
#print 'Este es el codigo de logica'

codigo1 = """
print '#################################################################'
print ''
print 'Manejo de excepciones:'
F = time.strftime("%d/%m/%Y")
H = time.strftime("%H:%M:%S")
print F + ' - ' + H

IOdirN1= 'ctrolN1/ctrolN1-IO'
#lee temp amb
ent4 = IOdirN1 + '/' + ent + repr(4)
#ent4FULL = os.path.join(variablesG.G_DIR_BASE, ent4)
#print ent4FULL
with open(os.path.join(variablesG.G_DIR_BASE, ent4), 'r') as f:
     TAMB = f.readlines()
     TAMB = map(int, TAMB)
     TAMB = TAMB[0]
     print 'TAMB = ' + str(TAMB)

#lee temp UPS
ent3 = IOdirN1 + '/' + ent + repr(3)
#ent3FULL = os.path.join(variablesG.G_DIR_BASE, ent3)
#print ent3FULL
with open(os.path.join(variablesG.G_DIR_BASE, ent3), 'r') as f:
     TUPS = f.readlines()
     TUPS = map(int, TUPS)
     TUPS = TUPS[0]
     print 'TUPS = ' + str(TUPS)

#Trata el caso de que una temp supere max y la otra no
var1 = TAMB > TEMP_AMB_MAX
var2 = TUPS > TEMP_UPS_MAX
if (var1 != var2):
    print 'Temperatura Sistema UPS OK (salD2=0)'
    sal2 = IOdirN1 + '/' + sal + repr(2)
    with open(os.path.join(variablesG.G_DIR_BASE, sal2), 'w') as f:
       f.write('0')

if (TAMB > TEMP_AMB_MAX):
    if (TUPS > TEMP_UPS_MAX):
     	print 'Excepcion 1: Entrando en exploit (salD2=0)'
	print 'Temperatura Sistema UPS OK (salD2=0)'
        sal2 = IOdirN1 + '/' + sal + repr(2)
	with open(os.path.join(variablesG.G_DIR_BASE, sal2), 'w') as f:
           f.write('0')

	print 'Disparando comando de reinicio de UPS OK (salD0=1)'
        sal0 = IOdirN1 + '/' + sal + repr(0)
        with open(os.path.join(variablesG.G_DIR_BASE, sal0), 'w') as f:
           f.write('1')


else:
     print 'Temperatura Sistema UPS OK (salD2=0)'
     sal2 = IOdirN1 + '/' + sal + repr(2)
#     sal2FULL = os.path.join(variablesG.G_DIR_BASE, sal2)
#     print sal2FULL
     with open(os.path.join(variablesG.G_DIR_BASE, sal2), 'w') as f:
        f.write('0')
"""

codigo2 = """
print ''
print 'Incia logica de control:'
F = time.strftime("%d/%m/%Y")
H = time.strftime("%H:%M:%S")
print F + ' - ' + H

#Inicializa variables en dispN1
# Comando UPS ON/OFF
#IOdirN1= 'dispN1/dispN1-IO'
#ent0 = IOdirN1 + '/' + ent + repr(0)
#ent0FULL = os.path.join(variablesG.G_DIR_BASE, ent0)
#print ent0FULL
#with open(os.path.join(variablesG.G_DIR_BASE, ent0), 'w') as f:
#     f.write('0')

# Config UPS ON/OFF Remota
#ent1 = IOdirN1 + '/' + ent + repr(1)
#ent1FULL = os.path.join(variablesG.G_DIR_BASE, ent1)
#print ent1FULL
#with open(os.path.join(variablesG.G_DIR_BASE, ent1), 'w') as f:
#     f.write('0')

"""
