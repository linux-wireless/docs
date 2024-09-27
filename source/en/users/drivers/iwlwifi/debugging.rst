Bugs and support
================

Before you contact us...
------------------------

We try to give the best support we can with the best response time possible. We also don't have several levels of support, by contacting us, you contact the developers who are also busy with other tasks. Before reaching out to us, please make sure you have a supported Intel Wi-Fi device and that it is enabled. Many request are for problems in the rfkill area where the platform pulls the rfkill signal preventing us from doing anything.

If you see that Wi-Fi is hard blocked like in:

::

   3: phy0: Wireless LAN
       Soft blocked: yes
       Hard blocked: yes

you can blacklist the WMI module and see if that helps. The name of the WMI module will vary depending on the OEM. A simple lsmod \| grep wmi should give you a hint of what module to blacklist.

How to report?
--------------

Issues can be filed in `kernel's bugzilla <http://bugzilla.kernel.org>`__.

Make sure to set

-  Product: Drivers
-  Component: network-wireless-intel

Always attach the kernel log to your reports:

::

   dmesg > dmesg.log

and attach dmesg.log to the bug. Please also add the firmware version: <code> ethtool -i wlan0 \| grep firmware</code> Note: the interface name (here wlan0) can vary between distributions.

How to debug?
-------------

Prints
~~~~~~

The simplest way to provide minimal output is to dump your kernel log: dmesg. Sometimes we will ask for logs from the supplicant too - they typically land in syslog. iwlwifi can print more data to the kernel log if asked to: this is controlled by the debug module parameter. This is a `bitmap <https://git.kernel.org/cgit/linux/kernel/git/stable/linux-stable.git/tree/drivers/net/wireless/intel/iwlwifi/iwl-debug.h#n129>`__. To see more debug prints, `CONFIG_IWLWIFI_DEBUG <https://git.kernel.org/cgit/linux/kernel/git/stable/linux-stable.git/tree/drivers/net/wireless/intel/iwlwifi/Kconfig#n105>`__ must be enabled. Please don't add debug level unless instructed to do so. Adding more prints typically adds useless information.

Tracing
~~~~~~~

Another (more powerful) way to debug iwlwifi is to use tracing:

::

   sudo trace-cmd record -e iwlwifi

We will typically ask for more switches:

::

   sudo trace-cmd record -e iwlwifi -e mac80211 -e cfg80211 -e iwlwifi_msg

This records all the data that goes from and to the firmware. The output is a file: trace.dat which you can compress prior to sending. To enable tracing, `CONFIG_IWLWIFI_DEVICE_TRACING <https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/tree/drivers/net/wireless/intel/iwlwifi/Kconfig#n139>`__ must be set.

**Note: you must not remove the iwlwifi kernel module while tracing is running. You need to stop the tracing first!**

Air sniffing
~~~~~~~~~~~~

Your Intel device can act as a sniffer (which is also referred to as "monitor mode"). This means that it can record all the packets being sent over the air by all the other devices including your Access Point. When acting as a sniffer, your device cannot be connected to any Access Point or do anything else. The output of the air sniffing operation is a file with a pcap extension that can be parsed by the `Wireshark <https://www.wireshark.org>`__ program.

How to get a sniffer capture with your Intel device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To capture all A-MSDUs, you need to reload the iwlwifi driver with the ``amsdu_size=3`` module parameter.

In order to put your device in monitor mode and get a sniffer capture, you first need to stop using it as a Wi-Fi client. To do so there are several options:

-  Disable Wi-Fi from the Network Manager GUI and re-enable manually with ``rfkill unblock wifi`` This may not work on all the distributions.
-  Disable the Network Manager and kill the wpa_supplicant\ ``sudo service NetworkManager stop
   sudo killall wpa_supplicant``

Then you need to put it in monitor mode: <code> sudo iw wlan0 set type monitor </code>

After that, you can bring the interface up again and set the frequency (taking channel 1 as an example but you should check what frequency you want to listen to):

::

   sudo ifconfig wlan0 up
   sudo iw wlan0 set freq 2412

Then you can start the capture:

::

   sudo tcpdump -i wlan0 -w capture.pcap

This file can be opened by `Wireshark <https://www.wireshark.org/>`__ and sent for analysis by our developers. Note that this file can be fairly large if you capture a lot of traffic, but it can be compressed very efficiently.

How to put your Wi-Fi device back in normal client mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to get your device back in a regular client mode, you can either reboot or start the NeworkManager again:

::

   sudo service NetworkManager start

Firmware Debugging
~~~~~~~~~~~~~~~~~~

Note that we no longer provide support for the firmware of the devices using iwldvm.

How to provide information to debug the firmware?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Getting data from the firmware can often provide a lot of information, especially when the traffic is being stalled, latency is high, queues are stuck etc.. Here is how to do so. This is working starting kernel 3.19.

You'll need to allow DEV_COREDUMP by setting CONFIG_ALLOW_DEV_COREDUMP to Y. Then, you'll need to create a core dump. This can be done by:

::

   echo 1 > /sys/kernel/debug/iwlwifi/0000\:0X\:00.0/iwlmvm/fw_dbg_collect

(Check what is the X for your system)

You can now get the data from the devcoredump device and dump to a file:

::

   cat /sys/devices/virtual/devcoredump/devcdY/data > iwl.dump
   echo 1 > /sys/devices/virtual/devcoredump/devcdY/data

(Y is incremented each time)

The easiest is to define a udev rule to dump the data automatically as soon as a dump is created:

::

   SUBSYSTEM=="devcoredump", ACTION=="add", RUN+="/sbin/iwlfwdump.sh"

You'll typically have to paste this into a new file called /etc/udev/rules.d/85-iwl-dump.rules. This location can vary between distributions.

/sbin/iwlfwdump.sh can simply be:

::

   #!/bin/bash

   timestamp=$(date +%F_%H-%M-%S)
   filename=/var/log/iwl-fw-error_${timestamp}.dump
   cat /sys/${DEVPATH}/data > ${filename}
   echo 1 > /sys/${DEVPATH}/data

This way, each time a dump is created it will automatically land on your file system. Remember to make the /sbin/iwlfwdump.sh file executable (i.e. ``chmod a+x /sbin/iwlfwdump.sh``), so that the udev rule can execute it, otherwise it won't work.

Starting from 4.1, we can trigger firmware dumps when issues occur (e.g. when the association fails) this again requires a customized firmware. In that case, the developer working with you will let you know and you won't have to trigger the dump yourself using fw_dbg_collect debugfs hook.

Firmware crashes
^^^^^^^^^^^^^^^^

When the firmware crashes, you'll see a message like this:

::

   iwlwifi 0000:01:00.0: Microcode SW error detected.  Restarting 0x82000000.
   [snip]
   iwlwifi 0000:01:00.0: Loaded firmware version: XX.XX.XX.XX
   iwlwifi 0000:01:00.0: 0x0000090A | ADVANCED_SYSASSERT

In this case, please copy the full dmesg output since there may be data before and after this message that can be helpful.

In case of a firmware crash or queues being stuck, a dump will be automatically created. If you have the udev rule in place, you'll see the dump on your file system. No customization needed in that case, the dump from a regular firmware will already include valuable data, but we usually need more information than the data provided by a release version of the firmware. When you report a bug, please use a debug firmware from the list below. This will allow to include more data in the dump at the cost of extra PCI transactions:

.. image:: /en/users/drivers/iwlwifi/iwlwifi-3160-17.ucode.gz
   :alt: debug firmware version for 3160

.. image:: /en/users/drivers/iwlwifi/iwlwifi-7260-17.ucode.gz
   :alt: debug firmware version for 7260

.. image:: /en/users/drivers/iwlwifi/iwlwifi-7265-17.ucode.gz
   :alt: debug firmware version for 7265

.. image:: /en/users/drivers/iwlwifi/iwlwifi-7265d-29.ucode.gz
   :alt: debug firmware version for 7265D

.. image:: /en/users/drivers/iwlwifi/iwlwifi-3168-29.ucode.gz
   :alt: debug firmware version for 3168

.. image:: /en/users/drivers/iwlwifi/iwlwifi-8000C-36.ucode.gz
   :alt: debug firmware version for 8260

.. image:: /en/users/drivers/iwlwifi/iwlwifi-8265-36.ucode.gz
   :alt: debug firmware version for 8265

.. image:: /en/users/drivers/iwlwifi/iwlwifi-9000-pu-b0-jf-b0-43.ucode.gz
   :alt: debug firmware version for 9000

.. image:: /en/users/drivers/iwlwifi/iwlwifi-9260-th-b0-jf-b0-43.ucode.gz
   :alt: debug firmware version for 9260

Privacy aspects
~~~~~~~~~~~~~~~

By sending the debug logs, you are providing information to Intel such as your email address, peer’s MAC address, and other information. This information will be used only for the purpose of troubleshooting the issue you are reporting. Intel is committed to protecting your privacy. To learn more about Intel’s privacy practices, please visit `Intel's privacy site <http://www.intel.com/privacy>`__ or write Intel Corporation, ATTN Privacy, Mailstop RNB4-145, 2200 Mission College Blvd., Santa Clara, CA 95054 USA.

We recommend you encrypt the data using the iwlwifi developers's PGP keys before you send it via email or attach it to bug trackers:

-  Emmanuel Grumbach (18D075865D915B5E386F660F2D0B96FE6E363201);
-  Johannes Berg (C0EBC440F6DA091C884D8532E0F373F37BF9099A);
-  Gregory Greenman (F5C83636E8E2909E44319BAC083082600E73773C).

For instance:

::

   gpg --recv-keys C0EBC440F6DA091C884D8532E0F373F37BF9099A F5C83636E8E2909E44319BAC083082600E73773C 18D075865D915B5E386F660F2D0B96FE6E363201
   gpg --encrypt -r 18D075865D915B5E386F660F2D0B96FE6E363201 -r C0EBC440F6DA091C884D8532E0F373F37BF9099A -r F5C83636E8E2909E44319BAC083082600E73773C <file_to_encrypt>

This will generate a new, encrypted file that you should provide to us. Any of, and only, these developers will be able to open the file. Adding the three keys during encryption allows us to respond faster, since we're not restrained by a single developer's availability.
