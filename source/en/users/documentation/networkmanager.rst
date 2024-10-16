Network Manager
===============

In summary Network Manager is a connection manager and right now
supports working with Ethernet/PPP/Wireless.

Network Manager attempts to make networking invisible. When moving into
areas you've been before, Network Manager automatically connects to the
last network the user chose to connect to. Likewise, when back at the
desk, Network Manager will switch to the faster, more reliable wired
network connection.

Releases
--------

Latest release
~~~~~~~~~~~~~~

It is recommended distributions use Network Manager 0.7 from subversion.
Bellow are a few features worth mentioning.

Multiple Active Devices
^^^^^^^^^^^^^^^^^^^^^^^

To facilitate neat stuff like connection sharing, and to expand the
usefulness of Network Manager, we now allow more than one active network
device. In this model, the "active" device will be the one with the
default route and the highest route priority. Part of this effort
included:

- libnl enhancements for routing table manipulation
- cleanup of NM code for determining default device
- modifications of NM code to allow multiple active devices

System-wide Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

Obviously nobody likes to have to unlock the keyring on every login.
Wireless networks can't be used until somebody logs into the machine,
because Network Manager stores the authentication information on a
per-user basis. While there are various (we think) legitimate reasons
for this behavior, there is a need to configuration information to be
accessible outside of user sessions.

The current plan allows for users to "publish" configuration information
for specific wireless networks to all users of the system, or make the
data "system-wide". To preserve the same interface with which NM
currently retrieves configuration information (the NetworkManagerInfo
dbus API), a system-wide configuration daemon will be used. This daemon
must:

* have no UI, since it must run at system start up without X
* Access system configuration information like GConf mandatory/default
  settings, KDE configuration, text files
* Cooperate with user-session NMI instances, like applets  This
  enhancement is being tracked in
  `bug 331529 <https://bugzilla.gnome.org/show_bug.cgi?id=331529>`__

wpa_supplicant dbus Control Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We now have a dbus-based control interface for wpa_supplication. NM uses
dbus to talk to wpa_supplicant, rather than the old socket-based control
interface which simply didn't have enough flexibility. wpa_supplicant
needs to be started as a system daemon, much like dhcdbd and
(optionally) bind are today. This should reduce connection latency since
we don't need to exec a copy of wpa_supplicant for each connection.
Scanning is also now handled through wpa_supplicant for better
coordination.

wpa_supplicant 0.5 has basic dbus functionality, including the ability
to add/remove interfaces from its control, request scan results, and
broadcast scan result available signals. (updated 2006-06-26)

Rewritten libnm_glib
^^^^^^^^^^^^^^^^^^^^

libnm_glib was rewritten

More Wireless/Wired Authentication Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some 802.1x auth methods which wpa_supplicant is capable of are now
supported by NetworkManager.

Convert VPN dbus API to use Dicts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The code for using dicts is already in CVS
(libnm-util/dbus-dict-helpers.c); we need to convert the VPN service <->
NM dbus API over to use it. This will help forward and backward
compatibility of the VPN plugins by making the dbus API more flexible.
Some work has already been done to convert specific messages like the
IP4Config message to 'optionally' use dicts in a backwards compatible
way.

Clean up the dispatcher-daemon
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make it pass more stuff in the environment of the scripts it executes,
like primary IP address/netmask/gateway/etc of the new connection, stuff
like that perhaps. Should probably use the new libnm-glib too.

More libnl
^^^^^^^^^^

Move the relevant code from src/backends/NetworkManagerGeneric.c that
does system("/sbin/ip xxx") to libnl

KILL KILL KILL dhcdbd
^^^^^^^^^^^^^^^^^^^^^

Make NM spawn /sbin/dhclient and manage the DHCP client lifecycle within
NM rather than having dhcdbd do it. We want to spawn it with a custom
dhclient-script that forwards the options back to NetworkManager a lot
like the current dhclient-script sends them to dhcdbd. When we have
this, we can also do smart things about re-acquiring leases we have had
in the past for this AP, for example. (Robert Frank is looking into
this...)

Add BLOB support to wpa_supplicant D-Bus interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

wpa_supplicant can accept binary blobs for things like certificates, and
then you can refer to them via URLs like "blob://" in network
configuration blocks that NM sends to wpa_supplicant. We basically want
to download the certificate blob from NM to wpa_supplicant for a
specific connection, if it uses certificates (like with WPA-EAP), but I
don't think I added the BLOB command at all.

Basic rfkill support
^^^^^^^^^^^^^^^^^^^^

Starting with HAL 0.5.10, there is basic rfkill support. For the moment,
poll rfkill status every 5 seconds if a HAL object with the "killswitch"
capability exists. HAL will eventually grow signals for this which
should then be used instead of polling. Enable/disable wireless based on
rfkill status, and make the applet aware that NM has enabled/disabled
wireless networking.

Older releases
~~~~~~~~~~~~~~

You can find the older release on `GNOME's FTP site
<http://ftp.gnome.org/pub/GNOME/sources/NetworkManager/>`__.

Mailing list
------------

Network Manager has its own `mailing list
<http://mail.gnome.org/mailman/listinfo/networkmanager-list>`__.

wpa_supplicant usage
--------------------

In order to associate to a wireless network and scan NM uses
wpa_supplicant as its back-end.

Debugging Network Manager
-------------------------

If you have issues with Network Manager we recommend you start Network
Manager with debugging options.

Bugs on Network Manager
-----------------------

You can report bugs on Network manager on its `bugzilla
<http://bugzilla.gnome.org/enter_bug.cgi?product=NetworkManager>`__.

Hacking on Network Manager
--------------------------

This section describe how to get the code and design goals you should
keep in mind.

Getting the code
~~~~~~~~~~~~~~~~

In order to build NetworkManager you need the GNOME gnome-autogen.sh
script, found in the 'gnome-common' SVN module. Grab that and install
it, if you don't have it already::

   svn co svn://svn.gnome.org/svn/gnome-common/trunk gnome-common
   cd gnome-common
   ./autogen.sh --prefix=/usr
   cd macros2
   make
   sudo make install

Next, grab NetworkManager from SVN HEAD. To checkout and build from SVN
HEAD::

    git clone git://anongit.freedesktop.org/NetworkManager/NetworkManager.git
    cd NetworkManager
    ./autogen.sh --prefix=/usr --sysconfdir=/etc --localstatedir=/var
    make
    sudo make install

And if you want to play with the applet, you need network-manager-applet, too::

   svn co svn://svn.gnome.org/svn/network-manager-applet/trunk network-manager-applet
   cd NetworkManager
   ./autogen.sh --prefix=/usr --sysconfdir=/etc --localstatedir=/var
   make
   sudo make install

Design goals
~~~~~~~~~~~~

* Simplicity: operation should be simple. Users should not have to set
  up networks, properties, or profiles beforehand. Users should not be
  presented with complex, unnecessary dialogs that require them to enter
  details about anything more complicated than a WEP key. Also, we
  decided that profiles aren't very user-friendly, and therefore we
  actively try to avoid profiles. Example: there aren't any profile
  wizards, or anything resembling profiles. This is by design.
* Visual Clarity: user interface elements of NetworkManager (for
  example, the panel applet) should be simply laid out and should not
  show any settings other than those an average user would need on a
  daily basis. If the user isn't going to click on it at least every
  other day, it shouldn't be immediately visible in the menu. They only
  add to clutter and confuse the average user.

Example: infrequently used settings and options are not shown in the
NetworkManager panel applet.

* Automation: operation should be as automatic as possible. By default,
  everything should "Just Work" with as little interaction as possible.
  Everything that can be done automatically or detected automatically,
  should be. NetworkManager should not be doing
  things users don't expect.

Example: connecting to the last-used wireless network that's available
when NetworkManager starts up.
