mediatek
========

Introduction
~~~~~~~~~~~~

mac80211 wireless driver for MediaTek MT7xxx series

-  **mt76** driver handles:

   -  **MT7610U** 802.11a/b/g/n/ac 1T1R 2.4/5GHz USB Chip
   -  **MT7612**/**MT7602**/**MT7662** 802.11a/b/g/n/ac 2T2R 2.4/5GHz PCIe/USB Chip
   -  **MT7630E** 802.11a/b/g/n 1T1R 2.4/5GHz PCIe Chip
   -  **MT7610E** 802.11a/b/g/n/ac 1T1R 2.4/5GHz PCIe Chip
   -  **MT7603E** 802.11b/g/n 2T2R 2.4GHz PCIe chip and **MT7628** 802.11b/g/n 2T2R 2.4GHz SoC Device (**4.7+**)
   -  **MT7615** 802.11a/b/g/n/ac 4T4R 2.4/5GHz PCIe Chip (**5.2+**)
   -  **MT7622** 802.11b/g/n 4T4R 2.4GHz SoC Device (**5.7+**)
   -  **MT7663** 802.11a/b/g/n/ac 2T2R 2.4/5GHz PCIe/USB/SDIO Chip (**5.8+**)
   -  **MT7915**/**MT7916** 802.11a/b/g/n/ac/ax 4T4R 2.4/5GHz PCIe Chip (**5.9+**)
   -  **MT7986**/**MT7981** 802.11a/b/g/n/ac/ax 4T4R 2.4/5GHz SoC Device (**5.18+**)
   -  **MT7921** 802.11a/b/g/n/ac/ax 2T2R 2.4/5GHz/6Hz PCIe/USB/SDIO Chip

         * MT7921 PCIe is supported since (**5.12+**)
         * MT7921 SDIO is supported since (**5.16+**)
         * MT7921 USB is supported since (**5.18+**)
         * 6G band is supported by MT7921K

   - **MT7922** 802.11a/b/g/n/ac/ax 2T2R 2.4/5G/6GHz PCIe Chip (**5.16+**)
   - **MT7996** 802.11a/b/g/n/ac/ax/be 4T4R 2.4/5G/6GHz PCIe Chip (**6.2+**)
   - **MT7925** 802.11a/b/g/n/ac/ax/be 2T2R 2.4/5G/6GHz PCIe/USB Chip (**6.7+**)
   - **MT7992** 802.11a/b/g/n/ac/ax/be 4T4R 2.4/5T5R 5G PCIe Chip (**6.8+**)

-  **mt7601u** driver handles:

   -  **MT7601U** 802.11b/g/n 1T1R 2.4GHz USB Chip

note: 5Ghz MT7613BEN is handled as a mt7663 case (ChipID=0x7663) which is handled by mt7615 driver. Openwrt Archer c6 v3 uses it.

Unsupported chips
~~~~~~~~~~~~~~~~~

* `Any other MediaTek chips <https://deviwiki.com/wiki/MediaTek>`__

Firmware
~~~~~~~~

You can get the latest firmware from `linux-firmware.git
<https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/mediatek>`__

Developers & Support
~~~~~~~~~~~~~~~~~~~~

Send patches to the people and mailing lists below:

* To: Felix Fietkau <nbd@nbd.name> 
* To: Lorenzo Bianconi <lorenzo@kernel.org> 
* To: Ryder Lee <ryder.lee@mediatek.com>
* To: Shayne Chen <shayne.chen@mediatek.com> 
* To: Sean Wang <sean.wang@mediatek.com>
* To: Deren Wu <deren.wu@mediatek.com>
* Cc: <linux-mediatek@lists.infradead.org> - https://lists.infradead.org/mailman/listinfo/linux-mediatek
* Cc: <linux-wireless@vger.kernel.org> - http://vger.kernel.org/vger-lists.html#linux-wireless

IRC channel: #mt76-devel
