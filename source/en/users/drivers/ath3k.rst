ath3k
=====

ath3k is the Linux Bluetooth driver for Atheros AR3011/AR3012 Bluetooth
chipsets.

Firmware
--------

For AR3011, you can find the "ath3k-1.fw" on the linux-firmware.git tree::

   git://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git

For AR3012, you can find the "AthrBT_0x01020200.dfu" and
"ramps_0x01020200_26.dfu" or "ramps_0x01020200_40.dfu" on the
linux-firmware git tree::

   git://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/ar3k/

AR3011 over USB
---------------

This is supported through CONFIG_BT_ATH3K, merged upstream as of 2.6.33.
If you have an older kernel you can use :doc:`stable
compat-wireless-2.6.33 <../download/stable>` or later tarballs.

AR3011 with SFLASH configurations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When AR3011 ships with SFLASH configurations upon device load the AR3011
will actually appear to the host system as a generic USB Bluetooth
device and requires uploading of firmware onto the device to
re-enumerate itself as an AR3011 device. You need to add the VID/PID of
your device in both the btusb.c blacklist and the ath3k.c support list.
You can refer to an example `here
<http://git.kernel.org/?p=linux/kernel/git/stable/linux-stable.git;a=commit;h=e9036e336a8e5640871e0006ea4a89982b25046f>`__

AR3012 over USB
---------------

This is supported through CONFIG_BT_ATH3K, merged upstream as of 3.0.9.
Like AR3011 with SFLASH configuration, you need to add the VID/PID of
your device in both the btusb.c blacklist and the ath3k.c support list
to load AR3012 firmware. You can refer to what it's done for
0x0cf3/0x3004 one.

How to tell AR3011 and AR3012
-----------------------------

You can use lsusb -v to check the device descriptor. If it's AR3011, the
iProduct value is 0. If it's AR3012 the iProduct value is 2.

AR3001/AR3002 over UART
-----------------------

This is supported through CONFIG_BT_HCIUART_ATH3K, merged upstream as of
2.6.36 and BlueZ 4.77. You can find AR3001/AR3002 firmware on the
linux-firmware git tree::

   git://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/ar3k/
