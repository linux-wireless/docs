Power consumption on ath9k
==========================

This section documents our metrics used, results and interesting tidbits
of information about power consumption for ath9k. If you haven't already
go read :doc:`the Linux 802.11 power consumption
<../../documentation/power-consumption>` section first.

Measured power consumption
--------------------------

We measure the power by feeding external power to the PCIe with a meter
attached. We don't yet have any data that shows system level power at
this point. But this should be same as what it extracts from the
external power source.

We get the IDLE ASSOCIATED power save numbers as 0.02A.

AR9280 power consumption test results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   - 

      - Device state
      - L1
      - ASPM off
   - 

      - PS On, Associated
      - 116mW
      - 365mW
   - 

      - PS On + Ping traffic
      - 232mW
      - 450mW
   - 

      - PS off
      - 1090mW
      - 1090mW

ASPM tweaks
-----------

ath9k disables the PLL when in L0s as well as receiver clock when in L1,
this is done by using the `SerDes <SerDes>`__. Programming the `SerDes
<SerDes>`__ must go through the same 288 bit serial shift register as
the other analog registers. Hence the 9 writes observed. You can look at
the code used here:

- AR9002: ar9002_hw_configpcipowersave() (or ath9k_hw_configpcipowersave() in older kernels)
- AR9003: ar9003_hw_configpcipowersave()
