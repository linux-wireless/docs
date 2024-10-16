System on a chip
================

Broadcom produces many SoCs that can combine processor, ethernet, WiFi,
USB and more. *b43* can operate on WiFi cores present in SoCs similarly
to the ones present on standalone PCI/PCIe cards.

Known SSB SoCs
--------------

.. list-table::
   :header-rows: 1

   - 

      - Chip
      - 
      - 
      - MIPS
      - 
      - 80211
      - 
      - 
      - PCI
         rev
      - USB
         rev
      - CC
         rev
      - PMU
         rev
   - 

      - Name
      - id
      - pkg
      - 
      - rev
      - rev
      - PHY
      - Radio
      - \-
      - \-
      - \-
      - \-
   - 

      - BCM5352
      - 0x5352
      - 0x00
      - 3302
      - 6
      - 9
      - G/7
      - 0x2050/2
      - ─
      - 1.1/2
      - 14
      - ─
   - 

      - BCM5352E
      - 0x5352
      - 0x02
      - 3302
      - 6
      - 9
      - G/7
      - 0x2050/2
      - ─
      - 1.1/2
      - 14
      - ─
   - 

      - BCM5354
      - 0x5354
      - 0x00
      - 3302
      - 8
      - 13
      - LP/0
      - 0x2062/1
      - ─
      - 2.0/2
      - 20
      - 0
   - 

      - ?
      - 0x5365
      - 0x00
      - 3302
      - 1
      - ─
      - ─
      - ─
      - 8
      - 1.1/2
      - 5
      - ─
   - 

      - BCM4705
      - 0x4785
      - 0x0C
      - 3302
      - 7
      - ─
      - ─
      - ─
      - 11
      - 2.0/0
      - 15
      - ─
   - 

      - BCM4712
      - 0x4712
      - 0x00 / 0x02
      - 3302
      - 1
      - 7
      - G/2
      - 0x2050/2
      - 10
      - 1.1/1
      - 9
      - ─
   - 

      - BCM4704
      - 0x4704
      - 0x00
      - 3302
      - 3
      - ─
      - ─
      - ─
      - 8
      - 1.1/3
      - 3
      - ─

Known BCMA SoCs
---------------

.. list-table::
   :header-rows: 1

   - 

      - Chip
      - 
      - 
      - 
      - MIPS
      - 
      - 80211
      - 
      - 
      - 
      - PCIe
         rev
      - USB
         rev
      - CC
         rev
      - PMU
         rev
   - 

      - Name
      - id
      - rev
      - pkg
      - 
      - rev
      - rev
      - PHY
      - Radio
      - Supp.
      - 
      - 
      - 
      - 
   - 

      - BCM5356A1
      - 0x5356
      - 
      - 0x04
      - 74K
      - 3
      - 21
      - SSLPN/19
      - ?
      - No  [1]_
      - ─
      - ─
      - 33
      - ?
   - 

      - BCM5357B0
      - 0x5357
      - 0x1
      - 0x08
      - 74K
      - 4
      - 28
      - N/9
      - 0x2057/5
      - No  [2]_
      - ─
      - 2.0/5
      - 38
      - 9
   - 

      - BCM5358
      - 0x5357
      - 0x2
      - 0x08
      - 74K
      - 4
      - 28
      - N/9
      - 0x2057/5
      - No  [3]_
      - ─
      - 2.0/5
      - 38
      - 9
   - 

      - BCM5358
      - 0x5357
      - 
      - 0x09
      - 74K
      - 4
      - 28
      - N/9
      - 0x2057/5
      - No
      - ─
      - 2.0/5
      - 38
      - 9
   - 

      - BCM47186B0
      - 0x5357
      - 
      - 0x0A
      - 74K
      - 4
      - 28
      - N/9
      - 0x2057/5
      - No
      - ─
      - 2.0/5
      - 38
      - 9
   - 

      - BCM5357C0
      - 53572
      - 
      - 0x08
      - 74K
      - 5
      - 28
      - N/17
      - 0x2057/13
      - No  [4]_
      - ─
      - ─
      - 39
      - ?
   - 

      - BCM5356C0
      - 53572
      - 
      - 0x0B
      - 74K
      - 5
      - 28
      - ?
      - ?
      - ?
      - ─
      - ─
      - 39
      - ?
   - 

      - BCM4717A1
      - 0x4716
      - 
      - 0x09
      - 74K
      - 1
      - 17
      - N/5
      - 0x2056/7
      - Yes  [5]_
      - 14
      - 2.0/4
      - 31
      - 5
   - 

      - BCM4718A1
      - 0x4716
      - 
      - 0x0A
      - 74K
      - 1
      - 17
      - N/5
      - 0x2056/7
      - Yes  [6]_
      - 14
      - 2.0/4
      - 31
      - 5
   - 

      - BCM4716B0
      - 47162
      - 
      - 0x02
      - 74K
      - 2
      - 17
      - N/6
      - ?
      - ?
      - ─
      - ─
      - 31
      - ?
   - 

      - BCM4706
      - 0x5300
      - 
      - 0x00
      - 74K
      - 0
      - ─
      - ─
      - ─
      - ─
      - 14
      - 2.0/4
      - 31
      - ?

Known BCMA ARM SoCs
-------------------

.. list-table::
   :header-rows: 1

   - 

      - Chip
      - 
      - 
      - ARM
      - 
      - PCIe 2
         rev
      - USB rev
      - 
      - CC
         rev
   - 

      - Name
      - id
      - pkg
      - 
      - rev
      - 
      - 2.0
      - 3.0
      - 
   - 

      - BCM4708A0
      - 53010
      - 0x02
      - Cortex-A9
      - 1
      - 1
      - 1
      - 1
      - 42
   - 

      - BCM47081A0
      - 
      - 
      - 
      - 
      - 
      - 
      - 
      - 
   - 

      - BCM4709A0
      - 53010
      - 0x00
      - Cortex-A9
      - 1
      - 1
      - 1
      - 1
      - 42
   - 

      - BCM4709C0
      - 53030
      - 0x00
      - Cortex-A9
      - 1
      - 7
      - 7
      - 7
      - 42
   - 

      - BCM47189B0
      - 53573
      - 0x01
      - Cortex-A7
      - 0
      - 5
      - 5
      - ─
      - 54

Please note that devices with PCI(e)/USB core (working in a host mode) can have extra cards attached. We don't list them in the table, as it's vendor choice what additional card will be used. For example:

- Netgear WNDR3400 V1 uses BCM4718 and has extra BCM43224 attached
- Netgear WNDR3700 V3 uses BCM4718 but has extra BCM4331 attached

.. [1]
   Unsupported PHY type

.. [2]
   Unsupported radio 0x2057 revision 5

.. [3]
   Unsupported radio 0x2057 revision 5

.. [4]
   Unsupported radio 0x2057 revision 13

.. [5]
   Limited performance

.. [6]
   Limited performance
