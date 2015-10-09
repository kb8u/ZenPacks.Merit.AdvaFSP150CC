#################################################
#
# Model FSP150 Network Port using SNMP
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
####################################################################

__doc__="""FSP150NetPortMib

FSP150NetPortMib instantiates a FSP150 slot and populates the attributes
for model, serial number, etc.

"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.Merit.AdvaFSP150CC.lib.cardModels import cardType
from ZenPacks.Merit.AdvaFSP150CC.lib.slotTypes import slotType


class FSP150NetPortMib(SnmpPlugin):

    modname = "ZenPacks.Merit.AdvaFSP150CC.FSP150NetPort"
    relname = 'FSP150NetPort'

    # .1.3.6.1.4.1.2544.1.12.4.1.7 is cmEthernetNetPortTable in CM-FACILITY-MIB
    snmpGetTableMaps = (GetTableMap('netPortTable',
                                    '.1.3.6.1.4.1.2544.1.12.4.1.7',
                                    { '.1' : 'portIndex',
                                      '.2' : 'cmEthernetNetPortIfIndex',
                                      '.3' : 'cmEthernetNetPortEntityIndex',
                                      '.4' : 'cmEthernetNetPortAdminState',
                                      '.14': 'cmEthernetNetPortSfpPartNumber',
                                      '.69': 'cmEthernetNetPortSfpReach',
                                      '.70': 'cmEthernetNetPortLaserWaveLength',
                                    }),)

    def process(self, device, results, log):
        log.info('processing %s for %s' % (self.name(), device.id))
        getdata, tabledata = results

        netPortTable = tabledata.get('netPortTable')
        if not netPortTable:
            log.warn('Could not get netPortTable in %s' % self.name())
            return

        log.debug('got netPortTable: %s' % netPortTable)

        # find the INDEXes returned for netPortTable
        indexes = []
        for oidend in netPortTable:
            if oidend.startswith('1.'):
                indexes.append(oidend.split('1.',1)[1])
        if not indexes:
            log.debug('no indexes found for netPortTable in %s' % self.name())
            return

        rm = self.relMap()
        for index in indexes:
            # cmEthernetNetPortAdminState of 1 means port is in service 
            if netPortTable['4.' + index]['portIndex'] != 1:
                log.info('Network port %s is not in service' % index)
                continue
            else:
                log.info('Network port %s has been added' % index)

            om = self.objectMap()
            om.id = index
            om.neShelfSlotPortIndex = index
            om.cmEthernetNetPortIfIndex =netPortTable['2.' + index]['portIndex']
            om.cmEthernetNetPortEntityIndex = netPortTable['3.' + index]['portIndex']
            om.cmEthernetNetPortAdminState = 'In Service'
            om.cmEthernetNetPortSfpPartNumber = netPortTable['14.' + index]['portIndex']
            # string like '40 km'
            dx = str(int(netPortTable['69.' + index]['portIndex']/1000)) +' km'
            om.cmEthernetNetPortSfpReach = dx
            # string like '1310 nm'
            wavelength = str(netPortTable['70.' + index]['portIndex']) + ' nm'
            om.cmEthernetNetPortLaserWaveLength = wavelength
            rm.append(om)

        return rm
