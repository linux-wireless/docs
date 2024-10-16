ath6kl Architecture
===================

AR600x software is partitioned into host-side and target-side software.
The host side software or the driver is provided as a reference
implementation for selected platforms/OSes including Linux. The current
avatar of Linux driver is referred to as 'ath6kl' or the Legacy driver
for AR600x family of chips. The target-side software or the firmware
runs on the cbhip's network processor and is stored in the target
memory. It is a maintained by Atheros and is released as binary only.

The 'ath6kl' driver is organized into the following layers which
collectively define the host software stack. In general, functions in
the highest layer may call other functions at the same layer or one
layer down. Functions do not make direct calls to higher layers, though
upper layers may register callbacks with lower layers. A brief summary
of the driver components is given below.

.. image:: ../../../../media/en/users/drivers/driver-arch.png

Wireless Device Driver
~~~~~~~~~~~~~~~~~~~~~~

Bridges the control and data paths between the kernel and the HTC/WMI
layers. On the control path, it handles both the vendor specific
proprietary ioctls and the standard ones defined under wireless
extensions. The layer also implements the CFG80211 APIs and therefore
provides support for nl80211 based applications. On the data path it
handles the data between the HTC layer and IP stack. The relevant
sources are present in the ath6kl/os/linux/ directory.

Wireless Module Interface (WMI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the wireless application must send control messages to the AR600x
chipset, it calls into the WMI to create the messages. This layer
understands the host/target messaging protocol (WMI Protocol) and its
source is in the ath6kl/wmi/ directory. The header files
ath6kl/include/wmi.h and ath6kl/include/wmix.h list all messages from
host to target (commands) and from target to host (requests and events).

Host/Target Communication (HTC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The wireless device driver calls into HTC to handle message transport.
HTC does not understand the contents of messages it transports (only WMI
understands the contents of control messages), but it does understand
the mechanics of messaging with the AR600x chipset. It handles flow
control and knows which chipset addresses must be read and written to
relay messages. This layer source is in the ath6kl/htc2/ directory.

Host Interconnect Framework (HIF)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

HTC calls into the HIF layer when it needs to access the chipset address
space. An HIF implementation exists for each combination of platform and
interconnect API (e.g., HIF for Linux standard SDIO/MMC stack). This
layer abstracts away register and memory access details and provides an
interconnect-independent and platform-independent API for use (mainly)
by HTC. This layer source is in the ath6kl/hif/ directory.

Physical Interconnect
~~~~~~~~~~~~~~~~~~~~~

The HIF layer relies on underlying interconnect-specific and
platform-specific software to drive a hardware controller of some sort.
The interconnect layer plays a role in device discovery, setting up an
appropriate address space mapping and performing reads/writes through
that address space, and deals with error management over the physical
connection. For most serial buses, the HIF layers interfaces with a bus
driver that provides an abstracted view of the underlying host bus
adapter. These bus drivers may be provided by partners, OS vendors, or
Atheros.
