Documentation
#############

Here we start documentation for users for all new wireless utilities. The list
is short, but we'll try to add more as we go.

.. toctree::
   :maxdepth: 1

   documentation/modes
   documentation/faq
   documentation/iw
   documentation/module-parameters
   documentation/rfkill
   ../developers/regulatory/crda
   documentation/hostapd
   documentation/wpa_supplicant
   documentation/wowlan
   documentation/power-consumption
   ../developers/wapi
   ../developers/dfs
   documentation/acs
   ../developers/openwirelessmovement

External links
**************

- `WiMAX on Linux <http://linuxwimax.org/>`__
- `IWD Wifi Management Daemon <https://iwd.wiki.kernel.org/>`__

YouTube links
*************

* `Linux wireless support series - Baked: May 20 2011 <https://www.youtube.com/playlist?p=PLA12950D8456F1818>`__
* `RFC: 802.11 DFS support on mac80211 and ath9k <https://www.youtube.com/watch?v=_yyFiLFx4Mg>`__ - LinuxCon 2011 
* `802.11s on LInux mac80211 <https://www.youtube.com/watch?v=frvXN9pmLO4>`__ - LinuxCon 2011 
* `wmediumd for mac80211_hwsim <http://www.youtube.com/watch?v=FzZsTd4Bj7I>`__ - LinuxCon 2011 

by Adrian Chadd:

* `Inside the Atheros WiFi Chipset - Adrian Chadd <https://www.youtube.com/watch?v=WOcYTqoSQ68>`__ - subtitle: how I learned to love the HAL - Defcon 2014. - ath9k DMA, PHY, MAC ... 
* `The future of wireless networking - mobile, gigabit and beyond - Adrian Chadd <https://www.youtube.com/watch?v=pmespp2HDsU>`__ - (2013) 802.11ac, 802.11ad, hybrid operating modes, aggressive mobile power saving, the challenges involved in building a network stack that will handle 1+ gigabit/sec throughput. FreeBSD/Linux/Atheros HAL.
*  `Wireless drivers (ath9k, HAL, BSD) - Adrian Chadd <https://www.youtube.com/watch?v=9P-r3H0bY8c>`__

.. note:: 
     
     Adrian Chadd worked at Atheros for 18 months on chip bring-up and open
     source work. He worked with other Atheros developers to open source the USB
     firmware for the AR5513 and ath9k-htc hardware, as well as the AR9300 HAL,
     used by Linux and FreeBSD.

Wireless managers
*****************

This is the list of available known wireless managers you can use in distributions

.. toctree::
   :maxdepth: 1

   documentation/networkmanager
   documentation/wicd
   documentation/connman

Wireless sniffers / intrusion testing / packet injection utilities
******************************************************************

* `wireshark <https://www.wireshark.org/>`__ - a packet analyzer 
* `kismet <https://www.kismetwireless.net/>`__ - an 802.11 layer2 wireless network detector, sniffer, and intrusion detection system 
* :doc:`packetspammer <documentation/packetspammer>` - a mac80211 packet injection utility 
* `aircrack-ng <https://www.aircrack-ng.org/>`__ - an 802.11 WEP and WPA-PSK keys intrusion testing program 
* `Test AP injection code <https://w1.fi/gitweb/gitweb.cgi?p=hostap.git;a=blob_plain;f=wlantest/inject.c;hb=HEAD>`__
* `horst <https://br1.einfach.org/tech/horst/>`__ - lightweight 802.11 wireless LAN analyzer 

Helping users and developers
****************************

Please consider reading these sections to help developers help you more
efficiently.

.. toctree::
   :maxdepth: 1

   documentation/acs
   documentation/aspm
   documentation/bluetooth-coexistence
   documentation/connman
   documentation/dynamic-power-save
   documentation/faq
   documentation/fix_propagation
   documentation/hostapd
   documentation/iw
   documentation/modes
   documentation/module-parameters
   documentation/networkmanager
   documentation/packetspammer
   documentation/power-consumption
   documentation/reporting_bugs
   documentation/rfkill
   documentation/wicd
   documentation/wowlan
   documentation/wpa_supplicant

To the very curious user
************************

In case you want to read up on what things are being advanced within Linux
wireless. This should help users become familiar with our latest developments.

.. toctree::
   :maxdepth: 1

   ../developers/documentation/wireless-extensions
   ../developers/documentation/mac80211
   ../developers/documentation/cfg80211
   ../developers/documentation/nl80211
   ../developers/documentation/mac80211/tracing
   ../developers/testing/wifi-test
