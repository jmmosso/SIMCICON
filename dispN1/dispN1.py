#!/usr/bin/python -B

#Comentarios
#dispN1 = UPS
#Param. Constantes: tension, corriente y potencia de salida, con dos decimales
#Param. Variables: temperatura interna, entre MIN y MAX

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

#Importa Objetos del Sistema de Control Industrial (SCI)
import dispN1_logic
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import variablesG

#Incializacion LOG
logger_dispN1 = logging.getLogger('dispN1')
hdlr = logging.handlers.RotatingFileHandler(variablesG.G_DIR_LOGSRV + 'dispN1.log', maxBytes=200000,  backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s - %(message)s')
hdlr.setFormatter(formatter)
logger_dispN1.addHandler(hdlr)
logger_dispN1.setLevel(logging.INFO)

###################################################################
#Inicializacion de la controladora
###################################################################
logger_dispN1.critical('Inicio de dispositivo 1')

##################################################################
#Variables locales
TRUE = 1
# Parametros de salida, simplificamos a una sola fase (Mono, Fase A)
V_SAL = 220		# (Voltios), tension nominal de salida
I_SAL = 230		# (Amperes), corriente nominal de salida
I_SAL_MIN = 190
I_SAL_MAX = 203
PW_SAL = 40000		# (Watts), potencia para 400W * 100 Servidores en la salida
PVA_SAL = 50000		# (Volt Amperes), potencia de salida 
			# [ PVA_SAL = V_SAL * I_SAL * FI_SAL ], [PW_SAL = PVA_SAL * 0.8]
FI_SAL = 0.8		# Factor de correccion
FREC_SAL = 50		# (Hertz) en la salida
# Temperatura Interna
TEMP_INT_MIN = 15	# Grados centigrados C
TEMP_INT_MAX = 21

#Creacion de variables I/O (en subdir de ./ )
#Directorio que contiene a las variables
IOdirN1= 'dispN1-IO'
try:
    os.makedirs(IOdirN1)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
    else:
        print "\nAdvertencia! Directorio %s ya existe." % IOdirN1

#Crea Variables I/O-O digitales
sal = 'salD'
salN = 4
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
entN = 4
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

###################################################################
#Inicializa variables de entrada 
IOdirN1= 'dispN1/dispN1-IO'

# Comando UPS ON/OFF
ent0 = IOdirN1 + '/' + ent + repr(0)
ent0FULL = os.path.join(variablesG.G_DIR_BASE, ent0)
print ent0FULL
with open(os.path.join(variablesG.G_DIR_BASE, ent0), 'w') as f:
     f.write('0')

# Activar configuracion UPS ON/OFF 
ent1 = IOdirN1 + '/' + ent + repr(1)
ent1FULL = os.path.join(variablesG.G_DIR_BASE, ent1)
print ent1FULL
with open(os.path.join(variablesG.G_DIR_BASE, ent1), 'w') as f:
     f.write('1')


###################################################################
#Aqui comienza el codigo de la controladora
###################################################################


#Ejecuta el codigo una unica vez
#exec ctrolN1_logic.codigo1

#Ejecuta el codigo una vez por segundo, para siempre (hasta CTROL-C), import threading
def looper():    
    # i es el intervalo en segundos    
    threading.Timer(3, looper).start()    
    # codigo a ejecutar
    exec dispN1_logic.codigo1
    exec dispN1_logic.codigo2
#para iniciar 
looper()

def signal_handler(signal, frame):
 print ('Ha detenido el dispN1.')
 logger_dispN1.critical('Apagado del dispositivo 1')
 sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

