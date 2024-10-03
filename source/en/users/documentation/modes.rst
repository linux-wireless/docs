Wireless Modes
##############

A wireless interface always operates in one of the following operating modes.
The mode sets the main functionality of the wireless link.

AccessPoint (AP) infrastructure mode
************************************

An Access Point acts as the Master device in a managed wireless network. It
holds the network together by managing and maintaining lists of associated
Stations. It also manages security policies. The network is named after the
MAC-Address (BSSID) of the AP. The human readable name for the network, the
SSID, is also set by the AP.

.. important::

   To use AP mode in Linux you need to use :doc:`hostapd <hostapd>`, at least a
   current 0.6 release, preferably from git. See: https://wireless.erley.org

Station infrastructure mode
***************************

The Station device connects to an access point by sending certain management
packets to it. This process is called the *authentication* and *association*.
After the AP sent the *successful* association reply, the station is part of the
network.

This mode is also called *managed* in the wireless extension tools (``iwconfig``
et. al.)

Monitor mode
************

Monitor mode is a passive-only mode, no packets are transmitted. All incoming
packets are handed over to the host computer completely unfiltered. This mode is
useful to see what's going on on the network.

With mac80211, it is possible to have a network device in monitor mode in
addition to a regular device, this is useful to observe the network whilst using
it. However, not all hardware fully supports this as not all hardware can be
configured to show all packets while in one of the other operating modes,
monitor mode interfaces always work on a "best effort" basis.

With mac80211, it's also possible to transmit packets in monitor mode, which is
known as packet injection. This is useful for applications that wish to
implement MLME work in userspace, for example to support nonstandard MAC
extensions of IEEE 802.11.

.. seealso::

   :doc:`radiotap <../../developers/documentation/radiotap>`

Ad-Hoc (IBSS) mode
******************

The Ad-Hoc mode is used to create a wireless network without the need of having
a Master Access Point in the network. Each station in an IBSS network is
managing the network itself. Ad-Hoc is useful for connecting two or more
computers to each other when no (useful) AP is around for this purpose.

Wireless Distribution System (WDS)
**********************************

The Distribution System is the wired uplink connection to an AP. The Wireless
Distribution System is the wireless equivalent to it. WDS serves as a wireless
communication path between cooperating APs (usually in a single ESS), it can be
used instead of cabling. Read :doc:`iw WDS <iw>` documentation for details on
how to enable this, but also review and consider using :doc:`4-address mode
<iw>`.

Mesh
*****

Mesh interfaces are used to allow multiple devices to communication with each
other by establishing intelligent routes between each other dynamically.

Please see `Wikipedia's entry on 802.11s
<http://en.wikipedia.org/wiki/IEEE_802.11s>`__. and `Wireless mesh network(WMN)
<http://en.wikipedia.org/wiki/Wireless_mesh_network>`__.

In order to achieve mesh portal functionality, you can bridge a mesh interface
with a regular ethernet interface.