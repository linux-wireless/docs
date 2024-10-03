Orinoco
=======

.. toctree::

   orinoco/devices

This :doc:`FullMAC <../../developers/documentation/glossary>` driver
covers a range of older wireless cards which have varying capabilities.
All the cards share a common MAC controller. They differ by firmware
(supplied by Agere, Intersil or Symbol) and bus connection.

Depending on the card (and the bus it uses), you will need to load one
of the following drivers:

- airport - An Apple Powerbook/iBook internal Airport.
- orinoco_cs - Typical PCMCIA card.
- orinoco_nortel - PC Card connected to a PCI bus via custom PCMCIA-PCI adapter.
- orinoco_pci - Typical card connected via PCI.
- orinoco_plx - PCMCIA card connected to a PCI bus via a PLX bridge.
- orinoco_tmd - PCMCIA card connected to a PCI bus via a TMD chip.
- orinoco_usb - USB devices.
- spectrum_cs - Driver for Spectrum24 PCMCIA cards.

caveats
-------

WPA support is only available for Agere based cards, and requires a
firmware download on startup. This support was introduced in 2.6.28.

Monitor mode may only be stable with certain firmware revisions.

supported chips
---------------

* All the firmware variants are supported. 
* The Hermes I MAC controller is supported. 
* The Hermes II MAC controller is not supported. 
* Support for USB variants was included in kernel 2.6.35 

available devices
-----------------

See the :doc:`orinoco device list <orinoco/devices>`.

Note that support for Intersil (Prism) devices is being disabled from
v2.6.35. The hostap driver should be more capable for these cards. If
you really need it, enable the ``CONFIG_HERMES_PRISM`` kernel option.

features
--------

working
~~~~~~~

* Station mode 
* Ad-hoc mode 
* Monitor mode 
* WEP 
* WPA-PSK (TKIP) 

not working yet
~~~~~~~~~~~~~~~

* AP mode 
* Radiotap headers in monitor mode 

not supported
~~~~~~~~~~~~~

* WPA2 
* WPA-PSK (CCMP) 

device firmware
---------------

The driver will do its best to work with the firmware it finds on the
card. This may restrict the capabilities of the card.

Firmware download to RAM is available for Symbol based spectrum_cs
cards, and all Agere based cards (including the AirPort).

The spectrum_cs cards require two firmware files, symbol_sp24t_prim_fw
and symbol_sp24t_sec_fw. Extraction tools (for Windows drivers) can be
found in `orinoco-fwutils
<http://prdownloads.sourceforge.net/orinoco/>`__

The Agere firmware file must be named agere_sta_fw.bin. Extraction tools
(for Windows and Apple drivers) can be found in the `agere_fw_utils
<http://repo.or.cz/w/agere_fw_utils.git>`__ tree. WPA support requires
at least firmware v9.42. v9.48 is available from the `linux-firmware
<http://git.kernel.org/?p=linux/kernel/git/firmware/linux-firmware.git>`__
tree.

The Agere based USB cards require bridge firmware, orinoco_ezusb_fw.
Extraction tools can be found in `orinoco-fwutils
<http://prdownloads.sourceforge.net/orinoco/>`__. For WPA the bridge
firmware must be compatible with the v9.42 card firmware. This can be
retrieved by the following commands::

    wget http://web.archive.org/web/20061206062642/http://www.agere.com/mobility/docs/windows_drivers_sr02-2.3.zip
    unzip windows_drivers_sr02-2.3.zip WLAGS51.SYS
    dd if=WLAGS51.SYS of=orinoco_ezusb_fw skip=10312 count=436 bs=16

Known issues
------------

Roaming and WPA_supplicant
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   Lucent/Agere firmware doesn't support manual roaming

On the Agere cards, roaming is controlled by the firmware instead of
userspace. You will get the above message if userspace attempts to
associate with a specific AP rather than by :doc:`SSID
<../../developers/documentation/glossary>`.

If you are using wpa_supplicant use ``ap_scan=2`` mode.

NetworkManager uses wpa_supplicant, so the above also applies.

external links
--------------

* `http://savannah.nongnu.org/projects/orinoco/ <http://savannah.nongnu.org/projects/orinoco/>`__ 
* `Driver homepage <http://www.nongnu.org/orinoco>`__ 
* `Jean Tourhilles orinoco page <http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/Orinoco.html>`__ 
