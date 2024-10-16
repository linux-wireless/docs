P2P howto
=========

prerequisites
~~~~~~~~~~~~~

In order to test P2P, you need:

-  a current wireless-testing kernel (or compat-wireless equivalent) or kernel 3.0 later
-  wpa_supplicant from the `hostap <http://hostap.epitest.fi/gitweb/gitweb.cgi?p=hostap.git;a=summary>`__ git tree:

::

   git clone git://w1.fi/srv/git/hostap.git

, or possibly from the hostap-1 stabilisation tree

-  an Atheros ath9k device
-  OR an ar9170 USB device (with carl9170 driver!)
-  (OR another device that has a mac80211 driver, but these are known to work, iwlwifi does **not** currently work with any released microcode)

wpa_supplicant
^^^^^^^^^^^^^^

Use this config file for compiling:

::

   CONFIG_DRIVER_NL80211=y
   # optional, depending on libnl version you want to use:
   # CONFIG_LIBNL20=y

   CONFIG_CTRL_IFACE=y
   CONFIG_WPS=y
   CONFIG_WPS2=y
   CONFIG_P2P=y
   CONFIG_AP=y

   # and maybe DBus

running
~~~~~~~

Start wpa_supplicant with this config file:

::

   ctrl_interface=/var/run/wpa_supplicant
   ap_scan=1

   device_name=my-device-name
   device_type=1-0050F204-1

   # If you need to modify the group owner intent, 0-15, the higher
   # number indicates preference to become the GO. You can also set
   # this on p2p_connect commands.
   #p2p_go_intent=15

   # optional, can be useful for monitoring, forces
   # wpa_supplicant to use only channel 1 rather than
   # 1, 6 and 11:
   #p2p_listen_reg_class=81
   #p2p_listen_channel=1
   #p2p_oper_reg_class=81
   #p2p_oper_channel=1

like this:

::

   ./wpa_supplicant -Dnl80211 -c /path/to/p2p.conf -i wlan0 -dt

Then start ``./wpa_cli`` and use the various ``p2p_*`` commands, for example:

::

   p2p_find
   [wait for peer to be found]
   p2p_connect <peer-mac-addr> pbc go_intent=<0..15>

(or you can use pin of course, go_intent is optional.)

using multiple virtual interfaces for concurrent usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the driver advertises support, wpa_supplicant will automatically create secondary P2P interfaces. To force this without the driver advertising support, you can add the following to the config file:

::

   driver_param=use_p2p_group_interface=1

When this is added, start the supplicant normally on wlan0 like above. Then, when P2P negotiation finishes, it will create a new interface for the group (called "p2p-wlan0-0") and put it into the appropriate mode (GO or P2P client).
