Go back –> :doc:`Main ath9k driver page <../ath9k>`

ath9k and ath9k_htc debugging
-----------------------------

This page documents the debugging facilities available for ath9k and ath9k_htc

Enabling debug
--------------

If you have issues with ath9k or ath9k_htc you can enable debug. You will first need to enable the Kconfig option (CONFIG_ATH_DEBUG):

::

   Device Drivers  --->
     [*] Network device support  --->
           Wireless LAN  --->
             <M>   Atheros Wireless Cards  --->
                   [*] Atheros wireless debugging

Then you can use the module parameter *debug*. We cover below the different available debug levels you can use.

::

   enum ATH_DEBUG {
           ATH_DBG_RESET           = 0x00000001,
           ATH_DBG_QUEUE           = 0x00000002,
           ATH_DBG_EEPROM          = 0x00000004,
           ATH_DBG_CALIBRATE       = 0x00000008,
           ATH_DBG_INTERRUPT       = 0x00000010,
           ATH_DBG_REGULATORY      = 0x00000020,
           ATH_DBG_ANI             = 0x00000040,
           ATH_DBG_XMIT            = 0x00000080,
           ATH_DBG_BEACON          = 0x00000100,
           ATH_DBG_CONFIG          = 0x00000200,
           ATH_DBG_FATAL           = 0x00000400,
           ATH_DBG_PS              = 0x00000800,
           ATH_DBG_BTCOEX          = 0x00001000,
           ATH_DBG_WMI             = 0x00002000,
           ATH_DBG_BSTUCK          = 0x00004000,
           ATH_DBG_MCI             = 0x00008000,
           ATH_DBG_DFS             = 0x00010000,
           ATH_DBG_WOW             = 0x00020000,
           ATH_DBG_CHAN_CTX        = 0x00040000,
           ATH_DBG_DYNACK          = 0x00080000,
           ATH_DBG_ANY             = 0xffffffff
   };

If you want to debug calibration (0x00000008) and resets (0x00000001) for example you would use (0x00000008 \| 0x00000001) = 0x00000009. To debug everything just use 0xffffffff. Below is an example of how to enable debug for just configuration changes:

::

   modprobe ath9k debug=0x00000200 (or) modprobe ath9k_htc debug=0x00000200

You can also use modprobe.d configuration files, for example to enable ATH_DBG_CONFIG (0x00000200) and ATH_DBG_PS (0x00000800) you would have a file /etc/modprobe.d/atheros.conf with this:

::

   options ath9k debug=0xa00 (or) options ath9k_htc debug=0xa00

Debugfs files
-------------

To get debugfs you will need to mount it first. You can do so as follows:

::

   mount -t debugfs debugfs /sys/kernel/debug/

Debugfs files for ath9k
~~~~~~~~~~~~~~~~~~~~~~~

ath9k has several debugfs files which you can query for information and some which allow you to insert data. This can be enabled as:

::

   Device Drivers  --->
     [*] Network device support  --->
           Wireless LAN  --->
             <M>   Atheros Wireless Cards  --->
                   [M] Atheros 802.11n wireless cards support
                   [*]   Atheros ath9k debugging

Once the config options are enabled and debugfs is mounted, these would be seen:

::

   /sys/kernel/debug/ieee80211/phy0/ath9k/btcoex
   /sys/kernel/debug/ieee80211/phy0/ath9k/diversity
   /sys/kernel/debug/ieee80211/phy0/ath9k/gpio_val
   /sys/kernel/debug/ieee80211/phy0/ath9k/gpio_mask
   /sys/kernel/debug/ieee80211/phy0/ath9k/spectral_fft_period
   /sys/kernel/debug/ieee80211/phy0/ath9k/spectral_period
   /sys/kernel/debug/ieee80211/phy0/ath9k/spectral_count
   /sys/kernel/debug/ieee80211/phy0/ath9k/spectral_short_repeat
   /sys/kernel/debug/ieee80211/phy0/ath9k/spectral_scan_ctl
   /sys/kernel/debug/ieee80211/phy0/ath9k/spectral_scan0
   /sys/kernel/debug/ieee80211/phy0/ath9k/modal_eeprom
   /sys/kernel/debug/ieee80211/phy0/ath9k/base_eeprom
   /sys/kernel/debug/ieee80211/phy0/ath9k/dump_nfcal
   /sys/kernel/debug/ieee80211/phy0/ath9k/regdump
   /sys/kernel/debug/ieee80211/phy0/ath9k/ignore_extcca
   /sys/kernel/debug/ieee80211/phy0/ath9k/regval
   /sys/kernel/debug/ieee80211/phy0/ath9k/regidx
   /sys/kernel/debug/ieee80211/phy0/ath9k/paprd
   /sys/kernel/debug/ieee80211/phy0/ath9k/ani
   /sys/kernel/debug/ieee80211/phy0/ath9k/tx_chainmask
   /sys/kernel/debug/ieee80211/phy0/ath9k/rx_chainmask
   /sys/kernel/debug/ieee80211/phy0/ath9k/recv
   /sys/kernel/debug/ieee80211/phy0/ath9k/reset
   /sys/kernel/debug/ieee80211/phy0/ath9k/misc
   /sys/kernel/debug/ieee80211/phy0/ath9k/qlen_vo
   /sys/kernel/debug/ieee80211/phy0/ath9k/qlen_vi
   /sys/kernel/debug/ieee80211/phy0/ath9k/qlen_be
   /sys/kernel/debug/ieee80211/phy0/ath9k/qlen_bk
   /sys/kernel/debug/ieee80211/phy0/ath9k/queues
   /sys/kernel/debug/ieee80211/phy0/ath9k/xmit
   /sys/kernel/debug/ieee80211/phy0/ath9k/interrupt
   /sys/kernel/debug/ieee80211/phy0/ath9k/dma

Debugfs files for ath9k_htc
~~~~~~~~~~~~~~~~~~~~~~~~~~~

ath9k_htc has a few debugfs files which show driver statistics. Enable it as:

::

   Device Drivers  --->
     [*] Network device support  --->
           Wireless LAN  --->
             <M>   Atheros Wireless Cards  --->
                   [M] Atheros 802.11n wireless cards support
                   [*]   Atheros ath9k_htc debugging

Once enabled, these are available:

::

   /sys/kernel/debug/ieee80211/phy1/ath9k_htc/modal_eeprom
   /sys/kernel/debug/ieee80211/phy1/ath9k_htc/base_eeprom
   /sys/kernel/debug/ieee80211/phy1/ath9k_htc/debug
   /sys/kernel/debug/ieee80211/phy1/ath9k_htc/queue
   /sys/kernel/debug/ieee80211/phy1/ath9k_htc/slot
   /sys/kernel/debug/ieee80211/phy1/ath9k_htc/recv
   /sys/kernel/debug/ieee80211/phy1/ath9k_htc/xmit
   /sys/kernel/debug/ieee80211/phy1/ath9k_htc/tgt_rx_stats
   /sys/kernel/debug/ieee80211/phy1/ath9k_htc/tgt_tx_stats
   /sys/kernel/debug/ieee80211/phy1/ath9k_htc/tgt_int_stats
