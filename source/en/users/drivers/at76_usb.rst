at76_usb
--------

at76_usb driver supports USB devices using Atmel at76c50x chipsets. Only 802.11b protocol is supported. The driver has it's own 802.11 stack.

See also :doc:`at76c50x-usb <at76c50x-usb>`, the mac80211 port of this driver.

Status
------

The driver is now in staging tree and was included in linux 2.6.28 release. The driver is now in maintenance mode and all development should happen with :doc:`at76c50x-usb <at76c50x-usb>`.

Send all patches to Greg Kroah-Hartman <`gregkh@suse.de </mailto/gregkh@suse.de>`__> and CC Kalle Valo <`kalle.valo@iki.fi </mailto/kalle.valo@iki.fi>`__>.

History
-------

The original at76_usb git tree was here:

http://git.80211libre.org/at76_usb.git/

But it seems to be gone now. The current mac80211 port is in linux-testing and the history for the driver is here:

git://git.kernel.org/pub/scm/linux/kernel/git/linville/wireless-legacy.git at76

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
