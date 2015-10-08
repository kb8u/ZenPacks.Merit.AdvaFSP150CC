######################################################################
#
# FSP150NetPort object class
#
# Copyright (C) 2015 Russell Dwarshuis, Merit Network, Inc.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
######################################################################

__doc__="""FSP150NetPort

FSP150NetPort is an ethernet network-side component in a FSP150Device Device
"""

from Globals import DTMLFile
from Globals import InitializeClass

from Products.ZenRelations.RelSchema import *
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity


import logging
log = logging.getLogger('FSP150NetPort')


class FSP150NetPort(DeviceComponent, ManagedEntity, ZenPackPersistence):
    """FSP150NetPort object"""

    portal_type = meta_type = 'FSP150NetPort'

    # set default _properties
    neShelfSlotPortIndex = ''
    cmEthernetNetPortIfIndex = -1
    cmEthernetNetPortEntityIndex = -1
    cmEthernetNetPortAdminState = 'not set by modeler'
    cmEthernetNetPortSfpPartNumber = 'not set by modeler'
    cmEthernetNetPortSfpReach = 'not set by modeler'
    cmEthernetNetPortLaserWaveLength = 'not set by modeler'

    _properties = (
        {'id':'neShelfSlotPortIndex', 'type':'string', 'mode':''},
        {'id':'cmEthernetNetPortIfIndex', 'type':'int', 'mode':''},
        {'id':'cmEthernetNetPortEntityIndex', 'type':'int', 'mode':''},
        {'id':'cmEthernetNetPortAdminState', 'type':'string', 'mode':''},
        {'id':'cmEthernetNetPortSfpPartNumber', 'type':'string', 'mode':''},
        {'id':'cmEthernetNetPortSfpReach', 'type':'string', 'mode':''},
        {'id':'cmEthernetNetPortLaserWaveLength', 'type':'string', 'mode':''},
    )
        
    _relations = ManagedEntity._relations + (("FSP150Device",
                   ToOne(ToManyCont,
                         "ZenPacks.Merit.AdvaFSP150CC.FSP150Device",
                         "FSP150NetPort",)),)

    factory_type_information = ({
        'actions': ({
            'id': 'perfConf',
            'name': 'Template',
            'action': 'objTemplates',
            'permissions': (ZEN_CHANGE_DEVICE,),
            },),
        },)

    isUserCreatedFlag = True

    def isUserCreated(self):
        """
        Returns the value of isUserCreated. True adds SAVE & CANCEL buttons to Details menu
        """
        return self.isUserCreatedFlag

    def viewName(self):
        """Human readable version of this object"""
        if self.neShelfSlotPortIndex == '':
            return "Unknown"
        return('Network Port ' + self.neShelfSlotPortIndex.replace('.','-'))

    name = viewName

    def device(self):
        return self.FSP150Device()

    def manage_deleteComponent(self):
        self.getPrimaryParent()._delObject(self.id)


InitializeClass(FSP150NetPort)
