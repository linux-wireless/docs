Driverless devices
------------------

The term 'driverless' is partially inaccurate, but this is at least what ZyXEL brand it as.

Some ZD1211 devices come with the driver included on some kind of flash memory. When you plug these devices into a system for the first time, the device appears as a CDROM drive.

There is a virtual CD inside this virtual CDROM drive, which contains the windows driver. Upon insertion to a windows PC, this CDROM autoplays, and the windows driver is automatically installed. Soon after, the CDROM drive mysteriously disappears, and a networking device pops up in its place. On all future plugins, the WLAN device appears right away.

This is quite a neat idea, but doesn't fit with the Linux mentality where no external drivers are needed because the OS already ships them. More importantly, how do we get these devices working as WLAN adapters on Linux, when all we see by default is a CDROM drive?

How it works
~~~~~~~~~~~~

When you plug the device in, it registers itself as a CDROM drive. The USB device descriptor is purely mass storage, and it comes with two endpoints: bulk in, bulk out. The CDROM USB device has its own USB IDs which are not shared with any of the wireless device IDs. No WLAN interface is accessible at this point.

To convert this device into a WLAN device, you have to eject the CDROM through software (just like you would for any real CDROM). A short time after you have sent the eject command, the device disconnects from the system, and then reconnects. Upon reconnection, the device descriptor is completely different and the IDs have changed: at this point, the WLAN interface has appeared, and we can now use it to get on networks.

Presumably the windows driver (or windows userspace WLAN utility) simply keeps an eye open for a CDROM device to appear, and ejects it immediately.

Using these devices under Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

zd1211rw
^^^^^^^^

As of Linux 2.6.19-rc1, `zd1211rw <DriverRewrite>`__ supports these devices out-of-the-box. The usb-storage driver has been taught to ignore the device, and the zd1211rw driver will eject the virtual CDROM and claim the wireless interface that pops up as a result.

Ejecting the CDROM manually
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ejecting the CD may sound simple, but it is made tricky because the devices seem to do a relatively poor job of emulating a CDROM drive. When you plug the device in, it is claimed by the usb-storage driver. The usb-storage driver has a default delay of 5 seconds before it tries to scan for media, but during this pause, the device gets bored and disconnects itself. It then reconnects, and the delay starts again, and this loops forever.

A workaround here is to reduce this delay:

::

   # echo 0 > /sys/module/usb_storage/parameters/delay_use

After doing this, the device appears as a SCSI CDROM upon plugin. Unfortunately the kernel gets a little confused as to whether there is any media in the drive, and starts printing some odd messages. After 10-20 seconds, the device gets bored and reconnects itself. I'm not really sure what is going on here, but the delay is long enough to allow the user to eject the CDROM:

::

   # eject /dev/sr1

The device then reconnects as a WLAN device. You may have to add the IDs to the driver.

USB_ModeSwitch
^^^^^^^^^^^^^^

`USB_ModeSwitch <http://www.draisberghof.de/usb_modeswitch/>`__ is a mode switching tool for controlling "flip flop" (multiple device) USB gear. (0x0ace, 0x2011) and (0x0ace, 0x20ff) are already handled by usb_modeswitch.
