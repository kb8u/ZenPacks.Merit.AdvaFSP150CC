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
from ZenPacks.Merit.AdvaFSP150CC.lib.chassisModels import NetworkElementType


class FSP150DeviceMib(SnmpPlugin):

    # from Adva CM-ENTITY-MIB
    modname = "ZenPacks.Merit.AdvaFSP150CC.FSP150Device"

    snmpGetTableMaps = (GetTableMap('networkElementTable',
                                    '.1.3.6.1.4.1.2544.1.12.3.1.1',
                                    { '.1.1' : 'neIndex',
                                      '.1.3' : 'neType',
                                      '.1.6' : 'neDescription'}),)

    def process(self, device, results, log):
        log.info('processing %s for device %s' % (self.name(), device.id))
        getdata, tabledata = results

        neTable = tabledata.get('networkElementTable')['1']
        if not neTable:
            log.warn('Could not get networkElementTable in %s' % self.name())
            return

        # set hardware model
        try:
            tag = NetworkElementType[ str(neTable['neType']) ]
        except KeyError:
            log.warn('Could not find tag %s in zenpack lib/FSP150ChassisModels.py' % neTable['neType'])
            tag = 'unknown'
        try:
            model = neTable['neDescription']
        except KeyError:
            log.warn("Couldn't find model from neDescription")
            model = 'unknown'

        om = self.objectMap()

        om.neIndex = neTable['neIndex']
        om.neType = tag
        om.setHWProductKey = model

        return om
