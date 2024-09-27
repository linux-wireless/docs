Tech mailing list
-----------------

The EFF has set up a tech mailing list for those interested in helping. If interested please subscribe:

http://lists.openwireless.org/mailman/listinfo/tech

Open Wireless Movement - review for Linux
-----------------------------------------

The `EFF <https://www.eff.org>`__ has announced an effort to promote open wireless networks in metropolitan areas and recommendations on default software solutions available for 802.11 access points and some protocol / design review for enabling encrypted sessions with open wireless networks. The `EFF <https://www.eff.org>`__ is calling this an `Open Wireless Movement <https://www.eff.org/deeplinks/2011/04/open-wireless-movement>`__. This page is dedicated to reviewing their proposal and brainstorming / keeping track of solutions available on Linux.

This page will focus on the core innovating petitions by the EFF and technical solutions for Linux based 802.11 APs. In short the biggest technical challenges faced by the petition is to come up with alternative solutions to the main concerns of why home owners typically desire to close out their wireless networks to the public:

-  Protect their data
-  Priority of traffic

Open but encrypted WiFi
-----------------------

One of the ideas being recommended is the call for some enhancements which would allow anyone to connect to an 802.11 access point but at the same time enable encryption. One possible solution is to use WPA2-Enterprise and just come up with an easy to use mechanism for `EAP authentication <http://en.wikipedia.org/wiki/Extensible_Authentication_Protocol>`__.

For authentication with `EAP <http://en.wikipedia.org/wiki/Extensible_Authentication_Protocol>`__ possible solutions:

::

     * Use OpenID 
     * Use fixed username/passwd with [[http://en.wikipedia.org/wiki/Extensible_Authentication_Protocol#PEAP|PEAP]] 

Another idea is to use `IEEE 802.11u <http://en.wikipedia.org/wiki/IEEE_802.11u>`__ where the user would have to have a relationship with an external network and be enabled locally based on this criteria / arrangements.

Open but safer WiFi
-------------------

We could sanitize traffic coming from the wireless side to make it a lot harder to attack the network. For example:

::

       * Frames that aren't management frames, IPv4, IPv6, or ARP are dropped. 
       * For IPv4, AP tracks DHCP leases.  No IPv4 or ARP traffic passes until the client has a valid (and unexpired) lease. 
       *  * ARP from the wired side never gets onto the wireless side.  Instead, the AP answers on the client's behalf. 
       *  * ARP from the wireless side is sanitized. 
       *  * IPv4 from the wireless side is checked for consistency with the AP's ARP cache and the sender's DHCP lease. 
       *  * IPv4 from the wired side is dropped unless the destination MAC and IP match a valid wireless DHCP lease. 
       *   IPv6 would work similarly but is more complicated due to fancier autoconfiguration. 
       *   mDNS and similar protocols might need some thought.  As a first pass, unauthenticated clients could be banned from sending or receiving broadcast traffic other than DHCP. Something like this would make it hard to subvert the network from the wireless side and would prevent broken clients (like Android and iPad) from causing problems.  As a more extreme measure, unauthenticated wireless clients could be prohibited from communicating at all with anything else on the local network. 

Priority of traffic concerns
----------------------------

Traffic priority concerns can be addressed by enabling home owners to create two BSS on one 802.11 AP, one which is available to the public and another private BSS which has higher priority for traffic. Traffic shaping techniques can be used to enable these preferences, but we will also need quick easy access to set this up with a GUI interface.

Helping move between Open APs
-----------------------------

::

       *   * Use a common SSID 

Basic setup
-----------

To help test this you at least need a RADIUS server of some sort, how to set this up is documented on the :doc:`hostapd documentation page <../users/documentation/hostapd>`.
