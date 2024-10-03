ath6kl
======

.. toctree::

   TODO list <ath6kl/todo>
   architecture of ath6kl <ath6kl/architecture>
   Setting up ath6kl <ath6kl/setup>
   debugging help and tips <ath6kl/debug>
   ath6kl coding style <ath6kl/codingstyle>
   ath6kl/wext

Introduction
------------

**'ath6kl**' is the :doc:`FullMAC
<../../developers/documentation/glossary>` wireless driver for Atheros
AR600x family of chips, for example AR6003, AR6004 and AR6005.

Features
--------

- Station (client) mode
- IBSS (Ad-Hoc) mode
- AP mode (requires wpasupplicant/hostapd 1.0 or newer)
- 802.11abg
- 802.11n

    - HT20
    - HT40
    - AMPDU
    - Short GI (40 MHz only)

-  802.11i

    - WEP 64 / 127
    - WPA1 / WPA2

-  802.11d
-  802.11h
-  WMM
-  RFKILL
-  BT co-existence Not supported:

    - monitor mode (no firmware support)

Supported chipsets
------------------

- `AR6003 SDIO <http://www.qca.qualcomm.com/technology/technology.php?nav1=47&product=67>`__
- `AR6004 USB/SDIO <http://www.qca.qualcomm.com/technology/technology.php?nav1=47&product=109>`__
- `AR6005 SDIO <http://www.qca.qualcomm.com/technology/technology.php?nav1=47&product=110>`__ (recognised as ar6003)

Status
------

This driver is upstream as part of the Linux 2.6.37 release under the
staging area. From Linux 3.2 onwards it was promoted from staging to a
proper wireless driver.

It is also available for older kernels through the :doc:`stable
compat-wireless <../download/stable>` releases.

Hacking on ath6kl
-----------------

ath6kl is now part of wireless kernel trees. All the development happens
on `Kalle Valo's ath.git tree
<https://git.kernel.org/cgit/linux/kernel/git/kvalo/ath.git/>`__. To
clone the tree::

   git clone git://git.kernel.org/pub/scm/linux/kernel/git/kvalo/ath.git

The driver is located in drivers/net/wireless/ath/ath6kl. To compile the
driver enable CONFIG_ATH6KL which is found under Device Drivers/Network
device support/Wireless LAN/Atheros Wireless Cards/Atheros ath6kl
support. Also enable CONFIG_ATH6KL_DEBUG to include all debugging code.

Send any patches to Kalle Valo < `kvalo@qca.qualcomm.com
</mailto/kvalo@qca.qualcomm.com>`__ >, but remember also to CC both <
`ath6kl@lists.infradead.org </mailto/ath6kl@lists.infradead.org>`__ >
and < `linux-wireless@vger.kernel.org
</mailto/linux-wireless@vger.kernel.org>`__. To learn more about git you
can refer to our :doc:`Git guide
<../../developers/documentation/git-guide>`. It even documents how to
send patches with *git format-patch*.

Support
-------

For technical support send email to < `ath6kl@lists.infradead.org
</mailto/ath6kl@lists.infradead.org>`__ >, which is a public mailing
list for ath6kl developers and users. Everyone are welcome to `subcribe
to the list <http://lists.infradead.org/mailman/listinfo/ath6kl>`__.

In case there's something you want to send privately just to QCA
engineers, you can send email to < `ath6kl-devel@qca.qualcomm.com
</mailto/ath6kl-devel@qca.qualcomm.com>`__ >. But due to lack of time,
ath6kl developers are not normally able to give private support, so
please send questions to the public mailing list. You get better answers
that way.

IRC
~~~

We have an IRC channel with some of the ath6kl people.

::

   IRC server: irc.freenode.net
   IRC channel: #ath6kl

Please take into account the different timezones and schedules, it might
take a long time to get an answer.

Note: Windows boxen by default seem to block IRC ports so go find
yourself a Linux box ;)

Firmware
--------

Get the firmware from `linux-firmware.git
<http://git.kernel.org/?p=linux/kernel/git/firmware/linux-firmware.git>`__.

Devices
-------

- `Dell Latitude ST Tablet <http://www.mogilowski.net/lang/en-us/2012/02/15/install-ubuntu-on-dell-latitude-st-tablet/>`__ (AR6003 on SDIO)

Subscribe to this page!
-----------------------

You should subscribe to this page so you can get e-mail updates on
changes and news for ath6kl automatically. You'll get an e-mail as soon
as this page gets updated.

Statistics on contributions
---------------------------

Visit the `ath6kl contribution map
<https://docs.google.com/spreadsheet/pub?key=0AtNdeeyGJEJ7dG45U2xrZldlQm80Nlg5QzEwUmtNUGc&single=true&gid=1&output=html>`__
for details on contributions. If you'd like to help keep this
information up to date contact the ath6kl maintainers.

