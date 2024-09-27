Go back --> :doc:`Main ath9k driver page <../ath9k>`

ath9k bluetooth coexistence
---------------------------

This page documents how :doc:`bluetooth coexistence <../../documentation/bluetooth-coexistence>` is supported by ath9k.

Supported Coexistence Schemes
-----------------------------

-  :doc:`2-wire <../../documentation/bluetooth-coexistence>`
-  :doc:`3-wire <../../documentation/bluetooth-coexistence>`
-  MCI (Message-Based Coexistence Interface)

Enabling bluetooth coexistence
------------------------------

Bluetooth coexistence has to be manually enabled when loading ath9k by setting the *btcoex_enable* module parameter.

::

   modprobe ath9k btcoex_enable=1

Cards supporting BTCOEX
-----------------------

2-wire (two-chip cards with separate WLAN and BT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

     * WB197 ( AR9287 + AR3011 ) 

.. _wire-two-chip-cards-with-separate-wlan-and-bt-1:

3-wire (two-chip cards with separate WLAN and BT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

     * WB195 ( AR9285 + AR3011 ) 
     * WB225 ( AR9485 + AR3012 ) 

MCI (SoC-type cards with integrated WLAN and BT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

     * WB222 ( based on AR9462 ) 
     * WB335 ( based on AR9565 ) 

3-wire scheme details
---------------------

Some Atheros cards in both the AR9002 and AR9003 family use this scheme in which WLAN and Bluetooth time-shares their usage of the 2.4 GHz band. Three pins are used in this scheme.

.. list-table::
   :header-rows: 1

   - 

      - PIN
      - Driven by
      - Details
   - 

      - BT_ACTIVE
      - BT
      - Signals that Bluetooth device is expecting TX or RX activity. Provides WLAN with information about when the antenna is being used by Bluetooth.
   - 

      - BT_PRIORITY
      - BT
      - At the start of BT_ACTIVE, it is asserted to indicate the priority of the Bluetooth activity. Then, this pin indicates the TX/RX status of the Bluetooth activity.
   - 

      - WLAN_ACTIVE
      - WLAN
      - Indicates when WLAN has taken the antenna.

PTA (Packet Traffic Arbitration ) Algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BT weights and WLAN weights are programmed in the hardware by the driver. Hardware infers the Bluetooth activity by sampling the BT_ACTIVE signal. Whenever there’s Bluetooth activity, hardware compares the assigned weight of Bluetooth traffic and the current WLAN traffic. If Bluetooth traffic has a lower priority, hardware will continue WLAN traffic, thus stomping on the Bluetooth side (and possible interference on WLAN side as well). If Bluetooth traffic has a higher priority, hardware will abort WLAN traffic and treat it as if there’s collision on-air.
