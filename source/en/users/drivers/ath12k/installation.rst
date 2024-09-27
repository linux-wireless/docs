Go back --> :doc:`en/users/Drivers/ath12k <../ath12k>`

Installing ath12k
-----------------

As of this writing (August 2023) Linux distributions do not support ath12k devices out of box, so you need to install kernel and firmware manually. Here are simple instructions how to install Linux kernel v6.4 with ath12k PCI support and latest ath12k firmwares.

Clone kernel:

::

     git clone -b v6.4 git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git

Ensure below options are selected in the kernel (debugging and tracing support are optional):

::

   cd linux
   make menuconfig
   --> Select Device drivers
           --> Network device support
                   --> Wireless LAN
                           --> Enable as below
                                   <M> Qualcomm Technologies Wi-Fi 7 support (ath12k)
                                   <M>       Atheros ath12k PCI support
                                   [*]       ath12k debugging
                                   [*]       ath12k tracing support

Build and install the kernel and the kernel modules. There are multiple ways to do that depending on your preferences and the Linux distribution you are using, check the documentation for your distro how you want to do it. Few pointers:

-  https://wiki.debian.org/BuildADebianKernelPackage
-  https://wiki.ubuntu.com/Kernel/BuildYourOwnKernel
-  https://fedoraproject.org/wiki/Building_a_custom_kernel

Clone ath12k-firmware project which contains the latest firmware releases:

::

     git clone https://git.codelinaro.org/clo/ath-firmware/ath12k-firmware

To install ath12k firmware follow the instructions in `README <https://git.codelinaro.org/clo/ath-firmware/ath12k-firmware/-/blob/main/README.md?ref_type=heads>`__.
