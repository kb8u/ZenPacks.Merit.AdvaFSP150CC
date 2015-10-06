#################################################
#
# Model FSP150 slot using SNMP
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
####################################################################

__doc__="""FSP150SlotMib

FSP150SlotMib instantiates a FSP150 slot and populates the attributes
for slotIndex, model, etc.

"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.Merit.AdvaFSP150CC.lib.cardModels import cardType
from ZenPacks.Merit.AdvaFSP150CC.lib.slotTypes import slotType


class FSP150SlotMib(SnmpPlugin):

    # from Adva CM-ENTITY-MIB
    modname = "ZenPacks.Merit.AdvaFSP150CC.FSP150Slot"

    snmpGetTableMaps = (GetTableMap('slotTable',
                                    '.1.3.6.1.4.1.2544.1.12.3.1.3',
                                    { '.1' : 'slotIndex',
                                      '.2' : 'slotEntityIndex',
                                      '.3' : 'slotType',
                                      '.4' : 'slotCardType',
                                      '.5' : 'slotCardUnityName',
                                      '.7' : 'slotCardCLEICode',
                                      '.8' : 'slotCardPartNumber',
                                      '.9' : 'slotHwRev',
                                      '.10': 'slotSwRev',
                                      '.11': 'slotCardSerialNumber',
                                      '.15': 'slotCardSecondaryState',
                                      '.16': 'slotCardPhysicalAddress', }),)

    def process(self, device, results, log):
        log.info('processing %s for slot %s' % (self.name(), device.id))
        getdata, tabledata = results

        slotTable = tabledata.get('slotTable')
        if not slotTable:
            log.warn('Could not get slotTable in %s' % self.name())
            return

        log.debug('got slotTable: %s' % slotTable)

        # find the INDEXes returned for slotTable
        indexes = []
        for oidend in slotTable:
            if oidend.startswith('1.'):
                indexes.append(oidend.split('1.',1)[1])
        if not indexes:
            return

        rm = self.relMap()
        for index in indexes:
            om = self.objectMap()
            om.neShelfSlotIndex = index
            om.neIndex = int(index.split('.')[-1])
            om.slotEntityIndex = slotTable['2.' + index]['slotIndex']
            om.slotType = slotType[str(slotTable['3.' + index]['slotIndex'])]
            om.slotType = cardType[str(slotTable['4.' + index]['slotIndex'])]
            om.slotCardUnityName = slotTable['5.' + index]['slotIndex']
            om.slotCardCLEICode = slotTable['7.' + index]['slotIndex']
            om.slotCardPartNumber = slotTable['8.' + index]['slotIndex']
            om.slotHwRev = slotTable['9.' + index]['slotIndex']
            om.slotSwRev = slotTable['10.' + index]['slotIndex']
            om.slotCardSerialNumber = slotTable['11.' + index]['slotIndex']
            om.slotCardSecondaryState = slotTable['15.' + index]['slotIndex']
            om.slotCardPhysicalAddress = slotTable['16.' + index]['slotIndex']
            rm.append(om)

        log.debug('om is %s' % om)

        return rm
