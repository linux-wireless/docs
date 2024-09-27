Go back –> :doc:`Main ath9k driver page <../ath9k>`

ath9k Antenna Diversity
-----------------------

This page documents how antenna diversity is supported by ath9k.

What is Antenna Diversity ?
---------------------------

Adrian Chadd's excellent, detailed `notes <https://wiki.freebsd.org/dev/ath_hal(4)/AntennaDiversity>`__.

Supported cards
---------------

WLAN Only
~~~~~~~~~

-  HB95 (AR9285)
-  HB125 (AR9485)

WLAN and BT
~~~~~~~~~~~

WB195
^^^^^

.. list-table::

   - 

      - **WLAN**
      - **Bluetooth**
      - **Vendor ID**
      - **Device ID**
      - **Subvendor ID**
      - **Subdevice ID**
   - 

      - AR9285
      - AR3011
      - 0x168c
      - 0x002b
      - 0x1a3b (Azurewave)
      - 0x2c37

CUS198
^^^^^^

.. list-table::

   - 

      - **WLAN**
      - **Bluetooth**
      - **Vendor ID**
      - **Device ID**
      - **Subvendor ID**
      - **Subdevice ID**
   - 

      - AR9485
      - AR3012
      - 0x168c
      - 0x0032
      - 0x1a3b (Azurewave)
      - 0x2086
   - 

      - AR9485
      - AR3012
      - 0x168c
      - 0x0032
      - 0x1a3b (Azurewave)
      - 0x1237
   - 

      - AR9485
      - AR3012
      - 0x168c
      - 0x0032
      - 0x1a3b (Azurewave)
      - 0x2126
   - 

      - AR9485
      - AR3012
      - 0x168c
      - 0x0032
      - 0x1a3b (Azurewave)
      - 0x126A

CUS230
^^^^^^

.. list-table::

   - 

      - **WLAN**
      - **Bluetooth**
      - **Vendor ID**
      - **Device ID**
      - **Subvendor ID**
      - **Subdevice ID**
   - 

      - AR9485
      - AR3012
      - 0x168c
      - 0x0032
      - 0x1a3b (Azurewave)
      - 0x2152
   - 

      - AR9485
      - AR3012
      - 0x168c
      - 0x0032
      - 0x105b (Foxconn)
      - 0xe075

WB225
^^^^^

.. list-table::

   - 

      - **WLAN**
      - **Bluetooth**
      - **Vendor ID**
      - **Device ID**
      - **Subvendor ID**
      - **Subdevice ID**
   - 

      - AR9485
      - AR3012
      - 0x168c
      - 0x0032
      - 0x168c (Atheros)
      - 0x3119
   - 

      - AR9485
      - AR3012
      - 0x168c
      - 0x0032
      - 0x168c (Atheros)
      - 0x3122
   - 

      - AR9485
      - AR3012
      - 0x168c
      - 0x0032
      - 0x185f (WNC)
      - 0x3119
   - 

      - AR9485
      - AR3012
      - 0x168c
      - 0x0032
      - 0x185f (WNC)
      - 0x3027
   - 

      - AR9485
      - AR3012
      - 0x168c
      - 0x0032
      - 0x144d (Samsung)
      - 0x4105
   - 

      - AR9485
      - AR3012
      - 0x168c
      - 0x0032
      - 0x144d (Samsung)
      - 0x4106
   - 

      - AR9485
      - AR3012
      - 0x168c
      - 0x0032
      - 0x144d (Samsung)
      - 0x410d
   - 

      - AR9485
      - AR3012
      - 0x168c
      - 0x0032
      - 0x144d (Samsung)
      - 0x410e
   - 

      - AR9485
      - AR3012
      - 0x168c
      - 0x0032
      - 0x144d (Samsung)
      - 0x410f
   - 

      - AR9485
      - AR3012
      - 0x168c
      - 0x0032
      - 0x144d (Samsung)
      - 0xc706
   - 

      - AR9485
      - AR3012
      - 0x168c
      - 0x0032
      - 0x144d (Samsung)
      - 0xc680
   - 

      - AR9485
      - AR3012
      - 0x168c
      - 0x0032
      - 0x144d (Samsung)
      - 0xc708
   - 

      - AR9485
      - AR3012
      - 0x168c
      - 0x0032
      - 0x17aa (Lenovo)
      - 0x3218
   - 

      - AR9485
      - AR3012
      - 0x168c
      - 0x0032
      - 0x17aa (Lenovo)
      - 0x3219

WB335
^^^^^

There are 3 types of WB335-based cards. 1-ANT cards share a LNA between WLAN/BT. 2-ANT cards have dedicated LNA for BT and WLAN and have antennae in both slots (MAIN and ALT), but WLAN RX diversity is disabled for some cards (based on vendor requirements).

.. list-table::

   - 

      - **Type**
      - **No. of connected antennae**
      - **Shared LNA with BT**
      - **Antenna Diversity**
   - 

      - 1-ANT
      - 1
      - Yes
      - No
   - 

      - 2-ANT
      - 2
      - No
      - No
   - 

      - 2-ANT
      - 2
      - No
      - Yes

2-ANT cards supporting WLAN RX diversity.

.. list-table::

   - 

      - **WLAN**
      - **Bluetooth**
      - **Vendor ID**
      - **Device ID**
      - **Subvendor ID**
      - **Subdevice ID**
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x144d
      - 0x411a
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x144d
      - 0x411b
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x144d
      - 0x411c
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x144d
      - 0x411d
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x144d
      - 0x411e
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x168c
      - 0x3027
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x1028
      - 0x302c
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x11ad
      - 0x0642
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x11ad
      - 0x0652
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x11ad
      - 0x0612
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x11ad
      - 0x0832
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x11ad
      - 0x0692
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x1a3b
      - 0x2130
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x1a3b
      - 0x213b
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x1a3b
      - 0x2182
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x144f
      - 0x7202
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x1b9a
      - 0x2810
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x1b9a
      - 0x28a2
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x185f
      - 0x3027
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x185f
      - 0xa120
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x105b
      - 0xe07f
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x105b
      - 0xe081
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x17aa
      - 0x3026
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x17aa
      - 0x4026
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x1043
      - 0x85f2
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x1028
      - 0x020e

CUS252 (AR9565 + xLNA)

.. list-table::

   - 

      - **WLAN**
      - **Bluetooth**
      - **Vendor ID**
      - **Device ID**
      - **Subvendor ID**
      - **Subdevice ID**
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x168c
      - 0x3028
   - 

      - AR9565
      - AR3012
      - 0x168c
      - 0x0036
      - 0x1a3b
      - 0x2176

Enable WLAN/BT RX Antenna Diversity
-----------------------------------

To enable WLAN RX diversity using the ALT antenna, use the module parameter *bt_ant_diversity*. The Bluetooth interface has to be disabled when this feature is enabled in ath9k. Also, BTCOEX should be disabled, so the driver must **not** be loaded with *btcoex_enable=1*.

::

   modprobe ath9k bt_ant_diversity=1

This can also be turned on/off using the debugfs file *bt_ant_diversity*.

::

   echo 1 > /sys/kernel/debug/ieee80211/phy0/ath9k/bt_ant_diversity
   echo 0 > /sys/kernel/debug/ieee80211/phy0/ath9k/bt_ant_diversity

Debug statistics
----------------

The debugfs file *antenna_diversity* can be used to see how the LNA combining algorithm is performing.

::

   cat /sys/kernel/debug/ieee80211/phy*/ath9k/antenna_diversity

   Current MAIN config : LNA1
   Current ALT config  : LNA2
   Average MAIN RSSI   : 40
   Average ALT RSSI    : 16

   Packet Receive Cnt:
   -------------------
                             MAIN            ALT
   TOTAL COUNT   :          30932             63
   LNA1          :          30932              0
   LNA2          :              0             63
   LNA1 + LNA2   :              0              0
   LNA1 - LNA2   :              0              0

   LNA Config Attempts:
   --------------------
                             MAIN            ALT
   LNA1          :              5              0
   LNA2          :              0              5
   LNA1 + LNA2   :              0              0
   LNA1 - LNA2   :              0              0
