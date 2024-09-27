Firmware versioning best practices
----------------------------------

On this page we document how you should deal with firmware versioning for both proprietary firmware and open firmware for 802.11 and the Bluetooth subsystems of the Linux kernel. This includes aspects regarding API changes in the firmware and changes when you do not make API changes.

Firmware file guidelines for 802.11
-----------------------------------

Firmware API and version numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You should use foo-apiversion-codeversion.fw . The apiversion would change when there are API changes within the firmware that require actual driver changes. If you are just doing simple updates you would just bump up the codeversion. The driver can then simply use the API version for the actual filename and it can be symlinked to the latest codeversion for that API.

For example say you have a firmware on API 3, and its code revision is 1.4.1. The firmware would be named:

::

   foo-3-1.4.1.fw

As a short hand this would be symlinked to:

::

   foo-3.fw

API and version number bumps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The general rule of thumb is that if you break or change the firmware API firmware name that the driver uses should change, the API number being bumped once. For example if you have some new driver functionality that requires new firmware then you should use a new firmware name. If your firmware code changes do not involve breaking the driver API then you can keep the API version the same. It is up to you how you deal with the code version changes.

In general if you are just providing bug fixes you do not need to provide a new firmware filename for the module, using the old filename is fine so long as the same API was kept.

Deprecating old firmware APIs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TBD

Firmware file guidelines for Bluetooth
--------------------------------------

Bluetootooth devices end up working with the Linux kernel using HCI so typically all you need to do is upload the firmware for a device and then let the Bluetooth subsystem take over. Since the API is static and standard you should always use one filename for firmware for Bluetooth devices and simply replace the old firmware with a new firmware on the linux-firmware.git tree.
