#!/usr/bin/python
#https://docs.python.org/2.6/library/logging.html
import logging
import logging.handlers

logger_dispN1 = logging.getLogger('ECD_dispN1')


hdlr = logging.handlers.RotatingFileHandler('registro.log', maxBytes=2000, backupCount=5)
#hdlr = logging.FileHandler('registro.log')

formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s - %(message)s')
hdlr.setFormatter(formatter)
logger_dispN1.addHandler(hdlr)
logger_dispN1.setLevel(logging.WARNING)

logger_dispN1.debug('Esto es un debug_dispN1')
logger_dispN1.critical('Esto es un critico_dispN1')
logger_dispN1.error('Esto es un error_dispN1')
logger_dispN1.info('Esto es informativo_dispN1')
logger_dispN1.warning('Esto es advertencia _dispN1')

