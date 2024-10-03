Glossary
========

Terms we use throughout the wiki with which you should become familiar.

.. glossary::

   AP
     Access Point.

   BSS
     BSS stands for *Basic Service Set*. The coverage of an access point is called a BSS.

   cfg80211
     Kernel side of configuration management for wireless devices.
     :term:`nl80211` is the User-space side of configuration management for
     wireless devices. Works together with :term:`FullMAC` drivers and also
     with :term:`mac80211`-based drivers.

   CLI
     CLI stands for `Command-line interface
     <https://en.wikipedia.org/wiki/Command-line_interface>`__. These
     are utilities you can run in the console or terminal emulator.

   FullMAC
     FullMAC is a term used to describe a type of wireless card where
     the :term:`MLME` is managed in hardware. You would **not** use
     :term:`mac80211` to write a :term:`FullMAC` wireless driver.

   git-describe
     git-describe is a git command. It outputs something like this::

         v3.12-11297-g6579946

     The first part is the *tag* for the current release. The second
     part is the number of patches which have been applied since the tag
     was applied. The last part, after the first *g* is the SHA1 commit
     ID of the last commit applied.

   IBSS
     IBSS stands for *Independent Basic Service Set*. Its basically
     Ad-Hoc mode. See `Independent Basic Service Set
     <https://en.wikipedia.org/wiki/Independent_Basic_Service_Set>`__

   Information Element
     An Information Element (IE) is a part of management frames in the
     IEEE 802.11 wireless LAN protocol. IEs are a device's way to
     transfer descriptive information about itself inside management
     frames. There are usually several IEs inside each such frame, and
     each is built of `Type-length-value <https://en.wikipedia.org/wiki/Type-length-value>`__ (TLVs).

     The common structure of an IE is as follows::

           |   1   |    1   |     1-255       |
           +-------+--------+-----------------+
           | Type  | Length |     Data        |
           +-------+--------+-----------------+

     Whereas the vendor specific IE looks like this::

           |   1   |    1   |          4        |    1-251   |
           +-------+--------+-------------------+------------+
           |  221  | Length |        OUI        |     Data   |
           +-------+--------+-------------------+------------+

   iw
     :doc:`iw <../../users/documentation/iw>` is a new :term:`nl80211`
     based :term:`CLI` configuration utility for wireless devices.

   nl80211
     User-space side of configuration management for wireless devices.
     It is a Netlink-based user-space protocol. :term:`cfg80211` is Kernel
     side of configuration management for wireless devices.

     :doc:`Several user-space applications <../../users/documentation>`
     are available which utilize :term:`nl80211`. See :doc:`Developer
     Docs for nl80211 <nl80211>`.

   mac80211
     A driver API for SoftMAC wireless cards. See :doc:`Developer Docs
     for mac80211 <mac80211>`.

     See also :term:`SoftMAC`.

   MLME
     MLME Stands for *Media Access Control (MAC) Sublayer Management
     Entity*. MLME is the management entity where the Physical layer
     (PHY) MAC state machines reside. Examples of states a MLME may
     assist in reaching:

     - Authenticate
     - Deauthenticate
     - Associate
     - Disassociate
     - Reassociate
     - Beacon
     - Probe

     :term:`mac80211`'s MLME management implementation is currently
     handled by ``net/mac80211/mlme.c``. This handles only the
     client-side MLME.

   PHY
     physical-layer controller

   SME
     Station Management Entity, often prepended with AP (Access Point)

   SoftMAC
     SoftMAC is a term used to describe a type of WNIC where the
     :term:`MLME` is expected to be managed in software.
     :term:`mac80211` is a driver API for SoftMAC WNIC, for example.

   SSID
     SSID stands for *Service Set IDentifier*. The SSID is a code
     attached to all packets on a wireless network to identify each
     packet as part of that network. The code consists of a string of
     1-32 octets (usually represented as case sensitive alphanumeric
     characters).

     See also `SSID <https://en.wikipedia.org/wiki/Service_set_(802.11_network)>`__

   STA
     *Station* (or *STA*) is the generic term for a device with a radio
     that can communicate with other *stations* in a wireless network.
     Common forms of a *station* are access points (AP), computers, or
     phones.

     See also `Station\_(networking)
     <https://en.wikipedia.org/wiki/Station_(networking)>`__ or
     `Wireless access point
     <https://en.wikipedia.org/wiki/Wireless_access_point>`__.

   WE
     WE stands for :doc:`Wireless-Extensions <wireless-extensions>` -
     the old driver API and user <--> kernel communication transport.
     Obsoleted by :term:`cfg80211`

   WEXT
     WEXT stands for :doc:`Wireless-Extensions <wireless-extensions>` -
     the old driver API and user <--> kernel communication transport.
     Obsoleted by :term:`cfg80211`

   WIPHY
     Wireless :term:`PHY`
