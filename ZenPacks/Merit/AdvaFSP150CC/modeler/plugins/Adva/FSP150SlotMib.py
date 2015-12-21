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
for model, serial number, etc.

"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.Merit.AdvaFSP150CC.lib.cardModels import cardType
from ZenPacks.Merit.AdvaFSP150CC.lib.slotTypes import slotType


class FSP150SlotMib(SnmpPlugin):

    # from Adva CM-ENTITY-MIB
    modname = "ZenPacks.Merit.AdvaFSP150CC.FSP150Slot"
    relname = 'FSP150Slot'

    snmpGetTableMaps = (GetTableMap('slotTable',
                                    '.1.3.6.1.4.1.2544.1.12.3.1.3',
                                    { '.1' : 'slotIndex',
                                      '.2' : 'slotEntityIndex',
                                      '.3' : 'slotType',
                                      '.4' : 'slotCardType',
                                      '.5' : 'slotCardUnitName',
                                      '.7' : 'slotCardCLEICode',
                                      '.8' : 'slotCardPartNumber',
                                      '.9' : 'slotHwRev',
                                      '.10': 'slotSwRev',
                                      '.11': 'slotCardSerialNum',
                                      '.15': 'slotCardSecondaryState',
                                      '.16': 'slotCardPhysicalAddress', }),)

    def process(self, device, results, log):
        log.info('processing %s for %s' % (self.name(), device.id))
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
            om.id = index
            om.neShelfSlotIndex = index
            om.snmpindex = index
            om.slotEntityIndex = slotTable['2.' + index]['slotIndex']
            try:
                om.slotType =slotType[str(slotTable['3.' + index]['slotIndex'])]
            except KeyError:
                log.error('Unknown slotType %s for slot %s' % \
                          (str(slotTable['3.' + index]['slotIndex']), index))
                log.error('This needs to be added to zenpack lib/slotTypes.py')
                om.slotType = 'unknown'
            try:
                om.slotCardType = cardType[str(slotTable['4.' +index]['slotIndex'])]
            except KeyError:
                log.error('Unknown cardType %s for slot %s' % \
                          (str(slotTable['4.' +index]['slotIndex']), index))
                log.error('This needs to be added to zenpack lib/cardModels.py')
                om.slotCardType = 'unknown'
                
            om.slotCardUnitName = slotTable['5.' + index]['slotIndex']
            om.slotCardCLEICode = slotTable['7.' + index]['slotIndex']
            om.slotCardPartNumber = slotTable['8.' + index]['slotIndex']
            om.slotCardHwRev = slotTable['9.' + index]['slotIndex']
            om.slotCardSwRev = slotTable['10.' + index]['slotIndex']
            om.slotCardSerialNum = slotTable['11.' + index]['slotIndex']
            om.slotCardPhysicalAddress = slotTable['16.' + index]['slotIndex']
            rm.append(om)

        return rm
