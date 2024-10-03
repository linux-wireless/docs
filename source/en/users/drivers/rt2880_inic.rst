RT2880 iNIC
===========

RT2880 iNIC spells out "intelligent network interface card". The
intelligence about it is that this card contains a locked-down ralink
rt288x system on chip. It appears that this firmware is
cryptographically signed and cannot be replaced, so a driver needs to
talk to the RTOS using the mechanisms provided by the default firmware.

It is currently not supported by any Linux driver.

This PCIe card looks like so in lspci::

   00:0c.0 Class 0200: 1814:0801

The card is primarily used in routers. This card can be found in Asus
DSL-N13, Asus WL-127n, Alcatel Lucent Cellpipe 7130, Canal+ R7 set top
boxes, D-Link DIR-685, Pegatron WL227N-5G Wireless Card, and the Billion
BiPAC 7800N.

Source code
-----------

Vendor source code for this device was released by Canal+:

-  `Vendor code dump <https://github.com/kovz/ralink_inic>`__
-  `Canal+ source code dump <https://github.com/canalplus/r7oss/tree/master/G5/src/rt3662-modules-2.4.0.9.10>`__
