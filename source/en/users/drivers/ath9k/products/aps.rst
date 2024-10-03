APs with ath9k cards
====================

This list tries to document all known APs with ath9k cards.

Legend used to describe cards
-----------------------------

- HB: PCIe Half MiniCard
- XB: PCIe Full MiniCard
- MB: Mini PCI card
- CB: PCI Cardbus card
- SB: Single band, 1x2, 2x2 configuration
- DB: Dual band, 2x3, 2x2 configuration

Legend for Access Point components
----------------------------------

* FE: Fast Ethernet, 100 Mbit/s 
* GBe: GigaBit Ethernet 1000 Mbit/s 
* USB: USB ports available 
* OLED: Organic-LED Display 
* DBDC: DualBand-DualConcurrent, means AP can run in 2 GHz and 5 GHz at
  the same time 

Table of known APs with ath9k cards
-----------------------------------

WARNING of practicality: Not all models can be flashed with custom GPL
software at this time, see the `OpenWrt web
<http://wiki.openwrt.org/toh/start>`__ for latest information. However,
all of these routers have been identified to use supported Atheros 11n
radio chips.

.. list-table::
   :header-rows: 1

   - 

      - AP Model
      - Chipset
      - Chains
      - SB
      - DB
      - FE
      - GBe
      - OLED
      - DBDC
      - USB
   - 

      - Atlantiland A02-RB-W300N
      - 
      - 
      - 
      - 
      - 
      - 
      - 
      - 
      - 
   - 

      - `AzureWave <AzureWave>`__ AW-NR580
      - AR5416 (minipci)
      - 
      - 
      - 
      - 
      - 
      - 
      - 
      - 
   - 

      - Cameo Communications WLN2206
      - 
      - 2x2
      - (./)
      - 
      - (./)
      - 
      - 
      - 
      - 
   - 

      - Buffalo WZR-HP-G300NH
      - `AR9160+AR9103 <http://wiki.openwrt.org/toh/buffalo/wzr-hp-g300h>`__
      - ?
      - ?
      - ?
      - 
      - (./)
      - 
      - 
      - (./)
   - 

      - Buffalo WZR-HP-AG300H
      - `AR?+AR? <http://wiki.openwrt.org/toh/buffalo/wzr-hp-ag300h>`__
      - ?
      - ?
      - ?
      - 
      - (./)
      - 
      - (./)
      - (./)
   - 

      - D-Link DIR-615 v.C1 (AP81)
      - AR9001AP-2NG (AR9130+AR9102 +AR8216)
      - 2x2
      - (./)
      - 
      - (./)
      - 
      - 
      - 
      - 
   - 

      - D-Link DIR-625 v.C2 (IP5K+MB71)
      - AR5008-2NG (AR5416+AR2122
      - 2x2
      - (./)
      - 
      - (./)
      - 
      - 
      - 
      - 
   - 

      - D-Link DIR-635 v.A3 (IP5K+MB71)
      - AR5008-3NG (AR5416+AR2122
      - 3x3
      - (./)
      - 
      - 
      - (./)
      - 
      - 
      - (./)
   - 

      - D-Link DIR-825 v.A1 (IP5K+MB81+MB82)
      - AR9001-3NG (AR9160+AR9103) + AR9001-3NX (AR9160+AR9106)
      - 2x2
      - 
      - 
      - 
      - (./)
      - 
      - (./)
      - (./)
   - 

      - D-Link DIR-825 v.B1 (IP5K+MB81+MB82)
      - AR9001-3NG (AR9160+AR9103) + AR9001-3NX (AR9160+AR9106)
      - 2x2
      - 
      - 
      - 
      - (./)
      - 
      - (./)
      - (./)
   - 

      - D-Link DIR-855 v.A1 (IP5K+MB71+MB72)
      - AR5008-3NG (AR5416+AR2133) + AR5008-3NX (AR5416+AR5133)
      - 3x3
      - 
      - 
      - 
      - (./)
      - (./)
      - (./)
      - (./)
   - 

      - D-Link DGL-4500 v.A1 (IP5K+MB72) (DBSW)
      - AR5008-3NX (AR5416+AR5133)
      - 3x3
      - 
      - (./)
      - 
      - (./)
      - (./)
      - 
      - (./)
   - 

      - Level One WBR-6000
      - AR5416/AR2133
      - 3x3
      - (./)
      - 
      - (./)
      - 
      - 
      - 
      - 
   - 

      - Linksys WAP-4410N
      - 
      - 3x3
      - (./)
      - 
      - 
      - (./)
      - 
      - 
      - 
   - 

      - Linksys WRT160NL
      - 
      - 
      - (./)
      - 
      - 
      - (./)
      - 
      - 
      - (./)
   - 

      - Linksys WRT300N v2.0 (serial number SNP00\*)
      - AR5416 or AR5418
      - 3x3
      - (./)
      - 
      - (./)
      - 
      - 
      - 
      - 
   - 

      - Linksys WRT350N v2.0
      - AR5416
      - 3x3
      - (./)
      - 
      - 
      - (./)
      - 
      - 
      - (./)
   - 

      - Linksys WRT400N v1.0
      - dual-band AR9220 + single-band AR9223
      - 
      - (./)
      - 
      - 
      - (./)
      - 
      - 
      - (./)
   - 

      - Planex MZK-W300NH
      - AR9102
      - 2x2
      - (./)
      - 
      - (./)
      - 
      - 
      - 
      - 
   - 

      - Planex MZK-W04NU
      - AR9103
      - 3x3
      - (./)
      - 
      - (./)
      - 
      - 
      - 
      - (./)
   - 

      - Mercury MWR300T+
      - AR9103
      - 3x3
      - (./)
      - 
      - (./)
      - 
      - 
      - 
      - 
   - 

      - Netgear WNR2000
      - AR9103
      - 3x3
      - (./)
      - 
      - (./)
      - 
      - 
      - 
      - 
   - 

      - Netgear WNR3700
      - 
      - 
      - (./)
      - 
      - (./)
      - 
      - 
      - (./)
      - (./)
   - 

      - Netgear WN802Tv2
      - 
      - 
      - (./)
      - 
      - 
      - (./)
      - 
      - 
      - 
   - 

      - TP-Link TL-WR1043ND v1.0
      - 
      - 
      - (./)
      - 
      - (./)
      - 
      - 
      - 
      - 
   - 

      - TP-Link TL-WR941N
      - AR9103
      - 3x3
      - (./)
      - 
      - (./)
      - 
      - 
      - 
      - 
   - 

      - TP-Link TL-WR941ND
      - AR9103
      - 3x3
      - (./)
      - 
      - (./)
      - 
      - 
      - 
      - 
   - 

      - TP-Link TL-WR841N
      - AR5416
      - 2x2
      - 
      - 
      - 
      - 
      - 
      - 
      - 
   - 

      - TP-Link TL-WR841ND
      - AR5416
      - 2x2
      - (./)
      - 
      - (./)
      - 
      - 
      - 
      - 
   - 

      - TRENDnet TEW-632BRP v1.0 & v1.1
      - AR9102
      - 2x2
      - (./)
      - 
      - (./)
      - 
      - 
      - 
      - 
   - 

      - TRENDnet TEW-652BRP
      - AR9102
      - 2x2
      - (./)
      - 
      - (./)
      - 
      - 
      - 
      - 
   - 

      - Unex RNEA-83 (AP83)
      - AR9001AP-2NX (AR9130+AR9104)
      - 2x2
      - 
      - (./)
      - (./)
      - 
      - (./)
      - 
      - 
   - 

      - Unex RNEA-81 (AP83)
      - AR9001AP-2NX (AR9130+AR9104)
      - 2x2
      - 
      - (./)
      - (./)
      - 
      - (./)
      - 
      - 
   - 

      - Unex RPAA-82 (PB44)
      - AR9001AP-3NX2 (AR7161+AR9160+AR9106)
      - 3x3
      - 
      - (./)
      - 
      - (./)
      - 
      - (./)
      - 
   - 

      - Unex RNRA-83 (AP96)
      - AR9002AP-4XHG (AR7161+AR9220+AR9223+AR8316)
      - 2x2
      - 
      - (./)
      - 
      - (./)
      - 
      - (./)
      - (./)
   - 

      - Zyxel NBG-420N
      - AR9102
      - 2x2
      - (./)
      - 
      - (./)
      - 
      - 
      - 
      - 
   - 

      - Zyxel NBG-460N
      - AR9103
      - 3x3
      - (./)
      - 
      - 
      - (./)
      - 
      - 
      - 
   - 

      - Zyxel X550N
      - AR9103
      - 3x3
      - (./)
      - 
      - 
      - (./)
      - 
      - 
      - 
   - 

      - Zyxel X550NH
      - AR9103
      - 3x3
      - (./)
      - 
      - 
      - (./)
      - 
      - 
      - 
