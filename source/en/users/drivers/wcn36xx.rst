wcn36xx
-------

wcn36xx is a mac80211 driver for wcn3660 and wcn3680 chips found from Qualcomm SoC.

Caveats
-------

Currently wcn36xx only compiles with msm kernels and backports infrastructure is needed to get latest cfg80211 and mac80211.

Supported chips
---------------

wcn36xx supports both WCN3660 and WCN3680 chips.

Available devices
-----------------

wcn36xx was tested on Google Nexus 4(Mako), Sony Xperia - T(Mint), Z(Yuga), ZR(Dogo) and Z1(Honami). Basically, wcn36xx can support all MSM based devices.

Features
--------

As a general rule for this section, don't list every tiny detail, just the most important things one should know about.

Working
~~~~~~~

list wireless features that your driver supports, e.g. station mode, access point mode etc

-  11b, 11g, 11n, 11a
-  HW rate control
-  hardware encryption(TKIP, CCMP, WEP)
-  HW connection monitoring
-  aggregation (Immediate BA only)
-  `ProbeResponse <ProbeResponse>`__ offloading
-  Beacon filtering
-  Multicast filtering
-  WoW
-  power save
-  AP mode support
-  Ad-Hoc
-  11s mesh

Not working (yet)
~~~~~~~~~~~~~~~~~

list features that could be supported but are not yet

::

     * ARP offloading 
     * 80211AC 
     * P2P 
     * Miracast 
     * Bluetooth coexistence 
     * WAPI 
     * WMM 
     * CQM 
     * DFS 
     * Recovery(In case of chip hanging, wcn36xx must restart it) 

Not supported
~~~~~~~~~~~~~

::

       * list important features that the device will not support 

Sources
-------

wcn36xx is part of the mainline kernel. The latest developement version can be found on github:

https://github.com/KrasnikovEugene/wcn36xx

Device firmware
---------------

The latest greatest firmware can be found on here https://www.codeaurora.org/cgit/external/hisense/platform/vendor/qcom-opensource/wlan/prima/tree/firmware_bin?h=8130_CS

wcn36xx loads WCNSS_qcom_wlan_nv.bin file and sends it to the hardware.

Support
-------

Mailing list:

http://lists.infradead.org/mailman/listinfo/wcn36xx

There's an IRC channel #wcn36xx at Freenode.

Bug tracker:

https://github.com/KrasnikovEugene/wcn36xx/issues

Dissector
---------

If you are hacking on wcn36xx and want to see see what Qualcomm's prima driver (or wcn36xx) sends to and from fw, check out the wcn36xx-dissector. It allows you to view all commands and data in wireshark. It understands most commands and buffer structures.

https://github.com/kanstrup/wcn36xx-dissector

Compilation
-----------

Go to working directory
~~~~~~~~~~~~~~~~~~~~~~~

Change to a directory where you'll keep your git repositories like ~/git/

Checkout backports
~~~~~~~~~~~~~~~~~~

::

   git clone git://github.com/hauke/backports.git

Checkout linux-next
~~~~~~~~~~~~~~~~~~~

::

   git clone --no-checkout git://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git

The –no-checkout is there to save space since backports will pickout the relevant stuff anyway.

Checkout wcn36xx
~~~~~~~~~~~~~~~~

::

   git clone git://github.com/KrasnikovEugene/wcn36xx.git

Checkout wcn36xx from upstream or your own branch

Generate a build tree
~~~~~~~~~~~~~~~~~~~~~

Make sure you have "coccinelle" installed otherwise gentree will fail. Create a file named *copy-list.wcn36xx* in the backports folder containing:

::

   wcn36xx/ -> drivers/net/wireless/ath/wcn36xx/

Do a git log, find the first commit that says something like: "refresh on next-20131122". Then execute the command:

::

   cd backports
   ./gentree.py --verbose --clean --git-revision next-20131122 --extra-driver ../ copy-list.wcn36xx ../linux-next/ ../backport-wcn

This command will create the folder ../backport-wcn where it will put all the necessary linux stuff from linux-next. It will also apply a number of patches, if any of these fail you must sort it out otherwise the build folder will not be ready.

Time to build
~~~~~~~~~~~~~

::

   cd ../backport-wcn

Symlink the wcn36xx-folder into the backport-wcn-folder:

::

   ln -s ~/git/wcn36xx drivers/net/wireless/ath/wcn36xx

This sets up some links to your cm build:

::

   export CM_BUILD=mako
   export CM_ROOT=~/mako/cm-10.1

This executes the defconfig for the environment:

::

   make KLIB=$CM_ROOT/out/target/product/$CM_BUILD/obj/KERNEL_OBJ \
   KLIB_BUILD=$CM_ROOT/out/target/product/$CM_BUILD/obj/KERNEL_OBJ \
   ARCH=arm \
   CROSS_COMPILE=$CM_ROOT/prebuilts/gcc/linux-x86/arm/arm-eabi-4.6/bin/arm-eabi- \
   defconfig-wcn36xx

Builds the module and all necessary compat/cfg80211/mac80211 modules as well:

::

   make KLIB=$CM_ROOT/out/target/product/$CM_BUILD/obj/KERNEL_OBJ \
   KLIB_BUILD=$CM_ROOT/out/target/product/$CM_BUILD/obj/KERNEL_OBJ \
   ARCH=arm \
   CROSS_COMPILE=$CM_ROOT/prebuilts/gcc/linux-x86/arm/arm-eabi-4.6/bin/arm-eabi-

Build platform driver wcn36xx_msm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   cd drivers/net/wireless/ath/wcn36xx/wcn36xx_msm/
   make KLIB=$CM_ROOT/out/target/product/$CM_BUILD/obj/KERNEL_OBJ \
   KLIB_BUILD=$CM_ROOT/out/target/product/$CM_BUILD/obj/KERNEL_OBJ \
   ARCH=arm \
   CROSS_COMPILE=$CM_ROOT/prebuilts/gcc/linux-x86/arm/arm-eabi-4.6/bin/arm-eabi-

NOTES FOR OSX
~~~~~~~~~~~~~

To make this run on OSX (Mountain Lion) I had to do some changes. 1) The make commands shall not use the same path for the CROSS_COMPILE option. "linux-x86" must be replaced with "darwin-x86".

2) The Makefile in backport-wcn must be modified.

::

         * The comment on line 101 looking like this: 
         *  * # RHEL as well, sadly we need to grep for it                                ;\ 
         *  *  * It must be remove or else you will get a bash error. 3) You must modify the kconf/Makefile 
         *  *  * To the first line in this file (beginning with CFLAGS) add -DKBUILD_NO_NLS to the end. Otherwise you will get a lkc.h error when building. 

Installation
------------

Mako on CM 10.1
~~~~~~~~~~~~~~~

1) Compile `CyanogenMod <CyanogenMod>`__ as per instructions: http://wiki.cyanogenmod.org/w/Build_for_mako Be sure to checkout CM10.1:

::

   repo init -u git://github.com/CyanogenMod/android.git -b cm-10.1

2) From your CM_ROOT-folder configure the CM Kernel:

::

   make  -C kernel/lge/mako \
   O=$CM_ROOT/out/target/product/$CM_BUILD/obj/KERNEL_OBJ \
   INSTALL_MOD_PATH=../../system \
   ARCH=arm \
   CROSS_COMPILE="$CM_ROOT/prebuilts/misc/linux-x86/ccache/ccache $CM_ROOT/prebuilts/gcc/linux-x86/arm/arm-eabi-4.6/bin/arm-eabi-" \
   menuconfig

::

         *  *    * Enable loadable module support and all sub-menu entries. 
         *  *    * Enable CCM support under Cryptographic API. 
         *  *    * Disable cfg80211 - wireless configuration API under Networking support -> Wireless. 
         *  *    * Disable PRIMA-WLAN under Device drivers -> Staging drivers -> Qualcomm Atheros Prima WLAN module 

3) Replace mako_defconfig with the new .config:

::

   cp out/target/product/mako/obj/KERNEL_OBJ/.config \
   kernel/lge/mako/arch/arm/configs/mako_defconfig

4) Create new file device/lge/mako/init.mako.wcn36xx.sh:

::

   #!/system/bin/sh /system/bin/insmod /system/lib/modules/wcn36xx_msm.ko /system/bin/insmod /system/lib/modules/compat.ko /system/bin/insmod /system/lib/modules/cfg80211.ko /system/bin/insmod /system/lib/modules/mac80211.ko /system/bin/insmod /system/lib/modules/wcn36xx.ko 

5) Edit device/lge/mako/device.mk and add init.mako.wcn36xx.sh to PRODUCT_COPY_FILES:

::

   PRODUCT_COPY_FILES += \
           device/lge/mako/init.mako.bt.sh:system/etc/init.mako.bt.sh \
           device/lge/mako/init.mako.wcn36xx.sh:system/etc/init.mako.wcn36xx.sh

6) Edit device/lge/mako/init.mako.rc and comment out section 'service p2p_supplicant'. Then copy 'service wpa_supplicant' and rename that to 'service p2p_supplicant'.

7) Add to the end of device/lge/mako/init.mako.rc:

::

   service wcn36xx /system/bin/sh /system/etc/init.mako.wcn36xx.sh
       class main
       user root
       oneshot

8) Compile new images and flash them according to `CyanogenMod <CyanogenMod>`__ instructions.

9) Compile wcn36xx as per instructions above.

10) Install kernel modules to the device:

::

   adb root
   adb remount

   cd ../backports-output
   adb push compat/compat.ko /system/lib/modules/
   adb push net/wireless/cfg80211.ko /system/lib/modules/
   adb push net/mac80211/mac80211.ko /system/lib/modules/
   adb push drivers/net/wireless/ath/wcn36xx/wcn36xx.ko /system/lib/modules/
   adb push drivers/net/wireless/ath/wcn36xx/wcn36xx_msm/wcn36xx_msm.ko /system/lib/modules/

11) Reboot the device and now you should be able to use wcn36xx from GUI.

Mint on CM 10.1
~~~~~~~~~~~~~~~

::

         *  *      - Follow instructions ([[http://wiki.cyanogenmod.org/w/Build_for_mint|http://wiki.cyanogenmod.org/w/Build_for_mint]]) do download and build CM sources. 
         *  *      - In case of build error "No such file or directory: 'vendor/sony/blue-common/proprietary/boot/RPM.bin'" download file RPM.bin from [[https://github.com/TheMuppets/proprietary_vendor_sony|https://github.com/TheMuppets/proprietary_vendor_sony]] and put it to the folder 'vendor/sony/blue-common/proprietary/boot' 
         *  *      - Flash built image to the phone as described here [[http://www.xperiablog.net/2012/12/04/how-to-install-cyanogenmod-10-on-your-sony-xperia-t-guide/|http://www.xperiablog.net/2012/12/04/how-to-install-cyanogenmod-10-on-your-sony-xperia-t-guide/]] 
