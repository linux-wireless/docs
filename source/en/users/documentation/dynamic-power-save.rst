Dynamic power save
------------------

mac80211 has a feature called *Dynamic power save* which allows the wireless device to dynamically go into power save mode if the device is associated and no network traffic is going through the card for a certain period of time, with a default value set to 100 ms. To enable dynamic power save the wireless driver must support power save mode of operation.

Some device drivers only power save manually. Some others have it enabled all the time. To enable/disable power save manually you would use:

::

   iw wlan0 set power_save on

The dynamic power save timeout (the time for no traffic through the card before going to powersave) is affected by the :doc:`pm-qos <../../developers/documentation/pm-qos>` network latency setting.

To enable power save a wireless device can sleep at most the duration of the BSS :doc:`DTIM interval <../../developers/documentation/ieee80211/power-savings>`. It will wake up during that period to listen for beacons from the AP to see if the AP has buffered frames for it. Refer to the :doc:`power savings guide <../../developers/documentation/ieee80211/power-savings>` for more details as to how this works.

Drivers with power save enabled by default
------------------------------------------

-  Atheros ath9k for single-chips (>= AR9280)
-  TI wl1251
-  TI wl1271

Ways to tune dynamic power save from userspace
----------------------------------------------

Default timeout
~~~~~~~~~~~~~~~

You can tune dynamic power save by tuning the default timeout.

::

   iwconfig wlan0 power 500m

Network latency
~~~~~~~~~~~~~~~

You can also user :doc:`pm-qos <../../developers/documentation/pm-qos>` to tune dynamic power save based on network latency requirements of your userspace applications.
