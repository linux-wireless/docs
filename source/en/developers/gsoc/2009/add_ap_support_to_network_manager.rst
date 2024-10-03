Add AP Support to Network Manager
=================================

As of 2.6.29 the Linux kernel gets AP support for mac80211 drivers. We
don't yet have any GUI based configuration utilities for AP support.
Currently Network Manager uses wpa_supplicant for station configuration,
a possible approach here is to use hostapd for AP configuration and
usage.

wpa_supplicant now incorporates AP functionality, so that it is "only"
needed to take care of the GUI and wpa_supplicant dbus interface,
presenting AP vs. IBSS in a useful fashion, testing device capabilities
(possibly extending hal/devicekit) and configuring AP support over the
dbus interface.

Mentors
~~~~~~~

-  Dan Williams <dcbw@redhat.com>
