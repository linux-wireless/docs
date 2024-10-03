mwifiex
=======

`Manual <https://www.kernel.org/doc/readme/drivers-net-wireless-mwifiex-README>`__

Marvell 802.11n SDIO/PCI-E/USB :doc:`FullMAC <../../developers/documentation/glossary>` driver.

Supported chipsets
~~~~~~~~~~~~~~~~~~

-  **SDIO** SD8786/SD8787/SD8797/SD8897
-  **PCI-E** 8766/8897
-  **USB** USB8797

Firmware binary
~~~~~~~~~~~~~~~

The firmware can be obtained from `firmware tree <http://git.kernel.org/?p=linux/kernel/git/firmware/linux-firmware.git>`__.

AP Mode
~~~~~~~

[...some content removed for relicensing...]

| Due to radar presence many channels from 11a band are flagged as NO_IR i.e. do not initiate radiation.
| cfg80211 by default puts device into world domain where all channels from 11a band are prohibited from transmission.
| To enable specific channels from 11a band, driver needs to provide hint about current regulatory domain to cfg80211.This can be done by loading driver with regulatory alpha setting.
| Load mwifiex driver with following setting to enable 11a band operations:

::

   insmod mwifiex.ko reg_alpha2=<country-code>

| 

P2P Mode
~~~~~~~~

| mwifiex supports P2P operation mode, but P2P interface must be created using

::

   iw phy phy0 interface add p2p0 type __p2pcl

| 

| This interface can then be used with `wpa_supplicant <http://hostap.epitest.fi/wpa_supplicant/>`__.

| mwifiex driver does not support a separate interface for P2P device mode. Same interface which was used for P2P negotiation will later be used for P2P operations in GO or Client mode.
| To avoid creation of separate interface after P2P negoation by wpa_supplicant, please include following setting in your P2P conf file

::

   p2p_no_group_iface=1

| 
