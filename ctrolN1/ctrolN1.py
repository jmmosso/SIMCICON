#!/usr/bin/python -B
#Librerias de python
import threading
import os
import errno
import sys
import time
import subprocess
import signal
import logging
import logging.handlers
import hashlib

#Importa Objetos del Sistema de Control Industrial (SCI)
import ctrolN1_logic
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import variablesG

#Incializacion LOG
logger_ctrolN1 = logging.getLogger('ctrolN1')
hdlr = logging.handlers.RotatingFileHandler(variablesG.G_DIR_LOGSRV + 'ctrolN1.log', maxBytes=200000, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s - %(message)s')
hdlr.setFormatter(formatter)
logger_ctrolN1.addHandler(hdlr)
logger_ctrolN1.setLevel(logging.INFO)

###################################################################
#Inicializacion de la controladora
###################################################################
logger_ctrolN1.critical('Inicio de controladora 1')

#Variables locales
TRUE = 1
TEMP_AMB_MAX = 8
TEMP_UPS_MAX = 21

#Creacion de variables I/O (en subdir de ./ )
#Directorio que contiene a las variables
IOdirN1= 'ctrolN1-IO'
try:
    os.makedirs(IOdirN1)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
    else:
        print "\nAdvertencia! Directorio %s ya existe." % IOdirN1

#Crea Variables I/O-O digitales
sal = 'salD'
salN = 6
for x in xrange(salN):
     nombre1 = IOdirN1 + '/' + sal + repr(x)
     try:
       	file = open(nombre1,'w')   
       	file.close()
     except OSError as exception:
	if exception.errno != errno.EEXIST:
          raise
	else:
	  print "\nAdvertencia! Archivo %s ya existe." % nombre
else:
    print 'Se han creado %d ' % salN + 'variables de salida digital'

#Crea Variables I/O-I digitales
ent = 'entD'
entN = 6
for x in xrange(entN):
     nombre2 = IOdirN1 + '/' + ent + repr(x)
     try:
        file = open(nombre2,'w')
        file.close()
     except OSError as exception:
        if exception.errno != errno.EEXIST:
          raise
        else:
          print "\nAdvertencia! Archivo %s ya existe." % nombre
else:
    print 'Se han creado %d ' % entN + 'variables de entrada digital'


#Uso de variables Globales (G)
#print variablesG.G_DIR_BASE
#print variablesG.G_TEMP_AMB

#######################################################################
#Inicializa variables de salida 
print 'Inicializa variables de salida:'
IOdirN1= 'ctrolN1/ctrolN1-IO'

sal0 = IOdirN1 + '/' + sal + repr(0)
#sal0FULL = os.path.join(variablesG.G_DIR_BASE, sal0)
#print sal0FULL
with open(os.path.join(variablesG.G_DIR_BASE, sal0), 'w') as f:
     f.write('0')

sal1 = IOdirN1 + '/' + sal + repr(1)
#sal1FULL = os.path.join(variablesG.G_DIR_BASE, sal1)
#print sal1FULL
with open(os.path.join(variablesG.G_DIR_BASE, sal1), 'w') as f:
     f.write('1')

sal2 = IOdirN1 + '/' + sal + repr(2)
#sal2FULL = os.path.join(variablesG.G_DIR_BASE, sal2)
#print sal2FULL
with open(os.path.join(variablesG.G_DIR_BASE, sal2), 'w') as f:
     f.write('0')

#######################################################################
#Inicializa variables de entrada necesarias para que funcione la logica
#despues estas son escritas por los dispositivos del SCI
print 'Inicializa variables de entrada *necesarias para logica:' 

ent3 = IOdirN1 + '/' + ent + repr(3)
#ent3FULL = os.path.join(variablesG.G_DIR_BASE, ent3)
#print ent3FULL
with open(os.path.join(variablesG.G_DIR_BASE, ent3), 'w') as f:
     f.write('16')

ent4 = IOdirN1 + '/' + ent + repr(4)
#ent4FULL = os.path.join(variablesG.G_DIR_BASE, ent4)
#print ent4FULL
with open(os.path.join(variablesG.G_DIR_BASE, ent4), 'w') as f:
     f.write('7')


###################################################################
#Aqui comienza el codigo de la controladora
###################################################################
#Inicio del servidor SNMP
logger_ctrolN1.info('Inicio de servicio SNMP en controladora 1')
subprocess.Popen("./ctrolN1-snmp-srv.py", shell=False)
time.sleep(3)

#Calculo de MD5 de logica, si cambia de la ultima genera log
file_name = 'ctrolN1_logic.py'      
original_md5 = 'e8a515a2d9ef13b5525f98f0b7d641e8'

with open(file_name) as file_to_check:
    # read contents of the file
    data = file_to_check.read()    
    # pipe contents of the file through
    md5_returned = hashlib.md5(data).hexdigest()
    print ' '
    print '------------------------- ' 
    print 'verificacion MD5'
    print '------------------------- ' 
    print md5_returned

if original_md5 == md5_returned:
    print "MD5 valida."
    time.sleep(2)

else:
    print "MD5 ha cambiado desde la ultima vez que incio ctrolN1!."
    logger_ctrolN1.critical('La logica de ctrolN1 ha cambiado (alteracion MD5)')
    time.sleep(2)


#Ejecuta el codigo una unica vez
#exec ctrolN1_logic.codigo1

#Ejecuta el codigo una vez por segundo, para siempre (hasta CTROL-C), import threading
def looper():    
    # i es el intervalo en segundos    
    threading.Timer(3, looper).start()    
    # codigo a ejecutar
    exec ctrolN1_logic.codigo1
    exec ctrolN1_logic.codigo2
#para iniciar 
looper()

def signal_handler(signal, frame):
 print ('Ha detenido la ctrolN1.')
 logger_ctrolN1.critical('Apagado de la controladora 1')
 sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

