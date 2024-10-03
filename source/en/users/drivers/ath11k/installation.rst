Installing ath11k
=================

Driver
~~~~~~

ath11k is included in official Linux releases starting from v5.6, just
download the latest release from https://www.kernel.org/ or use a recent
enough Linux distribution. Ensure below options are selected in the
kernel (debug, tracing and spectral scan options are optional)::

   make menuconfig
   --> Select Device drivers
           --> Network device support
                   --> Wireless LAN
                           --> Enable as below
                                   <M> Qualcomm Technologies 11ax chipset support
                                   <M>       Atheros ath11k PCI support
                                   [*]       QCA ath11k debugging
                                   [*]       QCA ath11k debugfs support
                                   [*]       ath11k tracing support
                                   [*]     QCA ath11k spectral scan support

Build and install the kernel and the kernel modules. There are multiple
ways to do that depending on your preferences and the Linux distribution
you are using, check the documentation for your distro how you want to
do it. Few pointers:

- https://wiki.debian.org/BuildADebianKernelPackage
- https://wiki.ubuntu.com/Kernel/BuildYourOwnKernel
- https://fedoraproject.org/wiki/Building_a_custom_kernel

The ath11k firmware images are available from `linux-firmware.git
<https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/>`__
which all common Linux distributions should install by default. Latest
firmware images can be downloaded from `ath11k-firmware.git
<https://git.codelinaro.org/clo/ath-firmware/ath11k-firmware>`__ from
which they get eventually pushed to `linux-firmware.git
<https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/>`__.
