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
        return

        # find the INDEXes returned for netPortTable
        indexes = []
        for oidend in netPortTable:
            if oidend.startswith('1.'):
                indexes.append(oidend.split('1.',1)[1])
        if not indexes:
            return

        rm = self.relMap()
        for index in indexes:
            om = self.objectMap()
            om.id = netPortTable['5.' + index]['portIndex']
            om.neShelfNetPortIndex = index
            om.slotEntityIndex = netPortTable['2.' + index]['portIndex']
            om.slotType = slotType[str(netPortTable['3.' + index]['portIndex'])]
            om.slotCardType = cardType[str(netPortTable['4.' +index]['portIndex'])]
            om.slotCardUnitName = netPortTable['5.' + index]['portIndex']
            om.slotCardCLEICode = netPortTable['7.' + index]['portIndex']
            om.slotCardPartNumber = netPortTable['8.' + index]['portIndex']
            om.slotCardHwRev = netPortTable['9.' + index]['portIndex']
            om.slotCardSwRev = netPortTable['10.' + index]['portIndex']
            om.slotCardSerialNum = netPortTable['11.' + index]['portIndex']
            m.slotCardPhysicalAddress = netPortTable['16.' + index]['portIndex']
            rm.append(om)

        return rm
