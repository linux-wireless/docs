.. image:: en/users/drivers/iwlwifi/intel_rgb_3000.png
   :alt: en/users/drivers/iwlwifi/intel_rgb_3000.png
   :width: 0px
   :height: 140px

Introduction
============

Intel works with periodic releases of the iwlwifi driver that are tested with a specific combination of components. They are called LinuxCore releases and are numbered sequentially, e.g. LinuxCore11 is the latest stable release as of May 2015. These releases can be seen as snapshots of the development trees (including upstream) that are tested thoroughly together with a specific version of the firmware and userspace components (i.e. hostap).

Components
~~~~~~~~~~

The components used in each release are specific stabilization versions of the following:

-  iwlwifi driver
-  mac80211
-  cfg80211
-  backport
-  firmware
-  hostap

Who are you?
============

If you use a well known distribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you use a well maintained distribution, your device should be supported out of the box. If your device doesn't work at all (you can't even see it in the interface list), then it might mean that your kernel is too old or that you don't have the proper firmware. You can contact your distribution to have them fix this. In the meantime, you can use the backport tree to make your device work. Make sure to install the proper firmware as well. If your device works minimally (you can see it in the interface list), but you experience issues, please check the support section. You can also use the backport tree to check if the issue you are suffering from has been fixed in different releases. The backport tree is also an excellent tool to bisect regressions. Note that when you install the backport drivers, you disallow the usage of any WLAN device that is not supported by iwlmvm. To check if your device is supported by iwlmvm, please check `here </en/users/drivers/iwlwifi#Firmware>`__ in the module column.

If you are building your own system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are building your own system and you know that the only WLAN device you'll have is from Intel, the backport tree is what you need. You'll be able to get a driver / firmware combo that has been validated together. As a rule of thumb, you should take the latest Core version available.

A note about upstream policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The fact that Intel published a backport tree for its WLAN drivers doesn't impact its commitment to upstream all the code to the mainline kernel. It simply allows users who can't choose their kernel to work with a more recent driver. The backport tree allows us to provide a combo of the driver / firmware that has been fully validated. For a simple reason of capacity, we cannot test as thoroughly all the kernel versions / firmwares / devices matrix. There is code in the backport tree that is not in the mainline kernel, but this is transient. Eventually, all the code in the backport tree will reach mainline unless it has dependencies (platform drivers etc...).

Core release
============

A Core release includes all the components described `above </en/users/drivers/iwlwifi/core_release#Components>`__. Here is the way to match all these components together. backport, iwlwifi, mac80211 and cfg80211 come from the `backport-iwlwifi git repository <https://git.kernel.org/cgit/linux/kernel/git/iwlwifi/backport-iwlwifi.git/>`__. You'll find the relevant Core branches there (release/LinuxCoreX). For all the Core releases, the master branch `hostap <https://w1.fi/cgit/hostap/>`__ should be taken. The firmware can be found in `iwlwifi's linux-firmware clone <https://git.kernel.org/cgit/linux/kernel/git/iwlwifi/linux-firmware.git/>`__. Please don't open bugs on versions that are advertised as *End of life*. Here is the table to help you finding the right version of the different components:

.. list-table::
   :header-rows: 1

   - 

      - Core release
      - status
      - backport-iwlwifi
      - Firmware API number
   - 

      - Core14
      - //Last version for 7260, 7265 and 3160 //
      - `LinuxCore14 <https://git.kernel.org/cgit/linux/kernel/git/iwlwifi/backport-iwlwifi.git/log/?h=release/LinuxCore14>`__
      - -17.ucode `7260 <https://git.kernel.org/cgit/linux/kernel/git/iwlwifi/linux-firmware.git/plain/iwlwifi-7260-17.ucode>`__ `3160 <https://git.kernel.org/cgit/linux/kernel/git/iwlwifi/linux-firmware.git/plain/iwlwifi-3160-17.ucode>`__ `7265 <https://git.kernel.org/cgit/linux/kernel/git/iwlwifi/linux-firmware.git/plain/iwlwifi-7265-17.ucode>`__
   - 

      - Core26
      - // Last version for 3168 and 7265D//
      - `LinuxCore26 <https://git.kernel.org/cgit/linux/kernel/git/iwlwifi/backport-iwlwifi.git/log/?h=release/LinuxCore26>`__
      - -29.ucode `7265D <https://git.kernel.org/cgit/linux/kernel/git/iwlwifi/linux-firmware.git/plain/iwlwifi-7265D-29.ucode>`__\ `3168 <https://git.kernel.org/cgit/linux/kernel/git/iwlwifi/linux-firmware.git/plain/iwlwifi-3168-29.ucode>`__
   - 

      - Core33
      - // Last version for 8260 and 8265//
      - `core33 <https://git.kernel.org/cgit/linux/kernel/git/iwlwifi/backport-iwlwifi.git/log/?h=release/core33>`__
      - -36.ucode `8260 <https://git.kernel.org/cgit/linux/kernel/git/iwlwifi/linux-firmware.git/plain/iwlwifi-8000C-36.ucode>`__\ `8265 <https://git.kernel.org/cgit/linux/kernel/git/iwlwifi/linux-firmware.git/plain/iwlwifi-8265-36.ucode>`__
   - 

      - Core43
      - // Last version for 9260 and 9000//
      - `core43 <https://git.kernel.org/cgit/linux/kernel/git/iwlwifi/backport-iwlwifi.git/log/?h=release/core43>`__
      - -46.ucode `9260 <https://git.kernel.org/cgit/linux/kernel/git/iwlwifi/linux-firmware.git/plain/iwlwifi-9260-th-b0-jf-b0-46.ucode>`__\ `9000 <https://git.kernel.org/cgit/linux/kernel/git/iwlwifi/linux-firmware.git/plain/iwlwifi-9000-pu-b0-jf-b0-46.ucode>`__\ `AX 200 <https://git.kernel.org/cgit/linux/kernel/git/iwlwifi/linux-firmware.git/plain/iwlwifi-cc-a0-46.ucode>`__
   - 

      - Core45
      - maintained
      - `core45 <https://git.kernel.org/cgit/linux/kernel/git/iwlwifi/backport-iwlwifi.git/log/?h=release/core45>`__
      - -48.ucode `AX 200 <https://git.kernel.org/cgit/linux/kernel/git/iwlwifi/linux-firmware.git/plain/iwlwifi-cc-a0-48.ucode>`__
   - 

      - Core47
      - maintained
      - `core47 <https://git.kernel.org/cgit/linux/kernel/git/iwlwifi/backport-iwlwifi.git/log/?h=release/core47>`__
      - -48.ucode `AX 200 <https://git.kernel.org/cgit/linux/kernel/git/iwlwifi/linux-firmware.git/plain/iwlwifi-cc-a0-48.ucode>`__

Devices not maintained in mainline
==================================

From time to time, we remove support for existing devices from the mainline code base of the firmware. This means that those devices won't benefit from new features, but bug fixes will be back-ported to the Core release branch on which they are supported. For those devices, it is recommended to take the latest Core available for the driver and the latest firmware. For example for 7260, the Core14 firmware should be used together with the latest Core available for the driver. The driver for all those devices is maintained as part of the kernel, but they won't get newer firmware features. Those devices and the latest Core firmware that supports them are:

-  3160 (Core14)
-  7260 (Core14)
-  7265 (Core14)
-  7265D (Core26)
-  3165 (Core26)
-  3168 (Core26)
-  8260 (Core33)
-  8265 (Core33)
-  9000 (Core43)
-  9260 (Core43)

About vendor commands
=====================

iwlwifi implements a few vendor commands that are available in this tree. We strongly suggest that you disable the vendor commands Kconfig option (CPTCFG_IWLMVM_VENDOR_CMDS). Enabling vendor commands without actually sending them can cause incompatibility with certain versions of the supplicant (due to a supplicant bug) or too aggressive Multicast frames filtering. Note that CPTCFG_IWLMVM_VENDOR_CMDS is enabled by default and needs to be explicitly disabled.

How to install the driver
=========================

In order to install the driver, you'll need to download the sources:

::

   git clone https://git.kernel.org/pub/scm/linux/kernel/git/iwlwifi/backport-iwlwifi.git

Then, you can make the sources with vendor commands disabled:

::

   make defconfig-iwlwifi-public
   sed -i 's/CPTCFG_IWLMVM_VENDOR_CMDS=y/# CPTCFG_IWLMVM_VENDOR_CMDS is not set/' .config
   make -j4

Now it is time to install the modules you built

::

   sudo make install

Now you can reboot.

Support
=======

The support model for Core releases is the same as for the mainline kernel described in the `support section </en/users/drivers/iwlwifi#Support>`__. We will try to assist for any pure WLAN bug, but please take into account that platform integration isn't trivial: it can cause random issues. We also don't commit to work on all the platforms.
