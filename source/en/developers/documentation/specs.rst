About specifications
====================

This page contains a list of specifications used to write Linux drivers
for several wireless cards, and which, alternatively, can be used to
write drivers for any other platforms.

Broadcom hardware specifications
--------------------------------

The :doc:`b43 driver <../../users/drivers/b43>` was written based
on the reverse engineered specification. This device currently is known
to use two different firmware types, each of which changes the behavior
of the driver. Because of this we have two different drivers for each
handle each firmware. Fortunately we have specifications written for
both firmwares.

-  `Specifications for v3 firmware <http://bcm-specs.sipsolutions.net/>`__
-  `Specifications for V4 firmware <http://bcm-v4.sipsolutions.net/>`__

Atheros specifications
----------------------

Atheros Legacy-HAL
~~~~~~~~~~~~~~~~~~

Atheros has released their legacy under the ISC license

* `Atheros legacy HAL for their 802.11abg chipsets <http://www.kernel.org/pub/linux/kernel/people/mcgrof/legacy-hal.tar.bz2>`__

Sam Leffler's HAL
~~~~~~~~~~~~~~~~~

Atheros has worked with Sam Leffler to allow him to `release his HAL
<http://madwifi-project.org/wiki/news/20081129/sam-leffler-releases-hal-source>`__.
You can get it through svn::

   svn co http://svn.freebsd.org/base/projects/ath_hal

Further documentation
~~~~~~~~~~~~~~~~~~~~~

Atheros engage further with **active** upstream developers.

Airgo hardware
--------------

This is new and ongoing project.

* `Airgo specifications <http://airgo.wdwconsulting.net/mymoin/>`__

Ralink documentation
--------------------

Ralink has provided EEPROM channel documentation on two of their
chipsets.

* `RT61 EEPROM Channels <http://www.kernel.org/pub/linux/kernel/people/mcgrof/doc/ralink/RT61-EEPROM-Channels.pdf>`__
* `RT2460 EEPROM Channels <http://www.kernel.org/pub/linux/kernel/people/mcgrof/doc/ralink/RT2460_EEPROM_Channels.pdf>`__
* `RT2560 EEPROM Channels <http://www.kernel.org/pub/linux/kernel/people/mcgrof/doc/ralink/RT2560_EEPROM_Channels.pdf>`__
* `RT2571 EEPROM Channels <http://www.kernel.org/pub/linux/kernel/people/mcgrof/doc/ralink/RT2571_EEPROM_Channels.pdf>`__
* `RT2860 EEPROM Channells <http://www.kernel.org/pub/linux/kernel/people/mcgrof/doc/ralink/RT2860_EEPROM_channels.pdf>`__

STMicroelectronics hardware
---------------------------

This is a p54 variant used in some mobile devices.

* :download:`lmac_longbow.h <../../../media/en/developers/documentation/lmac_longbow.h>`
* :download:`../../../media/en/developers/documentation/stsw45x0c_lmac_api_ed1p4.pdf`

Texas Instruments hardware specifications
-----------------------------------------

* http://focus.ti.com/docs/prod/folders/print/wl1271-tiwi.html
* http://processors.wiki.ti.com/index.php/OMAP35x_Wireless_Connectivity_Solution_Hardware
* http://processors.wiki.ti.com/index.php/ARM_Processor_Wireless_Connectivity_Hardware_specifications
