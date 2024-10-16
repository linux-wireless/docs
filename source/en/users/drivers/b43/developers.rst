Developers info
===============

This page contains info for developers, not really useful for end users.

List of firmware
----------------

Earlier we were using other, older firmwares. The table contains all
drivers supported by fwcutter.

.. list-table::
   :header-rows: 1

   - 

      - Driver
      - Version of wl
      - Firmware
      - Firmware extractor
   - 

      - b43
      - `6.30.163.46 <http://www.lwfinger.com/b43-firmware/broadcom-wl-6.30.163.46.tar.bz2>`__
      - 784.2
      - b43-fwcutter-018
   - 

      - b43
      - `5.100.138 <http://www.lwfinger.com/b43-firmware/broadcom-wl-5.100.138.tar.bz2>`__
      - 666.2
      - b43-fwcutter-015
   - 

      - b43
      - `5.100.104.2 <http://www.lwfinger.com/b43-firmware/broadcom-wl-5.100.104.2.tar.bz2>`__
      - 644.1001
      - b43-fwcutter-015
   - 

      - b43
      - `5.10.144.3 <http://www.lwfinger.com/b43-firmware/broadcom-wl-5.10.144.3.tar.bz2>`__
      - 508.154
      - b43-fwcutter-015
   - 

      - b43
      - `5.10.56.2808 <http://www.lwfinger.com/b43-firmware/broadcom-wl-5.10.56.2808.tar.bz2>`__
      - 508.10872
      - b43-fwcutter-015
   - 

      - b43
      - `5.10.56.51 <http://www.lwfinger.com/b43-firmware/broadcom-wl-5.10.56.51.tar.bz2>`__
      - 508.1107
      - b43-fwcutter-015
   - 

      - b43
      - `5.10.56.27.3? <http://downloads.openwrt.org/sources/broadcom-wl-5.10.56.27.3_mipsel.tar.bz2>`__
      - 508.1084
      - b43-fwcutter-014
   - 

      - b43
      - `4.178.10.4 <http://downloads.openwrt.org/sources/broadcom-wl-4.178.10.4.tar.bz2>`__
      - 478.104
      - b43-fwcutter-013
   - 

      - b43
      - `4.150.10.5 <http://downloads.openwrt.org/sources/broadcom-wl-4.150.10.5.tar.bz2>`__
      - 410.2160
      - b43-fwcutter-012
   - 

      - b43
      - `4.80.53.0 <http://downloads.openwrt.org/sources/broadcom-wl-4.80.53.0.tar.bz2>`__
      - 351.126
      - b43-fwcutter-012
   - 

      - b43legacy
      - `3.130.20.0 <http://downloads.openwrt.org/sources/wl_apsta-3.130.20.0.o>`__
      - 295.14
      - b43-fwcutter-012
   - 

      - bcm43xx (deprecated)
      - `3.130.20.0 <http://downloads.openwrt.org/sources/wl_apsta-3.130.20.0.o>`__
      - 295.14
      - bcm43xx-fwcutter-006

bcm43xx
-------

bcm43xx is the old deprecated driver. It uses the ieee80211 + softmac
libraries of code shared with other drivers. This stack is deprecated
and being replaced by the new :doc:`mac80211
<../../../developers/documentation/mac80211>` stack. A new stack implies
brand new, re-written driver(s): b43 and b43legacy.

Related tools
-------------

ssb-sprom
^^^^^^^^^

A tool for the modification of the Broadcom Sonics Silicon Backplane
SPROM (e.g. you can permanently change the MAC address or the PCI IDs of
your wireless card – useful on some (e.g.  Compaq/HP) laptops where the
BIOS checks these at boot. It's now part of b43-tools::

    git clone git://git.bues.ch/b43-tools.git

To use the sprom tool, it is necessary to get a disk copy of your sprom
from the /sys file system. The file path for the sprom contents depends
on the bus layout of the specific computer being used and will be
something like::

     /sys/devices/pci0000:00/0000:00:0d.0/0000:04:00.0/ssb_sprom

It is not recommended that you try to type the name. Instead, you should
use the following commands to get the working copy::

    SSB_SPROM=$(find /sys/devices -name ssb_sprom)
    echo $SSB_SPROM``

If the echo command only results in a single instance of "/sys/...", you may proceed. For systems with more than one SSB-based interface, there will be such a string for each, and the command that sets the SSB_SPROM symbol will have to be changed. In the name above, the sequence states that this device is attached to the 0'th PCI bus via bridge 0d.0 and is device 04:00.0 on that bridge. To find which of your SSB devices to select, use the 'lspci -v' command. On my system, the first line of such output for my interface is "04:00.0 Network controller: Broadcom Corporation BCM94311MCG wlan mini-PCI (rev 02)". For this device, one would use::

    SSB_SPROM=$(find /sys/devices -name ssb_sprom | grep 04:00.0)
    echo $SSB_SPROM

Of course, the "04:00.0" needs to match your system, and check the
output value to determine that there is now a single instance of
"/sys..." and that the path matches the device whose SPROM is to be
changed. If not, adjust the string after 'grep' accordingly.

Once the SSB_SPROM variable matches the path to ssb_sprom for your
device, get a working copy of the sprom contents with::

    sudo cat
    $SSB_SPROM > ssb_sprom_copy

You may now look at the contents of your sprom with the command::

    ssb-sprom -i ssb_sprom_copy -P

As an example, let us suppose that you have purchased a Dell mini-pci
card to use in an HP laptop. The HP BIOS refuses to use the card when
the pcivendor is Dell (code 0x1028), not HP (code 0x103C). From the
information provided by an "ssb-prom –help" command, we learn that the
switch needed to change this vendor code is "–subv". To change that
code, we use the command::

    ssb-sprom -i ssb_sprom_copy -o new_ssb_sprom_copy --subv 0x103C

to write the HP vendor ID to our working copy. I use different input and
output files so as not to destroy the original. If further changes are
needed, for example the PCI product ID, the command::

        ssb-sprom -i new_ssb_sprom_copy -o new_ssb_sprom_copy --subp 0x137C

would be used. Note that the input and output files may be the same.

Once you think you have updated correctly, use the following to check the contents::

    ssb-sprom -i ssb_sprom_copy -P

Once the sprom contents are the way you want them, and presumably
correct, you are ready to rewrite the file. First, use::

    echo $SSB_SPROM

to ensure that this symbol still contains the SPROM path. If not, then
it will have to be reloaded as discussed above.

You are then ready to rewrite the sprom with::

    sudo cp new_ssb_sprom_copy $SSB_SPROM

IMPORTANT: The **2.6.32 kernel** will throw the following error message
and refuse to write the SPROM::

   SPROM write: Could not freeze devices. No suspend support. Is CONFIG_PM enabled?

Apply the following patch to the **2.6.32 kernel** to allow programming
the SPROM on that kernel. Alternatively install a newer or an older
kernel::

   http://marc.info/?l=linux-wireless&m=125900356410309&q=raw

Once again, you are urged to be absolutely certain of the contents of
the working copy BEFORE writing it to hardware. If your interface
becomes unusable as a result of writing incorrect data into the sprom,
the responsibility is YOURS. Once again, you have been warned.

A firmware assembler/disassembler can be found in the git repository
at::

    git clone git://git.bues.ch/b43-tools.git

There are more development and debugging tools available in the
b43-tools git repository. Just clone it and read the shipped
documentation files::

    git clone git://git.bues.ch/b43-tools.git

b43-tools mirror
----------------

A mirror of the b43-tools GIT repository
(git://git.bues.ch/b43-tools.git) can be found on github:
https://github.com/mbuesch/b43-tools
