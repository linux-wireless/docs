About Radiotap
==============

Radiotap is a `de facto <https://en.wikipedia.org/wiki/de_facto>`__
standard for 802.11 frame injection and reception. Details of radiotap
can be found on its new website.

- http://www.radiotap.org/

Linux support
-------------

Linux has started to embrace radiotap on its drivers and driver APIs.
Relevant files:

.. note::

   move ieee80211_radiotap.h to kerneldoc

-  `include/net/ieee80211_radiotap.h <http://git.kernel.org/?p=linux/kernel/git/linville/wireless-2.6.git;a=blob;f=include/net/ieee80211_radiotap.h;hb=HEAD>`__ - Our definitions for its support
-  `include/net/cfg80211.h <http://git.kernel.org/?p=linux/kernel/git/linville/wireless-2.6.git;a=blob;f=include/net/cfg80211.h;hb=HEAD>`__ - iterator support for possible radiotap arguments
-  `include/net/mac80211.h <http://git.kernel.org/?p=linux/kernel/git/linville/wireless-2.6.git;a=blob;f=include/net/mac80211.h;hb=HEAD>`__ - mac80211 support for radiotap

mac80211 support for radiotap
-----------------------------

mac80211 supports receiving radiotap headers before the actual 802.11
frame. The driver informs mac80211 when it adds a radiotap header by
enabling the *RX_FLAG_RADIOTAP* flag on *flag* member of *struct
ieee80211_rx_status*. When a driver is done with a frame it passes it to
mac80211 via *ieee80211_rx*.

mac80211 informs drivers it wants radiotap headers in its received skbs
during *ieee80211_open()*, the device's open routine (dev->open). It
does this when the type of interface being opened is of type
*NL80211_IFTYPE_MONITIR*, a monitor interface. It informs the driver by
enabling IEEE80211_CONF_RADIOTAP on *struct ieee80211_hw*\ s *struct
ieee80211_conf* *flags* Sequentially, mac80211 will disable this flag
during *ieee80211_stop()* (dev->stop) for *NL80211_IFTYPE_MONITOR*
interface types.
