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


class FSP150SlotMib(SnmpPlugin):

    # from Adva CM-ENTITY-MIB
    modname = "ZenPacks.Merit.AdvaFSP150CC.FSP150Slot"

    snmpGetTableMaps = (GetTableMap('slotTable',
                                    '.1.3.6.1.4.1.2544.1.12.3.1.3',
                                    { '.1' : 'slotIndex',
                                      '.2' : 'slotEntityIndex',
                                      '.3' : 'sloType',
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

        log.info('got slotTable: %s' % slotTable)

        return
#        om = self.objectMap()

#        om.neIndex = neTable['neIndex']
#        om.neType = tag
#        om.setHWProductKey = model

#        return om
