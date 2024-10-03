ath9k_htc
=========

.. toctree::
   :hidden:

   ath9k_htc/devices

ath9k_htc provides hardware support for Atheros AR9001 and AR9002 family
hardware.

Get the driver
--------------

The driver is part of wireless-testing. See this :doc:`guide
<../../developers/documentation/git-guide>` to use the wireless-testing
tree directly. Or you can use :doc:`compat-wireless <../download>` to
get the driver.

Chipsets supported
------------------

- AR9271
- AR7010 USB-PCIe bridge with AR928x wireless chips

Supported Devices
-----------------

See the :doc:`ath9k_htc device list <ath9k_htc/devices>`.

Mailing list
------------

:doc:`linux-wireless <../../developers/mailinglists>` is the recommended mailing list to use for questions regarding the driver. Firmware-related questions should go to `ath9k_htc_fw <http://lists.infradead.org/mailman/listinfo/ath9k_htc_fw>`__.

The archives for the old ath9k-devel list, which was closed in 2017, are available `here <https://lists.ath9k.org/mailman/listinfo/ath9k-devel>`__.

Configuring your kernel
-----------------------

Enable these options in your kernel config. Most distros will already have it enabled.

::

   CONFIG_ATH_COMMON=m
   CONFIG_ATH9K_HW=m
   CONFIG_ATH9K_COMMON=m
   CONFIG_ATH9K_HTC=m

Firmware
--------

This driver requires firmware. The firmware can be obtained from `firmware tree <http://git.kernel.org/?p=linux/kernel/git/firmware/linux-firmware.git>`__.

Alternately you can download it from here: http://wireless.kernel.org/download/htc_fw/.

:doc:`This firmware is now open <../../developers/gsoc/2012/ath9k_htc_open_firmware>`, to contribute check out:

::

       * [[https://github.com/qca/open-ath9k-htc-firmware|https://github.com/qca/open-ath9k-htc-firmware]] 

::

   Older firmware map:

   AR9271 - ar9271.fw
   AR7010 - ar7010.fw or ar7010_1_1.fw

::

   Newer firmware map:

   AR9271 - htc_9271.fw
   AR7010 - htc_7010.fw

The firmware has to be placed in the correct location, usually /lib/firmware. This could vary among distributions, so check your distro's policies if loading of the firmware fails.

Supported Features
------------------

::

         * Station Mode 
         * Monitor Mode 
         * AP Mode (**NOTE:** AP mode works only with up to 7 stations due to a [[https://lists.ath9k.org/pipermail/ath9k-devel/2013-April/010513.html|firmware limitation]]) 
         * IBSS Mode 
         * Mesh Mode 
         * Legacy (11g) operation 
         * HT support 
         * TX/RX 11n AMPDU aggregation 
         * HW Encryption 
         * LED 
         * Suspend/Resume 

Disabled Features
-----------------

::

           * [[PowerSave|PowerSave]] 

ath9k_htc uses the Autosleep feature of the wireless card. Basic PS support has been implemented in the driver, but it is disabled by default.

Modeswitching for AR7010
------------------------

AR7010 based cards operate by default in USB Mass storage mode and have to be 'switched' to wireless mode on plugging in. If you have an old `USB_ModeSwitch <http://www.draisberghof.de/usb_modeswitch/>`__ package, you can do this to load ath9k_htc automatically.

Add this line to /lib/udev/rules.d/40-usb_modeswitch.rules.

::

   # Atheros Wireless
   ATTRS{idVendor}=="0cf3", ATTRS{idProduct}=="20ff", RUN+="usb_modeswitch '%b/%k'"

Add a file **"0cf3:20ff"** in /etc/usb_modeswitch.d/ and add these lines to it.

::

   ########################################################
   # Atheros Wireless

   DefaultVendor= 0x0CF3
   DefaultProduct=0x20FF

   TargetVendor=  0x0CF3
   TargetProduct= 0x7010

   CheckSuccess=10
   NoDriverLoading=1

   MessageContent="5553424329000000000000000000061b000000020000000000000000000000"

Now, when the device is plugged in, ath9k_htc should load normally. If not, report to `ath9k_devel <https://lists.ath9k.org/mailman/listinfo/ath9k-devel>`__.

Debugging
---------

See :doc:`here <ath9k/debug>`.

Known issues
------------

- The AMPDU size is limited to 22 subframes for UB94/95 and 17 for UB91.
  Fixing this would require removing lots of cruft and structural
  changes in the firmware.
- This HW strongly depends on USB. Please chech `usb related issues
  <https://github.com/qca/open-ath9k-htc-firmware/wiki/usb-related-issues>`__
  before sending bug report.

AP/P2P Modes
------------

**This is experimental !**

Patches enabling P2P/AP modes have been merged in wireless-testing, it
would be part of the driver from Linux 3.0. Using only one VIF (Virtual
Interface) running in AP mode would be a good idea for now, multiple
interface support has not been tested extensively. Note: `PowerSave
<PowerSave>`__ is not properly supported yet.

Please do report bugs, crashes, weird behavior and other general
tantrums thrown by the driver.

TODO
----

A list of things that need to be fixed in the firmware.

* Handle AMPDU subframe limits properly. 
* Handle AMPDU density properly. 
* ERP protection needs to be fixed. 
* RTS/CTS has to be handled properly (for both management and data frames). 
* Processing multicast frames has to be fixed (MultiRateRetry etc.). 
* Short/Long preamble selection has to be fixed. 
* Duration calculation for data, control and management frames. 
* BAR transmission to be moved to the host. 
* Low RSSI issue for UB91/94. 
* TPC for UB94/95 - why is it required ? 
* NOACK handling. 
* Destination mask handling. 
* TX filtering (legacy and HT modes). 
* AMPDU delimiter calculation. 
* AccessClass distribution. 
* Unify TX statistics. 
* MIB interrupt processing (how the fsck does ANI even work now ?) 
* cwMin/cwMax handling. 
* _Three_ different data structures pointing to the same rate control data, really ? 
* Multicast frame completion. 
* World poverty. 
* :doc:`../../developers/gsoc/2012/ath9k_htc_open_firmware`
