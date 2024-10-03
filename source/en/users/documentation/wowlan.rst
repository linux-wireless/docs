Wake on Wireless LAN
====================

Wake on Wireless is a feature to allow the system to go into a low-power
state (e.g. ACPI S3 suspend) while the wireless NIC remains active and
does varying things for the host, e.g. staying connected to an AP or
searching for networks.

potential triggers
~~~~~~~~~~~~~~~~~~

Here's a non-exhaustive list of triggers:

- Reception of a user specified pattern (while connected)
- Reception of a Magic Packet frame (while connected)
- Disconnection from AP (while previously connected)
- Network found (while not connected and looking for networks to connect to)

configuration
~~~~~~~~~~~~~

Use iw to configure WoWLAN before going to sleep.

Going to suspend
~~~~~~~~~~~~~~~~

When the system is going to suspend, cfg80211/mac80211 will inform the
driver if WoWLAN is enabled. The driver then sets up the hardware
correctly according to the required triggers and when the bus suspend is
later invoked sets up the device as a wakeup source.

Waking up
~~~~~~~~~

When the wireless NIC detects a wakeup event, it will wake up the host
through the bus-specific methods:

* PCI-Express: The wireless device will send a PCI-Express Power
  Management Event (PME) message and/or assert the PCIE_WAKE_L signal.
  The PME message can only be sent if the device's PME Enable bit is
  set. With PCI-Express devices can still use the PCIE_WAKE_L signal
  even if the PME Enable bit is cleared.
* PCI: The wireless device will assert the PCI_PME_L signal to the PCI
  host. In order to send this signal the PME Enable bit must be enabled
  on the device. Note that on PC platforms often BIOS support is
  required for these methods.

The platform will then wake up the system and eventually the device
driver will be notified through the different resume callbacks to wake
up the device. The driver can then inform the upper layers of the reason
why it was woken up (if it received such trigger).

Random notes
~~~~~~~~~~~~

Non-WoW frames which are received are ignored (dropped), but frames
received should be ACKed by the STA wireless hardware without any help
from the host CPU.

There might be issues with multicast and broadcast frames when using
WPA/RSN if the device is not capable of rekeying -- in this case the
host must be woken up to handle the rekeying.

802.11 powersave and possibly SMPS will usually be used while suspended
to save power.

Some devices support a keep-alive frame to send to the AP, which might
be configurable. If supported, keep-alive frames will (at least for
ath9k) be sent right after a TBTT, it can be configured to be sent in
the order of 10 to 60 seconds.
