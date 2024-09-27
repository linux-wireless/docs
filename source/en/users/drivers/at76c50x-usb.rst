at76c50x-usb
------------

at76c50x-usb driver supports USB devices using Atmel at76c50x chipsets. Only 802.11b protocol is supported. The driver is using mac80211 stack.

See also :doc:`at76_usb <at76_usb>`, the driver which at76c50x-usb is based on.

Status
------

The driver is working with some devices, but it hasn't been widely tested yet. Currently it's available only from `sky <http://www.fixithere.net/sky-customer-service/>`__ wireless-testing tree.

The maintainer of the driver is Kalle Valo <`kalle.valo@iki.fi </mailto/kalle.valo@iki.fi>`__>. Send all patches to Kalle and CC linux-wireless mailing list.

History
-------

The original :doc:`at76_usb <at76_usb>` driver which had it's own 802.11 stack but based on the feedback in linux-wireless a mac80211 port was started and the driver was eventually renamed to at76c50x-usb. Help is very welcome to improve the driver.

Firmware
--------

Some Atmel wireless cards require firmware to be loaded. The firmware can be downloaded from this site:

http://www.thekelleys.org.uk/atmel/

Supported chipsets
------------------

-  at76c503-i3861
-  at76c503-i3863
-  at76c503-rfmd
-  at76c503-rfmd-acc
-  at76c505-rfmd
-  at76c505-rfmd2958
-  at76c505a-rfmd2958
-  at76c505amx-rfmd

TODO
----

::

     * fix rssi values 
     * short preamble support 
     * short slot support 
     * ad-hoc mode 
     * debugfs interface to help debugging 
     * power save 
     * rts/cts 
     * remove hex2str and mac2str 
     * check frame sequence numbering 
