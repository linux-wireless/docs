Realtek 802.11n, 802.11ac and 802.11ax drivers
==============================================

.. toctree::

   rtl819x/devices

mac80211 based
--------------

- **rtl8192ce** is a PCI-E driver for RTL8192CE/RTL8188CE devices.
- **rtl8192cu** is a USB driver for RTL8192CU/RTL8188CU devices. It's going to be replaced by rtl8xxxu.
- **rtl8192de** is a PCI-E driver for RTL8192DE/RTL8188DE devices.
- **rtl8192se** is a PCI-E driver for RTL8192SE/RTL8191SE devices.
- **rtl8723ae** is a PCI-E driver for RTL8723AE devices.
- **rtl8723bs** is a SDIO driver for RTL8723BS devices.
- **rtl8188ee** is a PCI-E driver for RTL8188EE devices.
- **rtl8723be** is a PCI-E driver for RTL8723BE devices (**3.15+**).
- **rtl8192su** is a USB driver for RTL8188SU/RTL8191SU/RTL8192SU devices. (**WIP**: http://github.com/chunkeey/rtl8192su)
- **rtl8821ae** is a PCI-E driver for RTL8821AE devices (**3.16+**).
- **rtl8192ee** is a PCI-E driver for RTL8192EE devices (**3.16+**).
- **rtl8xxxu** is a **multi-driver** for USB devices(RTL8723AU/RTL8723BU/RTL8191EU/RTL8192EU/RTL8188EU/RTL8188RU) (**4.3+**).
- **rtw88** is a 802.11ac PCI-E driver for 8822BE, 8822CE, 8723DE and 8821CE devices, and USB(**6.2+**) driver for RTL8723DU, RTL8821CU, RTL8822BU and RTL8822CU devices.
- **rtw89** is a 802.11ax PCI-E driver for 8852AE devices.

staging drivers
---------------

* **r8192e_pci** is a PCI-E driver for RTL8192E devices. 
* **r8190_pci** is a PCI driver for RTL8190P devices (**WIP**: http://github.com/lwfinger/rtl8190p)
* **r8723bs** is a SDIO/SPI driver for RTL8723A/B devices. It's going to be replaced by rtl8xxxu.
* **r8712u** is a USB driver for RTL8712U/RTL8192SU devices. It's going to be replaced by rtl8192su.
* **r8192du** is a USB driver for RTL8192DU devices. (**WIP**: http://github.com/lwfinger/rtl8192du). It's going to be replaced by rtl8xxxu.

They are included in the **staging** tree at
https://git.kernel.org/cgit/linux/kernel/git/gregkh/staging.git and they
are NOT supported by linux-wireless developers or mailing list. Instead
ask for support in
http://driverdev.linuxdriverproject.org/mailman/listinfo/driverdev-devel.
Maintainer is Greg Kroah-Hartman <gregkh@linuxfoundation.org>.

Firmware
--------

The firmware for those devices can be downloaded from:
https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git

Available devices
-----------------

See :doc:`this page <rtl819x/devices>` for a list of devices that based
on the rtl819x chip.
