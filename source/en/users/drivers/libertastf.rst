libertas_tf
-----------

libertas_tf supports the Marvell 88W8388 USB device as found in the `OLPC XO-1 <http://laptop.org>`__ laptop. Unlike the :doc:`libertas <libertas>` driver, ``libertas_tf`` uses thin firmware (found `here <http://dev.laptop.org/pub/firmware/libertas/thinfirm/>`__) with the ``mac80211`` stack.

Enabling libertas_tf
--------------------

To enable ``libertas_tf``, you must first enable ``mac80211``:

::

   Networking  --->
     Wireless  --->
       <M> Improved wireless configuration API
       <M> Generic IEEE 802.11 Networking Stack (mac80211)

You can then enable ``libertas_tf`` in the kernel configuration:

::

   Networking  --->
     Wireless  --->
       <M> Marvell 8xxx Libertas WLAN driver support with thin firmware
       <M> Marvell Libertas 8388 USB 802.11b/g cards with thin firmware

firmware
~~~~~~~~

The firmware can be obtained from `firmware tree <http://git.kernel.org/?p=linux/kernel/git/firmware/linux-firmware.git>`__.

Please also see the `libertastf HOWTO <http://dev.laptop.org/pub/firmware/libertas/thinfirm/HOW_TO>`__ for instructions on grabbing the corresponding firmware and loading the driver. The regular ``libertas`` driver **must** be unloaded and/or blacklisted in order to use ``libertas_tf``. Additional notes can be found on the `OLPC WiKi <http://wiki.laptop.org/go/Libertas_Thinfirmware_HOWTO>`__.

working
~~~~~~~

-  *Station Mode*
-  *Access Point*
-  *Mesh Point*
-  *Monitor*
