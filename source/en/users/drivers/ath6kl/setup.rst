Setting up ath6kl
=================

Kernel configuration
~~~~~~~~~~~~~~~~~~~~

Starting from Linux kernel 3.2 ath6kl is available from kernel
menuconfig::

   -> Device Drivers
    -> Network device support (NETDEVICES [=y])
     -> Wireless LAN (WLAN [=y])
      -> Atheros Wireless Cards (ATH_COMMON [=y])
       -> Atheros mobile chipsets support (ATH6KL [=m])

Or alternatively search for CONFIG_ATH6KL.

Suspend
~~~~~~~

ath6kl supports various suspend which can be controlled with two module
parameters, suspend_mode and wow_mode.

suspend_mode makes it possible to force a certain mode when host suspends:

.. list-table::
   :header-rows: 1

   - 

      - value
      - mode
   - 

      - 0
      - automatic (default)
   - 

      - 1
      - cutpower
   - 

      - 2
      - deepsleep
   - 

      - 3
      - wow

Definion of different suspend modes::

   ; automatic  : the suspend mode is chosen based on host hardware capabilities 
   ; cutpower  : the chip is powered off for maximum power savings and hence resume is slower 
   ; deepsleep  : the firmware is running on the chip but is kept 
   ; wow  : if ath6kl is connected to an AP device will maintain the connection with Wake-on-WLAN feature while host is suspended 

If wow mode is enabled it's possible to choose different wow submode with wow_mode parameter:

.. list-table::
   :header-rows: 1

   - 

      - value
      - mode
   - 

      - 0
      - default
   - 

      - 1
      - cutpower when disconnected
   - 

      - 2
      - deepsleep when disconnected

Definion of different wow modes::

   ; default  : Chooses the default mode from below which is subject to change. 
   ; cutpower  : 

If ath6kl is *not* connected to an AP the power is cut from the wifi
chip. If connected to an AP WoW mode is used::

   ; deepsleep  : 

If ath6kl is *not* connected to an AP the firmware is put to low power
deep sleep state. If connected to an AP WoW mode is used.
