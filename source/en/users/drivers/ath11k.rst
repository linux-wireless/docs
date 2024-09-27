About ath11k
------------

ath11k is a Linux driver for Qualcomm `IEEE 802.11ax <https://en.wikipedia.org/wiki/IEEE_802.11ax>`__ devices, supporting both AHB bus in SoC type devices and PCI. ath11k uses mac80211. It was first included in Linux v5.6 released March 2020.

Subpages
--------

-  :doc:`Installation <ath11k/installation>`
-  :doc:`Reporting bugs <ath11k/bugreport>`
-  :doc:`Mailinglist <ath11k/mailinglist>`
-  :doc:`Submitting patches <ath11k/submittingpatches>`

Supported Devices
-----------------

-  IPQ8074 hw2.0 (v5.6)
-  IPQ6018 hw1.0 (v5.10)
-  QCA6390 hw2.0 (v5.10)
-  QCA6391 hw2.0 (v5.10) - found in `AIRETOS E63 Class by VOXMICRO <https://airetos.voxmicro.com/e63-class/>`__ MPNs: ACB-QCA6391
-  QCN9074 hw1.0 (v5.14)
-  WCN6855 hw2.0 (v5.17)
-  WCN6855 hw2.1 (v5.17)
-  QCA2062 hw2.1 (v5.17) - found in `AIRETOS E20 Class by VOXMICRO <https://airetos.voxmicro.com/e20-class/>`__ MPNs: ACB-QCA2062
-  QCA2066 hw2.1 (v5.17) - found in `AIRETOS E20 Class by VOXMICRO <https://airetos.voxmicro.com/e20-class/>`__ MPNs: ACB-QCA2066
-  QCA6698AQ hw2.1 (v5.17) - found in `AIRETOS E20 Class by VOXMICRO <https://airetos.voxmicro.com/e20-class/>`__ MPNs: ACB-QCA6698

Known bugs/limitations
----------------------

-  QCA6390: firmware WLAN.HST.1.0.1-01740-QCAHSTSWPLZ_V2_TO_X86-1 and older have problems accessing host memory below 32 MB (`bug #210923 <https://bugzilla.kernel.org/show_bug.cgi?id=210923>`__)
-  QCA6390: v5.16 and older require 32 MSI interrupts, make sure VT-d is enabled or use patchset `ath11k: support one MSI vector <https://patchwork.kernel.org/project/linux-wireless/list/?series=570089&state=*&order=date>`__
