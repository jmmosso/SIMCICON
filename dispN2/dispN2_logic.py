#!/usr/bin/python

codigo2 = """
print '##########################################################'
print ''
print 'Incia logica de control:'
F = time.strftime("%d/%m/%Y")
H = time.strftime("%H:%M:%S")
print F + ' - ' + H


###################################################

#Inicializa variables de salida 
IOdirN1= 'dispN2/dispN2-IO'
sal0 = IOdirN1 + '/' + sal + repr(0)
sal0FULL = os.path.join(variablesG.G_DIR_BASE, sal0)
#print sal0FULL
x = variablesG.G_TEMP_AMB_MIN
y = variablesG.G_TEMP_AMB_MAX
z = random.randint(x, y)
z = str(z)
print 'dispN2 - escribe Temp. Ambiente en salD0: ' + z
with open(os.path.join(variablesG.G_DIR_BASE, sal0), 'w') as f:
     f.write(z)
logger_dispN2.info('Temp. Amb.: ' + z)

#Escribe Temperatura ambiente en ctrolN1-ent4 
IOdirN1= 'ctrolN1/ctrolN1-IO'
ent4 = IOdirN1 + '/' + ent + repr(4)
ent4FULL = os.path.join(variablesG.G_DIR_BASE, ent4)
print 'dispN2 - escribe Temp. Ambiente en ctrolN1-entD4: ' + z
with open(os.path.join(variablesG.G_DIR_BASE, ent4), 'w') as f:
     f.write(z)
"""
