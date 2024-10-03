rt2800pci
=========

Driver for `Ralink/MediaTek
<https://www.mediatek.com/products/connectivity-and-networking>`__ PCI
devices RT2760, RT2790, RT2860, RT2880, RT2890 & RT3052.

Available devices
-----------------

- http://rt2x00.serialmonkey.com/wiki/index.php/Hardware List of devices from the project site.

Unsupported chips
-----------------

* `RT5592 <https://www.mediatek.com/products/broadbandWifi/rt5592>`__, 802.11a/b/g/n 2T2R 2.4/5 GHz PCI Express Single Chip. (**WIP** Stanislaw Gruszka <[[mailto:stf_xl@wp.pl|stf_xl@wp.pl]]> : `http://rt2x00.serialmonkey.com/pipermail/users_rt2x00.serialmonkey.com/2013-March/005765.html <http://rt2x00.serialmonkey.com/pipermail/users_rt2x00.serialmonkey.com/2013-March/005765.html>`__). The Ralink driver for RT5592 can be downloaded from: `http://www.asus.com/Networking/PCEN53/HelpDesk_Download/ <http://www.asus.com/Networking/PCEN53/HelpDesk_Download/>`__ (direct link: `http://dlcdnet.asus.com/pub/ASUS/wireless/PCE-N53/Linux_PCE_N53_1008.zip <http://dlcdnet.asus.com/pub/ASUS/wireless/PCE-N53/Linux_PCE_N53_1008.zip>`__ )
* Any new `Ralink <https://wikidevi.com/wiki/Ralink>`__ or `MediaTek <https://wikidevi.com/wiki/MediaTek>`__ chip. Vendor drivers can be downloaded from: 

   * https://www.mediatek.com/products/connectivity-and-networking/broadband-wifi
   * https://www.mediatek.com/products/connectivity-and-networking/legacy-products

Features
--------

* //TODO// 

working
~~~~~~~

* Monitor Mode 
* Station Mode 
* AP Mode 
* TX aggregation 
* HW crypto 
* Multi BSS in AP mode 
* HT40 

not working yet
~~~~~~~~~~~~~~~

* Automatic MAC address assignment for more than one AP interface 

not supported
~~~~~~~~~~~~~

* //TODO// 

TODO
----

* Add support for more chips
* Warning "invalid TX_STA_FIFO content" gets issued sometimes, maybe
  only in conjunction with tx aggregation? Needs investigation.

Device firmware
---------------

* `rt2860.bin <http://git.kernel.org/?p=linux/kernel/git/firmware/linux-firmware.git>`__ 
* SoC devices (RT3050, RT3051 and RT3052) don't need firmware 

Support
-------

* ` rt2x00 mailing list-Archived <http://rt2x00.serialmonkey.com/pipermail/users_rt2x00.serialmonkey.com/>`__ 
* :doc:`../support`

External links
--------------

* `rt2x00 project website-Archived <http://rt2x00.serialmonkey.com/>`__ 
