wilc
====

wilc is a driver to support Microchip's ATWILC1000 802.11abgn chipset,
and ATWILC3000 802.11abgn + BLE 4.0 link controller.

Features
========

- IEEE 802.11 b/g/n (1x1) for up to 72 Mbps
- Integrated PA and T/R Switch
- Superior Sensitivity and Range via advanced PHY signal processing
- Wi-Fi Direct, station mode and Soft-AP support
- Supports IEEE 802.11 WEP, WPA2 Security Enterprise
- On-chip memory management engine to reduce host load
- SPI and SDIO host interfaces

Code
====

The code is available on linux kernel staging-testing branch on the staging repository

::

   git clone git://git.kernel.org/pub/scm/linux/kernel/git/gregkh/staging.git
   git checkout -b staging-testing 

References
==========

http://www.microchip.com/wwwproducts/en/ATWILC1000 http://www.microchip.com/wwwproducts/en/ATWILC3000
