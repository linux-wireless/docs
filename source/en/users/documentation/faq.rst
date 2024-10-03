FAQ
===

This is the list of questions most commonly asked by the newcomers to
the Linux wireless networking land, along with the answers.

Q: Is my XXX model device supported?
------------------------------------

A: Forget about XXX, what really matters is PCI or USB (depending on the
bus your device uses) ID pair: VID:PID. So to find out if your device is
supported, use ``lspci -nn`` or ``lsusb`` to learn the ID pair.

Then navigate to Google and type the request in the form ``"VID PID"
site:cateee.net/lkddb/`` (e.g. ``"14e4 170c" site:cateee.net/lkddb/``).
If there is a hit, this will allow you to learn which driver to use for
your device. If there is no, the device is most probably unsupported
(though if you are really sure some driver should support it, you can
try modifying the driver source to add the ID, or use ``newid`` sysfs
node for USB devices).

Q: I still have problems using my device
----------------------------------------

A: Follow this checklist:

#. Install the latest stable `backports <http://drvbp1.linux-foundation.org/~mcgrof/rel-html/backports/>`__
#. Navigate to the :doc:`driver <../drivers>` page corresponding to your device to learn about limitations or additional requirements.
#. Read ``dmesg`` output carefully, paying extra attention to firmware-related messages.
#. Use :doc:``rfkill list`` to see if there are any `rfkill <rfkill>`-related issues, there must be no kind of blocks present for you wireless interface. Sometimes there is a mechanical switch that needs toggling for leveraging "hard" block.
#. Try using :doc:`iw <iw>` and :doc:`wpa_supplicant <wpa_supplicant>` directly, without :doc:`NetworkManager <networkmanager>` or similar tools.
#. Install `bleeding edge backports <http://drvbp1.linux-foundation.org/~mcgrof/rel-html/backports/>`__ to see if the problem is reproducibile with that. In any case you might want to :doc:`report the issue <reporting_bugs>` as stable releases should have all known bugs fixed.

Q: iwconfig tells me bla-bla-bla error
--------------------------------------

A: Please use :doc:`iw <iw>` and :doc:`wpa_supplicant <wpa_supplicant>`
instead. ``iwconfig`` is using deprecated way of communication with the
kernel which is supported only in compatibility mode, has some
limitations and might be removed altogether at some point.

Q: iwconfig wlan0 mode master does not work
-------------------------------------------

A: Use :doc:`hostapd <hostapd>` and a :doc:`driver <../drivers>`
supporting AP mode for running in master/AP mode. Setting a device into
master mode with iwconfig is not supported by modern drivers.

Q: Why can't i use channel X, i did iw reg set NN but it is still unavailable
-----------------------------------------------------------------------------

A: Every card sold was certified to work in a particular regulatory
environment (that being set of channels, maximum allowed power, other
special flags etc). On Intel cards these restrictions are enforced by
firmware, Atheros's equipment has regdomain code in EEPROM which is read
on startup by the driver and then (if it's not "world" regdomain)
:doc:`CRDA <../../developers/regulatory>` is contacted to get a set of
regulatory requirements.

Q: I've installed some driver from somewhere, now i have ra0 interface etc...
-----------------------------------------------------------------------------

A: If you are using drivers directly from vendor (and not from upstream
Linux or compat-wireless) please ask your vendor for support through its
support channels, linux-wireless has nothing to do with that.
