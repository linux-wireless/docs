compat-wireless-old
===================

We started providing compatibility support since 2.6.22 as that is when
:doc:`mac80211 <../../developers/documentation/mac80211>` was introduced
onto the stock kernel but we have now added initial support for older
kernels, starting at 2.6.21.

Requirements
------------

You will need at least of these kernels:

- 2.6.21 (non-PCI support, PCI was never tested)
- 2.6.22
- 2.6.23
- 2.6.24
- 2.6.25
- 2.6.26 If you want to have support for WMM or 802.11n then you will need enabled in your kernel:

   - CONFIG_NETDEVICES_MULTIQUEUE
   - CONFIG_NET_SCHED If you **do not** have these enabled you will not
     get WMM or 802.11n support. Note that if you are on a kernel
     between 2.6.23..2.6.26 you should **not** have CONFIG_MAC80211_QOS
     enabled as part of your kernel as this was not part of your kernel,
     it was removed on 2.6.23 because the new CONFIG_NET_SCHED and
     CONFIG_NETDEVICES_MULTIQUEUE handled it for us.

Additionally, the kernel you're building for needs a valid ".config"
file, if it isn't present compat will assume you have PCI, USB and
PCMCIA built into your kernel and if not, fail building.

Release notes
-------------

Later kernels got WMM supported redesigned for mac80211, when using
compat-wireless old we will build our own WMM support for you without
usage of the new kernel QOS features. This is exactly how WMM was
handled in mac80211 on 2.6.22, but keep in mind 2.6.22 didn't come with
any mac80211 drivers, it came just with mac80211 itself. Since you get a
custom WMM support you also get 802.11n support, which requires WMM
support.

Its worth noting compat-wireless-old currently does not get any
attention from any developer as such its not getting further updates.
Patches are always welcomed though.

Where to download
-----------------

You can get compat-wireless-old from:

http://wireless.kernel.org/download/compat-wireless-2.6/

Building and installing
-----------------------

**Extract**:

Extract the content of the package::

   tar jxvf compat-wireless-old.tar.bz2

**Build**:

Build the latest Linux wireless subsystem::

   cd compat-wireless-old.tar.bz2
   make

**Install**:

We use the updates/ directory so your distribution's drivers are left intact::

   sudo make install

**Uninstall**:

This nukes our changes to updates/ so you can go back to using your
distribution's supported drivers::

   sudo make uninstall

**Unload**:

Since you might be replacing your old mac80211 drivers you should first
try to unload all existing mac80211 and related drivers. Note also that
broadcom, zydas, and atheros devices have old legacy drivers which you
need to be sure are removed first. We provide a mechanism to unload all
old and legacy drivers first so you should run to be sure::

   sudo make unload

**Load**:

Before loading modules you must first unload your old wireless subsystem
modules. Read above how to do this. If you know what module you need you
can simply load the module using modprobe. If you simply are not sure
you can use, just reboot the box.

Drivers
-------

Here is the list of all the drivers we support in this package.

.. list-table::

   - 

      - :doc:`Drivers <../drivers>`
   - 

      - :doc:`adm8211 <../drivers/adm8211>`
   - 

      - :doc:`at76_usb <../drivers/at76_usb>`
   - 

      - :doc:`ath9k <../drivers/ath9k>`
   - 

      - :doc:`ath5k <../drivers/ath5k>`
   - 

      - :doc:`b43 <../drivers/b43>`
   - 

      - :doc:`b43legacy <../drivers/b43>`
   - 

      - :doc:`iwl3945 <../drivers/iwl3945>`
   - 

      - :doc:`iwlagn <../drivers/iwl4965>`
   - 

      - :doc:`ipw2100 <../drivers/ipw2100>`
   - 

      - :doc:`ipw2200 <../drivers/ipw2200>`
   - 

      - :doc:`ub8xxx <../drivers/libertas>`
   - 

      - :doc:`libertas_cs <../drivers/libertas>`
   - 

      - :doc:`p54_pci <../drivers/p54>`
   - 

      - :doc:`p54_usb <../drivers/p54>`
   - 

      - :doc:`rndis_wlan <../drivers/rndis_wlan>`
   - 

      - :doc:`rt2400pci <../drivers/rt2400pci>`
   - 

      - :doc:`rt2400pci <../drivers/rt2400pci>`
   - 

      - :doc:`rt2500pci <../drivers/rt2500pci>`
   - 

      - :doc:`rt2500usb <../drivers/rt2500usb>`
   - 

      - :doc:`rt61pci <../drivers/rt61pci>`
   - 

      - :doc:`rt73usb <../drivers/rt73usb>`
   - 

      - `rtl8180 <en/users/Drivers/rtl8180>`__
   - 

      - :doc:`rtl8187 <../drivers/rtl8187>`
   - 

      - :doc:`zd1211rw <../drivers/zd1211rw>`

Known issues
------------

* ath9k on older kernels ath9k is currently only enabled on kernels >=
  2.6.26. If a developer is interested in older kernels they'll have to
  add compatibility support for it. 
* Strange wireless device names: Lets clarify device names first.
  Regularly you should only see two new device names: 

    * wmaster0
    * wlan0 The //wmaster0// device is what we call :doc:`the master
      device <../../developers/documentation/mac80211>`. The master
      device is an internal master device used only by mac80211. It
      should be ignored by users. If possible we will try to hide it
      from users later.

On distribution releases with old udev rules you may end up with strange
network device names, for example, *wlan0_rename*. You may also end up
with master device names such as *eth3*, when this was actually intended
to be named *wmaster0*. This happens because master interface has the
same MAC address as the real interface, and it is created first. The old
udev rule, which keys on the MAC addres, may rename it to device names
like *eth3*, for example. Then the real interface is created, udev sees
that it has already renamed an interface with that MAC and gives it the
*wlan0_rename* name.

If you delete the generated rename rules, it should create the correct
ones on the next boot. Alternately, you could add::

   ATTRS{type}="1"

selector to your current rule. Debian puts these autogenerated udev
rules in /etc/udev/rules.d/z25_persistent-net.rules. Other distributions
may vary slightly.

 * :doc:`nl80211 <../../developers/documentation/nl80211>`

Kernels <= 2.6.22 now get nl80211 support, however, genl_multicast_group
won't work. This compatibility cannot be extended to older kernels as
the struct genl_family was extended on 2.6.23 to add the struct
list_head mcast_groups. Without this you will not be able to use nl80211
events which uses this heavily. The compat-wireless-old release does not
have nl80211 events though so you should not care about this.

* b43: b43 and b43legacy now load. Since there was an old softmac
  broadcom driver we provide a load script for this driver. To load the
  new generation drivers (b43 and b43legacy) you can run::

       sudo b43load b43

  To revert back to bcm43xx you can run::

       sudo b43load bcm43xx

* :doc:`MadWifi <../drivers/madwifi>`:

If :doc:`MadWifi <../drivers/madwifi>` is present the build system will
detect this and disable it. It does this by simply renaming ath_pci.ko
to ath_pci.ko.ignore. This lets us disable the MadWifi driver without
blacklisting it which could cause issues with users later. If you would
like to enable MadWifi at a later time and disable ath5k you can run::

   sudo athload madwifi

To revert back to :doc:`ath5k <../drivers/ath5k>` you can run::

   sudo athload ath5k

* prism54, p54pci, p54usb? We don't provide prism54 in this package
  because distributions already provide it. p54 is its replacement.
  prism54 works only with full MAC cards. p54 works with both full MAC
  and soft MAC cards. Should prism54 get any new updates we'll start
  packaging it here. 
* Firmware: If your driver needs firmware please be sure to check the
  driver page for that driver here: 

:doc:`en/users/Drivers <../drivers>`

Building for external kernels
-----------------------------

If you have a kernel you do not have installed but yet want to build the
compat-wireless-old drivers for it you can use this syntax::

   make KLIB=/home/mcgrof/kernels/linux-2.6.23.9 \
      KLIB_BUILD=/home/mcgrof/kernels/linux-2.6.23.9

Bugs
----

If you've found a bug you are expected to fix it as this is not being
actively developed. Patches are always welcomed of course.

::

   linux-wireless@vger.kernel.org

How about compatibility work for kernels older than 2.6.21 ?
------------------------------------------------------------

Sure, feel free to send patches. The main work was designed to support
kernels >= 2.6.22 as that was when :doc:`mac80211
<../../developers/documentation/mac80211>` was introduced. Some drivers
are available for 2.6.21 but not all drivers can work on that kernel due
to an CRC-ITU-T algorithm dependency.

ChangeLog
---------

compat-wireless-old ChangeLog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See the `compat-wireless-old ChangeLog
<http://git.kernel.org/?p=linux/kernel/git/mcgrof/compat-wireless-2.6-old.git;a=summary>`__
to view changes made necessary in order to keep advancing this package.

License
-------

This work is a subset of the Linux kernel as such we keep the kernel's
Copyright practice. Some files have their own copyright and in those
cases the license is mentioned in the file. All additional work made to
building this package is licensed under the GPLv2.

Developers
----------

Hacking on compat-wireless-2.6-old
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The old compat-wireless tree is used for kernels <= 2.6.26. We don't
have an automatic script to update it. It is updated manually, as such
if you want it updated please send patches to linux-wireless mailing
list and hack on it as you would with the kernel using git on its own
tree.

TODO
----

* Compatibilty work for 2.6.18 –> 2.6.20 

RHEL5, Centos5, and Debian etch seems to be stuck on 2.6.18. Patches are welcomed.

* Dialog (make menuconfig) option for this package 

Patches for compatibility work
------------------------------

For kernels >= 2.6.27 please send patches against

::

   git://git.kernel.org/pub/scm/linux/kernel/git/mcgrof/compat-wireless-2.6-old.git

::

   To: Luis R. Rodriguez <mcgrof@winlab.rutgers.edu>
   CC: linux-wireless@vger.kernel.org
   Subject: [PATCH] compat-wireless-old: fix foo

Checking out compat-wireless-2.6-old.git tree
---------------------------------------------

To checkout the compat-wireless-2.6.git tree you do:

::

   git-clone git://git.kernel.org/pub/scm/linux/kernel/git/mcgrof/compat-wireless-2.6-old.git

Note: you do not need a wireless-testing clone to use or hack on this tree.
