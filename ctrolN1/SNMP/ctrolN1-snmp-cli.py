#!/usr/bin/python -B
from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
    cmdgen.CommunityData('public'),
    cmdgen.UdpTransportTarget(('localhost', 161)),

#viene en el ejemplo
#    'iso.3.6.1.2.1.1.1.0'

#1.3.6.1.4.1.42.1.0 = 470 (NO ATACA)
#    'iso.3.6.1.4.1.42.1.0'

#1.3.6.1.4.1.42.2.0 = Controladora ECD1 (NO ATACA)
#    'iso.3.6.1.4.1.42.2.0'

#1.3.6.1.4.1.42.4.0 = ECD1 (NO ATACA)
#    'iso.3.6.1.4.1.42.4.0'

#1.3.6.1.4.1.42.5.0 = ABF012139FFA34S1543F0KK1P19BF (SI ATACA)
#    'iso.3.6.1.4.1.42.5.0'

#1.3.6.1.4.1.42.6.0 = 5.7 (NO ATACA)
    'iso.3.6.1.4.1.42.6.0'


)
print('\n'.join([ '%s = %s' % varBind for varBind in varBinds]))
