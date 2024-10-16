ath6kl debugging
================

Logging
~~~~~~~

Use debug_mask module parameter to enable debug logs. For example, to
enable all possible log levels do::

   modprobe ath6kl_sdio.ko debug_mask=0xffffffff

The log messages printed using the standard kernel log facilies, for
example you can use dmesg or syslog to access them.

The log levels are defined in `debug.h
<http://git.kernel.org/?p=linux/kernel/git/linville/wireless-next.git;a=blob;f=drivers/net/wireless/ath/ath6kl/debug.h;hb=HEAD>`__.
Some useful debug_mask values:

.. list-table::

   - 

      - 0x140400
      - boot, suspend, wmi
   - 

      - 0x50480
      - irq, wmi, sdio, boot

Booting
~~~~~~~

When you see a message like this it means that firmware was able to boot::

   ar6003 hw 2.1.1 sdio fw 3.2.0.35 api 3

For getting detailed information about booting enable the BOOT log level.

Debugfs
~~~~~~~

ath6kl also has a debugfs interface for debugging driver and firmware
state. The debugfs directory is in ``ieee80211/phy*/ath6kl/`` under the
debugfs root directory, which is distribution dependent (usually
/sys/kernel/debug/ and needs to be mounted separately).

Few important files::

   ; tgt_stats  : various firmware statistics 
   ; fwlog  : latest firmware debug logs, use cp to copy the logs to a file 
   ; endpoint_stats  : HTC endpoint statistics 
   ; roam_table  : list of possible roaming candidates 
   ; reg_dump  : dump of firmware registers (slow) 

Tracing
~~~~~~~

Starting from Linux 3.10 release ath6kl has tracing support. There are
tracing points for sdio, htc and wmi packets. Also there are tracepoints
for all log messages, both normal and debug messages. Tracepoints are
very useful for ath6kl developers as they can inspect packets and post
process them freely after receiving the trace file.

To compile the tracing support enable CONFIG_ATH6KL_TRACING. This
compiles all the tracpoints to the driver but keeps them disables with a
minimal overhead. If you want to also trace ath6kl debug messages enable
CONFIG_ATH6KL_DEBUG as well.

To enable a trace point use trace-cmd, in this example both WMI
tracepoints are enabled::

   # trace-cmd record -e ath6kl_wmi_cmd -e ath6kl_wmi_event

To see the trace log stored in the default file trace.dat::

   # trace-cmd report
   version = 6
   cpus=1
                 iw-4411  [000] 18518.544058: ath6kl_wmi_cmd:       id 9 len 14
                 iw-4411  [000] 18518.544367: ath6kl_wmi_cmd:       id 10 len 41
                 iw-4411  [000] 18518.545039: ath6kl_wmi_cmd:       id 10 len 41
                 iw-4411  [000] 18518.545057: ath6kl_wmi_cmd:       id 10 len 41
                 iw-4411  [000] 18518.545074: ath6kl_wmi_cmd:       id 10 len 41
                 iw-4411  [000] 18518.545090: ath6kl_wmi_cmd:       id 10 len 41
                 iw-4411  [000] 18518.545107: ath6kl_wmi_cmd:       id 10 len 41

To see all the ath6kl tracepoints::

   # ls /sys/kernel/debug/tracing/events/ath6kl/
   ath6kl_htc_rx   ath6kl_log_dbg_dump  ath6kl_log_warn  ath6kl_sdio_wr    enable
   ath6kl_htc_tx   ath6kl_log_err       ath6kl_sdio_irq  ath6kl_wmi_cmd    filter
   ath6kl_log_dbg  ath6kl_log_info      ath6kl_sdio_rd   ath6kl_wmi_event

More information in :doc:`mac80211 tracing <../../../developers/documentation/mac80211/tracing>`.
