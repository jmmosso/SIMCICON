#!/usr/bin/python -B
from pysnmp.entity import engine, config
from pysnmp import debug
from pysnmp.entity.rfc3413 import cmdrsp, context, ntforg
from pysnmp.carrier.asynsock.dgram import udp
from pysnmp.smi import builder

import threading
import collections
import time

import os
import errno

#import subprocess
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import variablesG



#can be useful
#debug.setLogger(debug.Debug('all'))

MibObject = collections.namedtuple('MibObject', ['mibName',
                                   'objectType', 'valueFunc'])

class Mib(object):
    """Stores the data we want to serve. 
    """

    def __init__(self):
        self._lock = threading.RLock()
        self._test_count = 0

    def getTestDescription(self):
        return "Controladora ECD1"

    def getTestDescription1(self):
        return "ECD1"

    def getTestDesc(self):
	print '#!//////////////////////////////////////////////////////'
        print 'Anomalia de funcionamiento en servidor SNMP'
	print '#!//////////////////////////////////////////////////////'
	#subprocess.call("./ataque_vars.py", shell=False)
	
	IOdirN1= 'ctrolN1/ctrolN1-IO'
	ent = 'entD'
	ent3 = IOdirN1 + '/' + ent + repr(3)
	x = 25
	z = str(x)
	with open(os.path.join(variablesG.G_DIR_BASE, ent3), 'w') as f:
     	   f.write(z)

	ent4 = IOdirN1 + '/' + ent + repr(4)
	x = 12
	z = str(x)
	with open(os.path.join(variablesG.G_DIR_BASE, ent4), 'w') as f:
     	   f.write(z)

#	time.sleep(10)
#	os.popen("ifconfig eth0:3 down").read()

	return "ABF012139FFA34S1543F0KK1P19BF"

        

    def getTestDesc2(self):
        return "5.7"

    def getTestCount(self):
        with self._lock:
            return self._test_count

######################################


#    	    JM = 'variable'
#     	    try:
#        	file = open(JM,'w')
#        	file.close()
#     	    except OSError as exception:
#        	if exception.errno != errno.EEXIST:
#          	 raise
#            else:
#                print "\nAdvertencia! Archivo %s ya existe." % JM

#            with open(JM, 'w') as f:
#                f.write('1')



#####################################


    def setTestCount(self, value):
        with self._lock:
            self._test_count = value


def createVariable(SuperClass, getValue, *args):
    """This is going to create a instance variable that we can export. 
    getValue is a function to call to retreive the value of the scalar
    """
    class Var(SuperClass):
        def readGet(self, name, *args):
            return name, self.syntax.clone(getValue())
    return Var(*args)


class SNMPAgent(object):
    """Implements an Agent that serves the custom MIB and
    can send a trap.
    """

    def __init__(self, mibObjects):
        """
        mibObjects - a list of MibObject tuples that this agent
        will serve
        """

        #each SNMP-based application has an engine
        self._snmpEngine = engine.SnmpEngine()

        #open a UDP socket to listen for snmp requests
        config.addSocketTransport(self._snmpEngine, udp.domainName,
                                  udp.UdpTransport().openServerMode(('10.0.119.152', 161)))

        #add a v2 user with the community string public
        config.addV1System(self._snmpEngine, "agent", "public")
        #let anyone accessing 'public' read anything in the subtree below,
        #which is the enterprises subtree that we defined our MIB to be in
        config.addVacmUser(self._snmpEngine, 2, "agent", "noAuthNoPriv",
                           readSubTree=(1,3,6,1,4,1))

        #each app has one or more contexts
        self._snmpContext = context.SnmpContext(self._snmpEngine)

        #the builder is used to load mibs. tell it to look in the
        #current directory for our new MIB. We'll also use it to
        #export our symbols later
        mibBuilder = self._snmpContext.getMibInstrum().getMibBuilder()
        mibSources = mibBuilder.getMibSources() + (builder.DirMibSource('.'),)
        mibBuilder.setMibSources(*mibSources)

        #our variables will subclass this since we only have scalar types
        #can't load this type directly, need to import it
        MibScalarInstance, = mibBuilder.importSymbols('SNMPv2-SMI',
                                                      'MibScalarInstance')
        #export our custom mib
        for mibObject in mibObjects:
            nextVar, = mibBuilder.importSymbols(mibObject.mibName,
                                                mibObject.objectType)
            instance = createVariable(MibScalarInstance,
                                      mibObject.valueFunc,
                                      nextVar.name, (0,),
                                      nextVar.syntax)
            #need to export as <var name>Instance
            instanceDict = {str(nextVar.name)+"Instance":instance}
            mibBuilder.exportSymbols(mibObject.mibName,
                                     **instanceDict)

        # tell pysnmp to respotd to get, getnext, and getbulk
        cmdrsp.GetCommandResponder(self._snmpEngine, self._snmpContext)
        cmdrsp.NextCommandResponder(self._snmpEngine, self._snmpContext)
        cmdrsp.BulkCommandResponder(self._snmpEngine, self._snmpContext)


    def setTrapReceiver(self, host, community):
        """Send traps to the host using community string community
        """
        config.addV1System(self._snmpEngine, 'nms-area', community)
        config.addVacmUser(self._snmpEngine, 2, 'nms-area', 'noAuthNoPriv',
                           notifySubTree=(1,3,6,1,4,1))
	config.addTargetParams(self._snmpEngine,
                               'nms-creds', 'nms-area', 'noAuthNoPriv', 1)
        config.addTargetAddr(self._snmpEngine, 'my-nms', udp.domainName,
                             (host, 162), 'nms-creds',
                             tagList='all-my-managers')
        #set last parameter to 'notification' to have it send
        #informs rather than unacknowledged traps
        config.addNotificationTarget(
            self._snmpEngine, 'test-notification', 'my-filter',
            'all-my-managers', 'trap')


    def sendTrap(self):
        #print "Sending trap"
        ntfOrg = ntforg.NotificationOriginator(self._snmpContext)
        errorIndication = ntfOrg.sendNotification(
            self._snmpEngine,
            'test-notification',
            ('CTROL-MIB', 'testTrap'),
            ())


    def serve_forever(self):
	print '-----------------------'
        print "Starting SNMP v2 Agent."
        print '-----------------------'

	self._snmpEngine.transportDispatcher.jobStarted(1)
        try:
           self._snmpEngine.transportDispatcher.runDispatcher()
        except:
            self._snmpEngine.transportDispatcher.closeDispatcher()
            raise

class Worker(threading.Thread):
    """Just to demonstrate updating the MIB
    and sending traps
    """

    def __init__(self, agent, mib):
        threading.Thread.__init__(self)
        self._agent = agent
        self._mib = mib
        self.setDaemon(True)

    def run(self):
        while True:
            time.sleep(3)
            self._mib.setTestCount(mib.getTestCount()+1)
            self._agent.sendTrap()

if __name__ == '__main__':
    mib = Mib()
    objects = [MibObject('CTROL-MIB', 'modeloDisp', mib.getTestDescription1),
	       MibObject('CTROL-MIB', 'verSW', mib.getTestDesc2),
	       MibObject('CTROL-MIB', 'segClave', mib.getTestDesc),
               MibObject('CTROL-MIB', 'tipoDisp', mib.getTestDescription),
               MibObject('CTROL-MIB', 'testCount', mib.getTestCount)]
    agent = SNMPAgent(objects)
    agent.setTrapReceiver('192.168.0.152', 'traps')
    Worker(agent, mib).start()
    try:
        agent.serve_forever()
    except KeyboardInterrupt:
        print "Shutting down"
