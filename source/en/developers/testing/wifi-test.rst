Wifi-test
=========

.. warning::

   This project no longer exists. We've archived a copy of
   :download:`wifi-test 1.0
   <../../../media/en/developers/testing/wifi-test-1.0.tar.gz>`

wifi-test is fully automated test script for linux wireless drivers.
It's an open-source project.

Git tree
--------

::

   http://www.intellinuxwireless.org/repos/wifi-test.git

Mailing list and posting patches
--------------------------------

This project has its own `mailing list
<https://lists.sourceforge.net/lists/listinfo/wifi-test-devel>`__.

Wifi test 1.0
-------------

`wifi-test 1.0 <http://intellinuxwireless.org/testing/Download/wifi-test-1.0.tar.gz>`__ covers following wireless features:

- BSS: BSS association, fragmentation/RTS/CTS, BSS channels etc
- IBSS: IBSS association, IBSS fragmentation/RTS/CTS, IBSS channels.
- Security: WEP (BSS/IBSS), WPA/WPA2, 802.1X.
- Power management: S3/S4, RFKILL
- Performance: upload/download speed for different combinations.
- Others: Wext mode, nl80211 mode
- 802.11 a/b/g/n: Above features in a/b/g/n band.

Testing environment setup
-------------------------

The minimum testing system requirements are listed below.

* Two test machines: One as test machine, the other as peer machine in
  IBSS network testing. If only BSS is tested, one test machine is
  enough.
* One server machine: The server machine needs two Ethernet cards, one
  connects to the Test machine network and the other to the AP network.
* One AP: Support Cisco AP, Dlink and ASUS AP with CLI (Command Line
  Interface). For example, Dlink DWL-8200 AP and Cisco1200 series AP.
  Here is an example of our test environment:

::

   ---------------
   | Test Machine |
   --------------\
                  \ ---------                    --------
                   | Test    |     -------      |  AP    |   ---
                   | machine |----| Server |----| network|--| AP |
                   | network |     -------      |        |   ---
                  / ---------                    --------
   ------------- /
   | Peer Machine |
   --------------

Bugs
----

If you run into bugs please report them through the `Intel Bugzilla
<http://bugzilla.intellinuxwireless.org/>`__.
