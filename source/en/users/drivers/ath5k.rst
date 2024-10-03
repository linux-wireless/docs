About Ath5k
===========

.. toctree::

   ath5k/devices

Ath5k is a completely FOSS wireless driver for Atheros based wireless
chipset versions AR5xxx in the Linux Kernel. It has evolved out of
`MadWiFi <http://madwifi-project.org/>`__, `OpenHAL
<https://madwifi-project.org/wiki/About/OpenHAL>`__, and the
`open-sourced HAL
<http://www.kernel.org/pub/linux/kernel/people/mcgrof/legacy-hal.tar.bz2>`__
code of Atheros and `Sam Leffler
<http://svn.freebsd.org/base/projects/ath_hal/>`__.

News
----

2010-12-03
~~~~~~~~~~

**AHB Bus support**: Support for the AHB bus got merged. Now ath5k can
be used on AR231X and AR5312 embedded devices (WiSoC). (`commit
<http://git.kernel.org/?p=linux/kernel/git/linville/wireless-testing.git;a=commit;h=a0b907ee2a71052fefdf6151764095f3f97b3275>`__)

2010-11-30
~~~~~~~~~~

**Preparations for Turbo Mode and half/quarter rate support:** Big
internal update of PHY code to clean up turbo modes and reset and add
half/quarter rate support (50/10MHz channel widths). These new modes are
not enabled yet, and it's unlikely that there will be a standard API for
enabling them in the near future, however developers/researchers can use
them for various projects like 802.11p support. (`first commit
<http://git.kernel.org/?p=linux/kernel/git/linville/wireless-testing.git;a=commit;h=9320b5c4a7260d9593102f378201d17e3f030739>`__)

**Synthesizer-only channel change for newer chips:** On AR2413/AR5413 we
now support faster channel switching by skipping normal reset and
directly setting the channel on PHY while it's still active (`commit
<http://git.kernel.org/?p=linux/kernel/git/linville/wireless-testing.git;a=commitdiff;h=8aec7af99b1e4594c4bb9e1c48005e6111f97e8e>`__).

2010-10-05
~~~~~~~~~~

**Support for virtual STA and AP added:** Support for up to 4 virtual
APs and as many virtual STA interfaces as desired got added (`commit
<http://git.kernel.org/?p=linux/kernel/git/linville/wireless-testing.git;a=commit;h=b1ae1edf9e9872d3aa657cc34ae40c9aadfbc72f>`__).
This feature is sometimes also called "Multi ESSID" and allows us to
configure several AP and STA interfaces on top of only one physical
device.

2010-09-28
~~~~~~~~~~

**802.11e/WME/QoS support:** Support for QoS/WME, using multiple
hardware queues, got merged. (`commit
<http://git.kernel.org/?p=linux/kernel/git/linville/wireless-testing.git;a=commit;h=925e0b061300c94912be36eac16f0b44249a1add>`__)

2010-09-16
~~~~~~~~~~

**Hardware Encryption:** Hardware encryption is enabled again, by
sharing code with ath9k. Before that HW encryption was disabled in AP
mode due to bugs in the ath5k key handling. (`commit
<http://git.kernel.org/?p=linux/kernel/git/linville/wireless-testing.git;a=commit;h=e0f8c2a9b879e1e65d588a40a3c88db69a7d6956>`__)

2010-08-13
~~~~~~~~~~

**Disable ASPM L0s for all cards**: This fixes problems with PCI-E
cards, especially on Acer Aspire One. (`commit
<http://git.kernel.org/?p=linux/kernel/git/linville/wireless-testing.git;a=commit;h=6ccf15a1a76d2ff915cdef6ae4d12d0170087118>`__)

2010-04-07
~~~~~~~~~~

**ANI implementation added:** Adaptive Noise Immunity (ANI) got
implemented. This greatly improves performance in noisy environments.
(`commit
<http://git.kernel.org/?p=linux/kernel/git/linville/wireless-testing.git;a=commit;h=2111ac0d888767999c7dd6d1309dcc1fb8012022>`__)

Mailing list
------------

:doc:`linux-wireless <../../developers/mailinglists>` is the recommended mailing list to use.

The archives for the old ath5k-devel list, which was closed in 2017, are
available `here
<https://lists.ath5k.org/mailman/listinfo/ath5k-devel>`__.

Getting ath5k
-------------

The driver is pre-installed in most current Linux distributions. ath5k
is available through different places:

- The :doc:`wireless-testing <../../developers/process>` tree - this is where the latest code can be found and what the develpers work with.
- The :doc:`Linux wireless compatibility package <../download>` - the most easy way to get and install the latest versions on all stable kernels.
- The Linux kernel from version **2.6.25** and up. However, we recommend to use at least **2.6.31**.
- The Linux kernel **2.6.38** has some bugs in ath5k. We recommend to install the :doc:`Linux wireless compatibility package <../download>` if you are running this kernel and your internet connection is slow or unreliable.
- :doc:`ath5k on RHEL5 <ath9k/rhel5>`

Enabling ath5k
~~~~~~~~~~~~~~

To enable ath5k in the kernel configuration, you must first enable
mac80211::

   Networking support --->
     Wireless  --->
       <M>   cfg80211 - wireless configuration API
       <M>   Generic IEEE 802.11 Networking Stack (mac80211)

Please note that in older kernels there was another 802.11 networking
stack: ``< > Generic IEEE 802.11 Networking Stack``. You do not need
this. This option enables the old SoftMAC which is already removed from
newer kernels. You can still safely enable this though.

You can then enable ath5k in the kernel configuration under::

   Device Drivers  --->
     [*] Network device support  --->
           Wireless LAN  --->
             <M>   Atheros Wireless Cards  ---> 
               <M>   Atheros 5xxx wireless cards support

To try the driver you can do something like this::

   modprobe ath5k
   sudo ip link set wlan%d up
   sudo iwconfig wlan%d essid any
   # Make sure you get auth'd and then assoc'd
   # Then either set an IP manually or get it via DHCP
   ping gw

Supported Devices
-----------------

See the :doc:`ath5k device list <ath5k/devices>`. This list is still
very much incomplete - please add your device/card if it works! A longer
but less reliable list can be found at
http://madwifi-project.org/wiki/Compatibility. It's worth trying your
card with ath5k even though it is not in the list above, if it has one
of the following chips:

Supported Chips
~~~~~~~~~~~~~~~

::

   MAC/Single chip solutions
   -------------------------
   AR5210   - 802.11a   (Crete)
   AR5211   - 802.11ab  (Oahu)*
   AR5212   - 802.11abg (Venice)
   AR5213   - 802.11abg (Hainan)
   AR2413   - 802.11bg  (Griffin Lite)
   AR2414   - 802.11bg  (Griffin)
   AR2415   - 802.11bg  (Talon)**
   AR5413   - 802.11abg (Eagle Lite)
   AR5414   - 802.11abg (Eagle)
   AR5423/4 - 802.11abg (Condor)***
   AR2423/4 - 802.11bg  (Condor)***
   AR2425   - 802.11bg  (Swan)***
   AR2417   - 802.11bg  (Nala)

   PHY
   ----
   RF5110 (Fez)
   RF5111 (Sombrero)
   RF5112/2112 (Derby)
   RF5112a/2112a (Derby2)

\* = AR5211 supports draft-g mode (OFDM only) but it's not supported by ath5k \*\* = We still can't find an AR2415 to test so we are not sure if it works as it should \**\* = PCI-E Lite = No SuperA/G

Supported PCI IDs
~~~~~~~~~~~~~~~~~

Currently supported PCI ID list with respective status report on basic-testing as defined above.

::

   Vendor:device   Type    Name     Basic-testing
   168c:0207       AR5210  AR5210   No tx - working on it
   168c:0007       <<      <<       No tx - working on it

   168c:0011       AR5211  AR5211   Should work
   168c:0012       <<      <<       OK

   168c:0013       AR5212  AR521/3 OK
   a727:0013       <<      <<       Should Work
   10b7:0013       <<      <<       <<
   168c:0014       <<      <<       <<
   168c:0015       <<      <<       <<
   168c:0016       <<      <<       <<
   168c:0017       <<      <<       <<
   168c:0018       <<      <<       <<
   168c:0019       <<      <<       <<
   168c:001a       <<      AR2413/4 OK
   168c:001b       <<      AR5413/4 OK
   168c:001c       <<      Condor   OK (*)
   168c:001d       <<      AR2417   OK

Notes on supported devices
~~~~~~~~~~~~~~~~~~~~~~~~~~

"OK" means that card operates as good as with binary drivers.

"Should work" means that card hasn't been tested (we haven't received any reports) but since chipset is the same with a tested, working card, it should work as well.

(\*) 001c is used also for AR2425 parts.

Features
--------

Supports 802.11abg, depending on the chipset. This driver requires no firmware or binary-only HAL!

working
~~~~~~~

* //Station Mode// 
* //Ad-Hoc Mode// 
* //Mesh Point Mode// 
* //Access Point Mode// (enabled in Linux 2.6.31 and newer and in
  compat-wireless, can also be enabled by
  [[http://madwifi-project.org/wiki/UserDocs/ath5kAccessPoint|patching
  an older kernel]].) 
* //5/10MHz channels// 
* //Turbo (*)// 

not working yet
~~~~~~~~~~~~~~~

* //XR (*)// 
* //SuperA/G (*)// 

\* We don't plan on supporting XR mode nor dynamic 20/40MHz turbo mode supported by hw.

Hacking ath5k
-------------

Developers are encouraged to work using the git repository. If you are
not familiar with git please check out our :doc:`Linux wireless
git-guide <../../developers/documentation/git-guide>` and the
description of the :doc:`development process
<../../developers/process>`. Alternatively you can use the :doc:`Linux
wireless compatibility package <../download>` but please be sure to post
patches in unified diff format (diff -u). To learn how to submit patches
please read our :doc:`Submitting patches guideline
<../../developers/documentation/submittingpatches>`.

Documentation available
~~~~~~~~~~~~~~~~~~~~~~~

Read this section on :doc:`Atheros specifications and documentation
<../../developers/documentation/specs>`.

Atheros common module
~~~~~~~~~~~~~~~~~~~~~

ath5k uses the common shared :doc:`ath.ko module <ath>`.

Reported bugs on ath5k
----------------------

This is a collection of bug reports both unresolved and resolved to help
users track issues and to find patches for fixes which have not yet been
merged.

**Please** when submitting a bug report **always** include your card's
silicon revision for MAC and PHY chips, just look at your kernel log for
a line like this one... or ``dmesg |grep "ath5.*chip"``::

   ath5k phy0: Atheros AR2413 chip found (MAC: 0x78, PHY: 0x45)

...and put it in your report. ``lspci`` information is much less useful
than this.

ath5k TODO List
---------------

Things ath5k developers are currently working on, and other things to do:

* Tx power support (setting tx power) (Nick/Felix -works but experiments
  show that the card transmits only on some standard power levels
  instead of a power range as expected -still debuging, any ideas are
  welcome) 
* Power saving (Bob) 
* AR5210 support (EEPROM etc) (Nick) 
* EAR (EEPROM Added Registers) support 
* Documentation update/cleanup (Nick - added kerneldoc on all hw related
  functions and files, need to do some more reading) 
* Radar detection/DFS stuff 
* Update ath_info 
