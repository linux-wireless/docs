wpa_supplicant Linux documentation page
=======================================

`wpa_supplicant <http://w1.fi/wpa_supplicant/>`__ is a userspace
application which works as a WPA supplicant and SME (to handle
initiating MLME commands). This page is dedicated only to the
documentation relating to the Linux aspects of wpa_supplicant. For
further documentation please refer to:

- `wpa_supplicant's home page <http://w1.fi/wpa_supplicant/>`__
- Latest `README
  <https://w1.fi/cgit/hostap/tree/wpa_supplicant/README>`__ and
  well-commented `configuration file
  <https://w1.fi/cgit/hostap/tree/wpa_supplicant/wpa_supplicant.conf>`__

Supported Linux wireless cards/drivers
--------------------------------------

* Linux drivers that support Linux :doc:`Wireless Extensions
  <../../developers/documentation/wireless-extensions>` v19 or newer
  with WPA/WPA2 extensions 
* All Linux mac80211 drivers 
* Host AP driver for Prism2/2.5/3 (WPA and WPA2) 
* `Linuxant DriverLoader <http://www.linuxant.com/driverloader/>`__ with
  Windows NDIS driver supporting WPA/WPA2 
* Agere Systems Inc. Linux Driver (Hermes-I/Hermes-II chipset) (WPA, but
  not WPA2) 
* madwifi (Atheros ar521x) 
* ATMEL AT76C5XXx 
* Linux ndiswrapper 
* Broadcom wl.o driver 
* Wired Ethernet drivers 

Download
--------

Please refer to the wpa_supplicant home page for release information

http://w1.fi/wpa_supplicant/

Git
~~~

You can clone this tree::

   git://w1.fi/srv/git/hostap.git

If you have to use http you can also use::

   http://w1.fi/hostap.git

For your convenience we have here a few shortcuts:

* `Release graph <http://w1.fi/releases.html>`__
* `development branch ChangeLog <http://w1.fi/gitweb/gitweb.cgi?p=hostap.git;a=blob_plain;f=wpa_supplicant/ChangeLog>`__
* `stable branch ChangeLog <http://w1.fi/gitweb/gitweb.cgi?p=hostap-06.git;a=blob_plain;f=wpa_supplicant/ChangeLog>`__

Developer's documentation
-------------------------

* `Developers <http://w1.fi/wpa_supplicant/devel/>`__

Mailing lists
-------------

* `Mailing list <http://lists.shmoo.com/mailman/listinfo/hostap>`__
* `New mailing list archives <http://lists.shmoo.com/pipermail/hostap/>`__

Bugs / feature requests
-----------------------

If you want to make sure your bug report of feature request does not get
lost, please report it through the bug tracking system as a new
bug/feature request.

http://w1.fi/bugz/enter_bug.cgi

Setting the regulatory domain
-----------------------------

You can add a line to your wpa_supplicant configuration file which
specifies the ISO / IEC 3166 country code. This is available as of
wpa_supplicant version 0.6.7.

::

   country=US

Enabling control interface and nl80211 driver
---------------------------------------------

New wpa_supplicant (as of commit cd27df100b from git) command line options

::

   -o<driver> and -O<ctrl>

can now be used to override the parameters received in add interface
command from dbus or global ctrl_interface. This can be used to enable a
control interface when using NetworkManager or Connman or change the
wpa_supplicant driver used.

The wpa_supplicant control interface is used by wpa_cli and wpa_gui to
control wpa_supplicant. GUI applications use the DBUS service file to
run wpa_supplicant with specific parameters. You can edit this file to
take advantage of these new changes.

The wpa_supplicant service file is typically available on systems in the
following location::

   /usr/share/dbus-1/system-services/fi.epitest.hostap.WPASupplicant.service

This service file typically looks like this::

   [D-BUS Service]
   Name=fi.epitest.hostap.WPASupplicant
   Exec=/sbin/wpa_supplicant -u -f /var/log/wpa_supplicant.log
   User=root

Change it as follows to enable usage of wpa_cli or wpa_gui and also to
use nl80211 when available::

   [D-BUS Service]
   Name=fi.epitest.hostap.WPASupplicant
   Exec=/sbin/wpa_supplicant -u -onl80211 -O/var/run/wpa_supplicant
   User=root

If you are compiling the supplicant you will want
CONFIG_CTRL_IFACE_DBUS=y to enable -u, CONFIG_DRIVER_NL80211=y for
-onl80211 and CONFIG_CTRL_IFACE=y for the control interface. To enable
usage of wpa_cli you will also want CONFIG_READLINE=y. Also enable
CONFIG_DEBUG_FILE=y for the debug file.

WPS and WEP
-----------

The Wi-Fi Protected Setup (WPS; originally Wi-Fi Simple Config, or WSC)
2.0 specification added explicit requirement that disallows use of WEP.
wpa_supplicant complies with that requirement and rejects WEP networks
if WPS 2.0 is enabled. It should also be noted that there has been a
number of interoperability issues with WEP and WPS 1.0 since this
combination has never been tested in WFA certification programs.

WPS and hidden SSIDs
--------------------

Hidden SSIDs are explicitly disallowed with WPS (any version of WPS),
the protocol just does not work with hidden SSIDs.

RSN preauthentication
---------------------

Read :doc:`hostapd's RSN pre authentication documentation <hostapd>` for
a review on what is expected on the AP configuration side of things. If
APs are configured properly with RSN preauthentication wpa_supplicant
will by default enable this so long as WPA2 networks are used.

Based on some events wpa_supplicant update our RSN PMKSA candidate list
for preauthentication. The RSN PMKSA candidate list for wpa_supplicant
is determined by rsn_preauth_scan_result(). rsn_preauth_scan_result()
gets called today after a scan completion. For each BSS found it
rsn_preauth_scan_result() will ensure:

* It must not be the same AP (BSSID) its already associated to 
* Same SSID required 
* The AP must be ensuring it annotates it has preauthentication
  capability on its IEs otherwise we'll ignore processing RSN preauth
  for it unless the Opportunistic Key Caching has been enabled for the
  SSID on wpa_supplicant.conf (okc=1). 
* Enabling okc=1 will also first treat APs with the same SSID as if they
  had the same PMK, this behaviour is disabled by default RSN
  preauthentication is enabled by default on wpa_supplicant for WPA2
  networks you can modify okc=1 as documented above however. A full
  example working `wpa_supplicanat RSN preauthentication supplicant.conf
  <https://gist.github.com/mcgrof/5515450>`__ is available for review.
