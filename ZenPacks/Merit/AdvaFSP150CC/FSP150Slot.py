######################################################################
#
# FSP150Slot object class
#
# Copyright (C) 2015 Russell Dwarshuis, Merit Network, Inc.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
######################################################################

__doc__="""FSP150Slot

FSP150Slot is a component occuping a slot in a FSP150Device Device
"""

from Globals import DTMLFile
from Globals import InitializeClass

from Products.ZenRelations.RelSchema import *
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity


import logging
log = logging.getLogger('FSP150Slot')


class FSP150Slot(DeviceComponent, ManagedEntity, ZenPackPersistence):
    """FSP150Slot object"""

    portal_type = meta_type = 'FSP150Slot'

    # set default _properties
    neShelfSlotIndex = ''
    slotEntityIndex = -1,
    slotType = 'Not set by modeler'
    slotCardType = 'none'
    slotCardUnitName = 'Not set by modeler'
    slotCardCLEICode = 'unknown'
    slotCardPartNumber = 'Not set by modeler'
    slotCardHwRev = 'Not set by modeler'
    slotCardSwRev = 'Not set by modeler'
    slotCardSerialNum = 'Not set by modeler'
    slotCardPhysicalAddress = 'Not set by modeler'
    ckey = 0

    _properties = (
        {'id':'neShelfSlotIndex', type:'string', 'mode':''},
        # from CM-ENTITY-MIB
        {'id':'slotEntityIndex', 'type':'int', 'mode':''},
        {'id':'slotType', 'type':'string', 'mode':''},
        {'id':'slotCardType', 'type':'string', 'mode':''},
        {'id':'slotCardUnitName', 'type':'string', 'mode':''},
        {'id':'slotCardCLEICode', 'type':'string', 'mode':''},
        {'id':'slotCardPartNumber', 'type':'string', 'mode':''},
        {'id':'slotCardHwRev', 'type':'string', 'mode':''},
        {'id':'slotCardSwRev', 'type':'string', 'mode':''},
        {'id':'slotCardSerialNum', 'type':'string', 'mode':''},
        {'id':'slotCardPhysicalAddress', 'type':'string', 'mode':''},
        {'id':'ckey', 'type':'int', 'mode':''}
    )
        
    _relations = ManagedEntity._relations + (("FSP150Device",
                   ToOne(ToManyCont,
                         "ZenPacks.Merit.AdvaFSP150CC.FSP150Device",
                         "FSP150Slot",)),)

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
        if self.neShelfSlotIndex == '':
            return "Unknown"
        return('Slot ' + self.neShelfSlotIndex.replace('.','-'))

    name = viewName

    def getRRDTemplateName(self):
        if self.slotCardUnitName == 'Not set by modeler':
            return
        return self.slotCardUnitName

    def device(self):
        return self.FSP150Device()

    def manage_deleteComponent(self):
        self.getPrimaryParent()._delObject(self.id)


InitializeClass(FSP150Slot)
