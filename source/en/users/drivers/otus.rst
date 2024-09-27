otus
----

otus is an Atheros IEEE 802.11n USB Linux "vendor" driver, licensed under the permissive ISC license. This driver was used as base to write a new GPLv2 driver based on mac80211, :doc:`ar9170 <ar9170>`, which got merged upstream and later also replaced by a GPLv2 :doc:`carl9170 <carl9170>` with open GPLv2 firmware through the :doc:`carl9170.fw <carl9170.fw>` firmware work.

Code
----

This driver used to be merged into the Linux kernel under the staging area but*\* the Otus driver was deleted off of the kernel tree*\* : http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=cff55f50b882b197a52c4cf0108a43c615d1fdba since we have a better replacement. For those still looking for permissive licensed Otus driver code you can find here:

http://www.kernel.org/pub/linux/kernel/people/mcgrof/otus/

But note that this code had a dependency on a version of wpa_supplicant as documented below. If you are working on supporting this driver on other Operating Systems which does not accept GPL code you can likely just pull more updated code from the Linux kernel right before the Otus driver was removed. The Otus driver code in the Linux kernel remained permissive licensed until it was replaced with :doc:`carl9170 <carl9170>`

Supported hardware
------------------

Atheros 802.11n hardware:

-  UB81 - 2x2 2.4 GHz
-  UB82 - 2x2 2.4 GHz and 5 GHz
-  UB83 - 1x2 2.4 GHz All of these devices are AR9170.

Products in the market
----------------------

Dlink

::

     * DWA-160A1 Netgear 
       * WNDA3100 (Dual Band, USB ID 0846:9010, FCC ID PY307300073) 
       * WN111v2 (USB ID 0846:9001) TP-Link 
         * TL-WN821N AVM 
           * FRITZ!WLAN N USB Stick (USB ID 0x57c, 0x8401) - currently not running with the driver (see mailing list). SMC Networks 
             * SMCWUSB-N2 

Requirements
------------

::

               * Kernel 2.4 - 2.6 
               * openssl-dev package. 

Mailing list
------------

Our otus mailing list for this driver is:

https://lists.madwifi-project.org/mailman/listinfo/otus-devel

Get the code
------------

You can get the code here

::

   git://git.kernel.org/pub/scm/linux/kernel/git/mcgrof/otus.git

wpa_supplicant otus driver
--------------------------

This driver requires its own supplicant driver for wpa_supplicant 0.4.8. For your convenience you can find the tarball here:

http://www.kernel.org/pub/linux/kernel/people/mcgrof/otus/wpa_supplicant-0.4.8_otus.tar.bz2

Features supported
------------------

::

                 * IEEE standard compliance 
                 * IEEE 802.11a/b/g 
                 * IEEE 802.11h, 802.11d 
                 * IEEE 80211i 
                 * IEEE Draft 2.0 802.11n 
                 * Ad Hoc 
                 *  * join (2.4GHz, 5GHz if SKU allows) 
                 *  * create (2.4GHz , 5GHz if SKU allows) 
                 *  * Adhoc security: WEP 
                 *   Security: WPA/WPA2 (Personal / Enterprise) 
