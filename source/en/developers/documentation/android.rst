Support for cfg80211 / mac80211 Linux 802.11 drivers on Android
===============================================================

This section tries to document what is required to support 802.11 Linux
drivers on Android.

The current status quo
----------------------

Android uses wireless-extensions to support its 802.11 drivers. The
drivers that Android devices have up to this day used are all using
wireless-extensions for communication. The Android codebase also uses a
custom wpa_supplicant. The details of this can be found `on android's
porting wifi page <http://source.android.com/porting/wifi.html>`__ and
`on this porting wifi drivers to android
<http://blog.linuxconsulting.ro/2010/04/porting-wifi-drivers-to-android.html>`__
documentation.

Roadmap
-------

The current Android 802.11 interface should change to use nl80211. The
proper approach would be to extend nl80211 upstream (where necessary)
and use an unmodified wpa_supplicant in Android.

Doing this will mean adding support to Android for *all* new 802.11
cfg80211/mac80211 Linux drivers.

Work
----

Anyone working on this?

LKML References
---------------

-  `Android for mac80211 / cfg80211 802.11 nag v1 <https://lkml.org/lkml/2011/2/1/440>`__
-  `Android PM enhancements <https://lkml.org/lkml/2011/3/23/448>`__
