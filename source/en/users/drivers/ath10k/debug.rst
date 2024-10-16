How to debug ath10k
===================

Debug log messages
~~~~~~~~~~~~~~~~~~

ath10k contains various debug log levels (check
drivers/net/wireless/ath/ath10k/debug.h for up-to-date list):

.. code-block:: c

   enum ath10k_debug_mask {
           ATH10K_DBG_PCI          = 0x00000001,
           ATH10K_DBG_WMI          = 0x00000002,
           ATH10K_DBG_HTC          = 0x00000004,
           ATH10K_DBG_HTT          = 0x00000008,
           ATH10K_DBG_MAC          = 0x00000010,
           ATH10K_DBG_BOOT         = 0x00000020,
           ATH10K_DBG_PCI_DUMP     = 0x00000040,
           ATH10K_DBG_HTT_DUMP     = 0x00000080,
           ATH10K_DBG_MGMT         = 0x00000100,
           ATH10K_DBG_DATA         = 0x00000200,
           ATH10K_DBG_BMI          = 0x00000400,
           ATH10K_DBG_REGULATORY   = 0x00000800,
           ATH10K_DBG_TESTMODE = 0x00001000,
           ATH10K_DBG_WMI_PRINT    = 0x00002000,
           ATH10K_DBG_PCI_PS   = 0x00004000,
           ATH10K_DBG_AHB      = 0x00008000,
           ATH10K_DBG_ANY          = 0xffffffff,
   };

The debug log levels can be enabled either with a module parameter named
debug_mask or from sysfs. To get debug log messages enabled in the build
enable CONFIG_ATH10K_DEBUG.

To enable debug logs with the module parameter::

   # modprobe ath10k_core.ko debug_mask=0x16

Alternatively the debug logs can be enabled from sysfs anytime ath10k is
running::

   # echo 0x16 > /sys/module/ath10k_core/parameters/debug_mask

To check what is current debug_mask value::

   $ cat /sys/module/ath10k_core/parameters/debug_mask
   22

Note that the returned value is in decimal format, not hexadecimal.

debug_mask value is a bitwise OR operation of enum ath10k_debug_mask
values above. For example, to enable HTC, WMI and MAC debug levels use
python to calculate the value::

   $ python -c "print '0x%x' % (0x2 | 0x4 | 0x10)"
   0x16

Useful debug masks
^^^^^^^^^^^^^^^^^^

Example values for debug_mask to help started with debugging:

.. list-table::

   - 

      - 0x00000432
      - firmware boot and configuration related messages
   - 

      - 0xffffff3f
      - everything except PCI and HTT dumps
   - 

      - 0xffffffff
      - all possible debug messages (this will be a big one!)

Tracing
~~~~~~~

Enable tracing support with CONFIG_ATH10K_TRACING. If you want to get
debug logs included the trace (most of the time you do) also enable
CONFIG_ATH10K_DEBUG.

To trace all log messages, including debug logs, into trace.dat file::

   trace-cmd record -e ath10k_log*

To trace everything possible from ath10k, mac80211 and cfg80211::

   trace-cmd record -e mac80211 -e cfg80211 -e ath10k

To include hostapd (or wpa_supplicant) to the trace add -T switch to
hostapd command line.

To read the trace.dat file::

   trace-cmd report

See :doc:`mac80211 tracing
<../../../developers/documentation/mac80211/tracing>` for more
information.

HTT statistics
~~~~~~~~~~~~~~

The firmware provides various statistics for HTT (the data path in
ath10k). There are different types of statistics available:

.. code-block:: c

   enum htt_dbg_stats_type {
           HTT_DBG_STATS_WAL_PDEV_TXRX = 0x01,
           HTT_DBG_STATS_RX_REORDER    = 0x02,
           HTT_DBG_STATS_RX_RATE_INFO  = 0x04,
           HTT_DBG_STATS_TX_PPDU_LOG   = 0x08,
           HTT_DBG_STATS_TX_RATE_INFO  = 0x10,
   };

To enable statistics use bitwise OR operation to combine the values and
write it htt_stats_mask. Here's an example which enables TX PPDU logs::

   # echo 0x8 > /sys/kernel/debug/ieee80211/phy0/ath10k/htt_stats_mask

Not ath10k will query for those HTT statistics for every second. The
stats are delivered to user space through trace events and trace-cmd is
used to store the statistics::

   sudo trace-cmd record -e ath10k_htt_stats

Firmware version
~~~~~~~~~~~~~~~~

Firmware version can be retrieved with ethtool::

   $ sudo ethtool -i wlan1
   driver: ath10k_pci
   version: 3.12.0-rc3-wl+
   firmware-version: 1.0.0.636
   bus-info: 0000:02:00.0

Alternatively they are visible from kernel logs::

   $ dmesg | grep ath10k
   [11748.124678] ath10k_pci 0000:02:00.0: irq 33 for MSI/MSI-X
   [11748.125047] ath10k_pci 0000:02:00.0: pci irq msi interrupts 1 irq_mode 0 reset_mode 0
   [11749.393511] ath10k_pci 0000:02:00.0: qca988x hw2.0 (0x4100016c, 0x043202ff) fw 10.1.467.2-1 api 3 htt 2.1
   [11749.393576] ath10k_pci 0000:02:00.0: debug 1 debugfs 1 tracing 1 dfs 1 testmode 1

DFS
~~~

Radar can be simulated by debugfs entry::

   echo 1 > /sys/kernel/debug/ieee80211/phyX/ath10k/dfs_simulate_radar

This will trigger radar event to mac80211.

To prevent changing a channel after radar is detected, only for testing
purposes::

   echo 1 > /sys/kernel/debug/ieee80211/phyX/ath10k/dfs_block_radar_events

Use 0 to unblock it.

Be aware that currently ath10k pattern detector supports only ETSI
master region. For other regulatory domains single phyerr will trigger
radar event.

Manual bitrates configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to setup bitrates latest version of iw is required.

Just type iw to get short hint how to use it.

::

   iw
   .
   .
   dev <devname> set bitrates [legacy-<2.4|5> <legacy rate in Mbps>*]
   [ht-mcs-<2.4|5> <MCS index>*] [vht-mcs-<2.4|5> <NSS:MCSx,MCSy... | NSS:MCSx-MCSy>*]
   .
   .

Currently ath10k is limited to handle VHT MCS in ranges: none, 0-7, 0-8,
and 0-9. You cannot set any other ranges.

Not passing any arguments would clear the existing mask (if any)::

   iw wlan0 set bitrates

To set VHT, nss=2, mcs=9::

   iw wlan0 set bitrates legacy-5 ht-mcs-5 vht-mcs-5 2:9

To set legacy, 18Mbps::

   iw wlan0 set bitrates legacy-5 18 ht-mcs-5 vht-mcs-5

To set HT, nss=1, mcs=3::

   iw wlan0 set bitrates legacy-5 ht-mcs-5 3 vht-mcs-5

To set nss=1 MCS indexes 0-9:

   iw wlan0 set bitrates legacy-5 ht-mcs-5 vht-mcs-5 1:0-9

To set nss=2::

   iw wlan0 set bitrates legacy-5 ht-mcs-5 vht-mcs-5 1:0-9 2:0-9

It is possible to force SGI by adding force-sgi at the end of command::

   iw wlan0 set bitrates legacy-5 ht-mcs-5 vht-mcs-5 2:9 force-sgi

Few more complicated examples, only supported since 4.2 kernel::

   iw wlan0 set bitrates legacy-5 6 12 ht-mcs-5 1 2 3
   iw wlan0 set bitrates legacy-5 ht-mcs-5 7 8 9
   iw wlan0 set bitrates legacy-5 24 ht-mcs-5 vht-mcs-5 1:0-9

Simulating firmware crashes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's possible to manually trigger a firmware crash using
simulate_fw_crash debugfs file::

   echo hard > /sys/kernel/debug/ieee80211/phy0/ath10k/simulate_fw_crash

There are different ways to crash the firmware, simulate_fw_crash file
has a help text::

   # cat simulate_fw_crash
   To simulate firmware crash write one of the keywords to this file:
   `soft` - this will send WMI_FORCE_FW_HANG_ASSERT to firmware if FW supports that command.
   `hard` - this will send to firmware command with illegal parameters causing firmware crash.
   `assert` - this will send special illegal parameter to firmware to cause assert failure and crash.
   `hw-restart` - this will simply queue hw restart without fw/hw actually crashing.

Firmware crash dump file
~~~~~~~~~~~~~~~~~~~~~~~~

When the firmware crashes ath10k collects various information which
helps to debug the crash and creates a crash dump file. This is
available via dev_coredump facility from /sys/class/devcoredump.

To automatically collect devcoredump files add script
/usr/local/sbin/devcoredump-collect.sh:

.. code-block:: bash

   #!/bin/sh

   timestamp=$(date +%Y%m%d%H%M%S)
   filename="/var/spool/devcoredump/devcoredump-${timestamp}.dump"
   cp /sys/${DEVPATH}/data ${filename}
   echo 1 > /sys/${DEVPATH}/data
   logger "created ${filename}"

Create a directory for the dump files::

   sudo mkdir /var/spool/devcoredump

And add a udev rules script /etc/udev/rules.d/50-devcoredump.rules::

   SUBSYSTEM=="devcoredump", ACTION=="add", RUN+="/usr/local/sbin/devcoredump-collect.sh"
