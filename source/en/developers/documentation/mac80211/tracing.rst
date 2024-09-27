Driver API tracing
------------------

Enabling
~~~~~~~~

Since 2.6.32 mac80211 includes a tracing framework, and since 3.2 it is always enabled if possible (if EVENT_TRACING is enabled in the kernel.)

To be able to use it on kernels before 3.2, enable ``CONFIG_MAC80211_DRIVER_API_TRACER`` (requires tracing and ``CONFIG_MAC80211_DEBUG_MENU``).

Using trace-cmd
~~~~~~~~~~~~~~~

The easiest way to give a trace to other people is to use trace-cmd, see also https://lwn.net/Articles/410200/. To record a trace with trace-cmd, use

::

   trace-cmd record -e mac80211

This will record until you hit Ctrl-C to abort. The result is stored in a file "trace.dat" which you can send around for analysis. You should compress it before sending it to other people since it is relatively large but compresses well.

To analyse a file, use

::

   trace-cmd report -i trace.dat | less

cfg80211 and wpasupplicant
~~~~~~~~~~~~~~~~~~~~~~~~~~

Both cfg80211 and wpasupplicant have tracing support. Use '-e cfg80211' with trace-cmd to enable all cfg80211 tracing points. For wpasupplicant enable CONFIG_DEBUG_LINUX_TRACING build config and use -T switch to get log messages sent to the tracing framework.

Driver tracing
~~~~~~~~~~~~~~

In addition to mac80211, some drivers include tracing as well.

iwlwifi
^^^^^^^

For iwlwifi, set the ``IWLWIFI_DEVICE_TRACING`` Kconfig option. You can then get new trace subsystems:

::

   ; iwlwifi  : the commands exchanged between driver and device 
   ; iwlwifi_io  : the device IO accesses and interrupt information 
   ; iwlwifi_msg  : all debug messages from the driver 
   ; iwlwifi_ucode  : uCode events (not sure they're useful today) 
   ; iwlwifi_data  : data for TX/RX frames 

Recommended:

::

   trace-cmd record -e mac80211 -e mac80211_msg -e iwlwifi -e iwlwifi_msg -e iwlwifi_data
