rndis_wlan
==========

The **rndis_wlan** :doc:`FullMAC
<../../developers/documentation/glossary>` driver was added to the stock
kernel as of 2.6.25. It is also available through :doc:`the
compat-wireless-2.6 package <../download>` for pre-2.6.25 kernels.

supported chips
---------------

Broadcom 4320 USB WLAN chip, which is only wireless RNDIS chip known to
date. Althought rndis_wlan has vendor/device-id list, driver can also
autodetect any new wireless RNDIS device.

available devices
-----------------

- Asus WL169gE
- Belkin F5D7051
- BT Voyager 1055
- Buffalo WLI-U2-KG125S
- Buffalo WLI-USB-G54
- Eminent EM4045
- Linksys WUSB54GSCv1 (v2 unsupported)
- Linksys WUSB54GSv1
- Linksys WUSB54GSv2
- U.S. Robotics USR5420
- U.S. Robotics USR5421

what works
----------

* unencrypted networks 
* WPA/WPA2 PSK/Enterprise 
* WEP should work 
* ad-hoc should work, unencrypted and WEP 
* hidden networks, unencrypted and WEP 

what does not
-------------

* Hidden + WPA 

known problems
--------------

* Driver has been tested with b-variant of chipset/firmware. Older
  devices with a-variant of chipset/firmware used to operate poorly with
  this driver but this should be resolved on newer kernels (>=2.6.32). 

* The driver included in kernels <= 2.6.37 shows very few scan results
  with a-variant devices. Workaround this by configuring the device
  statically (e.g., /etc/network/interfaces or by issuing
  iwconfig/dhclient right after boot). Do not rely on a beacon being
  detected to determine if a network is available or not --- this is
  :doc:`NetworkManager <../documentation/networkmanager>`'s approach,
  which can make it take hours until it detects and configures an
  available network.  This issue should be resolved in kernel version
  2.6.38. 
