#!/usr/bin/python -B
#Librerias de python
import threading
import os
import errno
import sys
import random
import time
import signal
import logging
import logging.handlers
import subprocess

#Importa Objetos del Sistema de Control Industrial (SCI)
import dispN2_logic
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import variablesG

#Incializacion LOG
logger_dispN2 = logging.getLogger('dispN2')
hdlr = logging.handlers.RotatingFileHandler(variablesG.G_DIR_LOGSRV + 'dispN2.log', maxBytes=200000, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s - %(message)s')
hdlr.setFormatter(formatter)
logger_dispN2.addHandler(hdlr)
logger_dispN2.setLevel(logging.INFO)

#Inicia placa de red
#os.popen("ifconfig eth0:6 10.0.119.156 up").read()

###################################################################
#Inicializacion de la controladora
###################################################################
#Importa Objetos del Sistema de Control Industrial (SCI)
logger_dispN2.critical('Inicio de dispositivo 2')

import dispN2_logic
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import variablesG

#Variables locales
TRUE = 1

#Creacion de variables I/O (en subdir de ./ )
#Directorio que contiene a las variables
IOdirN1= 'dispN2-IO'
try:
    os.makedirs(IOdirN1)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
    else:
        print "\nAdvertencia! Directorio %s ya existe." % IOdirN1

#Crea Variables I/O-O digitales
sal = 'salD'
salN = 1
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
entN = 1
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


###################################################################
#Aqui comienza el codigo de la controladora
###################################################################

#subprocess.Popen("/sbin/ifconfig eth0:6 10.0.119.156", shell=False)


#Ejecuta el codigo una unica vez
#exec ctrolN1_logic.codigo1

#Ejecuta el codigo una vez por segundo, para siempre (hasta CTROL-C), import threading
def looper():    
    # i es el intervalo en segundos    
    threading.Timer(6, looper).start()    
    # codigo a ejecutar
    exec dispN2_logic.codigo2
#para iniciar 
looper()


def signal_handler(signal, frame):
 print ('Ha detenido el dispN2.')
 logger_dispN2.critical('Apagado del dispositivo 2')
# os.popen("ifconfig eth0:6 down").read()
 sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

