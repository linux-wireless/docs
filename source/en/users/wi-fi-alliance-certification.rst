Certified by Wi-Fi Alliance
===========================

.. list-table::
   :header-rows: 1

   - 

      - Date
      - Vendor
      - Certificate
      - Hardware
      - Driver (version)
      - Certified
   - 

      - September 11, 2019
      - Aeon Matrix Inc.
      - `Yardian Pro <http://certifications.prod.wi-fi.org/pdf/certificate/public/download?cid=WFA91694>`__ PRO1902 (link dead)
      - ?
      - `mt76 <https://github.com/openwrt/mt76/commit/a5f5605f>`__ (pre mainline)
      - 2,4 GHz, 1 Spatial Stream 2.4 GHz, STA, b/g/n, WMM, WPA2/WPA Personal, Short Guard Interval, TX A-MPDU, STBC Receive, 40 MHz operation in 2.4 GHz with coexistence mechanisms
   - 

      - January 14, 2019
      - GARDENA GmbH
      - `GARDENA smart Gateway <https://api.cert.wi-fi.org/api/certificate/download/public?variantId=14914>`__ (Art. 19005)
      - MT7688
      - `mt76 <https://github.com/openwrt/mt76/commit/6203d46fcc4577065209ea0ed9334d89df4f63f7>`__ (pre mainline)
      - 2,4 GHz, 1 Spatial Stream 2.4 GHz, STA, b/g/n, WMM, WPA2/WPA Personal, Short Guard Interval, TX A-MPDU, STBC Receive, 40 MHz operation in 2.4 GHz with coexistence mechanisms, Greenfield Preamble, STAUT Power Management

Work In Progress
================

rtl8xxxu on RTL8188CUS on GARDENA smart gateway
-----------------------------------------------

RealTek provides a GPLed Linux driver named "8192cu" for its RTL8188CUS
hardware. While it has worked `well enough to pass the Wi-Fi Alliance
certification
<https://api.cert.wi-fi.org/api/certificate/download/public?variantId=14856>`__,
the last release `is from 2017
<https://github.com/rettichschnidi/realtek-linux/tree/master/RTL8188C_8192C/USB/v4.0>`__,
its code does not work well with modern kernels (FullMAC, and
notoriously unstable) and does no longer receive any security updates.
Luckily, it has been superseded by TWO mainlined kernel drivers:

- rtl8192cu: Based on the RealTek driver, shoehorned into mainline
  Linux. Suffers from various stability issues and code is close to
  unreadable.
- rtl8xxxu: Written from scratch, :doc:`will replace rtl8192cu
  <drivers/rtl819x>`. It has been shown to to be stable during long-term
  testing. Code is readable. Not (yet) feature equivalent to the 8192cu
  or even the rtl8192cu.

Both, rtl8192cu and rtl8xxxu are worse than 8192cu when it comes to
features and performance.

Given the code quality and stability, it is the goal of GARDENA to
develop the rtl8xxxu driver as far as needed to pass the Wi-Fi Alliance
certification.

A big hurdle is `the lack of sources as well as documentation for the
firmware
<https://blog.linuxplumbersconf.org/2016/ocw/system/presentations/4089/original/2016-11-02-rtl8xxxu-presentation.pdf>`__.
Therefore, digging in the (hard to read) sources of the vendor driver is
needed.

Hardware
~~~~~~~~

- End product: ARMv5, Atmel SAM9G25 based GARDENA smart gateway
  (`sources
  <https://github.com/husqvarnagroup/smart-garden-gateway-public>`__)
- For development: x86_amd64, `Edimax EW-7811UN
  <https://www.edimax.com/edimax/merchandise/merchandise_detail/data/edimax/de/wireless_adapters_n150/ew-7811un/>`__

Progress: Hardware is already on the market, nothing left to do or could
be changed for that matter.

Firmware
~~~~~~~~

All driver development and the verification is getting done with
firmware version 88.2, which is part of linux-wireless `since release
20201118
<https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/commit/rtlwifi?id=2ea86675db1349235e9af0a9d0372b72da4db259>`__.

Before linux-wireless release 20201118, the provided firmware was
version 80.0, which is known to hang on the GARDENA smart gateway as
long-term tests have shown (and on other machines too - Google knows).
Only a cold reset resolved the problem, which is easy to do for an USB
WLAN stick but problematic (human intervention needed) on a embedded
device that has no hardware reset capabilities for the USB device.

Driver development
~~~~~~~~~~~~~~~~~~

Setup
^^^^^

Reto
''''

- AP: various (mainly Linksys WRT3200ACM with TA 00:60:6e:00:07:7d, BS 24:f5:a2:c0:4e:b1, SSID "customer-wifi")
- STAs:

   - Thinkpad T420/Edimax EW-7811UN (08:be:ac:0b:14:c4; amd64)
   - GARDENA smart gateways (various MAC addresses; ARMv5)

- Capturing device: Asus PCE-AX58BT (Intel AX200)
- iperf3 host: Workstation with IPv4 address 10.42.0.1
- Distance: Variable, but generally close (1-3m distance)
- Environment: Residual area; not clean/standardized, but using a (seemingly) non-crowded channel (12)

Chris
'''''

- AP: Dlink DIR-612 (2x2) SSID: CHT57196 with BSSID: 18:0f:76:c5:0a:ea
- STA: rtl8xxxu running on Edimax EW-7811UN (amd64)
- Distance: fixed to 3m and 6m for experiment
- Environment: use less-noisy channel 9 in a 8x9 square meters area which only have 1 router.

Baseline
^^^^^^^^

The rtl8xxxu driver performance (throughput) gets compared to the latest
vendor driver release (8192cu), which has been patched to work on recent
Linux versions (5.10+):
https://github.com/husqvarnagroup/8192cu_rtl8188cus

Progress
^^^^^^^^

.. list-table::
   :header-rows: 1

   - 

      - Priority
      - Task
      - Wi-Fi Alliance Test Case
      - State
      - Optional
   - 

      - 1
      - ACK #1: Fix Block ACKs to include (ack) recently sent frames
      - n/a (but a prerequisite)
      - WIP
      - n
   - 

      - 2
      - ACK #2: Fix regular ACKs to work also with non-MCS2 packets
      - n/a (but a prerequisite)
      - WIP
      - n
   - 

      - unknown
      - Allow setting TX power limit via iw
      - none, but needed for EMC
      - implemented, needs to be verified by GARDENA
      - n
   - 

      - unknown
      - TX Power: power by rate.
      - none, but maybe required for EMC
      - not yet implemented
      - n
   - 

      - unknown
      - A-MSDU (RX support)
      - 5.2.38
      - not yet implemented
      - n
   - 

      - unknown
      - WMM: Wi-Fi Multimedia
      - many
      - not yet implemented
      - n (but ASD?)
   - 

      - unknown
      - 802.11n: STBC Receive
      - 5.2.46
      - implemented, needs to be verified
      - n
   - 

      - unknown
      - A-MPDU: #1. Handle ampdu_action properly on TX. Ex.ADDBA, DELBA, BAR
      - 5.2.47
      - implemented, needs to be verified
      - n
   - 

      - unknown
      - A-MPDU: #2. Make sure BAR to be handled correctly on RX
      - 5.2.47
      - not yet implemented
      - n
   - 

      - unknown
      - iw station dump: "tx bitrate: (unknown)" (n/a)
      - n/a
      - fixed
      - y
   - 

      - unknown
      - iw output: "Available Antennas: TX 0 RX 0" (n/a)
      - n/a
      - fixed
      - y
   - 

      - unknown
      - Reach MCS5 ~ MCS7 rate under rate control
      - n/a
      - not yet implemented
      - y
   - 

      - unknown
      - Protected Management Frames (For WPA3 support)
      - unknown
      - not yet implemented, HW support unknown (RTL8188CUS)
      - y
   - 

      - unknown
      - CRDA + RegDB support: Static TX power limit, global
      - unknown
      - not yet implemented
      - y
   - 

      - unknown
      - CRDA + RegDB support: Country support (implement regd_notifier())
      - unknown
      - not yet implemented
      - y
   - 

      - none
      - Greenfield mode
      - 5.2.41 (no longer existing)
      - not yet implemented
      - y
   - 

      - unknown
      - Regulatory domain: Hook the TX power set/get of the cfg80211 to the driver
      - none
      - not yet implemented
      - y
   - 

      - none
      - Firmware upload failure
      - n/a
      - not yet fixed
      - y
   - 

      - none
      - RX IQK failed
      - n/a
      - not yet fixed
      - y

ACK #1: Fix Block ACKs to include (ack) recently sent frames
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

rtl8xxxu: During block ACK sessions, the STA does not ACK frames sent by
the AP in time, causing the AP to resend them. It is unknown whether the
frames have not been properly received by the STA or if the STA is
"just" too slow to ACK them in time.

This results in retransmission percentages of 10-50%. While still
yielding usable performance (10-40 MBit/s), this percentage is too high
for passing the Wi-Fi Alliance certification.

8192cu: ACK-ing all sent frames in time, resulting in only 1-2%
retransmitted frames and great performance (35+ MBit/s).

Firmware upload failure
'''''''''''''''''''''''

The following error happens frequently on Reto's machine, but does not
happen on the GARDENA smart gateway::

   kernel: usb 1-1.5.4: new high-speed USB device number 8 using ehci-pci
   kernel: usb 1-1.5.4: New USB device found, idVendor=7392, idProduct=7811, bcdDevice= 2.00
   kernel: usb 1-1.5.4: New USB device strings: Mfr=1, Product=2, SerialNumber=3
   kernel: usb 1-1.5.4: Product: 802.11n WLAN Adapter
   kernel: usb 1-1.5.4: Manufacturer: Realtek
   kernel: usb 1-1.5.4: SerialNumber: 00e04c000001
   kernel: usb 1-1.5.4: Vendor: Realtek
   kernel: usb 1-1.5.4: Product: 802.11n WLAN Adapter
   kernel: usb 1-1.5.4: rtl8192cu_parse_efuse: dumping efuse (0x80 bytes):
   kernel: usb 1-1.5.4: 00: 29 81 00 74 cd 00 00 00
   kernel: usb 1-1.5.4: 08: ff 00 92 73 11 78 03 41
   kernel: usb 1-1.5.4: 10: 32 00 85 62 9e ad 08 be
   kernel: usb 1-1.5.4: 18: ac 0b 14 c4 0a 03 52 65
   kernel: usb 1-1.5.4: 20: 61 6c 74 65 6b 00 16 03
   kernel: usb 1-1.5.4: 28: 38 30 32 2e 31 31 6e 20
   kernel: usb 1-1.5.4: 30: 57 4c 41 4e 20 41 64 61
   kernel: usb 1-1.5.4: 38: 70 74 65 72 00 00 00 00
   kernel: usb 1-1.5.4: 40: 00 00 00 00 00 00 00 00
   kernel: usb 1-1.5.4: 48: 00 00 00 00 00 00 00 00
   kernel: usb 1-1.5.4: 50: 00 00 00 00 00 00 00 00
   kernel: usb 1-1.5.4: 58: 06 00 27 27 27 00 00 00
   kernel: usb 1-1.5.4: 60: 29 29 29 00 00 00 00 00
   kernel: usb 1-1.5.4: 68: 00 00 00 00 11 11 33 00
   kernel: usb 1-1.5.4: 70: 00 00 00 00 00 02 00 00
   kernel: usb 1-1.5.4: 78: 0f 00 00 00 36 00 00 00
   kernel: usb 1-1.5.4: RTL8188CU rev A (TSMC) 1T1R, TX queues 2, WiFi=1, BT=0, GPS=0, HI PA=0
   kernel: usb 1-1.5.4: RTL8188CU MAC: 08:be:ac:0b:14:c4
   kernel: usb 1-1.5.4: rtl8xxxu: Loading firmware rtlwifi/rtl8192cufw_TMSC.bin
   kernel: usb 1-1.5.4: Firmware revision 88.2 (signature 0x88c1)
   kernel: usb 1-1.5.4: rtl8xxxu_writeN: Failed to write block at addr: 1c00 size: 0080
   kernel: rtl8xxxu: probe of 1-1.5.4:1.0 failed with error -11

[STRIKEOUT:Unsure if this is a common issue.] Seems hardware specific - USB dongle probably broken.

RX IQK failed
'''''''''''''

The following error happens frequently on Reto's machine, but does not
happen on the GARDENA smart gateway::

   kernel: usb 1-1.5.4: Vendor: Realtek
   kernel: usb 1-1.5.4: Product: 802.11n WLAN Adapter
   kernel: usb 1-1.5.4: rtl8192cu_parse_efuse: dumping efuse (0x80 bytes):
   kernel: usb 1-1.5.4: 00: 29 81 00 74 cd 00 00 00
   kernel: usb 1-1.5.4: 08: ff 00 92 73 11 78 03 41
   kernel: usb 1-1.5.4: 10: 32 00 85 62 9e ad 08 be
   kernel: usb 1-1.5.4: 18: ac 0b 14 c4 0a 03 52 65
   kernel: usb 1-1.5.4: 20: 61 6c 74 65 6b 00 16 03
   kernel: usb 1-1.5.4: 28: 38 30 32 2e 31 31 6e 20
   kernel: usb 1-1.5.4: 30: 57 4c 41 4e 20 41 64 61
   kernel: usb 1-1.5.4: 38: 70 74 65 72 00 00 00 00
   kernel: usb 1-1.5.4: 40: 00 00 00 00 00 00 00 00
   kernel: usb 1-1.5.4: 48: 00 00 00 00 00 00 00 00
   kernel: usb 1-1.5.4: 50: 00 00 00 00 00 00 00 00
   kernel: usb 1-1.5.4: 58: 06 00 27 27 27 00 00 00
   kernel: usb 1-1.5.4: 60: 29 29 29 00 00 00 00 00
   kernel: usb 1-1.5.4: 68: 00 00 00 00 11 11 33 00
   kernel: usb 1-1.5.4: 70: 00 00 00 00 00 02 00 00
   kernel: usb 1-1.5.4: 78: 0f 00 00 00 36 00 00 00
   kernel: usb 1-1.5.4: RTL8188CU rev A (TSMC) 1T1R, TX queues 2, WiFi=1, BT=0, GPS=0, HI PA=0
   kernel: usb 1-1.5.4: RTL8188CU MAC: 08:be:ac:0b:14:c4
   kernel: usb 1-1.5.4: rtl8xxxu: Loading firmware rtlwifi/rtl8192cufw_TMSC.bin
   kernel: usb 1-1.5.4: Firmware revision 88.2 (signature 0x88c1)
   kernel: usb 1-1.5.4: rtl8xxxu_iqk_path_a: Path A RX IQK failed!
   kernel: usb 1-1.5.4: rtl8xxxu_iqk_path_a: Path A RX IQK failed!
   kernel: usbcore: registered new interface driver rtl8xxxu

[STRIKEOUT:Unsure if this is a common issue.] Seems hardware specific - USB dongle probably broken.

Patches
^^^^^^^

.. list-table::
   :header-rows: 1

   - 

      - Number
      - Description
      - Link
      - Testing results (Reto)
      - Upstream State
   - 

      - 1
      - Handle BSS_CHANGED_TXPOWER/IEEE80211_CONF_CHANGE_POWER
      - https://github.com/husqvarnagroup/linux/commit/798796ff5070255a7cccc7529c272b629da79d7b
      - 
      - 
   - 

      - 2
      - Handle for mac80211 get_txpower
      - https://github.com/husqvarnagroup/linux/commit/5df123ce78422b76603eedf799fc50f5e3303011
      - 
      - 
   - 

      - 3
      - Enable RX STBC by default
      - https://github.com/husqvarnagroup/linux/commit/4efe4bf653a14b61ff9b3969050bc696976415eb
      - 
      - 
   - 

      - 4
      - Feed antenna information for mac80211
      - https://github.com/husqvarnagroup/linux/commit/070d0eca2dbe8086a215c33f6d3ee10cfe9a17cc
      - 
      - 
   - 

      - 5
      - Fill up txrate info for all chips
      - https://github.com/husqvarnagroup/linux/commit/fa14d07da5566c8abebccd68473ddc17e908be45
      - 
      - 
   - 

      - 6
      - Fix the reported rx signal strength
      - https://github.com/husqvarnagroup/linux/commit/95f19fff95a62ab67ecc50d75e8c59669f936bd2
      - 
      - 
   - 

      - 7
      - Fix the handling of TX A-MPDU aggregation
      - https://lore.kernel.org/linux-wireless/20210804151325.86600-1-chris.chiu@canonical.com/
      - GARDENA gateway: Improves TX throughput, but worsens retry percentage; Reverse issue for RX.
      - Merged
   - 

      - 8
      - Improve the retransmission rate with HW_RTS enable
      - https://github.com/husqvarnagroup/linux/commit/31a00cbf0245877e9a98cdec6903758a928482e5
      - GARDENA gateway: Neither throughput nor retry percentage improved
      - 
   - 

      - 9
      - Set RTS rate to 24M for AMPDU
      - https://github.com/husqvarnagroup/linux/commit/b35338e600b003f830c4533c162a53c57d9d34d2
      - GARDENA gateway: No positive effects observable
      - will not be upstreamed
   - 

      - 10
      - Reduce number of USB interrupts
      - https://lore.kernel.org/linux-wireless/d32690a6-f679-c676-1461-10b47ae3428b@gmail.com/
      - GARDENA gateway: Clearly improves throughput and retries
      - Merged
   - 

      - 11
      - Use lower tx rates for the ack packet
      - https://lore.kernel.org/linux-wireless/20211001040044.1028708-1-chris.chiu@canonical.com/
      - GARDENA gateway: Neither throughput nor retry percentage improved
      - Merged

Driver Testing
~~~~~~~~~~~~~~

Reto
^^^^

Setup
'''''

#. Blacklist all drivers (rlt8xxxu, 8192cu, rtl8192cu)
#. Ensure no drivers are loaded
#. Load driver to be tested (rlt8xxxu, 8192cu, rtl8192cu) with insmod
#. Start 802.11 capture
#. Start wpa_supplicant on DUT
#. Once IP address got assigned, measure the performance using iperf3:

   - TCP TX Throughput: ``iperf3 -c 10.42.0.1``
   - TCP RX Throughput: ``iperf3 -c --reverse 10.42.0.1``

Repos
'''''

- Linux: https://github.com/husqvarnagroup/linux
- 8192cu: https://github.com/husqvarnagroup/realtek-8192cu_rtl8188cus

Analysis
''''''''

- The throughput values are the ones reported by iperf3 (the lower value if server/client values differ)
- The retry values are taken from Wireshark in menu "Wireless" -> "WLAN Traffic"

TCP TX Throughput
'''''''''''''''''

.. list-table::
   :header-rows: 1

   - 

      - DUT
      - AP
      - Driver
      - Throughput [Mbits/sec]; retries [%]
      - AP <-> DUT
      - Notes
      - PCAP
   - 

      - amd64, Edimax
      - Linksys
      - Linux v5.10.51, rtl8xxxu (vanilla)
      - 30.6 Mbits/s; 12%
      - 2m, two monitors in line of sight
      - Many "ghost MAC addresses"
      - https://files.reto-schneider.ch/rtl8xxxu/2021-07-23-Testing/2021-07-23-1-Linux-5.10.51-2021-07-22-vanilla-rtl8xxxu-edimax-08:be:ac:0b:14:c4-iperf-tx-tcp-12%25-retries-at-30.6MBps.pcapng.gz
   - 

      - amd64, Edimax
      - Linksys
      - Linux v5.10.51, rtl8xxxu (vanilla)
      - 13.1 Mbits/s; 3%
      - 2m, two monitors in line of sight
      - Many "ghost MAC addresses"; unexplained performance/retry drop
      - https://files.reto-schneider.ch/rtl8xxxu/2021-07-23-Testing/2021-07-23-3-Linux-5.10.51-2021-07-22-vanilla-rtl8xxxu-edimax-08:be:ac:0b:14:c4-iperf-tx-tcp-3%25-retries-at-13.1MBps.pcapng.gz
   - 

      - amd64, Edimax
      - Linksys
      - Linux v5.10.51, 8192cu (tag rs/2021-07-23)
      - 4.02 Mbits/s; 17.2%
      - 2m, two monitors in line of sight
      - No "ghost MAC addresses"; Surprisingly bad performance
      - https://files.reto-schneider.ch/rtl8xxxu/2021-07-23-Testing/2021-07-23-5-Linux-5.10.51-2021-07-22-8192cu-edimax-08:be:ac:0b:14:c4-iperf-tx-tcp-16%25-retries-at-4.02MBps.pcapng.gz
   - 

      - amd64, Edimax
      - Linksys
      - Linux v5.10.51, 8192cu (tag rs/2021-07-23)
      - 3.91 Mbits/s; 18.8%
      - 2m, two monitors in line of sight
      - No "ghost MAC addresses"; Surprisingly bad performance
      - https://files.reto-schneider.ch/rtl8xxxu/2021-07-23-Testing/2021-07-23-6-Linux-5.10.51-2021-07-22-8192cu-edimax-08:be:ac:0b:14:c4-iperf-tx-tcp-18%25-retries-at-3.91MBps.pcapng.gz
   - 

      - amd64, Edimax
      - Linksys
      - Linux v5.10.51, 8192cu (tag rs/2021-07-23)
      - 49.7 Mbits/s; 4.8%
      - 1m, direct line of sight
      - Some "ghost MAC addresses"
      - https://files.reto-schneider.ch/rtl8xxxu/2021-07-23-Testing/2021-07-23-8-Linux-5.10.51-2021-07-22-8192cu-edimax-08:be:ac:0b:14:c4-iperf-tx-tcp-4.8%25-retries-at-49.7MBps.pcapng.gz
   - 

      - amd64, Edimax
      - Linksys
      - Linux v5.10.51, rtl8xxxu (vanilla)
      - 45.7 Mbits/s; 9.4%
      - 1m, direct line of sigh
      - No "ghost MAC addresses"
      - https://files.reto-schneider.ch/rtl8xxxu/2021-07-23-Testing/2021-07-23-10-Linux-5.10.51-2021-07-22-vanilla-rtl8xxxu-edimax-08:be:ac:0b:14:c4-iperf-tx-tcp-9.4%25-retries-at-45.7MBps.pcapng.gz
   - 

      - ARMv5, GARDENA smart Gateway (00:1d:43:c0:19:8a)
      - Linksys
      - Linux v5.10.52, 8192cu (tag rs/2021-07-23)
      - 30.6 Mbits/s; 0.9%
      - 1m, direct line of sigh
      - Some "ghost MAC addresses"; This is the kind of performance wanted
      - `https://files.reto-schneider.ch/rtl8xxxu/2021-07-24-Testing/2021-07-24-3-Linux-5.10.52-8192cu-gateway-00:1d:43:c0:19:8a-iperf-tx-tcp-0.9%-retries-at-30.6MBps.pcapng.gz <https://files.reto-schneider.ch/rtl8xxxu/2021-07-24-Testing/2021-07-24-3-Linux-5.10.52-8192cu-gateway-00:1d:43:c0:19:8a-iperf-tx-tcp-0.9%-retries-at-30.6MBps.pcapng.gz>`__
   - 

      - ARMv5, GARDENA smart Gateway (00:1d:43:c0:19:8a)
      - Linksys
      - Linux v5.10.52, 8192cu (tag rs/2021-07-23)
      - 42.5 Mbits/s; 2.4%
      - 1m, direct line of sigh
      - Some "ghost MAC addresses"; This is the kind of performance wanted
      - `https://files.reto-schneider.ch/rtl8xxxu/2021-07-24-Testing/2021-07-24-4-Linux-5.10.52-8192cu-gateway-00:1d:43:c0:19:8a-iperf-tx-tcp-2.4%-retries-at-42.5MBps.pcapng.gz <https://files.reto-schneider.ch/rtl8xxxu/2021-07-24-Testing/2021-07-24-4-Linux-5.10.52-8192cu-gateway-00:1d:43:c0:19:8a-iperf-tx-tcp-2.4%-retries-at-42.5MBps.pcapng.gz>`__
   - 

      - ARMv5, GARDENA smart Gateway (00:1d:43:c0:19:8a)
      - Linksys
      - Linux v5.10.52, rtl8xxxu (vanilla)
      - 12.5 Mbits/s; 17%
      - 1m, direct line of sigh
      - Many "ghost MAC addresses"
      - `https://files.reto-schneider.ch/rtl8xxxu/2021-07-24-Testing/2021-07-24-1-Linux-5.10.52-vanilla-rtl8xxxu-gateway-00:1d:43:c0:19:8a-iperf-tx-tcp-17%-retries-at-12.5MBps.pcapng.gz <https://files.reto-schneider.ch/rtl8xxxu/2021-07-24-Testing/2021-07-24-1-Linux-5.10.52-vanilla-rtl8xxxu-gateway-00:1d:43:c0:19:8a-iperf-tx-tcp-17%-retries-at-12.5MBps.pcapng.gz>`__
   - 

      - ARMv5, GARDENA smart Gateway (00:1d:43:c0:19:8a)
      - Linksys
      - Linux v5.10.52, rtl8xxxu (patch 10; tag gardena/rs/v5.10.52-rtl8xxxu-writeup-1-reduce-usb-interrupt-v1)
      - 20.6 Mbits/s; 12%
      - 1m, direct line of sigh
      - Few(er) "ghost MAC addresses"; Clear improvement over vanilla
      - `https://files.reto-schneider.ch/rtl8xxxu/2021-07-24-Testing/2021-07-24-9-Linux-5.10.52-rtl8xxxu-1-usb-interrupt-reduction-gateway-00:1d:43:c0:19:8a-iperf-tx-tcp-12.0%-retries-at-20.6MBps.pcapng.gz <https://files.reto-schneider.ch/rtl8xxxu/2021-07-24-Testing/2021-07-24-9-Linux-5.10.52-rtl8xxxu-1-usb-interrupt-reduction-gateway-00:1d:43:c0:19:8a-iperf-tx-tcp-12.0%-retries-at-20.6MBps.pcapng.gz>`__
   - 

      - ARMv5, GARDENA smart Gateway (00:1d:43:c0:19:8a)
      - Linksys
      - Linux v5.10.52, rtl8xxxu (patches 10, 7; gardena/rs/v5.10.52-rtl8xxxu-writeup-3-tx-apdu-aggregation-v1)
      - 24.3 Mbits/s; 39.9%
      - 1m, direct line of sigh
      - Tons of "ghost MAC addresses"; Performance improved, but \*terrible\* retry rate
      - https://files.reto-schneider.ch/rtl8xxxu/2021-07-27-Testing/2021-07-27-1-Linux-5.10.52-rtl8xxxu-3-tx-apdu-aggregation-gateway-00:1d:43:c0:19:8a-iperf-tx-tcp-39.9%25-retries-at-24.3MBps.pcapng.gz
   - 

      - ARMv5, GARDENA smart Gateway (00:1d:43:c0:19:8a)
      - Linksys
      - Linux v5.10.52, rtl8xxxu (patches 10, 8; tag gardena/rs/v5.10.52-rtl8xxxu-writeup-4-hw-rts-v1)
      - 15.2 Mbits/s; 17.7%
      - 1m, direct line of sigh
      - Few "ghost MAC addresses"; Throughout and retry percentage worsened
      - https://files.reto-schneider.ch/rtl8xxxu/2021-07-27-Testing/2021-07-27-3-Linux-5.10.52-rtl8xxxu-writeup-4-hw-rts-gateway-00:1d:43:c0:19:8a-iperf-tx-tcp-17.7%25-retries-at-15.2MBps.pcapng.gz
   - 

      - ARMv5, GARDENA smart Gateway (00:1d:43:c0:19:8a)
      - Linksys
      - Linux v5.10.52, rtl8xxxu (patches 10, 8, 7; tag gardena/rs/v5.10.52-rtl8xxxu-writeup-5-ampdu-v1)
      - 20.8 Mbits/s; 46.5%
      - 1m, direct line of sigh
      - Many "ghost MAC addresses"; Terrible retry performance; Patch 9 does not change this.
      - https://files.reto-schneider.ch/rtl8xxxu/2021-07-27-Testing/2021-07-27-5-Linux-5.10.52-rtl8xxxu-writeup-5-ampdu-v1-gateway-00:1d:43:c0:19:8a-iperf-tx-tcp-46.5%25-retries-at-20.8MBps.pcapng.gz

TCP RX Throughput
'''''''''''''''''

.. list-table::
   :header-rows: 1

   - 

      - DUT
      - AP
      - Driver
      - Throughput [Mbits/sec]; retries [%]
      - AP <-> DUT
      - Notes
      - PCAP
   - 

      - amd64, Edimax
      - Linksys
      - Linux v5.10.51, rtl8xxxu (vanilla)
      - 38.9 Mbits/s; 16%
      - 2m, two monitors in line of sight
      - Many "ghost MAC addresses"
      - https://files.reto-schneider.ch/rtl8xxxu/2021-07-23-Testing/2021-07-23-2-Linux-5.10.51-2021-07-22-vanilla-rtl8xxxu-edimax-08:be:ac:0b:14:c4-iperf-rx-tcp-16%25-retries-at-37.2MBps.pcapng.gz
   - 

      - amd64, Edimax
      - Linksys
      - Linux v5.10.51, rtl8xxxu (vanilla)
      - 41.7 Mbits/s; 15.6%
      - 2m, two monitors in line of sight
      - Many "ghost MAC addresses"
      - https://files.reto-schneider.ch/rtl8xxxu/2021-07-23-Testing/2021-07-23-4-Linux-5.10.51-2021-07-22-vanilla-rtl8xxxu-edimax-08:be:ac:0b:14:c4-iperf-rx-tcp-15.6%25-retries-at-41.7MBps.pcapng.gz
   - 

      - amd64, Edimax
      - Linksys
      - Linux v5.10.51, 8192cu (tag rs/2021-07-23)
      - 41.8 Mbits/s; 10%
      - 2m, two monitors in line of sight
      - Many "ghost MAC addresses"
      - https://files.reto-schneider.ch/rtl8xxxu/2021-07-23-Testing/2021-07-23-7-Linux-5.10.51-2021-07-22-8192cu-edimax-08:be:ac:0b:14:c4-iperf-rx-tcp-10%25-retries-at-41.4MBps.pcapng.gz
   - 

      - amd64, Edimax
      - Linksys
      - Linux v5.10.51, 8192cu (tag rs/2021-07-23)
      - 49.7 Mbits/s; 9.9%
      - 1m, direct line of sight
      - Many "ghost MAC addresses"
      - https://files.reto-schneider.ch/rtl8xxxu/2021-07-23-Testing/2021-07-23-9-Linux-5.10.51-2021-07-22-8192cu-edimax-08:be:ac:0b:14:c4-iperf-rx-tcp-4.8%25-retries-at-49.7MBps.pcapng.gz
   - 

      - amd64, Edimax
      - Linksys
      - Linux v5.10.51, rtl8xxxu (vanilla)
      - 47.5 Mbits/s; 10.8%
      - 1m, direct line of sight
      - Many "ghost MAC addresses"
      - https://files.reto-schneider.ch/rtl8xxxu/2021-07-23-Testing/2021-07-23-11-Linux-5.10.51-2021-07-22-vanilla-rtl8xxxu-edimax-08:be:ac:0b:14:c4-iperf-rx-tcp-10.9%25-retries-at-47.5MBps.pcapng.gz
   - 

      - ARMv5, GARDENA smart Gateway (00:1d:43:c0:19:8a)
      - Linksys
      - Linux v5.10.52, 8192cu (tag rs/2021-07-23)
      - 47.3 Mbits/s; 0.2%
      - 1m, direct line of sigh
      - Zero "ghost MAC addresses"; This is the kind of performance wanted.
      - `https://files.reto-schneider.ch/rtl8xxxu/2021-07-24-Testing/2021-07-24-5-Linux-5.10.52-8192cu-gateway-00:1d:43:c0:19:8a-iperf-rx-tcp-0.2%-retries-at-47.3MBps.pcapng.gz <https://files.reto-schneider.ch/rtl8xxxu/2021-07-24-Testing/2021-07-24-5-Linux-5.10.52-8192cu-gateway-00:1d:43:c0:19:8a-iperf-rx-tcp-0.2%-retries-at-47.3MBps.pcapng.gz>`__
   - 

      - ARMv5, GARDENA smart Gateway (00:1d:43:c0:19:8a)
      - Linksys
      - Linux v5.10.52, rtl8xxxu (vanilla)
      - 24.4 Mbits/s; 28.2%
      - 1m, direct line of sigh
      - Many "ghost MAC addresses"; This performance needs to be optimized
      - https://files.reto-schneider.ch/rtl8xxxu/2021-07-24-Testing/2021-07-24-7-Linux-5.10.52-vanilla-rtl8xxxu-gateway-00:1d:43:c0:19:8a-iperf-rx-tcp-28.2%25-retries-at-24.4MBps.pcapng.gz
   - 

      - ARMv5, GARDENA smart Gateway (00:1d:43:c0:19:8a)
      - Linksys
      - Linux v5.10.52, rtl8xxxu (patch 10)
      - 33.1 Mbits/s; 27%
      - 1m, direct line of sigh
      - Many "ghost MAC addresses"; Slight improvement thanks to patch #10
      - `https://files.reto-schneider.ch/rtl8xxxu/2021-07-24-Testing/2021-07-24-10-Linux-5.10.52-rtl8xxxu-1-usb-interrupt-reduction-gateway-00:1d:43:c0:19:8a-iperf-rx-tcp-27%-retries-at-33.1MBps.pcapng.gz <https://files.reto-schneider.ch/rtl8xxxu/2021-07-24-Testing/2021-07-24-10-Linux-5.10.52-rtl8xxxu-1-usb-interrupt-reduction-gateway-00:1d:43:c0:19:8a-iperf-rx-tcp-27%-retries-at-33.1MBps.pcapng.gz>`__
   - 

      - ARMv5, GARDENA smart Gateway (00:1d:43:c0:19:8a)
      - Linksys
      - Linux v5.10.52, rtl8xxxu (patches 10, 7)
      - 12.4 Mbits/s; 22.3%
      - 1m, direct line of sigh
      - Very few "ghost MAC addresses"; Slightly improved retry rate, but terrible throughput
      - https://files.reto-schneider.ch/rtl8xxxu/2021-07-27-Testing/2021-07-27-2-Linux-5.10.52-rtl8xxxu-3-tx-apdu-aggregation-gateway-00:1d:43:c0:19:8a-iperf-rx-tcp-22.3%25-retries-at-12.4MBps.pcapng.gz
   - 

      - ARMv5, GARDENA smart Gateway (00:1d:43:c0:19:8a)
      - Linksys
      - Linux v5.10.52, rtl8xxxu (patches 10, 8)
      - 32.8 Mbits/s; 25.9%
      - 1m, direct line of sigh
      - No "ghost MAC addresses"; Retry percentage slightly improved
      - https://files.reto-schneider.ch/rtl8xxxu/2021-07-27-Testing/2021-07-27-4-Linux-5.10.52-rtl8xxxu-writeup-4-hw-rts-gateway-00:1d:43:c0:19:8a-iperf-rx-tcp-25.9%25-retries-at-32.8MBps.pcapng.gz
   - 

      - ARMv5, GARDENA smart Gateway (00:1d:43:c0:19:8a)
      - Linksys
      - Linux v5.10.52, rtl8xxxu (patches 10, 8, 7)
      - 8.29 Mbits/s; 26.5%
      - 1m, direct line of sigh
      - Terrible overall performance. Patch 9 does not change this.
      - https://files.reto-schneider.ch/rtl8xxxu/2021-07-27-Testing/2021-07-27-6-Linux-5.10.52-rtl8xxxu-writeup-5-ampdu-v1-gateway-00:1d:43:c0:19:8a-iperf-rx-tcp-26.5%25-retries-at-8.29MBps.pcapng.gz

Chris
^^^^^

Setup
'''''

#. Blacklist all drivers (rlt8xxxu, 8192cu, rtl8192cu)
#. Ensure no drivers are loaded
#. Load driver to be tested (rlt8xxxu, 8192cu) with insmod
#. Start 802.11 capture
#. Once IP address got assigned, measure the performance using iperf3:

   - TCP TX Throughput: ``iperf3 -c 192.168.0.11 -t 30 -i 1``
   - TCP RX Throughput: ``iperf3 -c --reverse 192.168.0.11 -t 30 -i 1``

Repos
'''''

- Linux: https://github.com/mschiu77/linux/tree/chris/ampdu_action
- 8192cu: https://github.com/mschiu77/rtl8188cus_vendor

Analysis
''''''''

- The throughput values are the ones reported by iperf3 (the lower value if server/client values differ)
- The retry values are taken from Wireshark in menu "Wireless" -> "WLAN Traffic"

TCP TX Throughput
'''''''''''''''''

.. list-table::
   :header-rows: 1

   - 

      - DUT
      - AP
      - Driver
      - Throughput [Mbits/sec]; retries [%]
      - AP <-> DUT
      - Notes
      - PCAP
   - 

      - amd64, Edimax
      - DLink
      - Linux v5.13.1 rtl8xxxu
      - 23~27 Mbits/s; 12~14%
      - 3m, direct line of sight
      - performance drop for a few seconds
      - https://mega.nz/folder/LI0ATTAK#0E2J5DHksD1jQi1oJCOJWg
   - 

      - amd64, Edimax
      - DLink
      - Linux v5.13.1 rtl8xxxu
      - 7-14 Mbits/s; 16~20%
      - 6m, direct line of sight
      - performance drop to 0 sometimes
      - https://mega.nz/folder/vMdgADRD#XHljNHbzzlp63qqFsT-rkQ
   - 

      - amd64, Edimax
      - DLink
      - Linux v5.12, 8192cu (https://github.com/mschiu77/rtl8188cus_vendor.git master)
      - 40~42 Mbits/s; 9%
      - 3m, direct line of sight
      - steady performance
      - https://mega.nz/folder/GAcwnDjY#Xf9lVMriWcPpIUACjuZiqg
   - 

      - amd64, Edimax
      - DLink
      - Linux v5.12, 8192cu ((https://github.com/mschiu77/rtl8188cus_vendor.git master)
      - 13-16 Mbits/s; 20~23%
      - 6m, direct line of sight
      - steady throughput w/o sudden drop
      - https://mega.nz/folder/HZ8iQRqY#2ss6WW9u6oxInJvT2R6iCw

.. _tcp-rx-throughput-1:

TCP RX Throughput
'''''''''''''''''

.. list-table::
   :header-rows: 1

   - 

      - DUT
      - AP
      - Driver
      - Throughput [Mbits/sec]; retries [%]
      - AP <-> DUT
      - Notes
      - PCAP
   - 

      - amd64, Edimax
      - DLink
      - Linux v5.13.1 rtl8xxxu
      - 36 Mbits/s; 12%
      - 3m, direct line of sight
      - performance is stable high
      - https://mega.nz/folder/3Zs0nDrK#i1fnW6Bp5E_jeC3dcPlWaw
   - 

      - amd64, Edimax
      - DLink
      - Linux v5.13.1 rtl8xxxu
      - 16 Mbits/s; 30%
      - 6m, direct line of sight
      - performance is stably low
      - https://mega.nz/folder/TcsQAZoI#VbQiPZF1B7EJK1_82x2kOg
   - 

      - amd64, Edimax
      - DLink
      - Linux v5.12, 8192cu
      - 35 Mbits/s; 10%
      - 3m, direct line of sight
      - performance is stable high
      - https://mega.nz/folder/KIsmCBRR#rN9X9sXrdLo7It8qj8PQgQ
   - 

      - amd64, Edimax
      - DLink
      - Linux v5.12, 8192cu
      - 20 Mbits/s; 11%
      - 6m, direct line of sight
      - performance and retry are better than rtl8xxxu
      - https://mega.nz/folder/2Q1WBJqS#6dU1pQ9OXbveETqlfQcZ2w

Observations
~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   - 

      - Criterion
      - rtl8xxxu
      - rtl8192cu
      - 8192cu
      - Comment
   - 

      - wlan.frag != 1
      - rarely
      - often
      - never
      - Maybe a side-effect of failed transfers. Never sent by AP.
   - 

      - Block ACK Initiator
      - STA, then AP
      - AP, then AP
      - AP, then STA
      - 
   - 

      - Block ACK Starting Sequence Control
      - oldest possible sequence #
      - 
      - first non-acked sequence #
      - Should be benign, see https://gjermundraaen.com/2021/03/29/802-11-compressed-blockack-two-different-behaviors/
   - 

      - A-MSDU
      - Permitted when ADDBA initiated by STA, not when by AP
      - alway permitted
      - never permitted
      - 
   - 

      - Block ACK Timeout [1024 us]
      - 0x0 (disabled)
      - 0x1388
      - 0x1388
      - 
   - 

      - wlan.qos.amsdupresent == 1
      - some
      - 
      - 
      - 

Register Comparison
~~~~~~~~~~~~~~~~~~~

Reto
^^^^

- Issue: When using the rtl8xxxu driver, the communication has a much higher retransmission rate (20%) than with the other drivers (8192cu: < 5%, rtl8192cu: < 7.5%). Mainly, because the DUT fails to send ACKs in time, causing the AP to resend many frames. Issue can be seen best in the RX traces (iperf3 receiving data from the AP).
- Traces: https://files.reto-schneider.ch/diesunddas/rtl8xxxu/2021-11-09-Testing/t420-2021-11-09T05:20:20+01:00/
- Please note: Only differentiating registers and their values are shown. Whenever additional information about bits/bitmasks is available, those are printed too.

RF Register
'''''''''''

.. list-table::
   :header-rows: 1

   - 

      - Driver
      - Source
      - Filename
   - 

      - 8192cu
      - debugfs
      - 8192cu-gardena-rs-dump-registers-v0.ko-74:da:38:0e:49:7d-rx-rf_reg_dump-05-iperf-done
   - 

      - rtl8192cu
      - debugfs
      - rtl8192cu-gardena-rs-v5.10.69-dump-registers-v13-10-g1f3acbbe2d2a.ko-74:da:38:0e:49:7d-rx-rf_reg_dump-05-iperf-done
   - 

      - rtl8xxxu
      - debugfs
      - rtl8xxxu-gardena-rs-v5.10.69-dump-registers-v13-10-g1f3acbbe2d2a.ko-74:da:38:0e:49:7d-rx-rf_reg_dump-05-iperf-done

.. list-table::
   :header-rows: 1

   - 

      - Address
      - Mask
      - Name
      - #0: 8192cu
      - #1: rtl8192cu
      - #2: rtl8xxxu
      - Hint
   - 

      - 0x0000
      - 0xFF
      - AC
      - 0xB2
      - 0x36
      - 0x16
      - 
   - 

      - 
      - 0x4
      - ACM_HW_CTRL_VI
      - 0x0
      - 0x1
      - 0x1
      - 
   - 

      - 0x0001
      - 0xFF
      - IQADJ_G1
      - 0x2C
      - 0x2E
      - 0x0F
      - 
   - 

      - 0x0002
      - 0xFF
      - IQADJ_G2
      - 0x08
      - 0x08
      - 0x03
      - 
   - 

      - 0x001C
      - 0xFF
      - RX_BB2
      - 0x18
      - 0x18
      - 0x78
      - 
   - 

      - 0x0024
      - 0xFF
      - T_METER
      - 0x10
      - 0x10
      - 0x0F
      - 
   - 

      - 0x0042
      - 0xFF
      - T_METER_8723B
      - 0x03
      - 0x08
      - 0x0F
      - 
   - 

      - 0x0043
      - 0xFFFFFFFF
      - UNKNOWN_43
      - 0x0210E700
      - 0x0210E700
      - 0x0FFF0100
      - 
   - 

      - 0x0055
      - 0xFF
      - UNKNOWN_55
      - 0x94
      - 0x94
      - 0xFF
      - 
   - 

      - 0x0056
      - 0xFFFF
      - UNKNOWN_56
      - 0x000D
      - 0x000D
      - 0x000F
      - 
   - 

      - 0x00B0
      - 0xFFFFFFFF
      - S0S1
      - 0x000AAAAA
      - 0x000AAAAA
      - 0x000FFF01
      - 
   - 

      - 0x00DF
      - 0xFFFFFFFF
      - UNKNOWN_DF
      - 0x00B61400
      - 0x00B61400
      - 0x0FFF0100
      - 
   - 

      - 0x00ED
      - 0xFFFF
      - UNKNOWN_ED
      - 0x0000
      - 0x0000
      - 0x0FFF
      - 
   - 

      - 0x00EF
      - 0xFFFFFFFF
      - WE_LUT
      - 0x0AAAAA00
      - 0x0AAAAA00
      - 0x0FFF0100
      - 
   - 

      - 0x003F
      - 0xFFFFFF
      - unknown
      - 0x0C7200
      - 0x2E3600
      - 0xFF0100
      - 
   - 

      - 0x0047
      - 0xFFFFFFFF
      - unknown
      - 0x0C840000
      - 0x0C840000
      - 0x0FFF0100
      - 
   - 

      - 0x004B
      - 0xFFFFFFFF
      - unknown
      - 0x08992E00
      - 0x08992E00
      - 0x0FFF0100
      - 
   - 

      - 0x004F
      - 0xFFFFFFFF
      - unknown
      - 0x09000F00
      - 0x09000F00
      - 0x0FFF0100
      - 
   - 

      - 0x0053
      - 0xFFFF
      - unknown
      - 0x4400
      - 0x4400
      - 0x0100
      - 
   - 

      - 0x0058
      - 0xFFFFFFFF
      - unknown
      - 0x0000740C
      - 0x0000740C
      - 0x000FFF01
      - 
   - 

      - 0x005C
      - 0xFFFFFFFF
      - unknown
      - 0x000FC378
      - 0x000FC318
      - 0x000FFF01
      - 
   - 

      - 0x0060
      - 0xFFFFFFFF
      - unknown
      - 0x0000B614
      - 0x0000B614
      - 0x000FFF01
      - 
   - 

      - 0x0064
      - 0xFFFFFFFF
      - unknown
      - 0x00000010
      - 0x00000010
      - 0x000FFF01
      - 
   - 

      - 0x0068
      - 0xFFFFFFFF
      - unknown
      - 0x000577F0
      - 0x000577F0
      - 0x000FFF01
      - 
   - 

      - 0x006C
      - 0xFFFFFFFF
      - unknown
      - 0x0000001A
      - 0x0000001A
      - 0x000FFF01
      - 
   - 

      - 0x0070
      - 0xFFFFFFFF
      - unknown
      - 0x000AAAAA
      - 0x000AAAAA
      - 0x000FFF01
      - 
   - 

      - 0x0080
      - 0xFFFFFFFF
      - unknown
      - 0x00082CB2
      - 0x00082E36
      - 0x000FFF01
      - 
   - 

      - 0x0084
      - 0xFFFFFFFF
      - unknown
      - 0x000210E7
      - 0x000210E7
      - 0x000FFF01
      - 
   - 

      - 0x0088
      - 0xFFFFFFFF
      - unknown
      - 0x000C8400
      - 0x000C8400
      - 0x000FFF01
      - 
   - 

      - 0x008C
      - 0xFFFFFFFF
      - unknown
      - 0x0008992E
      - 0x0008992E
      - 0x000FFF01
      - 
   - 

      - 0x0090
      - 0xFFFFFFFF
      - unknown
      - 0x0009000F
      - 0x0009000F
      - 0x000FFF01
      - 
   - 

      - 0x0094
      - 0xFFFFFFFF
      - unknown
      - 0x000D9444
      - 0x000D9444
      - 0x000FFF01
      - 
   - 

      - 0x0098
      - 0xFFFFFFFF
      - unknown
      - 0x0000740C
      - 0x0000740C
      - 0x000FFF01
      - 
   - 

      - 0x009C
      - 0xFFFFFFFF
      - unknown
      - 0x000FC318
      - 0x000FC318
      - 0x000FFF01
      - 
   - 

      - 0x00A0
      - 0xFFFFFFFF
      - unknown
      - 0x0000B614
      - 0x0000B614
      - 0x000FFF01
      - 
   - 

      - 0x00A4
      - 0xFFFFFFFF
      - unknown
      - 0x00000010
      - 0x00000010
      - 0x000FFF01
      - 
   - 

      - 0x00A8
      - 0xFFFFFFFF
      - unknown
      - 0x000577F0
      - 0x000577F0
      - 0x000FFF01
      - 
   - 

      - 0x00AC
      - 0xFFFFFFFF
      - unknown
      - 0x0000001A
      - 0x0000001A
      - 0x000FFF01
      - 
   - 

      - 0x00C0
      - 0xFFFFFFFF
      - unknown
      - 0x00082CB2
      - 0x00082E36
      - 0x000FFF01
      - 
   - 

      - 0x00C4
      - 0xFFFFFFFF
      - unknown
      - 0x000210E7
      - 0x000210E7
      - 0x000FFF01
      - 
   - 

      - 0x00C8
      - 0xFFFFFFFF
      - unknown
      - 0x000C8400
      - 0x000C8400
      - 0x000FFF01
      - 
   - 

      - 0x00CC
      - 0xFFFFFFFF
      - unknown
      - 0x0008992E
      - 0x0008992E
      - 0x000FFF01
      - 
   - 

      - 0x00D0
      - 0xFFFFFFFF
      - unknown
      - 0x0009000F
      - 0x0009000F
      - 0x000FFF01
      - 
   - 

      - 0x00D4
      - 0xFFFFFFFF
      - unknown
      - 0x000D9444
      - 0x000D9444
      - 0x000FFF01
      - 
   - 

      - 0x00D8
      - 0xFFFFFFFF
      - unknown
      - 0x0000740C
      - 0x0000740C
      - 0x000FFF01
      - 
   - 

      - 0x00DC
      - 0xFFFFFF
      - unknown
      - 0x0FC318
      - 0x0FC318
      - 0x0FFF01
      - 
   - 

      - 0x00E3
      - 0xFFFFFFFF
      - unknown
      - 0x00001000
      - 0x00001000
      - 0x0FFF0100
      - 
   - 

      - 0x00E7
      - 0xFFFFFFFF
      - unknown
      - 0x0577F000
      - 0x0577F000
      - 0x0FFF0100
      - 
   - 

      - 0x00EB
      - 0xFFFF
      - unknown
      - 0x1A00
      - 0x1A00
      - 0x0100
      - 

BB Register
'''''''''''

.. list-table::
   :header-rows: 1

   - 

      - Driver
      - Source
      - Filename
   - 

      - 8192cu
      - debugfs
      - 8192cu-gardena-rs-dump-registers-v0.ko-74:da:38:0e:49:7d-rx-bb_reg_dump-05-iperf-done
   - 

      - rtl8192cu
      - debugfs
      - rtl8192cu-gardena-rs-v5.10.69-dump-registers-v13-10-g1f3acbbe2d2a.ko-74:da:38:0e:49:7d-rx-bb_reg_dump-05-iperf-done
   - 

      - rtl8xxxu
      - debugfs
      - rtl8xxxu-gardena-rs-v5.10.69-dump-registers-v13-10-g1f3acbbe2d2a.ko-74:da:38:0e:49:7d-rx-bb_reg_dump-05-iperf-done

.. list-table::
   :header-rows: 1

   - 

      - Address
      - Mask
      - Name
      - #0: 8192cu
      - #1: rtl8192cu
      - #2: rtl8xxxu
      - Hint
   - 

      - 0x0818
      - 0xFFFFFFFF
      - FPGA0_POWER_SAVE
      - 0x12200385
      - 0x12200385
      - 0x02200385
      - Bit 28 never set by [rtl]8192cu
   - 

      - 
      - 0x10000000
      - FPGA0_POWER_SAVE_ENABLE
      - 0x1
      - 0x1
      - 0x0
      - 
   - 

      - 0x082C
      - 0xFFFFFFFF
      - FPGA0_XB_HSSI_PARM2
      - 0x8C000000
      - 0x8C000000
      - 0x00000000
      - Ignore (RF B path)
   - 

      - 0x0830
      - 0xFFFFFFFF
      - TX_AGC_B_RATE18_06
      - 0x0A0C0F0F
      - 0x03030303
      - 0x0A0C0F0F
      - Ignore (RF B path)
   - 

      - 0x0834
      - 0xFFFFFFFF
      - TX_AGC_B_RATE54_24
      - 0x04050708
      - 0x03030303
      - 0x04050708
      - Ignore (RF B path)
   - 

      - 0x0838
      - 0xFFFFFFFF
      - TX_AGC_B_CCK1_55_MCS32
      - 0x00000000
      - 0x00000000
      - 0x3F3F3F00
      - Ignore (RF B path)
   - 

      - 0x083C
      - 0xFFFFFFFF
      - TX_AGC_B_MCS03_MCS00
      - 0x0B0C0D0E
      - 0x00000000
      - 0x0B0C0D0E
      - Ignore (RF B path)
   - 

      - 0x0840
      - 0xFFFFFFFF
      - FPGA0_XA_LSSI_PARM
      - 0x02400060
      - 0x02400060
      - 0x0180740C
      - 
   - 

      - 
      - 0xFF00000
      - FPGA0_XA_LSSI_PARM_ADDR
      - 0x24
      - 0x24
      - 0x18
      - 
   - 

      - 
      - 0xFFFFF
      - FPGA0_XA_LSSI_PARM_DATA
      - 0x60
      - 0x60
      - 0x740C
      - 
   - 

      - 0x0848
      - 0xFFFFFFFF
      - TX_AGC_B_MCS07_MCS04
      - 0x01030509
      - 0x00000000
      - 0x01030509
      - Ignore (RF B path)
   - 

      - 0x084C
      - 0xFFFFFFFF
      - TX_AGC_B_MCS11_MCS08
      - 0x0B0C0D0E
      - 0x00000000
      - 0x0B0C0D0E
      - Ignore (RF B path)
   - 

      - 0x085C
      - 0xFFFFFFFF
      - FPGA0_XCD_SWITCH_CTRL
      - 0x631B25A4
      - 0x631B25A4
      - 0x001B25A4
      - 
   - 

      - 0x0860
      - 0xFFFFFFFF
      - FPGA0_XA_RF_INT_OE
      - 0x66F60230
      - 0x66F60230
      - 0x66F60210
      - 
   - 

      - 0x0868
      - 0xFFFFFFFF
      - TX_AGC_B_MCS15_MCS12
      - 0x01030509
      - 0x00000000
      - 0x01030509
      - Ignore (RF B path)
   - 

      - 0x086C
      - 0xFFFFFFFF
      - TX_AGC_B_CCK11_A_CCK2_11
      - 0x2B2B2200
      - 0x2B2B2B00
      - 0x2A2A2A3F
      - Ignore (RF B path)
   - 

      - 0x0870
      - 0xFFFF
      - FPGA0_XA_RF_SW_CTRL
      - 0x0700
      - 0x0700
      - 0x0760
      - 
   - 

      - 0x0874
      - 0xFFFF
      - FPGA0_XC_RF_SW_CTRL
      - 0x8000
      - 0x8000
      - 0x4000
      - 
   - 

      - 0x0876
      - 0xFFFF
      - FPGA0_XD_RF_SW_CTRL
      - 0x2208
      - 0x2208
      - 0x2200
      - 
   - 

      - 0x0878
      - 0xFFFF
      - FPGA0_XA_RF_PARM
      - 0x0808
      - 0x2808
      - 0x0808
      - 
   - 

      - 0x08B8
      - 0xFFFFFFFF
      - HSPI_XA_READBACK
      - 0x00100010
      - 0x00100010
      - 0x001FFF01
      - 
   - 

      - 0x0B68
      - 0xFFFFFFFF
      - CONFIG_ANT_A
      - 0x80000000
      - 0x00080000
      - 0x80000000
      - 
   - 

      - 0x0C14
      - 0xFFFFFFFF
      - OFDM0_XA_RX_IQ_IMBALANCE
      - 0x400004FE
      - 0x400008FE
      - 0x400008FE
      - 
   - 

      - 0x0C50
      - 0xFFFFFFFF
      - OFDM0_XA_AGC_CORE1
      - 0x69543435
      - 0x6954341E
      - 0x6954341E
      - 
   - 

      - 0x0C58
      - 0xFFFFFFFF
      - OFDM0_XB_AGC_CORE1
      - 0x69543435
      - 0x6954341E
      - 0x69543420
      - 
   - 

      - 0x0C70
      - 0xFFFFFFFF
      - OFDM0_AGC_PARM1
      - 0x2C7F0005
      - 0x2C7F0005
      - 0x2C7F000D
      - 
   - 

      - 0x0C90
      - 0xFFFFFFFF
      - OFDM0_XC_TX_IQ_IMBALANCE
      - 0x00171D25
      - 0x00161C24
      - 0x00252323
      - 
   - 

      - 0x0E00
      - 0xFFFFFFFF
      - TX_AGC_A_RATE18_06
      - 0x36383B3B
      - 0x2F2F2F2F
      - 0x35373A3A
      - 
   - 

      - 0x0E04
      - 0xFFFFFFFF
      - TX_AGC_A_RATE54_24
      - 0x30313334
      - 0x2F2F2F2F
      - 0x2F303233
      - 
   - 

      - 0x0E08
      - 0xFFFFFFFF
      - TX_AGC_A_CCK1_MCS32
      - 0x03902B2A
      - 0x03902B2A
      - 0x03902A2A
      - 
   - 

      - 0x0E10
      - 0xFFFFFFFF
      - TX_AGC_A_MCS03_MCS00
      - 0x3738383A
      - 0x2C2C2C2C
      - 0x36373739
      - 
   - 

      - 0x0E14
      - 0xFFFFFFFF
      - TX_AGC_A_MCS07_MCS04
      - 0x2D2F3132
      - 0x2C2C2C2C
      - 0x2C2E3031
      - 
   - 

      - 0x0E18
      - 0xFFFFFFFF
      - TX_AGC_A_MCS11_MCS08
      - 0x3738393A
      - 0x2C2C2C2C
      - 0x36373839
      - 
   - 

      - 0x0E1C
      - 0xFFFFFFFF
      - TX_AGC_A_MCS15_MCS12
      - 0x2D2F3135
      - 0x2C2C2C2C
      - 0x2C2E3034
      - 
   - 

      - 0x0E30
      - 0xFFFFFFFF
      - TX_IQK_TONE_A
      - 0x01008C00
      - 0x10008C1F
      - 0x01008C00
      - 
   - 

      - 0x0E34
      - 0xFFFFFFFF
      - RX_IQK_TONE_A
      - 0x01008C00
      - 0x10008C1F
      - 0x01008C00
      - 
   - 

      - 0x0EA0
      - 0xFFFFFFFF
      - RX_POWER_BEFORE_IQK_A
      - 0x000561D4
      - 0x00066A94
      - 0x00057BA4
      - 
   - 

      - 0x0EA8
      - 0xFFFFFFFF
      - RX_POWER_AFTER_IQK_A
      - 0x00015694
      - 0x0000CCF4
      - 0x0000E634
      - 
   - 

      - 0x0EAC
      - 0xFFFFFFFF
      - RX_POWER_AFTER_IQK_A_2
      - 0x04013000
      - 0x04023000
      - 0x04023000
      - 
   - 

      - 0x08A8
      - 0xFFFFFFFF
      - unknown
      - 0x00000010
      - 0x00000010
      - 0x0000000F
      - 
   - 

      - 0x08AC
      - 0xFFFFFFFF
      - unknown
      - 0x00000020
      - 0x00001AC0
      - 0x00000500
      - 
   - 

      - 0x08EC
      - 0xFFFFFFFF
      - unknown
      - 0x36383B3B
      - 0x2F2F2F2F
      - 0x35373A3A
      - 
   - 

      - 0x08F0
      - 0xFFFFFFFF
      - unknown
      - 0x30313334
      - 0x2F2F2F2F
      - 0x2F303233
      - 
   - 

      - 0x08F4
      - 0xFFFFFFFF
      - unknown
      - 0x00000006
      - 0x00000007
      - 0x0000000D
      - 
   - 

      - 0x08F8
      - 0xFFFFFFFF
      - unknown
      - 0x000000D3
      - 0x000000E9
      - 0x000000E3
      - 
   - 

      - 0x09C0
      - 0xFFFFFFFF
      - unknown
      - 0x00297F80
      - 0x00234E97
      - 0x00308A25
      - 
   - 

      - 0x0A08
      - 0xFFFFFFFF
      - unknown
      - 0x8CCD8300
      - 0x8CCD8300
      - 0x8C838300
      - 
   - 

      - 0x0A2C
      - 0xFFFFFFFF
      - unknown
      - 0x00D38000
      - 0x00D38000
      - 0x00D30000
      - 
   - 

      - 0x0A50
      - 0xFFFFFFFF
      - unknown
      - 0x0504C708
      - 0x0201ED07
      - 0x490CC909
      - 
   - 

      - 0x0A54
      - 0xFFFFFFFF
      - unknown
      - 0x08305200
      - 0x10307600
      - 0x10308E03
      - 
   - 

      - 0x0A5C
      - 0xFFFFFFFF
      - unknown
      - 0x00000014
      - 0x0000035F
      - 0x00000200
      - 
   - 

      - 0x0A74
      - 0xFFFFFFFF
      - unknown
      - 0x00003007
      - 0x00003007
      - 0x00000007
      - 
   - 

      - 0x0C84
      - 0xFFFFFFFF
      - unknown
      - 0x50F60000
      - 0x20F60000
      - 0x20F60000
      - 
   - 

      - 0x0CF4
      - 0xFFFFFFFF
      - unknown
      - 0x00250000
      - 0x002C0000
      - 0x002C0000
      - 
   - 

      - 0x0CF8
      - 0xFFFFFFFF
      - unknown
      - 0x00000000
      - 0x00000000
      - 0x00000020
      - 
   - 

      - 0x0CFC
      - 0xFFFFFFFF
      - unknown
      - 0x00000006
      - 0x00000007
      - 0x0000000D
      - 
   - 

      - 0x0DA0
      - 0xFFFFFFFF
      - unknown
      - 0x0002016A
      - 0x0010083C
      - 0xB64DFFFF
      - 
   - 

      - 0x0DA4
      - 0xFFFFFFFF
      - unknown
      - 0x00010001
      - 0x00000015
      - 0x0635B8BC
      - 
   - 

      - 0x0DA8
      - 0xFFFFFFFF
      - unknown
      - 0x00000001
      - 0x00000000
      - 0x000005D9
      - 
   - 

      - 0x0DAC
      - 0xFFFFFFFF
      - unknown
      - 0xFC7C0000
      - 0xFD3C0000
      - 0xF8000000
      - 
   - 

      - 0x0DB0
      - 0xFFFFFFFF
      - unknown
      - 0xF6D60000
      - 0xFD080000
      - 0x0A200000
      - 
   - 

      - 0x0DB4
      - 0xFFFFFFFF
      - unknown
      - 0xF6D6E000
      - 0xFD08E000
      - 0x0A200000
      - 
   - 

      - 0x0DB8
      - 0xFFFFFFFF
      - unknown
      - 0x00600000
      - 0x009F0000
      - 0xFEFD0000
      - 
   - 

      - 0x0DBC
      - 0xFFFFFFFF
      - unknown
      - 0x185C0000
      - 0x14C40000
      - 0x0B160000
      - 
   - 

      - 0x0DC4
      - 0xFFFFFFFF
      - unknown
      - 0x03FA0000
      - 0x03F10000
      - 0x00030000
      - 
   - 

      - 0x0DC8
      - 0xFFFFFFFF
      - unknown
      - 0x00000006
      - 0x00000000
      - 0x0000000C
      - 
   - 

      - 0x0DD0
      - 0xFFFFFFFF
      - unknown
      - 0x0000000B
      - 0x0000000B
      - 0x00000009
      - 
   - 

      - 0x0DD4
      - 0xFFFFFFFF
      - unknown
      - 0x00000007
      - 0x00000009
      - 0x00000006
      - 
   - 

      - 0x0DD8
      - 0xFFFFFFFF
      - unknown
      - 0x00ED0B21
      - 0x00FD0721
      - 0x00DF0925
      - 
   - 

      - 0x0DDC
      - 0xFFFFFFFF
      - unknown
      - 0x00002700
      - 0x00002A00
      - 0x00002700
      - 
   - 

      - 0x0DE0
      - 0xFFFFFFFF
      - unknown
      - 0x16D60000
      - 0x1D080000
      - 0x0A200000
      - 
   - 

      - 0x0DE8
      - 0xFFFFFFFF
      - unknown
      - 0x000288E9
      - 0x0003192F
      - 0x0000DFDC
      - 
   - 

      - 0x0DF4
      - 0xFFFFFFFF
      - unknown
      - 0x78C10000
      - 0x78410000
      - 0x78C10000
      - 
   - 

      - 0x0E90
      - 0xFFFFFFFF
      - unknown
      - 0x00A6CBA4
      - 0x00A858E8
      - 0x00A36EC4
      - 
   - 

      - 0x0E98
      - 0xFFFFFFFF
      - unknown
      - 0x00000C68
      - 0x000008B4
      - 0x000005C4
      - 
   - 

      - 0x0F80
      - 0xFFFFFFFF
      - unknown
      - 0x00000001
      - 0x00000007
      - 0x00000006
      - 
   - 

      - 0x0F84
      - 0xFFFFFFFF
      - unknown
      - 0x00000004
      - 0x0000002C
      - 0x0000007B
      - 
   - 

      - 0x0F88
      - 0xFFFFFFFF
      - unknown
      - 0x00000187
      - 0x0000025C
      - 0x00000363
      - 
   - 

      - 0x0F90
      - 0xFFFFFFFF
      - unknown
      - 0x06ED0012
      - 0x04C70010
      - 0x04F3000A
      - 
   - 

      - 0x0F94
      - 0xFFFFFFFF
      - unknown
      - 0x05470DA9
      - 0x171A4708
      - 0x310A09C8
      - 
   - 

      - 0x0FA0
      - 0xFFFFFFFF
      - unknown
      - 0x06050000
      - 0x0EEF0000
      - 0x14DE0000
      - 
   - 

      - 0x0FA4
      - 0xFFFFFFFF
      - unknown
      - 0x000201C9
      - 0x0000530C
      - 0x00001CD9
      - 
   - 

      - 0x0FA8
      - 0xFFFFFFFF
      - unknown
      - 0x00011407
      - 0x0000C407
      - 0x00011407
      - 
   - 

      - 0x0FAC
      - 0xFFFFFFFF
      - unknown
      - 0x0A00FC8E
      - 0x0000A886
      - 0x0A001C0E
      - 
   - 

      - 0x0FB0
      - 0xFFFFFFFF
      - unknown
      - 0x0810040A
      - 0x0810040A
      - 0x08F0040A
      - 
   - 

      - 0x0FB4
      - 0xFFFFFFFF
      - unknown
      - 0x000A5AC8
      - 0x00005AC8
      - 0x000AB351
      - 
   - 

      - 0x0FB8
      - 0xFFFFFFFF
      - unknown
      - 0x0101BB86
      - 0x00B98A49
      - 0x00B58546
      - 

MAC Register
''''''''''''

.. list-table::
   :header-rows: 1

   - 

      - Driver
      - Source
      - Filename
   - 

      - 8192cu
      - debugfs
      - 8192cu-gardena-rs-dump-registers-v0.ko-74:da:38:0e:49:7d-rx-mac_reg_dump-05-iperf-done
   - 

      - rtl8192cu
      - debugfs
      - rtl8192cu-gardena-rs-v5.10.69-dump-registers-v13-10-g1f3acbbe2d2a.ko-74:da:38:0e:49:7d-rx-mac_reg_dump-05-iperf-done
   - 

      - rtl8xxxu
      - debugfs
      - rtl8xxxu-gardena-rs-v5.10.69-dump-registers-v13-10-g1f3acbbe2d2a.ko-74:da:38:0e:49:7d-rx-mac_reg_dump-05-iperf-done

.. list-table::
   :header-rows: 1

   - 

      - Address
      - Mask
      - Name
      - #0: 8192cu
      - #1: rtl8192cu
      - #2: rtl8xxxu
      - Hint
   - 

      - 0x0000
      - 0xFFFF
      - SYS_ISO_CTRL
      - 0x80F8
      - 0x8000
      - 0x80F8
      - 
   - 

      - 
      - 0x20
      - SYS_ISO_CTRL_ANALOG_IPS
      - 0x1
      - 0x0
      - 0x1
      - 
   - 

      - 
      - 0x80
      - SYS_ISO_CTRL_BIT_7
      - 0x1
      - 0x0
      - 0x1
      - 
   - 

      - 0x0002
      - 0xFFFF
      - SYS_FUNC
      - 0xFC17
      - 0xFC17
      - 0xDC1F
      - 
   - 

      - 
      - 0x8
      - SYS_FUNC_UPLL
      - 0x0
      - 0x0
      - 0x1
      - 
   - 

      - 
      - 0x2000
      - SYS_FUNC_DIO_RF
      - 0x1
      - 0x1
      - 0x0
      - 
   - 

      - 0x001C
      - 0xFFFFFF
      - RSV_CTRL
      - 0x1D3100
      - 0x8E2100
      - 0x3E3100
      - 
   - 

      - 0x0021
      - 0xFF
      - LDOV12D_CTRL
      - 0x55
      - 0x25
      - 0x25
      - 
   - 

      - 0x0022
      - 0xFF
      - LDOHCI12_CTRL
      - 0x0F
      - 0x0F
      - 0x57
      - 
   - 

      - 0x0030
      - 0xFFFFFFFF
      - EFUSE_CTRL
      - 0x8021FAFF
      - 0x8021FAFF
      - 0x8020A7FF
      - 
   - 

      - 0x0042
      - 0xFF
      - GPIO_IO_SEL
      - 0x88
      - 0x08
      - 0x08
      - 
   - 

      - 0x0043
      - 0xFF
      - MAC_PINMUX_CFG
      - 0x07
      - 0x00
      - 0x00
      - 
   - 

      - 0x0044
      - 0xFFFFFFFF
      - GPIO_PIN_CTRL
      - 0x00FB0000
      - 0x07880000
      - 0x00000000
      - 
   - 

      - 0x004C
      - 0xFF
      - LEDCFG0
      - 0x08
      - 0x80
      - 0x82
      - 
   - 

      - 0x004D
      - 0xFF
      - LEDCFG1
      - 0x00
      - 0x80
      - 0x82
      - 
   - 

      - 0x0080
      - 0xFFFFFFFF
      - MCU_FW_DL
      - 0x0C0300C6
      - 0x000300C6
      - 0x000300C6
      - 
   - 

      - 0x0088
      - 0xFFFF
      - HMBOX_EXT_0
      - 0xFFFF
      - 0xF005
      - 0xFFFF
      - 
   - 

      - 0x008A
      - 0xFFFF
      - HMBOX_EXT_1
      - 0xF005
      - 0xF005
      - 0x0000
      - 
   - 

      - 0x00F4
      - 0xFFFFFFFF
      - GPIO_OUTSTS
      - 0x000007FB
      - 0x00000088
      - 0x00000000
      - 
   - 

      - 0x010C
      - 0xFFFFFFFF
      - TRXDMA_CTRL
      - 0x0000FAF4
      - 0x0000FAF0
      - 0x0000FAF0
      - 
   - 

      - 
      - 0x4
      - TRXDMA_CTRL_RXDMA_AGG_EN
      - 0x1
      - 0x0
      - 0x0
      - 
   - 

      - 0x011C
      - 0xFFFFFFFF
      - RXFF_PTR
      - 0x03000300
      - 0x03000300
      - 0x13801380
      - 
   - 

      - 0x0124
      - 0xFFFFFFFF
      - HISR
      - 0x0004A600
      - 0x0004A600
      - 0x00043200
      - 
   - 

      - 0x0128
      - 0xFFFFFFFF
      - HIMRE
      - 0x00000000
      - 0x00FFFFFF
      - 0x00000000
      - 
   - 

      - 0x012C
      - 0xFFFFFF
      - HISRE
      - 0x003200
      - 0x000000
      - 0x000000
      - 
   - 

      - 0x0134
      - 0xFFFFFFFF
      - FWISR
      - 0x020001C8
      - 0x020001C8
      - 0x02000108
      - 
   - 

      - 0x0154
      - 0xFFFFFFFF
      - TC1_CTRL
      - 0x00000500
      - 0x00000000
      - 0x00000000
      - 
   - 

      - 0x0158
      - 0xFFFFFFFF
      - TC2_CTRL
      - 0x05001400
      - 0x00000000
      - 0x00000000
      - 
   - 

      - 0x01A0
      - 0xFFFFFFFF
      - C2HEVT_MSG_NORMAL
      - 0x03000083
      - 0x00000000
      - 0x00000000
      - 
   - 

      - 0x01B8
      - 0xFFFFFFFF
      - C2HEVT_MSG_TEST
      - 0x00000004
      - 0x00000000
      - 0x00000000
      - 
   - 

      - 0x01C4
      - 0xFFFFFFFF
      - MCUTST_2
      - 0x000050C7
      - 0x000050C6
      - 0x000050C7
      - 
   - 

      - 0x01C8
      - 0xFFFFFFFF
      - FMTHR
      - 0x80000000
      - 0x00000000
      - 0x00000000
      - 
   - 

      - 0x01D0
      - 0xFFFFFFFF
      - HMBOX_0
      - 0x35000005
      - 0xA0000F86
      - 0xA0000F86
      - 
   - 

      - 0x01D4
      - 0xFFFFFFFF
      - HMBOX_1
      - 0x35000005
      - 0xA0000F86
      - 0x00000102
      - 
   - 

      - 0x01D8
      - 0xFFFFFFFF
      - HMBOX_2
      - 0x36000005
      - 0x03020403
      - 0xA0000F86
      - 
   - 

      - 0x01DC
      - 0xFFFFFFFF
      - HMBOX_3
      - 0x36000005
      - 0x00000102
      - 0x00000000
      - 
   - 

      - 0x01E8
      - 0xFFFFFFFF
      - BB_ACCEESS_CTRL
      - 0x0000F840
      - 0x00000000
      - 0x00000000
      - 
   - 

      - 0x01EC
      - 0xFFFFFFFF
      - BB_ACCESS_DATA
      - 0x00032D95
      - 0x00000000
      - 0x00000000
      - 
   - 

      - 0x0200
      - 0xFFFFFFFF
      - RQPN
      - 0x00EA000C
      - 0x00E70009
      - 0x00E9000C
      - 
   - 

      - 0x0204
      - 0xFFFFFFFF
      - FIFOPAGE
      - 0x00EA000C
      - 0x00E70009
      - 0x00E9000C
      - 
   - 

      - 0x0208
      - 0xFFFFFFFF
      - TDECTRL
      - 0x9201F960
      - 0x8C00F910
      - 0xC400F910
      - 
   - 

      - 0x020C
      - 0xFFFFFFFF
      - TXDMA_OFFSET_CHK
      - 0x00FD0320
      - 0x00FD0000
      - 0x00FD0320
      - 
   - 

      - 0x0214
      - 0xFFFFFFFF
      - RQPN_NPQ
      - 0x00000202
      - 0x00000808
      - 0x00000202
      - 
   - 

      - 0x0280
      - 0xFFFFFFFF
      - RXDMA_AGG_PG_TH
      - 0x00000030
      - 0x00000000
      - 0x00000000
      - 
   - 

      - 0x0400
      - 0xFFFFFFFF
      - VOQ_INFO
      - 0x000000FF
      - 0x000000FF
      - 0xFF0000FF
      - 
   - 

      - 0x041C
      - 0xFFFFFFFF
      - CPU_MGQ_INFORMATION
      - 0x000000FC
      - 0x000000F9
      - 0x000000F9
      - 
   - 

      - 0x0420
      - 0xFFFFFF
      - FWHW_TXQ_CTRL
      - 0x713F80
      - 0x313F80
      - 0x313F80
      - 
   - 

      - 0x0425
      - 0xFF
      - TXPKTBUF_MGQ_BDNY
      - 0xFC
      - 0xF9
      - 0xF9
      - 
   - 

      - 0x0427
      - 0xFF
      - MULTI_BCNQ_OFFSET
      - 0x91
      - 0x8B
      - 0xC3
      - 
   - 

      - 0x0428
      - 0xFFFF
      - SPEC_SIFS
      - 0x100A
      - 0x0A10
      - 0x100A
      - Endian error in rtl8192cu?
   - 

      - 
      - 0xFF
      - SPEC_SIFS_CCK
      - 0xA
      - 0x10
      - 0xA
      - 
   - 

      - 
      - 0xFF00
      - SPEC_SIFS_OFDM
      - 0x10
      - 0xA
      - 0x10
      - 
   - 

      - 0x042A
      - 0xFFFF
      - RETRY_LIMIT
      - 0x3030
      - 0x3030
      - 0x0704
      - rtl8xxxu: Adjusted by mac80211
   - 

      - 
      - 0x3F
      - RETRY_LIMIT_LONG
      - 0x30
      - 0x30
      - 0x4
      - 
   - 

      - 
      - 0x3F00
      - RETRY_LIMIT_SHORT
      - 0x30
      - 0x30
      - 0x7
      - 
   - 

      - 0x0430
      - 0xFFFFFFFF
      - DARFRC
      - 0x00000000
      - 0x01000000
      - 0x00000000
      - 
   - 

      - 0x0438
      - 0xFFFFFFFF
      - RARFRC
      - 0x04030201
      - 0x01000000
      - 0x04030201
      - 
   - 

      - 0x0440
      - 0xFFFFFFFF
      - RESPONSE_RATE_SET
      - 0x0000015F
      - 0x0080015D
      - 0x0080015F
      - 
   - 

      - 0x0450
      - 0xFFFFFFFF
      - ARFR3
      - 0x0000FFFD
      - 0x0FFFFFFF
      - 0x0FFFFFFF
      - 
   - 

      - 0x045C
      - 0xFF
      - AMPDU_MIN_SPACE
      - 0x07
      - 0x07
      - 0x05
      - 
   - 

      - 0x0460
      - 0xFFFFFF
      - FAST_EDCA_CTRL
      - 0x086666
      - 0x086666
      - 0x080000
      - 
   - 

      - 0x0480
      - 0xFFFFFF
      - INIRTS_RATE_SEL
      - 0x0C0A08
      - 0x0C0A0A
      - 0x0C0A04
      - 
   - 

      - 0x04A4
      - 0xFFFFFFFF
      - POWER_STATUS
      - 0x00000001
      - 0x00000001
      - 0x00000000
      - 
   - 

      - 0x04C0
      - 0xFFFF
      - PKT_VO_VI_LIFE_TIME
      - 0x0400
      - 0x1000
      - 0x1000
      - 
   - 

      - 0x04C2
      - 0xFFFF
      - PKT_BE_BK_LIFE_TIME
      - 0x0400
      - 0x1000
      - 0x1000
      - 
   - 

      - 0x04CA
      - 0xFF
      - MAX_AGGR_NUM
      - 0x0A
      - 0x08
      - 0x0A
      - 
   - 

      - 0x04CB
      - 0xFF
      - RTS_MAX_AGGR_NUM
      - 0x0C
      - 0x07
      - 0x0C
      - 
   - 

      - 0x04CF
      - 0xFF
      - RA_TRY_RATE_AGG_LMT
      - 0x02
      - 0x00
      - 0x02
      - 
   - 

      - 0x04DC
      - 0xFFFF
      - NQOS_SEQ
      - 0x003C
      - 0x0000
      - 0x0000
      - 
   - 

      - 0x0500
      - 0xFFFFFFFF
      - EDCA_VO_PARAM
      - 0x002F3222
      - 0x002F7302
      - 0x002F3202
      - 
   - 

      - 0x0504
      - 0xFFFFFFFF
      - EDCA_VI_PARAM
      - 0x005E4322
      - 0x005EF702
      - 0x005E4302
      - 
   - 

      - 0x0508
      - 0xFFFFFFFF
      - EDCA_BE_PARAM
      - 0x005EA42B
      - 0x005EA42B
      - 0x0000A403
      - 
   - 

      - 0x050C
      - 0xFFFFFFFF
      - EDCA_BK_PARAM
      - 0x0000A44F
      - 0x0000FF07
      - 0x0000A407
      - 
   - 

      - 0x0514
      - 0xFFFF
      - SIFS_CCK
      - 0x100A
      - 0x0A0A
      - 0x0E0A
      - 
   - 

      - 0x0516
      - 0xFFFF
      - SIFS_OFDM
      - 0x100A
      - 0x0A0A
      - 0x0E0A
      - 
   - 

      - 0x0550
      - 0xFF
      - BEACON_CTRL
      - 0x08
      - 0x08
      - 0x09
      - 
   - 

      - 0x0551
      - 0xFF
      - BEACON_CTRL_1
      - 0x18
      - 0x10
      - 0x10
      - 
   - 

      - 0x0558
      - 0xFF
      - DRIVER_EARLY_INT
      - 0x03
      - 0x05
      - 0x05
      - 
   - 

      - 0x0560
      - 0xFFFFFFFF
      - TSFTR
      - 0x1CB1C31E
      - 0x168A306C
      - 0x0FFFBC85
      - Ignore (Timer)
   - 

      - 0x0568
      - 0xFFFFFFFF
      - TSFTR1
      - 0x0193582E
      - 0x023BEA8D
      - 0x02D23588
      - Ignore (Timer)
   - 

      - 0x0608
      - 0xFFFFFFFF
      - RCR
      - 0x700060CE
      - 0xF00069CE
      - 0x700060CE
      - 
   - 

      - 
      - 0x100
      - RCR_ACCEPT_CRC32
      - 0x0
      - 0x1
      - 0x0
      - 
   - 

      - 
      - 0x800
      - RCR_ACCEPT_DATA_FRAME
      - 0x0
      - 0x1
      - 0x0
      - 
   - 

      - 
      - 0x80000000
      - RCR_APPEND_FCS
      - 0x0
      - 0x1
      - 0x0
      - 
   - 

      - 0x063A
      - 0xFFFF
      - MAC_SPEC_SIFS
      - 0x100A
      - 0x0A0A
      - 0x100A
      - 
   - 

      - 0x063C
      - 0xFFFF
      - R2T_SIFS
      - 0x0808
      - 0x0A08
      - 0x0808
      - 
   - 

      - 0x063E
      - 0xFFFF
      - T2T_SIFS
      - 0x0A0A
      - 0x0A0C
      - 0x0A0A
      - 
   - 

      - 0x0652
      - 0xFFFF
      - NAV_UPPER
      - 0x0000
      - 0x0020
      - 0x00EB
      - 
   - 

      - 0x0664
      - 0xFFFFFFFF
      - RXERR_RPT
      - 0xA0000000
      - 0x00004708
      - 0x000009C8
      - 
   - 

      - 0x0670
      - 0xFFFFFFFF
      - CAM_CMD
      - 0x00010028
      - 0x00010008
      - 0x00010008
      - 
   - 

      - 0x0674
      - 0xFFFFFFFF
      - CAM_WRITE
      - 0xF5248051
      - 0xFFFF8011
      - 0xFFFF8011
      - 
   - 

      - 0x067C
      - 0xFFFFFFFF
      - CAM_DEBUG
      - 0x0000C005
      - 0x00000000
      - 0x00000000
      - 
   - 

      - 0x0680
      - 0xFFFFFFFF
      - SECURITY_CFG
      - 0x0000010C
      - 0x000000CC
      - 0x000000CF
      - 
   - 

      - 0x0692
      - 0xFFFF
      - PS_RX_INFO
      - 0x320E
      - 0x321F
      - 0x320F
      - 
   - 

      - 0x06A0
      - 0xFFFF
      - RXFLTMAP0
      - 0x0000
      - 0xFFFF
      - 0xFFFF
      - 
   - 

      - 0x06A8
      - 0xFFFFFFFF
      - BCN_PSR_RPT
      - 0x00032001
      - 0x00000001
      - 0x00000001
      - 
   - 

      - 0x013C
      - 0xFFFFFFFF
      - unknown
      - 0x00002600
      - 0x00000600
      - 0x00000600
      - 
   - 

      - 0x01A8
      - 0xFFFFFFFF
      - unknown
      - 0x0000D001
      - 0x00000000
      - 0x00000000
      - 
   - 

      - 0x0434
      - 0xFFFFFFFF
      - unknown
      - 0x10080404
      - 0x07060504
      - 0x10080404
      - 
   - 

      - 0x043C
      - 0xFFFFFFFF
      - unknown
      - 0x08070605
      - 0x07060504
      - 0x08070605
      - 
   - 

      - 0x04E8
      - 0xFFFFFFFF
      - unknown
      - 0x00000000
      - 0x00000000
      - 0x00000379
      - 
   - 

      - 0x06B8
      - 0xFFFFFFFF
      - unknown
      - 0x00000000
      - 0x00010000
      - 0x00000000
      - 
