################################################################################
#
# File used to display information in GUI for Adva FSP150CC components
# Gets information from ZODB to be displayed to the user.
#
# Copyright (C) 2015 Russell Dwarshuis, Merit Network, Inc.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""info.py

Representation of FSP150CC components.

"""

from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.decorators import info
from ZenPacks.Merit.AdvaFSP150CC import interfaces


class SlotInfo(ComponentInfo):
    implements(interfaces.ISlotInfo)
    slotCardUnitName = ProxyProperty("slotCardUnitName")
    slotCardPartNumber = ProxyProperty("slotCardPartNumber")
    slotCardSerialNum = ProxyProperty("slotCardSerialNum")
    ckey = ProxyProperty("ckey")

class NetPortInfo(ComponentInfo):
    implements(interfaces.INetPortInfo)
    cmEthernetNetPortSfpPartNumber = ProxyProperty("cmEthernetNetPortSfpPartNumber")
    cmEthernetNetPortSfpReach = ProxyProperty("cmEthernetNetPortSfpReach")
    cmEthernetNetPortLaserWaveLength = ProxyProperty("cmEthernetNetPortLaserWaveLength")
