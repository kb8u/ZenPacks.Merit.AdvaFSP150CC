######################################################################
#
# FSP150Device object class
#
# Copyright (C) 2015 Russell Dwarshuis, Merit Network, Inc.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
######################################################################

from Globals import InitializeClass
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.Device import Device
from Products.ZenModel.ZenossSecurity import ZEN_VIEW
from copy import deepcopy


class FSP150Device(Device,ZenPackPersistence):
    "A FSP150 Device"

    meta_type = 'FSP150Device'

    _relations = Device._relations + (
        ('FSP150Slot',
         ToManyCont(ToOne,
                    'ZenPacks.Merit.AdvaFSP150.FSP150Slot',
                    'FSP150Slot')),
        )

    factory_type_information = deepcopy(Device.factory_type_information)

    def __init__(self, *args, **kw):
        Device.__init__(self, *args, **kw)
        self.buildRelations()


InitializeClass(FSP150Device)
