#!/usr/bin/python -B
from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
    cmdgen.CommunityData('public'),
    cmdgen.UdpTransportTarget(('localhost', 161)),
#    'iso.3.6.1.4.1.42.2.0'
    'iso.3.6.1.4.1.42.1.0'
)

print('\n'.join([ '%s = %s' % varBind for varBind in varBinds]))


errorIndication, errorStatus, errorIndex, varBinds1 = cmdGen.getCmd(
    cmdgen.CommunityData('public'),
    cmdgen.UdpTransportTarget(('localhost', 161)),
#    'iso.3.6.1.4.1.42.3.0'
#    'iso.3.6.1.4.1.42.1.0'
     'iso.3.6.1.2.1.1.3.0'
)

print('\n'.join([ '%s = %s' % varBind for varBind in varBinds1]))

