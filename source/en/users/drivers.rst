Existing Linux Wireless drivers
###############################

.. toctree::
   :hidden:

   drivers/acx1xx
   drivers/adm8211
   drivers/agnx
   drivers/airo
   drivers/ar5120
   drivers/ar5523
   drivers/ar6k
   drivers/ar9170.fw
   drivers/ar9170
   drivers/ar9271
   drivers/at76_usb
   drivers/at76c50x-usb
   drivers/ath
   drivers/ath10k
   drivers/ath11k
   drivers/ath12k
   drivers/ath3k
   drivers/ath5k
   drivers/ath6kl
   drivers/ath9k
   drivers/ath9k_htc
   drivers/atheros-bt
   drivers/atheros
   drivers/atmel
   drivers/b43
   drivers/bcm43xx
   drivers/brcm80211
   drivers/carl9170.fw
   drivers/carl9170
   drivers/cw1200
   drivers/driverpagetemplate
   drivers/ipw2100
   drivers/ipw2200
   drivers/iwl3945
   drivers/iwl4965
   drivers/iwlegacy
   drivers/iwlwifi
   drivers/iwmc3200wifi
   drivers/libertas
   drivers/libertastf
   drivers/mac80211_hwsim
   drivers/madwifi
   drivers/mediatek
   drivers/mwifiex
   drivers/mwl8k
   drivers/orinoco
   drivers/otus
   drivers/p54
   drivers/qtnfmac
   drivers/rndis_wlan
   drivers/rt2400
   drivers/rt2400pci
   drivers/rt2500pci
   drivers/rt2500usb
   drivers/rt2800pci
   drivers/rt2800usb
   drivers/rt2880_inic
   drivers/rt61pci
   drivers/rt73usb
   drivers/rtl8187
   drivers/rtl819x
   drivers/stlc45xx
   drivers/vt665x
   drivers/wcn36xx
   drivers/wfx
   drivers/wil6210
   drivers/wilc
   drivers/wl1251
   drivers/wl12xx
   drivers/wl18xx
   drivers/wlags49_h2
   drivers/zd1211rw

We currently have a fair amount of working drivers that cover most of the
available wireless networking cards. However, they don't implement all features
and may have some issues, due to various reasons like companies not providing
specs. Below is an alphabetically sorted list of drivers and what they currently
can and can't do.

.. seealso::

   `Linux wireless drivers in Wikipedia
   <https://en.wikipedia.org/wiki/Comparison_of_open_source_wireless_drivers>`__

.. note::

   All drivers can of course run in :doc:`station mode <documentation/modes>`,
   but only a few drivers support the other available :doc:`wireless modes
   <documentation/modes>`! Support of :doc:`cfg80211
   <../developers/documentation/glossary>` also offers benefits.

Supported drivers
*****************

.. list-table::
   :header-rows: 1

   - 

      - Driver
      - Manufacturer
      - cfg80211
      - AP
      - IBSS
      - mesh
      - monitor
      - PHY modes
      - Buses
   - 

      - :doc:`adm8211 <drivers/adm8211>`
      - ADMtek/Infineon
      - yes
      - no
      - no
      - no
      - ?
      - B
      - PCI
   - 

      - :doc:`airo <drivers/airo>`
      - Aironet/Cisco
      - no
      - ?
      - ?
      - ?
      - ?
      - B
      - PCI / PCMCIA
   - 

      - :doc:`ar5523 <drivers/ar5523>`
      - Atheros
      - yes
      - no
      - no
      - no
      - yes
      - A(2)/B/G
      - USB
   - 

      - :doc:`at76c50x-usb <drivers/at76c50x-usb>`
      - Atmel
      - yes
      - no
      - no
      - no
      - no
      - B
      - USB
   - 

      - :doc:`ath5k <drivers/ath5k>`
      - Atheros
      - yes
      - yes
      - yes
      - yes
      - yes
      - A/B/G
      - PCI / PCI-E / PCMCIA
   - 

      - :doc:`ath6kl <drivers/ath6kl>`
      - Atheros
      - yes
      - no
      - yes
      - no
      - no
      - A/B/G/N
      - SDIO / USB
   - 

      - :doc:`ath9k <drivers/ath9k>`
      - Atheros
      - yes
      - yes
      - yes
      - yes
      - yes
      - A/B/G/N
      - PCI / PCI-E / AHB / PCMCIA
   - 

      - :doc:`ath9k_htc <drivers/ath9k_htc>`
      - Atheros
      - yes
      - yes
      - yes
      - yes
      - yes
      - B/G/N
      - USB
   - 

      - :doc:`ath10k <drivers/ath10k>`
      - Qualcomm Atheros
      - yes
      - yes
      - yes (6)
      - yes (6)
      - yes (6)
      - A/B/G/N/AC
      - PCI-E / AHB / SDIO
   - 

      - :doc:`ath11k <drivers/ath11k>`
      - Qualcomm Atheros
      - yes
      - yes
      - no
      - yes (6)
      - yes (6)
      - A/B/G/N/AC/AX
      - PCI-E / AHB
   - 

      - :doc:`ath12k <drivers/ath12k>`
      - Qualcomm Atheros
      - yes
      - yes
      - no
      - yes (6)
      - yes (6)
      - A/B/G/N/AC/AX/BE
      - PCI-E
   - 

      - :doc:`atmel <drivers/atmel>`
      - Atmel
      - no
      - ?
      - ?
      - ?
      - ?
      - B
      - PCI / PCMCIA
   - 

      - :doc:`b43 <drivers/b43>`
      - Broadcom
      - yes
      - yes
      - yes
      - yes
      - yes
      - A(2)/B/G
      - SSB / PCI / PCI-E / PCMCIA
   - 

      - :doc:`b43legacy <drivers/b43>`
      - Broadcom
      - yes
      - yes
      - yes
      - yes
      - yes
      - A(2)/B/G
      - PCI / SSB
   - 

      - :doc:`brcmfmac <drivers/brcm80211>`
      - Broadcom
      - yes
      - yes
      - yes
      - no
      - no
      - A(1)/B/G/N/AC
      - USB / SDIO / PCI-E
   - 

      - :doc:`brcmsmac <drivers/brcm80211>`
      - Broadcom
      - yes
      - yes
      - no
      - no
      - yes
      - A(1)/B/G/N
      - PCI-E / AXI
   - 

      - :doc:`carl9170 <drivers/carl9170>`
      - ZyDAS/Atheros
      - yes
      - yes
      - yes
      - yes
      - yes
      - A(1)/B/G/N
      - USB
   - 

      - :doc:`cw1200 <drivers/cw1200>`
      - ST-Ericsson
      - yes
      - ?
      - ?
      - ?
      - ?
      - A/B/G/N
      - SPI / SDIO
   - 

      - `hostap <http://w1.fi/>`__
      - Intersil/Conexant
      - no
      - ?
      - ?
      - ?
      - ?
      - B
      - PCI / PCMCIA
   - 

      - :doc:`ipw2100 <drivers/ipw2100>`
      - Intel
      - no
      - no
      - yes
      - no
      - no
      - B
      - PCI
   - 

      - :doc:`ipw2200 <drivers/ipw2200>`
      - Intel
      - no
      - no (3)
      - yes
      - no
      - no
      - A/B/G
      - PCI
   - 

      - :doc:`iwlegacy <drivers/iwlegacy>`
      - Intel
      - yes
      - no
      - yes
      - no
      - no
      - A/B/G
      - PCI-E
   - 

      - :doc:`iwlwifi <drivers/iwlwifi>`
      - Intel
      - yes
      - yes (6)
      - yes
      - no
      - yes
      - A/B/G/N/AC/AX/BE
      - PCI-E
   - 

      - :doc:`libertas <drivers/libertas>`
      - Marvell
      - no
      - no
      - yes
      - yes (4)
      - no
      - B/G
      - USB / PCMCIA / SDIO / GSPI
   - 

      - :doc:`libertas_tf <drivers/libertastf>`
      - Marvell
      - yes
      - yes
      - no
      - yes
      - ?
      - B/G
      - USB
   - 

      - :doc:`mac80211_hwsim <drivers/mac80211_hwsim>`
      - Jouni
      - yes
      - yes
      - yes
      - no
      - yes
      - A/B/G/N
      - NONE!
   - 

      - :doc:`mt76 <drivers/mediatek>`
      - Mediatek
      - yes
      - yes
      - yes
      - yes
      - yes
      - A/B/G/N/AC/AX
      - PCIe / SoC / USB / SDIO
   - 

      - :doc:`mt7601u <drivers/mediatek>`
      - Mediatek
      - yes
      - ?
      - ?
      - ?
      - ?
      - B/G/N/
      - USB
   - 

      - :doc:`mwifiex <drivers/mwifiex>`
      - Marvell
      - yes
      - yes
      - yes
      - ?
      - ?
      - A/B/G/N
      - SDIO / PCI-E / USB
   - 

      - :doc:`mwl8k <drivers/mwl8k>`
      - Marvell
      - yes
      - yes
      - ?
      - ?
      - yes
      - A/B/G/N
      - PCI
   - 

      - :doc:`orinoco <drivers/orinoco>`
      - Agere/Intersil/Symbol
      - yes
      - no
      - yes
      - no
      - yes
      - B
      - PCI / PCMCIA / USB
   - 

      - :doc:`p54pci <drivers/p54>`
      - Intersil/Conexant
      - yes
      - yes
      - yes
      - yes
      - yes
      - A(1)/B/G
      - PCI / PCMCIA
   - 

      - :doc:`p54spi <drivers/p54>`
      - Conexant/ST-NXP
      - yes
      - yes
      - yes
      - yes
      - yes
      - A(1)/B/G
      - SPI
   - 

      - :doc:`p54usb <drivers/p54>`
      - Intersil/Conexant
      - yes
      - yes
      - yes
      - yes
      - yes
      - A(1)/B/G
      - USB
   - 

      - `\*\* prism2_usb <http://www.linux-wlan.org/>`__
      - Intersil/Conexant
      - yes
      - ?
      - ?
      - ?
      - ?
      - B
      - USB
   - 

      - :doc:`qtnfmac <drivers/qtnfmac>`
      - Quantenna
      - yes
      - yes
      - no
      - no
      - no
      - A/B/G/N/AC
      - PCI-E
   - 

      - :doc:`\*\* r8192e_pci <drivers/rtl819x>`
      - Realtek
      - no
      - ?
      - ?
      - ?
      - ?
      - B/G/N
      - PCI-E
   - 

      - :doc:`\*\* r8192u_usb <drivers/rtl819x>`
      - Realtek
      - no
      - ?
      - ?
      - ?
      - ?
      - B/G/N
      - USB
   - 

      - :doc:`\*\* r8712u <drivers/rtl819x>`
      - Realtek
      - no
      - ?
      - ?
      - ?
      - ?
      - B/G/N
      - USB
   - 

      - `ray_cs <en/users/Drivers/ray_cs>`__
      - Raytheon
      - no
      - ?
      - ?
      - ?
      - ?
      - pre802.11
      - PCMCIA
   - 

      - :doc:`rndis_wlan <drivers/rndis_wlan>`
      - Broadcom
      - yes
      - no
      - yes
      - no
      - no
      - B/G
      - USB
   - 

      - :doc:`rt61pci <drivers/rt61pci>`
      - Ralink
      - yes
      - yes
      - yes
      - no
      - yes
      - A(1)/B/G
      - PCI
   - 

      - :doc:`rt73usb <drivers/rt73usb>`
      - Ralink
      - yes
      - yes
      - yes
      - no
      - yes
      - A(1)/B/G
      - USB
   - 

      - :doc:`rt2400pci <drivers/rt2400pci>`
      - Ralink
      - yes
      - yes
      - yes
      - no
      - yes
      - B
      - PCI
   - 

      - :doc:`rt2500pci <drivers/rt2500pci>`
      - Ralink
      - yes
      - yes
      - yes
      - no
      - yes
      - A(1)/B/G
      - PCI
   - 

      - :doc:`rt2500usb <drivers/rt2500usb>`
      - Ralink
      - yes
      - yes
      - yes
      - no
      - yes
      - A(1)/B/G
      - USB
   - 

      - :doc:`rt2800pci <drivers/rt2800pci>`
      - Ralink
      - yes
      - yes
      - ?
      - ?
      - yes
      - A(1)/B/G/N
      - PCI
   - 

      - :doc:`rt2800usb <drivers/rt2800usb>`
      - Ralink
      - yes
      - yes
      - yes
      - yes(5)
      - yes
      - A(1)/B/G/N
      - USB
   - 

      - :doc:`rtl8xxxu <drivers/rtl819x>`
      - Realtek
      - yes
      - ?
      - ?
      - ?
      - ?
      - A(1)/B/G/N
      - USB
   - 

      - :doc:`rtl8180 <drivers/rtl8187>`
      - Realtek
      - yes
      - no
      - no
      - no
      - ?
      - B/G
      - PCI
   - 

      - :doc:`rtl8187 <drivers/rtl8187>`
      - Realtek
      - yes
      - no
      - yes
      - no
      - yes
      - B/G
      - USB
   - 

      - :doc:`rtl8188ee <drivers/rtl819x>`
      - Realtek
      - yes
      - ?
      - ?
      - ?
      - ?
      - B/G/N
      - PCI-E
   - 

      - :doc:`rtl8192ce <drivers/rtl819x>`
      - Realtek
      - yes
      - ?
      - ?
      - ?
      - yes
      - B/G/N
      - PCI-E
   - 

      - :doc:`rtl8192cu <drivers/rtl819x>`
      - Realtek
      - yes
      - yes
      - ?
      - ?
      - yes
      - B/G/N
      - USB
   - 

      - :doc:`rtl8192de <drivers/rtl819x>`
      - Realtek
      - yes
      - ?
      - ?
      - ?
      - ?
      - B/G/N
      - PCI-E
   - 

      - :doc:`rtl8192se <drivers/rtl819x>`
      - Realtek
      - yes
      - yes
      - ?
      - ?
      - ?
      - B/G/N
      - PCI-E
   - 

      - :doc:`rtl8723ae <drivers/rtl819x>`
      - Realtek
      - yes
      - ?
      - ?
      - ?
      - ?
      - B/G/N
      - PCI-E
   - 

      - :doc:`rtl8723bs <drivers/rtl819x>`
      - Realtek
      - ?
      - ?
      - ?
      - no
      - no
      - B/G/N
      - SDIO
   - 

      - :doc:`\*\* r8723au <drivers/rtl819x>`
      - Realtek
      - yes
      - ?
      - ?
      - ?
      - ?
      - B/G/N
      - USB
   - 

      - :doc:`\*\* vt6655 <drivers/vt665x>`
      - VIA
      - yes
      - yes
      - yes
      - no
      - no
      - A/B/G
      - PCI
   - 

      - :doc:`\*\* vt6656 <drivers/vt665x>`
      - VIA
      - yes
      - yes
      - yes
      - no
      - no
      - A/B/G
      - USB
   - 

      - :doc:`wcn36xx <drivers/wcn36xx>`
      - Qualcomm Atheros
      - yes
      - yes
      - yes
      - yes
      - yes
      - A/B/G/N
      - 
   - 

      - :doc:`wfx <drivers/wfx>`
      - Silicon Laboratories
      - yes
      - yes
      - no
      - no
      - no
      - A/B/G/N
      - SPI / SDIO
   - 

      - :doc:`wil6210 <drivers/wil6210>`
      - Atheros
      - yes
      - yes
      - no
      - no
      - yes
      - AD
      - PCI-E
   - 

      - `\*\* winbond <http://code.google.com/p/winbondport/>`__
      - Winbond
      - yes
      - ?
      - ?
      - ?
      - ?
      - B
      - USB
   - 

      - :doc:`\*\* wilc <drivers/wilc>`
      - Microchip
      - yes
      - yes
      - no
      - no
      - no
      - A/B/G/N
      - SPI / SDIO
   - 

      - :doc:`wl1251 <drivers/wl1251>`
      - Texas Instruments
      - yes
      - no
      - yes
      - ?
      - yes
      - B/G
      - SPI / SDIO
   - 

      - :doc:`wl12xx <drivers/wl12xx>`
      - Texas Instruments
      - yes
      - yes
      - yes
      - no
      - no
      - A(1)/B/G/N
      - SPI / SDIO
   - 

      - :doc:`wl18xx <drivers/wl18xx>`
      - Texas Instruments
      - yes
      - yes
      - yes
      - ?
      - ?
      - A/B/G/N
      - SDIO
   - 

      - `wl3501_cs <en/users/Drivers/wl3501_cs>`__
      - Z-Com
      - no
      - ?
      - ?
      - ?
      - ?
      - pre802.11
      - PCMCIA
   - 

      - :doc:`\*\* wlags49_h2 <drivers/wlags49_h2>`
      - Lucent/Agere
      - no
      - ?
      - ?
      - ?
      - ?
      - B/G
      - PCI / PCMCIA
   - 

      - `zd1201 <en/users/Drivers/zd1201>`__
      - ZyDAS/Atheros
      - no
      - ?
      - ?
      - ?
      - ?
      - B
      - USB
   - 

      - :doc:`zd1211rw <drivers/zd1211rw>`
      - ZyDAS/Atheros
      - yes
      - yes
      - yes
      - yes
      - yes
      - A(2)/B/G
      - USB

.. note::

   \*\* **staging drivers**

Out of the tree drivers(Unsupported)
************************************

.. list-table::
   :header-rows: 1

   - 

      - Driver
      - Manufacturer
      - cfg80211
      - AP
      - IBSS
      - mesh
      - monitor
      - PHY modes
      - Buses
   - 

      - :doc:`acx1xx <drivers/acx1xx>`
      - Texas Instruments
      - yes
      - ?
      - ?
      - no
      - ?
      - B
      - PCI / PCMCIA / USB
   - 

      - :doc:`agnx <drivers/agnx>`
      - Airgo/Qualcom
      - yes
      - ?
      - ?
      - ?
      - ?
      - A/B/G
      - PCI
   - 

      - :doc:`ar6k <drivers/ar6k>`
      - Atheros
      - ?
      - ?
      - ?
      - ?
      - ?
      - B/G
      - ?
   - 

      - `poldhu <http://poldhu.sf.net/>`__
      - NWN
      - no
      - ?
      - ?
      - ?
      - ?
      - B
      - PCMCIA
   - 

      - :doc:`RT2880 iNIC <drivers/rt2880_inic>`
      - Ralink
      - ?
      - ?
      - ?
      - ?
      - ?
      - ?
      - PCI

Notes:

#. 802.11a capabilities depend on the actual radio chip used. 
#. 802.11a devices exist, but currently can't be used with this driver, A/B/G devices will work in B/G mode only. 
#. There is support with a special, out-of-tree driver and special firmware, see http://sf.net/projects/ipw2200-ap
#. Slightly different mesh implementation than mac80211's, in firmware. 
#. Tested with RT2870/RT3070 driver 
#. Only some devices 

Abandoned/Deprecated Drivers(Unsupported)
*****************************************

.. list-table::
   :header-rows: 1

   - 

      - Driver
      - Manufacturer
      - :doc:`cfg80211 <../developers/documentation/cfg80211>`
      - :doc:`AP <documentation/modes>`
      - :doc:`ad-hoc <documentation/modes>`
      - :doc:`mesh <documentation/modes>`
      - :doc:`monitor <documentation/modes>`
      - PHY modes
      - BUS
      - Replaced by
   - 

      - :doc:`ar9170usb <drivers/ar9170>`
      - ZyDAS/Atheros
      - yes
      - no
      - yes
      - no
      - yes
      - A(1)/B/G/N
      - USB
      - :doc:`carl9170 <drivers/carl9170>`
   - 

      - `arlan <http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=af449f924c95fa8d4f57c9b71e9b104a5079fa33>`__
      - Aironet/Cisco
      - no
      - ?
      - ?
      - ?
      - ?
      - pre802.11
      - ISA
      -
   - 

      - :doc:`at76_usb <drivers/at76_usb>`
      - Atmel
      - no
      - no
      - no
      - no
      - no
      - B
      - USB
      - :doc:`at76c50x-usb <drivers/at76c50x-usb>`
   - 

      - `netwave_cs <http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=e5b3e80016198ee55c82dfd653c1dee99a38964b>`__
      - Netwave/Xircom
      - no
      - ?
      - ?
      - ?
      - ?
      - pre802.11
      - PCMCIA
      -
   - 

      - :doc:`otus <drivers/otus>`
      - ZyDAS/Atheros
      - no
      - ?
      - no
      - no
      - no
      - A/B/G/N
      - USB
      - :doc:`carl9170 <drivers/carl9170>`
   - 

      - :doc:`prism54 <drivers/p54>`
      - Intersil/Conexant
      - no
      - ?
      - ?
      - ?
      - ?
      - A/B/G
      - PCI / PCMCIA
      - :doc:`p54pci <drivers/p54>`
   - 

      - :doc:`stlc45xx <drivers/stlc45xx>`
      - ST/Nokia
      - yes
      - no
      - no
      - no
      - no
      - B/G
      - SPI
      - :doc:`p54spi <drivers/p54>`
   - 

      - `wavelan <http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=1d794e3b353b50ab5d9d46f7c15607f9ec8c78e0>`__
      - Lucent
      - no
      - ?
      - ?
      - ?
      - ?
      - pre802.11
      - ISA / PCMCIA
      -
