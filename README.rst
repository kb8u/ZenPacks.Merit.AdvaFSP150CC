============================
ZenPacks.Merit.AdvaFSP150CC
============================

.. contents::

Description
===========
Provides monitoring of FSP150CC optical transport systems manufactured by Adva
Optical Networking in Zenoss.


Zenpack contents
================
The ZenPack has the following:

/Network/AdvaFSP150 Device Class
--------------------------
* The hardware model is populated in the device overview page.

Component modeling
------------------
Modelers detect "Slot" and "NetPort" components.  The slots are an abstraction
Adva uses to differentiate different product capabilities in the Adva FSP150
family since most models don't have physical slots in them.  NetPorts for
the GE-112 are the SFPs that plug into them.

Command
------

- update_Adva150_optical_power_threshold
Create rrd template local copy and/or update the threshold for receive
optical power on amplifiers, transponders, OSCs and ROADMs so that they will
generate an Error level alert if the optical signal degrades 3 dB from
the current value.

Requirements
============

* Zenoss Versions Supported: 4.x
* External Dependencies: None
* ZenPack Dependencies: None
* Configuration: No Special configuration should be necessary.

Installation
============
Normal Installation (packaged egg)

*NOTE* This version requires a modified version of SnmpPerformanceConfig.py
be copied to $ZENHOME/Products/ZenHub/services/ from the to_install directory
of this Zenpack.  The modified version allows SNMP indexes to be at places
other than the end of on OID.  As the zenoss user, copy the file before
restarting zenoss or the zenoss daemons.

Download the appropriate package for your Zenoss version from the Zenoss
Zenpack site:

* Zenoss 4.0+ `Latest Package`_
  
Then copy it to your Zenoss server and run the following commands as the zenoss
user::

    zenpack --install <package.egg>
    cp $ZENHOME/ZenPacks/<package.egg>/to_install/SnmpPerformanceConfig.py $ZENHOME/Products/ZenHub/services
    zenoss restart
    
If you don't want to do a full restart, you should be able to just restart
zenhub, zenperfsnmp and zopectl::

    zenhub restart && zenperfsnmp restart &&  zopectl restart
   
Developer Installation (link mode)
----------------------------------
If you wish to further develop and possibly contribute back to this
ZenPack you should clone the git repository, then install the ZenPack in
developer mode using the following commands::

    git clone git://github.com/kb8u/zenoss/ZenPacks.Merit.AdvaFSP150CC
    zenpack --link --install ZenPacks.Merit.AdvaFSP150CC
    zenoss restart
    
Change History
==============

* 1.0

  * Initial Release

Known Issues
===========

* Only GE-112 "Slots" have a performance monitoring template.
