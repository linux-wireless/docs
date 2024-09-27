Go back –> :doc:`Atheros Linux wireless drivers <atheros>`

About ath9k
-----------

ath9k is a completely FOSS wireless driver for all Atheros IEEE 802.11n PCI/PCI-Express and AHB WLAN based chipsets.

Subscribe to this page!
-----------------------

You should subscribe to this page so you can get e-mail updates on changes and news for ath9k automatically. You'll get an e-mail as soon as this page gets updated.

Mailing list
------------

:doc:`linux-wireless <../../developers/mailinglists>` is the recommended mailing list to use.

The archives for the old ath9k-devel list, which was closed in 2017, are available:

https://lists.ath9k.org/mailman/listinfo/ath9k-devel

Get the latest ath9k driver
---------------------------

ath9k is part of the kernel, but the latest version can be obtained from `backports <https://backports.wiki.kernel.org/index.php/Main_Page>`__.

Enabling ath9k
--------------

To enable ath9k, you must first enable mac80211 through *make menuconfig* when compiling your kernel. If you do not know what this means then please learn to compile kernels or rely on your Linux distribution's kernel. Below are the options you need to enable ath9k through *make menuconfig*.

::

   Networking  --->
     Wireless  --->
       <M> Improved wireless configuration API
       <M> Generic IEEE 802.11 Networking Stack (mac80211)

You can then enable ath9k in the kernel configuration under

::

   Device Drivers  --->
     [*] Network device support  --->
           Wireless LAN  --->
             Atheros Wireless Cards ---->
               <M>   Atheros 802.11n wireless cards support

Supported chipsets
------------------

| SB = single-band 2.4GHz
| DB = dual-band 2.4GHz or 5GHz

-  AR2427 1x1 SB (no 11n)

-  AR5008:

   -  AR5418+AR5133
   -  AR5416+AR5133
   -  AR5416+AR2133

-  AR9001:

   -  AR9160 2x2 DB
   -  AR9102 2x2 SB
   -  AR9103 3x3 SB

-  AR9002:

   -  AR9220 2x2 DB
   -  AR9223 2x2 SB
   -  AR9227 2x2 SB
   -  AR9280 2x2 DB
   -  AR9281 2x2 SB
   -  AR9285 1x1 SB
   -  AR9287 2x2 SB

-  AR9003:

   -  AR9380 3x3 DB
   -  AR9382 2x2 DB
   -  AR9331 1x1 SB
   -  AR9340 2x2 DB

-  AR9004:

   -  AR9485 1x2 SB
   -  AR9462 2x2 DB
   -  AR9565 1x1 SB
   -  AR9580 3x3 DB
   -  AR9590 3x3 DB
   -  AR9592 2x2 DB
   -  AR9550 3x3 DB

Available devices
-----------------

See the :doc:`ath9k device list <ath9k/devices>`.

Features and modes of operation
-------------------------------

All of these modes of operation are supported and should work on all ath9k cards.

Modes of operation
~~~~~~~~~~~~~~~~~~

-  Station
-  AP
-  IBSS
-  Monitor
-  Mesh point
-  WDS
-  P2P GO/CLIENT

Features
~~~~~~~~

-  802.11abg
-  802.11n

   -  HT20
   -  HT40
   -  AMPDU
   -  Short GI (Both 20 and 40 MHz)
   -  LDPC
   -  TX/RX STBC

-  802.11i

   -  WEP 64 / 127
   -  WPA1 / WPA2

-  802.11d
-  802.11h
-  802.11w/D7.0
-  WPS
-  WMM
-  LED
-  RFKILL
-  BT co-existence
-  AHB and PCI bus
-  TDLS
-  WoW
-  Antenna Diversity

A little history on ath9k
-------------------------

When it went in
~~~~~~~~~~~~~~~

ath9k was announced to have been `merged into Linux-2.6.27-rc3 <http://lwn.net/Articles/293784/>`__ by Linus on Tue, 12 Aug 2008 19:33:16 -0700 (PDT), and consisted of 58.8% of the entire rc3 patch.

Early distributions which picked it up
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`OpenWrt <http://openwrt.org/>`__ became the `first distribution to pick up ath9k and contribute to it <https://dev.openwrt.org/changeset/11884>`__.

Other sections
--------------

For more information please see:

-  :doc:`Bugs <ath9k/bugs>`
-  :doc:`Power consumption <ath9k/power-consumption>`
-  :doc:`Bluetooth Coexistence <ath9k/btcoex>`
-  :doc:`Antenna Diversity <ath9k/antennadiversity>`
-  :doc:`Wake on WLAN <ath9k/wow>`
-  :doc:`DFS <ath9k/dfs>`
-  :doc:`Debugging <ath9k/debug>`
-  :doc:`Products with supported ath9k cards <ath9k/products>`
-  :doc:`ath.ko module <ath>`
-  :doc:`RHEL <ath9k/rhel5>`
-  :doc:`initvals-tool <ath9k/initvals-tool>`
-  :doc:`Spectral scan <ath9k/spectral_scan>`
-  Youtube presentations about ath9k internals by Adrian Chadd, see `Documentation </en/users/documentation>`__
