Central Regulatory Domain Agent
===============================

CRDA acts as the udev helper for communication between the kernel and
userspace for regulatory compliance. It relies on :doc:`nl80211
<../documentation/nl80211>` for communication. CRDA is intended to be
run only through udev communication from the kernel. The user should
never have to run it manually except if debugging udev issues.

License
-------

CRDA is licensed under the `copyleft-next
<https://raw.github.com/richardfontana/copyleft-next/master/Releases/copyleft-next-0.3.0>`__
license while :doc:`wireless-regdb <wireless-regdb>` is licensed under
the `ISC license <https://en.wikipedia.org/wiki/ISC_license>`__.

Code
----

https://git.kernel.org/cgit/linux/kernel/git/mcgrof/crda.git/

::

   git://git.kernel.org/pub/scm/linux/kernel/git/mcgrof/crda.git

Releases
--------

You can find official crda releases on the `crda release page
<http://drvbp1.linux-foundation.org/~mcgrof/rel-html/crda/>`__, older
releases can be downloaded through the `crda archive
<https://www.kernel.org/pub/software/network/crda/>`__

Status
------

The new regulatory infrastructure went in as of 2.6.28, so CRDA can be
used in kernels >= 2.6.28. It is required for 802.11d operation in
2.6.29.

CRDA is no longer needed as of kernel v4.15 since commit `007f6c5e6eb45
<https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=007f6c5e6eb45>`__
("cfg80211: support loading regulatory database as firmware file") added
support to use the kernel's firmware request API which looks for the
firmware on /lib/firmware.

Host requirements
-----------------

- libc/ublibc
- regulatory.bin file
- libnl >= libnl1
- udevd [but read below for alternative] You can skip out on the CRDA
  and udev requirement by using CONFIG_CFG80211_INTERNAL_REGDB but read
  below on its own requirements.

CONFIG_CFG80211_INTERNAL_REGDB
------------------------------

If you do not want to install CRDA on a host, you can simply enable the
CONFIG_CFG80211_INTERNAL_REGDB on your kernel. Once enabled you can
place the db.txt from the wireless-regdb into net/wireless/db.txt. The
downside to using this option is that you will need to rebuild your
kernel for any regulatory updates, therefore using
CONFIG_CFG80211_INTERNAL_REGDB is not recommended.

If using CONFIG_CFG80211_INTERNAL_REGDB without updating
net/wireless/db.txt you'll end up with the static world regulatory
domain, so if using CONFIG_CFG80211_INTERNAL_REGDB you should be sure to
update net/wireless/db.txt otherwise you may end up spending a lot of
time debugging an issue that does not exist. To help with this a patch
has been sent to print a warning when a kernel has been built with
CONFIG_CFG80211_INTERNAL_REGDB but the database is emtpy. If you happen
to also have CONFIG_CFG80211_REG_DEBUG then compiling of the kernel will
simply fail.

Build requirements
------------------

* python and the m2crypto package (python-m2crypto)
* libgcrypt or libssl (openssl) header files
* nl library and header files (libnl1 and libnl-dev) available at git://git.kernel.org/pub/scm/libs/netlink/libnl.git
* RSA public key of Seth Forshee, we include this as part of this
  package so you do not need to install it. This RSA public key comes
  from the wireless-regdb.git tree and we keep it up to date here.
* regulatory database (regulatory.bin, no need to build just put the
  file in REG_BIN location) from::

      git://git.kernel.org/pub/scm/linux/kernel/git/sforshee/wireless-regdb.git

Letting the kernel call CRDA
----------------------------

We use userspace events (uevents) to let the kernel speak to userspace.
Below is an example udev rule you can place into your distribution's
udev rules directory (usually ``/etc/udev/rules.d/``). Note that most
distributions have udev configured with inotify on the udev rules
directory, so there is no need to restart udev after adding the new
rule.

::

   # Example file, should be put in /etc/udev/rules.d/regulatory.rules
   KERNEL=="regulatory*", ACTION=="change", SUBSYSTEM=="platform", RUN+="/sbin/crda"

Dynamic reading of trusted public keys
--------------------------------------

CRDA can be built with gcrypt or openssl support. If using openssl
(USE_OPENSSL=1) you can enable dynamic loading of trusted public keys
and stuff. Trusted public keys can be put into the directory::

   /etc/wireless-regdb/pubkeys

gcrypt support does not support reading public keys dynamically as gcrypt currently lacks a PEM parser.

Changing regulatory domains
---------------------------

Helping compliance by allowing to change regulatory domains
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Linux allows changing regulatory domains in compliance with regulatory
restrictions world wide, including the US FCC. In order to achieve this
devices always respect their programmed regulatory domain and a country
code selection will only enhance regulatory restrictions. This is in
accordance with the `FCC part 15 country code selection knowledge base
publication number 594280
<https://fjallfoss.fcc.gov/oetcf/kdb/forms/FTSSearchResultPage.cfm?switch=P&id=39498>`__.
As an example if your device was programmed for operation in the US
which allows operation on channels 1-11 on the 2.4 GHz band and you
visit Japan which allows operation on channels 1-14 and you change your
regulatory domain to JP you will not be able to use channel 12, 13 or 14
(CCK). But if you have a device programmed for operation in Japan and
visit the US and you select US as your regulatory domain you will have
channel 12-14 disabled.

Userspace applications can request the kernel to change regulatory
domains. The following userspace applications currently allow you to do
this:

* :doc:`../../users/documentation/iw`
* the latest `wpa_supplicant <http://hostap.epitest.fi/wpa_supplicant/>`__ (from the git tree)

Using iw to change regulatory domains
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use iw from the command line as follows::

   iw reg set US

Using wpa_supplicant to change regulatory domains
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get the `wpa_supplicant <http://hostap.epitest.fi/wpa_supplicant/>`__
(as of 0.6.7) and then add as part of your configuration file a line
that has something like this::

   COUNTRY=US

Using Network Manager to change regulatory domains
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This needs to be implemented, but since Network Manager uses
wpa_supplicant it should just be a matter of adding a user interface
option to let a user select an alpha2 and then adding the country entry
into the wpa_supplicant configuration entered.

Debugging kernel to CRDA communication
--------------------------------------

To debug communication between the kernel and udev you can monitor udev
events::

   udevadm monitor --environment kernel
