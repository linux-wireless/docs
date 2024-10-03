Adding new device IDs to zd1211rw
=================================

Given that there are various different configurations of ZD1211 devices
available (different :doc:`RF types <rftypes>`, ZD1211 vs ZD1211B, etc),
we have not copied over the entire list of USB ID's from the
vendor/vendor-based drivers. We require that each device ID is tested
before we add it to zd1211rw.

If you attempt to use zd1211rw and ``dmesg`` doesn't indicate that
zd1211rw is at all interested in the USB device you just plugged in, you
probably need to add the ID to the driver.

If you have one of these currently-unsupported devices, we'd really
appreciate it if you could make a small modification to the zd1211rw
driver and then test your device with the new driver. The process is
fairly simple.

Please note that zd1211rw has requirements such as userspace firmware
and a very recent kernel version. See the :doc:`driver homepage
<../zd1211rw>` for more info.

Easy and fast way
-----------------

do::

   # lsusb
   # modprobe zd1211rw
   # echo "VVVV DDDD FFFFFFFF FFFFFFFF 0 0 z" > /sys/bus/usb/drivers/zd1211rw/new_id

VVVV that is Vendor ID(get it from lsusb output)

DDDD that is Device ID(get it from lsusb output)

z that is **0** for ZD1211 or **1** for ZD1211B chips or **2** for "Driverless" devices that need ejecting.

example::

   # lsusb
   Bus 001 Device 001: ID 0ace:1211
   # modprobe zd1211rw
   # echo "0ace 1211 FFFFFFFF FFFFFFFF 0 0 0" > /sys/bus/usb/drivers/zd1211rw/new_id

Hard way
--------

1. Modify the driver
~~~~~~~~~~~~~~~~~~~~

Install and configure the kernel sources as you normally would,
including the zd1211rw driver.

Open up drivers/net/wireless/zd1211rw/zd_usb.c in your favourite text
editor. Towards the top of the file, you will see a table called
**usb_ids**. The start of it looks like:

.. code-block:: c

   static struct usb_device_id usb_ids[] = {
           /* ZD1211 */
           { USB_DEVICE(0x0ace, 0x1211), .driver_info = DEVICE_ZD1211 },
           { USB_DEVICE(0x07b8, 0x6001), .driver_info = DEVICE_ZD1211 },

Look up the USB ID for your product (you can find this with **lsusb**).
In this example we'll assume your device ID is 1111:2222. Add an entry
similar to the one below to the table, so the start of the table now
reads:

The line that was added is highlighted in red. It is fairly self
explanatory - you can how 1111:2222 was inserted into the table.

If you have a ZD1211B device then you must use DEVICE_ZD1211B instead of
DEVICE_ZD1211.

The order of entries in the table does not matter. It does not matter if
you create a ZD1211B entry in the section labelled ZD1211.

2. Compile and load
~~~~~~~~~~~~~~~~~~~

The process here is normal: compile and install your kernel, reboot if
necessary, and then load the module.

3. Test the driver
~~~~~~~~~~~~~~~~~~

Connect to a network, and try it out.

4. Mail the list
~~~~~~~~~~~~~~~~

Write a mail to `zd1211-devs
<http://sourceforge.net/mail/?group_id=129083>`__ (subscribers only) and
to :doc:`linux-wireless <../../../developers/mailinglists>` mailing
lists with your success/failure report.

Please include:

- The brand and retail product name of your device
- The USB ID's (duh)
- The chip ID string, which can be read by ``# dmesg | egrep "zd1211b? chip"``
- The FCC ID of your product, if it is is visible. Here is an example of a chip ID string: ``zd1211 chip 07b8:6001 v4330 full 00-12-0e AL2230_RF pa0 g--``

If your RF is not supported, you will not get an ID string. The driver
will bail out earlier with this type of error message: ``zd1211 RF
YOUR_RF 0x? is not supported.``

Please tell us about either situation in your mail.

Stuck ?
-------

If you run into any problems with the above steps, please write to the
`zd1211-devs <http://sourceforge.net/mail/?group_id=129083>`__
(subscribers only) and to :doc:`linux-wireless
<../../../developers/mailinglists>` mailing list. Somebody should be
able to help you out.
