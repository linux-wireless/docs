mac80211 driver-level interface semantics
-----------------------------------------

One of the huge advantages of mac80211 is that we can improve consistency between drivers. However there is still work needed to define some semantics in order to make all drivers behave similarly.

MAC addresses
~~~~~~~~~~~~~

Typically, drivers read a MAC address from EEPROM and write it into a device register. You should read the EEPROM during initial probe and store it in *wiphy->perm_addr* (use SET_IEEE80211_PERM_ADDR), however you should not initially program it into the active device to avoid it acknowledging frames.

When an interface is added through the ``add_interface`` callback, look at conf->mac_addr and program this into your hardware.

Remember to apply ``remove_interface`` considerations to MAC address too, i.e. remove the MAC address on the device on ``remove_interface``.

Firmware
~~~~~~~~

Firmware should not be loaded during the probe operation, it should be deferred until the first time an interface is added. However, your driver must read the device MAC address during probe and store it in wiphy (the mac address needs to be available before the interface comes up, much of userspace relies on this). [1]_

You should use the generic firmware loaded in the kernel to request firmware from userspace and if it returns errors pass these errors up as the return value from the ``add_interface`` callback.

--------------

.. [1]
   This assumes that you have a mechanism for reading the MAC address before firmware is loaded. This is true for all existing drivers, and will hopefully remain that way for future drivers too
