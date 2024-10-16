ath10k backports releases
=========================

`Backports <https://backports.wiki.kernel.org/index.php/Main_Page>`__
project can be used to run latest ath10k driver on older kernels. For
normal users it's recommended to use official backports releases or the
ones provided by the distro.

Here are simple instructions how to install ath10k from a backports release:

#. Download `latest backports release <http://drvbp1.linux-foundation.org/~mcgrof/rel-html/backports/>`__ and unpack it.
#. Run defconfig for ath10k: ``make defconfig-ath10k``
#. Compile backports: ``make``
#. Install backports: ``sudo make install``
#. Reboot system and ath10k should load automatically.
#. To check that you are really using ath10k from backports make sure that compat module is loaded and ath10k_pci module uses it::

     $ lsmod | grep compat
     compat                 36104  6 iwldvm,iwlwifi,ath10k_pci,ath10k_core,mac80211,cfg80211

#. To check version of backports project::

     $ dmesg | grep backport
     [   23.210662] Loading modules backported from Linux version next-20140221-0-gfaa2e6f
     [   23.210665] Backport generated by backports.git backports-20140221-0-g8e94650

See `backports documentation
<https://backports.wiki.kernel.org/index.php/Documentation>`__ for more
info.

Cooked monitor interface
------------------------

If the host kernel is v3.2 or older, even when using backports projects,
hostapd is forced to use cooked monitor interface (mon.wlan0) in AP
mode. This might create some performance issues and that's why it's
recommended to port the commit below to the host kernel so that hostapd
does not need to use cooked monitor interface::

   commit 6e3e939f3b1bf8534b32ad09ff199d88800835a0
   Author: Johannes Berg <johannes.berg@intel.com>
   Date:   Wed Nov 9 10:15:42 2011 +0100

       net: add wireless TX status socket option

Compiling custom ath10k backports
---------------------------------

For developers wanting to make changes to ath10k it's possible to create backports releases on your own:

#. Clone the backports tree: ``git clone git://git.kernel.org/pub/scm/linux/kernel/git/backports/backports.git``
#. Clone the ath.git containing latest ath10k: ``git clone git://git.kernel.org/pub/scm/linux/kernel/git/kvalo/ath.git``
#. Go to the backports tree: ``cd backports``
#. create file copy-list.ath with this content::

       COPYING
       MAINTAINERS

       # This just defines some macros, simply take it
       include/linux/bitfield.h
       include/linux/average.h

       drivers/net/wireless/Kconfig
       drivers/net/wireless/Makefile

       include/linux/ieee80211.h
       include/linux/pci_ids.h
       include/linux/ath9k_platform.h
       include/uapi/linux/nl80211.h

       include/net/cfg80211.h
       include/net/cfg80211-wext.h
       include/net/ieee80211_radiotap.h
       include/net/lib80211.h
       include/net/mac80211.h
       include/net/regulatory.h
       include/net/codel.h
       include/net/codel_impl.h
       include/net/codel_qdisc.h
       include/net/fq.h
       include/net/fq_impl.h

       net/Makefile
       net/Kconfig
       net/wireless/
       net/mac80211/

       drivers/net/wireless/ath/
       drivers/net/wireless/mac80211_hwsim.c
       drivers/net/wireless/mac80211_hwsim.h

#. Create the backports output tree::

       ./gentree.py --verbose --clean --git-revision master \
           --copy-list copy-list.ath ../ath ../backports-output

#. Go to the backports output tree: ``cd ../backports-output/``
#. At the time of this writing mac80211 led support failed to compile, disable that: ``sed -i s/CPTCFG_MAC80211_LEDS=y/CPTCFG_MAC80211_LEDS=n/ defconfigs/ath10k``
#. Create .config: ``make defconfig-ath10k``
#. Compile modules: ``make -j 10``

To run ath10k:

#. First check if there are drivers using cfg80211 running: ``lsmod | grep cfg80211``
#. Remove all such drivers, for example: \* ``sudo modprobe -r ath9k``
#. unload mac80211 and cfg80211: ``sudo modprobe -r mac80211 cfg80211``
#. Make sure that :doc:`ath10k firmware <firmware>` is installed.
#. Now you can load the all backported modules::

       sudo insmod compat/compat.ko
       sudo insmod net/wireless/cfg80211.ko
       sudo insmod net/mac80211/mac80211.ko
       sudo insmod drivers/net/wireless/ath/ath.ko
       sudo insmod drivers/net/wireless/ath/ath10k/ath10k_core.ko
       sudo insmod drivers/net/wireless/ath/ath10k/ath10k_pci.ko

#. Now ath10k is loaded and can be used normally::

       [ 2162.207812] ath10k_pci 0000:05:00.0: PCI INT A disabled
       [ 2165.136293] ath10k_pci 0000:05:00.0: BAR 0: assigned [mem 0xf0000000-0xf01fffff 64bit]
       [ 2165.136320] ath10k_pci 0000:05:00.0: BAR 0: set to [mem 0xf0000000-0xf01fffff 64bit] (PCI address [0xf0000000-0xf01fffff])
       [ 2165.136343] ath10k_pci 0000:05:00.0: PCI INT A -> GSI 19 (level, low) -> IRQ 19
       [ 2165.136365] ath10k_pci 0000:05:00.0: setting latency timer to 64
       [ 2165.140502] ath10k: MSI-X didn't succeed (1), trying MSI
       [ 2165.140606] ath10k_pci 0000:05:00.0: irq 44 for MSI/MSI-X
       [ 2165.140660] ath10k: MSI interrupt handling
       [ 2165.175112] ath10k: Hardware name qca988x hw2.0 version 0x4100016c
       [ 2166.343783] ath10k: UART prints disabled
       [ 2166.348550] ath10k: firmware 999.999.0.636 booted
       [ 2166.358939] ath10k: htt target version 2.1
       [ 2166.362076] ath: EEPROM regdomain: 0x0
       [ 2166.362080] ath: EEPROM indicates default country code should be used
       [ 2166.362083] ath: doing EEPROM country->regdmn map search
       [ 2166.362086] ath: country maps to regdmn code: 0x3a
       [ 2166.362089] ath: Country alpha2 being used: US
       [ 2166.362091] ath: Regpair used: 0x3a
       [ 2166.364798] cfg80211: Calling CRDA for country: US

To unload ath10k and backports::

   sudo rmmod drivers/net/wireless/ath/ath10k/ath10k_pci.ko
   sudo rmmod drivers/net/wireless/ath/ath10k/ath10k_core.ko
   sudo rmmod drivers/net/wireless/ath/ath.ko
   sudo rmmod net/mac80211/mac80211.ko
   sudo rmmod net/wireless/cfg80211.ko
   sudo rmmod compat/compat.ko
