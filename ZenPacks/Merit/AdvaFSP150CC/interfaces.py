################################################################################
#
# Used for 'Display' drop-down in 'Components' section of GUI.
# Has nothing to do with interfaces on a device.
#
# Copyright (C) 2015 Russell Dwarshuis, Merit Network, Inc.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""interfaces

describes the form field on the user interface.

"""

from Products.Zuul.interfaces import IComponentInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t


class ISlotInfo(IComponentInfo):
    """ Info adapter for Slot (container) component """
    inventoryUnitName = schema.Text(title    = u"Model",
                                    readonly = True,
                                    group    = 'Details')

class INetPortInfo(IComponentInfo):
    """ Info adapter for Network Port component """
    inventoryUnitName = schema.Text(title    = u"Model",
                                    readonly = True,
                                    group    = 'Details')
