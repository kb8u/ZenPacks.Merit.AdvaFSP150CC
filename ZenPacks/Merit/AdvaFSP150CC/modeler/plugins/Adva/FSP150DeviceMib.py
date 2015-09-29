#################################################
#
# Model FSP150 device using SNMP
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
####################################################################

__doc__="""FSP150DeviceMib

FSP150DeviceMib instantiates a FSP150 device and populates the attributes
for serial number, model, etc.

"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.Merit.AdvaFSP150.lib.FSP150neType import NetworkElementType


class FSP150DeviceMib(SnmpPlugin):

    # from Adva CM-ENTITY-MIB
    modname = "ZenPacks.Merit.AdvaFSP150CC.FSP150Device"

    snmpGetMap = GetTableMap('.1.3.6.1.4.1.2544.1.12.3.1.1',
                             'networkElementTable',
                             { '1.1.1' : 'neIndex',
                               '1.3.1' : 'neType',
                               '1.6.1' : 'neDescription'})

    def process(self, device, results, log):
        log.info('processing %s for device %s' % self.name(), device.id())
        getdata, tabledata = results

        neTable = tabledata.get('networkElementTable')
        if not neTable:
            log.warn('Could not get networkElementTable in %s' % self.name())
            return

        # set hardware model
        try:
            model = chassisModels[ NetworkElementType['neType'] ]
        except KeyError:
            log.warn('Could not find model number %s in zenpack lib/FSP150ChassisModels.py' % NetworkElementType['neType'])
            model = 'unknown'

        rm = self.relMap()

        om.neIndex = int(neTable['neIndex'])

        rm.append(om)
        return rm
