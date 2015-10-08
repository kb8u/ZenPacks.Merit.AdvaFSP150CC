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

from Products.ZenRelations.RelSchema import *
from Products.ZenModel.Device import Device


class FSP150Device(Device):
    "A FSP150 Device"

    neIndex = None
    neType = 'unknown'

    _properties = Device._properties + (
        {'id' : 'neIndex','type':'int'},
        {'id' : 'neType', 'type':'string'},
    )

    _relations = Device._relations + (
        ('FSP150Slot',
         ToManyCont(ToOne,
                    'ZenPacks.Merit.AdvaFSP150CC.FSP150Slot',
                    'FSP150Device')),
        ('FSP150NetPort',
         ToManyCont(ToOne,
                    'ZenPacks.Merit.AdvaFSP150CC.FSP150NetPort',
                    'FSP150Device')),
    )
