Wireless module parameters
==========================

This page is dedicated to the 802.11 subsystem's module parameters. We
try to keep these to a minimum.

mac80211
--------

These are the module parameters for mac80211

ieee80211_disable_40mhz_24ghz
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use this to disable 40 MHz support from the 2.4 GHz band
completely. This module parameter exist on mac80211 since 2.6.39 but
after kernel 3.0 the module parameter was moved to cfg80211 so you would
do

cfg80211
--------

These are the module parameters for cfg80211

ieee80211_disable_40mhz_24ghz
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use this to disable 40 MHz support from the 2.4 GHz band
completely. This is available on cfg80211 after the 3.0 kernel release.
