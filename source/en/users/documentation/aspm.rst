Go back --> :doc:`Documentation <../documentation>`

ASPM on Linux
-------------

This section is a review of ASPM and the Linux tweaks/debugging utilities available for testing ASPM. I can't find another wiki to place this in yet on https://wiki.kernel.org/, it should be moved eventually.

ASPM review
-----------

ASPM is a PCI-E enhancement. It allows for a device to go completely into electrically idle state, meaning it will not send or receive electrical signals for a while. To achieve this the PCI-E specification has come up with instructions a PCI-E endpoint (device) should follow for signaling to a root complex (the bus) that it is going idle, or waking up. Communication at the PCI-E bus can be tricky to align with an endpoint and because of this there are patterns a PCI-E device will use to train the link to come out of electrical idle states. There are several states a device will enter when using ASPM, namely L1, L0s.

PCIE cards should always support ASPM, what the ASPM requirements says today is that L1 is mandatory and L0s is optional unless the formfactor specifications explicitly requies it. Not sure which form factors explicitly require L0s (anyone?). Additionally software must not enable L0s in either direction on a given Link unless components on both sides of the Link each support L0s.

The way it typically works internally on endpoints (devices) is that there are idle timers (counters) in the chipset. There is a set point at which the PCIe link is idle enough to enter L0s, and a second point at which we're idle enough to enter L1. A device could potentially 'support' L0s but internally the timers could be set such that L0s and L1 happen at the same time or L0s happens after L1, so the link will essentially never enter L0s. ASPM compliance may vary by device, ASPM specification has varied as new releases have been made.

Determining if you have ASPM enabled
------------------------------------

You can verify by using lspci -vvv as root.

When ASPM is enabled
~~~~~~~~~~~~~~~~~~~~

This is an example that has ASPM enabled:

::

   05:00.0 Network controller: Atheros Communications Inc. AR928X Wireless Network Adapter (PCI-Express) (rev 01)
           Subsystem: Atheros Communications Inc. Device 3099
           Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR+ FastB2B- DisINTx-
           Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
           Latency: 0, Cache Line Size: 64 bytes
           Interrupt: pin A routed to IRQ 19
           Region 0: Memory at dbdf0000 (64-bit, non-prefetchable) [size=64K]
           Capabilities: [40] Power Management version 2
                   Flags: PMEClk- DSI- D1+ D2- AuxCurrent=375mA PME(D0+,D1+,D2-,D3hot+,D3cold-)
                   Status: D0 NoSoftRst- PME-Enable- DSel=0 DScale=0 PME-
           Capabilities: [50] MSI: Enable- Count=1/1 Maskable- 64bit-
                   Address: 00000000  Data: 0000
           Capabilities: [60] Express (v1) Legacy Endpoint, MSI 00
                   DevCap: MaxPayload 128 bytes, PhantFunc 0, Latency L0s <512ns, L1 <64us
                           ExtTag- AttnBtn- AttnInd- PwrInd- RBE- FLReset-
                   DevCtl: Report errors: Correctable- Non-Fatal- Fatal- Unsupported-
                           RlxdOrd+ ExtTag- PhantFunc- AuxPwr- NoSnoop-
                           MaxPayload 128 bytes, MaxReadReq 512 bytes
                   DevSta: CorrErr- UncorrErr+ FatalErr- UnsuppReq+ AuxPwr- TransPend-
                   LnkCap: Port #0, Speed 2.5GT/s, Width x1, ASPM unknown, Latency L0 <512ns, L1 <64us
                           ClockPM- Surprise- LLActRep- BwNot-
                   LnkCtl: ASPM L1 Enabled; RCB 128 bytes Disabled- Retrain- CommClk+
                           ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
                   LnkSta: Speed 2.5GT/s, Width x1, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
           Capabilities: [90] MSI-X: Enable- Count=1 Masked-
                   Vector table: BAR=0 offset=00000000
                   PBA: BAR=0 offset=00000000
           Capabilities: [100] Advanced Error Reporting
                   UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq+ ACSViol-
                   UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                   UESvrt: DLP+ SDES- TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
                   CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr-
                   CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr-
                   AERCap: First Error Pointer: 14, GenCap+ CGenEn- ChkCap+ ChkEn-
           Capabilities: [140] Virtual Channel <?>
           Capabilities: [160] Device Serial Number 00-00-00-00-00-00-00-00
           Kernel driver in use: ath9k
           Kernel modules: ath9k

When ASPM is disabled
~~~~~~~~~~~~~~~~~~~~~

This is an example output when ASPM is disabled:

::

   localhost ~ # lspci -vvvv -s 03:00
   03:00.0 Network controller: Atheros Communications Inc. AR928X Wireless Network Adapter (PCI-Express) (rev 01)
           Subsystem: Atheros Communications Inc. Device 309a
           Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
           Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
           Latency: 0, Cache Line Size: 64 bytes
           Interrupt: pin A routed to IRQ 17
           Region 0: Memory at f0100000 (64-bit, non-prefetchable) [size=64K]
           Capabilities: [40] Power Management version 2
                   Flags: PMEClk- DSI- D1+ D2- AuxCurrent=375mA PME(D0+,D1+,D2-,D3hot+,D3cold-)
                   Status: D0 NoSoftRst- PME-Enable- DSel=0 DScale=0 PME-
           Capabilities: [50] MSI: Enable- Count=1/1 Maskable- 64bit-
                   Address: 00000000  Data: 0000
           Capabilities: [60] Express (v1) Legacy Endpoint, MSI 00
                   DevCap: MaxPayload 128 bytes, PhantFunc 0, Latency L0s <512ns, L1 <64us
                           ExtTag- AttnBtn- AttnInd- PwrInd- RBE- FLReset-
                   DevCtl: Report errors: Correctable- Non-Fatal- Fatal- Unsupported-
                           RlxdOrd+ ExtTag- PhantFunc- AuxPwr- NoSnoop-
                           MaxPayload 128 bytes, MaxReadReq 512 bytes
                   DevSta: CorrErr- UncorrErr+ FatalErr- UnsuppReq+ AuxPwr- TransPend-
                   LnkCap: Port #0, Speed 2.5GT/s, Width x1, ASPM unknown, Latency L0 <512ns, L1 <64us
                           ClockPM- Surprise- LLActRep- BwNot-
                   LnkCtl: ASPM Disabled; RCB 128 bytes Disabled- Retrain- CommClk+
                           ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
                   LnkSta: Speed 2.5GT/s, Width x1, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
           Capabilities: [90] MSI-X: Enable- Count=1 Masked-
                   Vector table: BAR=0 offset=00000000
                   PBA: BAR=0 offset=00000000
           Capabilities: [100] Advanced Error Reporting
                   UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq+ ACSViol-
                   UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                   UESvrt: DLP+ SDES- TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
                   CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr-
                   CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- NonFatalErr-
                   AERCap: First Error Pointer: 14, GenCap+ CGenEn- ChkCap+ ChkEn-
           Capabilities: [140] Virtual Channel <?>
           Capabilities: [160] Device Serial Number 00-00-00-00-00-00-00-00
           Kernel driver in use: ath9k
           Kernel modules: ath9k

Why is ASPM disabled for my device?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ASPM *should* automatically be negotiated by the BIOS based on all the endpoints connected on a root complex. IF your device has ASPM disabled it is likely because:

-  the BIOS determined that needed to happen
-  PCIE requires ASPM but L0s is optional so you might have L0s disabled and only L1 enabled
-  you have a buggy BIOS
-  you have no BIOS and your systems programmers didn't address ASPM yet

ASPM for 802.11
---------------

Testing on battery lifetime shows that the difference between having L1 and L1/L0s both could at max save up to five minutes of battery life in the best possible scenario where the 802.11 link is the most idle. This comes right down to the frequency the driver is accessing registers on the chip.

Linux kernel ASPM support
-------------------------

An Operating System should not need to muck with ASPM, the BIOS would have dealt with the capability exchanges between the root complex and the different endpoints. Of course, BIOSes are buggy though -- so the Linux kernel does have the capability to oversee and review the capabilities by itself and overrule the BIOS. ASPM support in the Linux kernel is also used to expose ASPM capabilities for PCIE devices to userspace (need confirmation, I see this being done in the code, but makes no sense).

You can also muck with ASPM settings to debug root complex/endpoints. This is a feature which should \*not\* be used by the average user, this is designed more for developers, choosing the wrong parameters can damage your device.

The option to debug ASPM is available through the CONFIG_PCIEASPM kernel configuration:

::

   config PCIEASPM
           bool "PCI Express ASPM support(Experimental)"
           depends on PCI && EXPERIMENTAL && PCIEPORTBUS
           default n
           help
             This enables PCI Express ASPM (Active State Power Management) and
             Clock Power Management. ASPM supports state L0/L0s/L1.

             When in doubt, say N.

Enabling this will compile drivers/pci/pcie/aspm.c

Force enable or disable ASPM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This boot parameter is available:

<code> pcie_aspm= [PCIE] Forcibly enable or disable PCIe Active State Power

::

                         Management.
                 off     Disable ASPM.
                 force   Enable ASPM even on devices that claim not to support it.
                         WARNING: Forcing ASPM on may cause system lockups.</code>

Note that this will try to enable ASPM on all devices, check below of a way to do it for devices individually.

Enabling ASPM with enable_aspm
------------------------------

enable_aspm is a script which you can use to enable ASPM for your device, once you know its address and the root complex on which its using. You can read below how to find out what root complex a device uses. The script can be downloaded from:

::

   http://drvbp1.linux-foundation.org/~mcgrof/scripts/enable-aspm

There are only 3 parameters you will need to change:

::

   ROOT_COMPLEX="00:1c.1"
   ENDPOINT="03:00.0"

   # We'll only enable the last 2 bits by using a mask
   # of :3 to setpci, this will ensure we keep the existing
   # values on the byte.
   #
   # Hex  Binary  Meaning
   # -------------------------
   # 0    0b00    L0 only
   # 1    0b01    L0s only
   # 2    0b10    L1 only
   # 3    0b11    L1 and L0s
   ASPM_SETTING=3

Also if you have new **setpci**, you should add **.B** after address in all **setpci** calls.

Enabling ASPM with setpci
-------------------------

The PCIE Link Control Register is properly parsed with *lspci -vvv* but you might want to know exactly how to determine if your device has ASPM support manually. This is required to know exactly where to poke a PCIE device to force enable ASPM manually for a specific root complex or endpoint device. This section covers how to do this.

How to read the Link Control Register for ASPM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Link Control Register on the PCI device tells us if ASPM is enabled and what ASPM settings will be used. How to find the register for the Link Control Register for any PCIE device is explained below -- but first lets review what to look out for on the register. Look at the last byte of the Link Control Register on the PCIE device the values to decode for ASPM are as follows:

::

   0b00 = L0 only
   0b01 = L0s only
   0b10 = L1 only
   0b11 = L1 and L0s

How to find the Link Control Register on a PCIE device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First find the bus address for the device you want to check for. On a box with Atheros you might get:

::

   user@tux ~ $ lspci | grep -i atheros
   03:00.0 Network controller: Atheros Communications Inc. Device 0030 (rev 01)

The *03:00.0* is the bus address. Now first check on which root complex this device sits on, by using lspci -t. You do this to first find the Link Control Register settings of your root complex. Only after you've tuned that should you tune the card. You should unload the module or turn the device off prior to tweaking with it. For the root complex this should not be needed.

::

   -[0000:00]-+-00.0
              +-02.0
              +-02.1
              +-03.0
              +-03.2
              +-03.3
              +-19.0
              +-1a.0
              +-1a.1
              +-1a.7
              +-1b.0
              +-1c.0-[0000:02]--
              +-1c.1-[0000:03]----00.0
              +-1c.2-[0000:04]--
              +-1c.3-[0000:05-0c]--
              +-1c.4-[0000:0d-14]--
              +-1d.0
              +-1d.1
              +-1d.2
              +-1d.7
              +-1e.0-[0000:15-18]--+-00.0
              |                    \-00.1
              +-1f.0
              +-1f.1
              +-1f.2
              \-1f.3

In this case we see 03:00.0 sits on 00:1c.1 so you can now do *lspci -s 00:1c.1 -xxx* on that root complex and to get the PCI config space of that device. The PCIE spec has a fun little algorithm to find the Link Control Register out of the PCI config space. The logic is as follows:

::

     * Read 0x34 and read the register that points to 
     * If that value is not 0x10 then read the next byte (0x35) and go read that register 
     * If that register is not 0x10 then read the next byte and go read that register 
     * Repeat this until you find a register that has 0x10 
     * Once you find the register with 0x10 then add 0x10 to the final register you were reading 
     * The Link Control Register is this final register + 0x10 Lets analyze a real world example of a root complex, specifically the one of the root complex above. 

::

   user@tux ~ $ sudo lspci -s 00:1c.1 -xxx
   00:1c.1 PCI bridge: Intel Corporation 82801H (ICH8 Family) PCI Express Port 2 (rev 03)
   00: 86 80 41 28 07 05 10 00 03 00 04 06 10 00 81 00
   10: 00 00 00 00 00 00 00 00 00 03 03 00 30 30 00 00
   20: 00 dc 30 df e1 df e1 df 00 00 00 00 00 00 00 00
   30: 00 00 00 00 40 00 00 00 00 00 00 00 0b 02 04 00
   40: 10 80 41 01 c0 8f 00 00 00 00 10 00 11 2c 11 02
   50: 40 00 11 30 e0 a0 18 00 00 00 48 01 00 00 00 00
   60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   80: 05 90 01 00 0c 30 e0 fe 69 41 00 00 00 00 00 00
   90: 0d a0 00 00 aa 17 ad 20 00 00 00 00 00 00 00 00
   a0: 01 00 02 c8 00 00 00 00 00 00 00 00 00 00 00 00
   b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   d0: 00 00 00 00 00 00 00 00 80 00 11 08 00 00 00 00
   e0: 00 0f c7 00 06 07 08 00 33 00 00 00 00 00 00 00
   f0: 00 00 00 00 00 00 00 00 86 0f 05 00 00 00 00 00

So first read 0x34, and we see it is 0x40 (do not hop to the next byte here). We read 0x40 and see it is 0x10. Now we add 0x40 + 0x10 = 0x50. We read 0x50. 0x50 is the value of the Link Control Register. 0x50 has a value of 0x40. This means only L0 is enabled so ASPM is completely disabled. To tweak ASPM for this root complex then we we would do have to first keep the original value and then OR it with our new ASPM settings.

Note: as it turns out 0x50 is also used for the Link Control Register for ICH6, ICH7, ICH8, ICH9.

::

   # Disables ASPM, enables only L0 (this was the existing setting)
   sudo setpci -s 00:1c.1 0x50.B=0x40

   # Enable L0s only 
   sudo setpci -s 00:1c.1 0x50.B=0x41

   # Enable L1 only
   sudo setpci -s 00:1c.1 0x50.B=0x42

   # Enable L1 and L0s
   sudo setpci -s 00:1c.1 0x50.B=0x43

Now you can start to toy with your device. A big fat warning prior to this part:

**You should not have to do any this unless you are writing your own system BIOS or have a buggy BIOS. Apart from these settings you may also need to do specific changes to the root complex or the device to tune the devices accordingly for issues on root complexes or devices. Talk to your vendor for errata/documentation for this.**

Now -- lets get on to tweaking your device. Since you have the bus address of your 802.11 device you can now use this to get its respective PCI config space in hex.

::

   user@tux ~ $ sudo lspci -s 03:00.0 -xxx
   03:00.0 Network controller: Atheros Communications Inc. Device 0030 (rev 01)
   00: 8c 16 30 00 03 01 10 40 01 00 80 02 10 00 00 00
   10: 04 00 3e df 00 00 00 00 00 00 00 00 00 00 00 00
   20: 00 00 00 00 00 00 00 00 00 00 00 00 8c 16 16 31
   30: 00 00 00 00 40 00 00 00 00 00 00 00 0b 01 00 00
   40: 01 50 c3 5b 00 00 00 00 00 00 00 00 00 00 00 00
   50: 05 70 84 01 00 00 00 00 00 00 00 00 00 00 00 00
   60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   70: 10 00 02 00 00 87 04 05 10 20 0b 00 11 5c 03 00
   80: 41 00 11 10 00 00 00 00 00 00 00 00 00 00 00 00
   90: 00 00 00 00 10 00 00 00 00 00 00 00 00 00 00 00
   a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

This example is a little more complicated so we'll analyze it line by line:

::

   00: 8c 16 30 00 03 01 10 40 01 00 80 02 10 00 00 00
   10: 04 00 3e df 00 00 00 00 00 00 00 00 00 00 00 00
   20: 00 00 00 00 00 00 00 00 00 00 00 00 8c 16 16 31
   30: 00 00 00 00 40 00 00 00 00 00 00 00 0b 01 00 00
       ^            ^
       |            |
      0x30         0x34

   So 0x34 = 0x40. 0x40 is not 0x10 so we go read 0x40 now

   40: 01 50 c3 5b 00 00 00 00 00 00 00 00 00 00 00 00
       ^
       |
      0x40 = 0x01, this is not 0x10 so read the next byte

   40: 01 50 c3 5b 00 00 00 00 00 00 00 00 00 00 00 00
          ^
          |
         0x41 = 0x50, so go read that register next

   50: 05 70 84 01 00 00 00 00 00 00 00 00 00 00 00 00
       ^
       |
      0x50 = 0x05, this is not 0x10, so go read the next byte.
      The next byte 0x51 = 0x70 so we go read that register next.

   70: 10 00 02 00 00 87 04 05 10 20 0b 00 11 5c 03 00
       ^
       |
       At last, 0x70 = 0x10. So now we do 0x70 + 0x10 = 0x80 and go read 0x80.

   80: 41 00 11 10 00 00 00 00 00 00 00 00 00 00 00 00
       ^
       |
       0x80 = 0x41
       0x41 = 0b1000001 so this has ASPM L0s on only.

Assuming your root complex has L1 enabled as well already you can force ASPM L1 or tune ASPM off if it had it on. To change the ASPM settings of the device you would change only the last two bits of the byte 0x80 here, so keep the other values (OR the values) as follows:

::

   # Disables ASPM, enables only L0
   sudo setpci -s 03:00.0 0x80.B=0x40

   # Enable L0s only (this was the existing setting)
   sudo setpci -s 03:00.0 0x80.B=0x41

   # Enable L1 only
   sudo setpci -s 03:00.0 0x80.B=0x42

   # Enable L1 and L0s
   sudo setpci -s 03:00.0 0x80.B=0x43

802.11 ASPM device tweaks
-------------------------

Devices are typically not expected to have to do anything for ASPM but some tuning can be done on the PCI-E devices to reprogram L0s/L1 entrance and exit latency timers, the number of FTS packets we send to exit L0s, amongst other things.

::

       * [[en/users/Drivers/ath9k/power-consumption|ath9k ASPM tunings]] - ASPM tunings for ath9k 
