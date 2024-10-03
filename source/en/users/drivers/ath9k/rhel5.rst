Using ath9k on RHEL5
====================

`RHEL 5.5 get a wireless facelift
<http://www.redhat.com/docs/en-US/Red_Hat_Enterprise_Linux/5.5.b1/html/Release_Notes/#id3302322>`__.
The facelift consists of getting a new mac80211, cfg80211 and some
wireless drivers backported from 2.6.32 down to 2.6.18. Along with it
came ath9k. This section documents how to get the kernels to get ath9k
on your Centos5/RHEL5 kernels and tries to track any issues present on
them.

Kernel
------

Go grab the kernels here:

http://people.redhat.com/linville/kernels/rhel5/

If you do not have RHEL 5.4 you can try Centos 5.4.

Usage notes
-----------

RHEL 5.4 and 5.5 only support wireless extensions as such only the old
functionality that you are used to with 802.11 will be available. This
is enough to get you using IBSS, and Station mode of operation. AP mode
of operation is not supported, neither is Mesh.

Regulatory wise since this backport did not include nl80211 support it
does mean static regulatory domains are used only. For Atheros cards on
this kernel (ath5k, ath9k) this means the static Atheros world
regulatory domain will be used. Since AP and Mesh is not supported on
this release the only known implication this will have on Atheros
drivers should be not being able to initialize beaconing on some 5 GHz
channels for IBSS. For details on what this implies refer to the
:doc:`ath initialization <../ath>` page.

Tested cards
------------

-  AR5416
-  AR9280
-  AR9285
-  AR9287

Supported modes of operation
----------------------------

* Station 
* IBSS 
* Monitor Mesh is not enabled on the build and AP requires nl80211 and
  since nl80211 is not supported on this kernel you will not be able to
  use AP mode of operation. 

Known issues
------------

* https://bugzilla.redhat.com/show_bug.cgi?id=543719 - AR9285 associates but requires tcpdump to get DHCP replies. 
* http://download.spinellicreations.com/workaround_bugzilla_543719 - workaround allows AR9285 get DHCP replies. Tested on RHEL 5.4 and 5.5 clones (Scientific Linux). 

Enabling Network Manager
------------------------

Upon logging into the GNOME desktop Network Manager is already stared
but the applet does not come up. To do that, as root do::

   service NetworkManager start

To make it automatically enabled do::

   chkconfig NetworkManager on

It should be noted that running this will prevent you from using
wpa_supplicant or the root console to configure and manage the wireless
device manually.
