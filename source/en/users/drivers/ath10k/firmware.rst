Go back --> :doc:`ath10k <../ath10k>`

ath10k firmware
---------------

The ath10k firmware images are available from `linux-firmware.git <https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/>`__ which all common Linux distributions should install by default. Latest firmware images can be downloaded from `ath10k-firmware.git <https://git.codelinaro.org/clo/ath-firmware/ath10k-firmware>`__ from which they get eventually pushed to `linux-firmware.git <https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/>`__.

Firmware API versions
---------------------

Because firmware changes between versions we have introduced firmware API concept to ath10k. This makes it possible to support different versions of ath10k.

Firmware API 1
~~~~~~~~~~~~~~

The first version. Firmware images are in separate files: firmware.bin and otp.bin. There's no FW IE support. Deprecated since March 2014 and removed on March 2016.

Firmware API 2
~~~~~~~~~~~~~~

Embedding both firmware and otp images into same file firmware-2.bin. Firmware meta data provided through FW IE. Added in commit 1a222435a dated Sep 27 2013, for Linux 3.13. Deprecated, no new firmware releases use this anymore.

Firmware API 3
~~~~~~~~~~~~~~

Adding support for 10.2 firmware for QCA988X and ATH10K_FW_FEATURE_WMI_10_2 feature for 10.2 WMI mappings. Added in commit 24c88f7807fb7 dated Jul 27 2014. Deprecated, no new firmware releases use this anymore.

Firmware API 4
~~~~~~~~~~~~~~

Adding support for ATH10K_FW_IE_WMI_OP_VERSION. Added in commit 4a16fbec1cd0a dated December 17th 2014.

Firmware API 5
~~~~~~~~~~~~~~

Adding support for ATH10K_FW_IE_HTT_OP_VERSION, needed to support 10.2.4.48-2 on QCA988X. Added in commit 53513c302f35e March 25 2015.

Firmware API 6
~~~~~~~~~~~~~~

Workaround for board id being zero on QCA6174 hw3.0 starting from firmware release WLAN.RM.4.4-00022-QCARMSWPZ-2. Added in commit aad1fd7f7677 April 19 2017, first release v4.12-rc1.

Also for QCA9377 hw1.0 fix IRAM bank compatibility starting from firmware release WLAN.TF.2.1-00014-QCARMSWP-1. Added in commit fc8b92635f79 February 2018, first release v4.17-rc1.
