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
import variablesG

#Incializacion LOG
logger_ctrolN1 = logging.getLogger('ctrolN1')
hdlr = logging.handlers.RotatingFileHandler(variablesG.G_DIR_LOGSRV + 'ctrolN1.log', maxBytes=20000, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s - %(message)s')
hdlr.setFormatter(formatter)
logger_ctrolN1.addHandler(hdlr)
logger_ctrolN1.setLevel(logging.INFO)

