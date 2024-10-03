iwlwifi
=======

.. toctree::

   iwlwifi/core_release
   iwlwifi/debugging

Introduction
------------

**iwlwifi** is the wireless driver for Intel's current wireless chips. For older chips, there are other drivers:

- :doc:`ipw2100 <ipw2100>`
- :doc:`ipw2200 <ipw2200>`
- :doc:`iwlegacy <iwlegacy>` (for Intel® PRO/Wireless 3945ABG and Intel® Wireless Wi-Fi Link 4965AGN)

Features
--------

* Station (client)
* AP mode on 2.4GHz (on devices driven by iwlmvm, note no 5GHz AP
  support `due to LAR <https://bugzilla.kernel.org/show_bug.cgi?id=206469#c2>`__
* P2P and multi-role (on devices driven by iwlmvm)
* Monitor (sniffer) - see note below
* IBSS (Ad-Hoc)

Supported Devices
-----------------

The following devices are supported (since kernel version):

*  Wi-Fi 7 products

    * `Intel® Wi-Fi 7 BE200 <https://www.intel.com/content/www/us/en/products/sku/230078/intel-wifi-7-be200/specifications.html>`__ (6.5)

* Wi-Fi 6E products

    * `Intel® Wi-Fi 6E AX411 <https://www.intel.com/content/www/us/en/products/sku/217242/intel-wifi-6e-ax411-gig/specifications.html>`__ (5.14)
    * `Intel® Wi-Fi 6E AX211 <https://www.intel.com/content/www/us/en/products/docs/wireless/wi-fi-6e-ax211-module-brief.html>`__ (5.14)
    * `Intel® Wi-Fi 6E AX210 <https://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/wi-fi-6e-ax210-product-brief.pdf>`__ (5.10)

* Wi-Fi 6 products

    * `Intel® Wi-Fi 6 AX201 <https://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/wi-fi-6-ax201-module-brief.pdf>`__ (5.2)
    * `Intel® Wi-Fi 6 AX200 <https://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/wi-fi-6-ax200-module-brief.pdf>`__ (5.1)

* 802.11ac products

    * `Intel® Wireless-AC 9462 <http://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/dual-band-wireless-ac-9462-brief.pdf>`__ (4.14)
    * `Intel® Wireless-AC 9461 <http://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/dual-band-wireless-ac-9461-brief.pdf>`__ (4.14)
    * `Intel® Wireless-AC 9260 <http://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/dual-band-wireless-ac-9260-brief.pdf>`__ (4.14)
    * `Intel® Wireless-AC 9560 <http://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/dual-band-wireless-ac-9560-brief.pdf>`__ (4.14)
    * `Intel® Wireless-AC 8265 <http://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/dual-band-wireless-ac-8265-brief.pdf>`__ (4.6)
    * `Intel® Wireless-AC 3168 <http://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/dual-band-wireless-ac-3168-brief.pdf>`__ (4.6)
    * `Intel® Wireless-AC 8260 <http://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/dual-band-wireless-ac-8260-brief.pdf>`__ (4.1)
    * `Intel® Wireless-AC 3165 <http://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/dual-band-wireless-ac-3165-brief.pdf>`__ (4.1)

* 802.11n or 802.11ac products (SKU dependent)

    * `Intel® Wireless 7265 <http://www.intel.com/content/www/us/en/wireless-products/dual-band-wireless-ac-7265.html>`__ (3.13)
    * `Intel® Wireless 7260 <http://www.intel.com/content/www/us/en/wireless-products/dual-band-wireless-ac-7260-bluetooth.html>`__ (3.10)
    * `Intel® Wireless 3160 <http://www.intel.com/content/www/us/en/wireless-products/dual-band-wireless-ac-3160-bluetooth.html>`__ (3.10)

* 802.11abgn products

    * `Intel® Centrino® Advanced-N 6235 <http://www.intel.com/content/www/us/en/wireless-products/centrino-advanced-n-6235.html>`__ (3.2) 
    * `Intel® Centrino® Advanced-N 6230 <http://www.intel.com/content/www/us/en/processors/centrino/centrino-advanced-n-6230-brief.html>`__ (2.6.36)
    * `Intel® Centrino® Advanced-N 6205 <http://www.intel.com/content/www/us/en/wireless-products/centrino-advanced-n-6205.html>`__ (2.6.35) 
    * `Intel® Centrino® Advance-N + WiMAX 6150 <http://www.intel.com/content/www/us/en/processors/centrino/centrino-advanced-n-wimax-6150-brief.html>`__ (2.6.30) 
    * `Intel® Centrino® Advanced-N + WiMAX 6250 <http://download.intel.com/support/wireless/wmax/6250/sb/intel_centrino_advancedn_wimax_6250_product_brief1.pdf>`__ (2.6.30) 
    * `Intel® Centrino® Ultimate-N 6300 <http://www.intel.com/content/www/us/en/wireless-products/centrino-ultimate-n-6300.html>`__ (2.6.30) 
    * `Intel® Centrino® Advanced-N 6200 <http://www.intel.com/products/wireless/adapters/6200/>`__ (2.6.30) 
    * `Intel® WiMAX/Wi-Fi Link 5350 <http://www.intel.com/Assets/PDF/prodbrief/320663.pdf>`__ (2.6.27) 
    * `Intel® Ultimate N Wi-Fi Link 5300 <http://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/ultimate-n-wifi-link-5300-brief.pdf>`__ (2.6.27)
    * `Intel® WiMAX/Wi-Fi Link 5150 <http://www.intel.com/Assets/PDF/prodbrief/320663_5150.pdf>`__ (2.6.29)
    * `Intel® Wi-Fi Link 5100 Series <http://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/wifi-link-5100-brief.pdf>`__ (2.6.27)

* 802.11bgn products

    * `Intel® Centrino® Wireless-N 2230 <http://www.intel.com/content/www/us/en/wireless-products/centrino-wireless-n-2230.html>`__ (3.2) 
    * `Intel® Centrino® Wireless-N 2200 <http://www.intel.com/content/www/us/en/wireless-products/centrino-wireless-n-2200.html>`__ (3.2) 
    * `Intel® Centrino® Wireless-N 105 <http://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/centrino-wireless-n-105-brief.pdf>`__ (3.2) 
    * `Intel® Centrino® Wireless-N 135 <http://www.intel.com/content/dam/www/public/us/en/documents/product-briefs/centrino-wireless-n-135-brief.pdf>`__ (3.2) 
    * `Intel® Centrino® Wireless-N 100 <http://www.intel.com/content/www/us/en/processors/centrino/centrino-wireless-n-100-brief.html>`__ (2.6.37) 
    * `Intel® Centrino® Wireless-N 130 <http://www.intel.com/content/www/us/en/processors/centrino/centrino-wireless-n-130-brief.html>`__ (2.6.37) 
    * `Intel® Centrino® Wireless-N 1030 <http://www.intel.com/content/www/us/en/processors/centrino/centrino-wireless-n-1030-brief.html>`__ (2.6.36) 
    * `Intel® Centrino® Wireless-N 1000 <http://www.intel.com/content/www/us/en/processors/centrino/centrino-wireless-n-1000-brief.html>`__ (2.6.30) 

For more information on Intel Wireless products, please visit `Intel
Wireless <http://www.intel.com/wireless>`__.

Git repositories
----------------

There are four repositories that we maintain:

* `iwlwifi-fixes <http://git.kernel.org/?p=linux/kernel/git/iwlwifi/iwlwifi-fixes.git;a=summary>`__ with fixes for the current kernel release cycle 
* `iwlwifi-next <http://git.kernel.org/?p=linux/kernel/git/iwlwifi/iwlwifi-next.git;a=summary>`__ with features for the next kernel release cycle 
* `iwlwifi/linux-firmware <http://git.kernel.org/?p=linux/kernel/git/iwlwifi/linux-firmware.git;a=summary>`__ that feeds the official `linux-firmware <http://git.kernel.org/?p=linux/kernel/git/firmware/linux-firmware.git>`__ tree. It contains early releases, or content that just hasn't been merged in mainline `linux-firmware <http://git.kernel.org/?p=linux/kernel/git/firmware/linux-firmware.git>`__ yet.
* `iwlwifi/backport-iwlwifi.git <https://git.kernel.org/cgit/linux/kernel/git/iwlwifi/backport-iwlwifi.git/>`__ which is a backport based tree with iwlwifi / mac80211 / cfg80211 commits only. This tree is ideal for bisecting.

Firmware
--------

If not installed by your distribution already (check the packages) you
can get the latest firmware from `linux-firmware.git
<http://git.kernel.org/?p=linux/kernel/git/firmware/linux-firmware.git>`__.

If you do get it from linux-firmware.git, you'll have to copy the files
to the appropriate location on your system. Where that appropriate
location is depends (again) on your system distribution. You can
typically find this location by looking in the udev scripts of your
distro, the default on most distributions is /lib/firmware.

Installation of the firmware is simply::

   # cp iwlwifi-*.{ucode,pnvm} /lib/firmware/

You can now load the driver.

Support
-------

If you have technical issues or general questions about Intel Wi-Fi on
Linux, please contact `Intel Customer Support
<https://intel.com/content/www/us/en/support/contact-support.html?productId=59484,59485,83418#@11>`__.

For bug reports and debugging, please see the :doc:`page
<iwlwifi/debugging>` dedicated to that.

7260, 3160, 7265, 7265D, 3165 and 3168 support
----------------------------------------------

Those devices will not be supported by the newest firmware versions: the
last firmware that was released for 3160, 7260 and 7265 is -17.ucode.
Bug fixes will be ported to -17.ucode. 7265D, 3165 and 3168's latest
firmware version is -29.ucode. In order to determine if your 7265 device
is a 'D' version, you can check the dmesg output::

   Detected Intel(R) Dual Band Wireless AC 7265, REV=0x210

The revision number of a 7265D device is 0x210, if you see any other
number, you have a 7265 device.

Firmware_class dependency
-------------------------

The firmware necessary to support the devices is distributed separately
under the `firmware license
<http://git.kernel.org/?p=linux/kernel/git/firmware/linux-firmware.git;a=blob_plain;f=LICENCE.iwlwifi_firmware;hb=HEAD>`__.

Note that many distributions ship the firmware, you could install the
"linux-firmware" package or similar. If that doesn't work, or you need
newer firmware, read on.?

The driver loads the firmware using the kernel's firmware_class
infrastructure. More information can be found under in the
`Documentation/firmware_class/README
<http://kernel.org/doc/Documentation/firmware_class/README>`__ file in
the kernel source. In order to function correctly the driver requires
this to be enabled in your kernel. When you configure the kernel, you
can find this option in the following location::

   Device Drivers ->
       Generic Driver Options ->
           Userspace firmware loading support

You can determine if your kernel currently has firmware loader support
by looking for the ``CONFIG_FW_LOADER`` definition on your kernel's
``.config`` file.

In addition to having the firmware_class support in your kernel, you
must also have a working userspace infrastructure configured. The steps
for installing and configuring this are very distribution specific and
the tools differ, but distributions have this enabled.

Once you have the firmware loader in place (or if you aren't sure and
you just want to try things to see if it works), you need to install the
firmware file into the appropriate location.

About the backport tree
-----------------------

We merge the updates coming from the backport infrastructure on a
regular basis. This means that the bleeding edge of the backport tree
will run against decently recent kernel (usually against Linus's tree).
If you checkout an earlier branch / commit in backport-iwlwifi.git, you
might not be able to work against the most recent kernel. Please keep
that in mind. We have a release cycle based on the backport tree. These
`Core releases </en/users/drivers/iwlwifi/Core_release>`__ can be very
useful for someone who wants to integrate our Wi-Fi solution into his
home made system.

About dual-boot with Windows and "fast-boot" enabled
----------------------------------------------------

If you have a dual-boot machine with a recent version of Windows and
start seeing problems during initialization of the WiFi device when
booting Linux, the problem could be due to the "fast startup" feature on
Windows.

With this feature enabled, Windows don't really shut down the entire
system, but leaves things partially running so you can start the machine
faster again. Try to disable this option, on Windows 10 it should be in
"Control Panel->Hardware and Sound->Power Options->System Settings".
Select "Chooose what the power buttons do" to access the System Settings
from the Power Options. Then disable the "Fast Startup" option in
"Shutdown Settings". This will cause Windows to fully shutdown and may
solve the issue.

About platform noise
--------------------

Wi-Fi heavily relies on radio frequencies, and those are subject to
interference. Interference may come from another Wi-Fi device, or from
many other non Wi-Fi devices (e.g. microwaves) that operates on the same
frequency, and it might also come from other components of your own
device/computer – this is known as 'platform noise'. Platform noise
depends on the actual platform/computer and its design/manufacturing,
and not on the Intel Wi-Fi module.

Some common sources of platform noise might be:

- The PCIe bus, especially when switching in/out of power saving modes.
- `USB3 <https://www.intel.com/content/www/us/en/io/universal-serial-bus/usb3-frequency-interference-paper.html>`__ and graphics (in certain scenarios).
- Sometimes, even the fact that several ingredients’ ground lines are connected can cause noise.

This kind of interference might happen on 2.4GHz band, it is much less likely to happen on 5.2GHz band. Also note that using 40MHz (and not 20MHz) channel bandwidth will increase the probability to suffer from platform noise (since more frequencies might impact the Wi-Fi performance).

Some potential work-around options to this issue:

- Disable Wi-Fi's power save (prevent the PCIe link to go to power
  save): power_scheme=1 module parameter for iwlmvm
- Disable USB3 in BIOS (if possible), it not, just stop using it
- Disable 40MHz on 2.4GHz: cfg80211_disable_40mhz_24ghz module parameter
- Use 5GHz band (on devices that support 5GHz operation)

The fact that one of these options helped doesn't prove that the issue
being troubleshooted is 'platform noise', but it may be an indication.

Another thing that can be tried is to modify the antenna position. The
antennas are typically located in the lid of the laptop. It is worth
trying to open / close the lid or to rotate the system and see if it has
any effect.

About the monitor / sniffer mode
--------------------------------

Our devices support monitor mode. When you have VHT APs around, you
should load the iwlwifi module with::

   amsdu_size=3

This will put lots of pressure on the memory subsystem, but it will
allow you to hear 12K long packets. You may see firmware crashes in case
you didn't set that module parameter.

About iwldvm support and known issues
-------------------------------------

Wi-Fi / Bluetooth coexistence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Having Wi-Fi and Bluetooth running at the same time is a challenge.
These scenarios have been tested thoroughly on 7260 and up, less so on
earlier devices. This is why some people may face issues with devices
that are handled by iwldvm. For users of these devices who have problems
when Wi-Fi and Bluetooth are running concurrently, we suggest to disable
BT Coex by loading iwlwifi with bt_coex_active=0 as a module parameter.

Power management
~~~~~~~~~~~~~~~~

Starting from 3.17, power management has been disabled in iwldvm because
users reported it improved the behavior and was a valid work around for
`issues <https://bugzilla.kernel.org/show_bug.cgi?id=84031>`__. The
commit that disabled power management is `here
<https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=f8dfc607b2b460e8e8adfdfb3c5f5bba3a4ad01b>`__.

To enable manually power management, you can set the following module
parameters to these values: iwlwifi.power_save=Y and iwldvm.force_cam=N.
