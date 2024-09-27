Wireless usage of pm-qos
------------------------

The Linux kernel supports a *power management Quality Of Service* (aka **pm-qos**) infrastructure to allow customizations of different kernel subsystem for power savings enhancements based on userspace application requirements. This work was added as of the 2.6.24 kernel and is implemented on kernel/pm_qos_params.c.

There are different types of requirements for which user can inform the kernel for power save tuning:

-  cpu_dma_latency
-  network_latency
-  network_throughput
-  system_bus_freq Each subsystem can in turn then register notifiers for userspace requirements notifications and updates. The 802.11 subsystem makes use of pm-qos to enhance power savings.

mac80211 usage of pm-qos
------------------------

mac80211 informs the kernel to be notified of userspace network latency updates. It does this for every wireless driver registered to the mac80211. Upon userspace network latency requirement changes mac80211 will tune itself. As it stands mac80211 only uses the network latency changes to update its policy on :doc:`dynamic power save <../../users/documentation/dynamic-power-save>`. :doc:`Dynamic power save <../../users/documentation/dynamic-power-save>` is used by mac80211 to automatically go into power save mode when there is no traffic present and the driver supports power save.

The default pm-qos network latency is 2000 ms. Userspace applications can register network latencies smaller than this.

The configured network latency will affect the timeout used for :doc:`dynamic power save <../../users/documentation/dynamic-power-save>`. The algorithm used to choose the timeout based on the network latency is currently rather crude. For the dafault network latency value the default dynamic power save timeout is used (100ms), and for latency ranges less than that predefined timeout values are used so that a network latency above 500 ms will disable the dynamic power save and less than or equal to 50 ms will use the longest timeout (300 ms).

If the network latency a userspace application registers is **greater** than your BSS's beacon interval (typically in TUs, convert it to us) then dynamic power save will be disabled for as longs as the userspace application holds the latency requirement. If however the latency requirement is greater than the beacon interval the :doc:`DTIM interval <ieee80211/power-savings>` will be compared against the network latency to see if we can enable power save to ensure delivery of buffered frames within each beacon at DTIM interval instead of each beacon. This is computed as follows:

::

   u8 dtimper = found->vif.bss_conf.dtim_period;
   int maxslp = 1;

   if (dtimper > 1)
           maxslp = min_t(int, dtimper,
                               latency / beaconint_us);

   local->hw.conf.max_sleep_period = maxslp;
   local->ps_sdata = found;

Registering userspace latency requirements
------------------------------------------

Userspace registers latency requirements by opening up the file:

::

   /dev/network_latency

and writing to it its expected network latency requirements. The userspace application should hold the file open until it no longer has the network latency requirements.

pm-qos for kernels older than 2.6.24
------------------------------------

The :doc:`compat.git <../../users/download/hacking>` tree used by :doc:`compat-wireless <../../users/download>` backports pm-qos for kernels older than 2.6.24. This is only supported for compat-wireless releases made based on kernels >= 2.6.33.
