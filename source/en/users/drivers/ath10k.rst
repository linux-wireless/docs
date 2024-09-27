About ath10k
------------

ath10k is the mac80211 wireless driver for Qualcom Atheros QCA988x family of chips, which support `IEEE 802.11ac <https://en.wikipedia.org/wiki/IEEE_802.11ac>`__. It was first included in Linux 3.11-rc1 released on 2013-07-14.

The ath10k driver is located under `drivers/net/wireless/ath/ath10k <https://git.kernel.org/cgit/linux/kernel/git/kvalo/ath.git/tree/drivers/net/wireless/ath/ath10k>`__ directory. For more information see :doc:`en/users/drivers/ath10k/sources <ath10k/sources>`.

Subpages
--------

-  :doc:`Support and reporting bugs <ath10k/support>`
-  :doc:`Sources <ath10k/sources>`
-  :doc:`Submitting Patches <ath10k/submittingpatches>`
-  :doc:`Board Files <ath10k/boardfiles>`
-  :doc:`FAQ <ath10k/faq>`
-  :doc:`Backports <ath10k/backports>`
-  :doc:`Architecture <ath10k/architecture>`
-  :doc:`Debug <ath10k/debug>`
-  :doc:`Firmware <ath10k/firmware>`
-  :doc:`Configuration <ath10k/configuration>`
-  :doc:`Coding Style <ath10k/codingstyle>`
-  :doc:`Spectral Scan <ath10k/spectral>`
-  :doc:`Monitor Mode <ath10k/monitor>`
-  :doc:`Mesh Mode <ath10k/mesh>`
-  :doc:`TODO <ath10k/todo>`
-  :doc:`Private Support <ath10k/privatesupport>`

Supported Devices
-----------------

ath10k supports Qualcomm Atheros 802.11ac QCA98xx hw2.0 and QCA6174 based devices, here's a list of known products:

-  QCA9880/QCA9882 Version 2 found in `AIRETOS E98 Class by VOXMICRO <https://airetos.voxmicro.com/e98-class/>`__ MPNs: AEX-QCA9880 & AEX-QCA9882
-  QCA9890/QCA9892 Version 2 found in `AIRETOS E98 Class by VOXMICRO <https://airetos.voxmicro.com/e98-class/>`__ MPNs: AEX-QCA9890 & AEX-QCA9892
-  QCA9888 found in `2x2 MU-MIMO 802.11ac Wave 2 Wireless Module - Compex WLE650V5-18A <http://www.compex.com.sg/product/wle650v5-18/>`__
-  QCA9890 found in `SparkLan WPEA-352ACNRBI - supports 802.11ac radio <https://www.sparklan.com/product/wpea-352acnrbi-qca9890-3t3r-industrial-grade-module/>`__
-  QCA9890 Version 2 found in `A family of Dual band/Single band/high powered/extended temp radio modules from Doodle Labs <http://www.doodlelabs.com/products/802-11-wifi-mimo-radio-transceivers/>`__
-  QCA9882-BR4A found in `SparkLan WPEQ-256ACN <https://www.sparklan.com/product/wpeq-256acn-qca9882-2t2r-ap-mode-module/>`__
-  QCA9882-BR4A found in `SparkLan WPEQ-257ACN <https://www.sparklan.com/product/wpeq-257acn-qca9882-2t2r-ap-mode-module/>`__
-  QCA9892-BR4B found in `SparkLan WPEQ-256ACNI <https://www.sparklan.com/product/wpeq-256acni-qca9882-2t2r-industrial-grade-module/>`__
-  QCA9892 Version 2 found in `A family of Dual band/Single band/high powered/extended temp radio modules from Doodle Labs <http://www.doodlelabs.com/products/802-11-wifi-mimo-radio-transceivers/>`__
-  QCA9882 Version 2 found in `Compex WLE600V5-27 11ac 2x2 miniPCIe Wireless Module <http://www.compex.com.sg/product/wle600v5-27/>`__
-  QCA9880 Version 2 found in `SparkLan WPEA-352ACNRB - supports 802.11ac radio <https://www.sparklan.com/product/wpea-352acnrb-qca9890-3t3r-industrial-grade-module/>`__
-  QCA9880 Version 2 found in `Compex acWave: WPJ344 - supports 802.11ac radio <http://wiki.openwrt.org/toh/compex/wpj344>`__
-  QCA9880 Version 2 found in `Compex WLE900V5-18 <http://www.compex.com.sg/product/wle900v5-27/>`__
-  QCA9880 Version 2 found in `Compex WLE900V5-27 <http://www.compex.com.sg/product/wle900v5-27/>`__
-  QCA9880 Version 2 found in `Compex WLE900VX <http://www.compex.com.sg/product/wle900vx/>`__ [1]
-  QCA9880 Version 2 found in `Unex: DAXA-O1 <http://www.unex.com.tw/product/daxa-o1>`__
-  QCA9882 Version 2 found in `Compex WLE600V5-18 <http://www.compex.com.sg/product/wle600v5-27/>`__
-  QCA9882 Version 2 found in `Compex WLE600V5-27 <http://www.compex.com.sg/product/wle600v5-27/>`__
-  QCA9882 Version 2 found in `Compex WLE600VX <http://www.compex.com.sg/product/wle600vx/>`__
-  QCA9880 Version 2 found in `TP-Link : Archer C7 v2.x <http://wiki.openwrt.org/toh/tp-link/tl-wdr7500>`__
-  QCA9880 Version 2 found in `TP-Link : WDR7500 v3.0 <http://wiki.openwrt.org/toh/tp-link/tl-wdr7500>`__
-  QCA9880/QCA9890 found in `jjPlus JWX6052 <https://www.emwicon.com/product-2#jwx6052/>`__ and `jjPlus JWX6053 <https://www.emwicon.com/product-2#jwx6053/>`__
-  QCA9882/QCA9892 found in `jjPlus JWX6055 <https://www.emwicon.com/product-2#jwx6055/>`__ and `jjPlus JWX6056 <https://www.emwicon.com/product-2#jwx6056/>`__
-  QCA9880/QCA9890 found in `EmWicon JWX6052(3x3) <https://www.emwicon.com/product-2#jwx6052>`__ and `EmWicon JWX6053(3x3 Industrial Grade) <https://www.emwicon.com/product-2#jwx6053>`__
-  QCA9882/QCA9892 found in `EmWicon JWX6055(2x2) <https://www.emwicon.com/product-2#jwx6055>`__ and `EmWicon JWX6056(2x2 Industrial Grade) <https://www.emwicon.com/product-2#jwx6056>`__
-  QCA9377-5 found in `SparkLan WNFQ-158ACN(BT) <http://www.sparklan.com/p2-products-detail.php?PKey=1d2bsjqrHnqa85aaHl0mpJtOWcBpjf5kKBc0DfFEU90&WNFQ-158ACN(BT)/>`__
-  QCA9886 found in `WLE650V5-18 <http://www.compex.com.sg/product/wle650v5-18/>`__
-  QCA6174A-5 found in `AIRETOS E61 Class by VOXMICRO <https://airetos.voxmicro.com/e61-class/>`__ MPNs: AFX-QCA6174
-  QCA6174 / QCA6174A found in `Compex WLT674 <https://compex.com.sg/shop/wifi-module/wlt674/>`__ and `Bointec DPE109A <http://bointec.com/p4-products_detail.php?PKey=6851tczr12Q8EfPpaG9ML6ap7bJe2sSKZYPXP_9jLIE>`__
-  QCA6174A-5 found in `SparkLan WPEA-251ACNI(BT) <https://www.sparklan.com/product/wpea-251acni-bt-qca6174a-mu-mimo-industrial-grade-module/>`__
-  QCA6174A-5 found in `SparkLan WPEQ-261ACNI(BT) <https://www.sparklan.com/product/wpeq-261acnibt-qca6174a-mu-mimo-industrial-grade-module/>`__
-  QCA6174A-5 found in `SparkLan WPEQ-262ACNI(BT) high power <https://www.sparklan.com/product/wpeq-262acnibt-qca6174a-industrial-grade-module/>`__
-  QCA6174A-5 found in `SparkLan WPEQ-261ACNI(BT) <https://www.sparklan.com/product/wpeq-261acnibt-qca6174a-mu-mimo-industrial-grade-module/>`__
-  QCA6174A-5 found in `SparkLan WNFQ-261ACNI(BT) <https://www.sparklan.com/product/wnfq-261acnibt-qca6174a-m-2-industrial-module/>`__
-  QCA6174A-5 found in `SparkLan WNFQ-262ACNI(BT) <https://www.sparklan.com/product/wnfq-262acnibt-qca6174a-b-key-industrial-module-sparklan/>`__
-  QCA6174A-5 found in `SparkLan WNFQ-258ACN(BT) <https://www.sparklan.com/product/wnfq-258acnbt-qca6174a-2t2r-m-2-module/>`__
-  QCA6174A-5 found in `SparkLan WNSQ-261ACN(BT) <https://www.sparklan.com/product/wnsq-261acnbt-qca6174a-2t2r-m-2-module/>`__
-  QCA6174A-5 found in `SparkLan WPEQ-261ACN(BT) <https://www.sparklan.com/product/wpeq-261acnbt-qca6174a-2t2r-mu-mimo-module/>`__
-  QCA6174A-5 found in `jjPlus JWX6058 <https://www.jjplus.com/jwx6058/>`__ and `jjPlus JWW6051 <https://www.jjplus.com/jww6051/>`__
-  QCA6174A-5 found in `EmWicon JWX6058(mPCIe) <https://www.emwicon.com/product-2#jwx6058>`__ and `EmWicon JWW6051(M.2) <https://www.emwicon.com/product-2#jww6051>`__
-  QCA9984 /QCA9994 found in `Compex WLE1216V5-20 <https://compex.com.sg/shop/wifi-module/wle1216v5-20/>`__
-  QCA9984 /QCA9994 found in `EmWicon WMX6401/WMX6402 <https://www.emwicon.com/product-2#wmx6401>`__
-  IPQ4018 found in `8Devices Jalapeno module <https://www.8devices.com/products/jalapeno>`__

[1] The Compex WLE900VX card enumerates as PCI device on some PCs but not for some other PCs. The reason could possibly be PC hardware or kernel version. Detailed info: https://bugzilla.kernel.org/show_bug.cgi?id=84821. The Chaos Calmer wpj344a_150827_vCC.img provided by http://www.compex.com.sg/downloads/ can detect and enable the WLE900VX card with ath10k.

Not supported
-------------

ath10k does NOT support older QCA98xx hw1.0 chips found, for example, from these devices:

-  QCA9880 Version 1 found in `TP-Link WDR-7500 v2 and Archer C7 v1.x <http://wiki.openwrt.org/toh/tp-link/tl-wdr7500>`__

Any SDIO or USB devices are not supported, but work is ongoing to add that.

Known bugs/limitations
----------------------

-  firmware does not support association to the same AP from different virtual STA interfaces (driver prints "ath10k: Failed to add peer XX:XX:XX:XX:XX:XX for VDEV: X" in that case)
-  packet injection isn't supported yet
-  applying ath9k regulatory domain hack patch from OpenWRT causes firmware crash (reason: regulatory hint function is never called and ath10k never sends scan channel list to the firmware which in turn causes firmware to crash on scan)
-  tx rate is reported as 6mbps due to firmware limitation (no tx rate information in tx completions); instead see /sys/kernel/debug/ieee80211/phyX/ath10k/fw_stats
-  WEP doesn't work with AP_VLANs - frames are sent unencrypted (observed on: 999.999.0.636, 10.2.4.20-1, 10.1.467.2-1)
-  TX speeds are extremely poor on certain chips (QCA6174 is one). A `patch <https://gist.github.com/harrykipper/d1bedb234c4af0692f7ccd33329a02d7>`__ solves the issue in most cases (`source <https://bbs.archlinux.org/viewtopic.php?pid=1689990#p1689990>`__)
