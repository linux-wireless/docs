ath10k spectral scan
====================

Atheros 802.11ac chipsets include a built-in spectral analysis feature.
They have the ability to report FFT data from the baseband under
software controlled conditions.

These information can be used to create an open source spectrum analyzer
or interference classifier

To try it out, you can use the following commands while having an open
connection (e.g. running an AP) to acquire samples for the current
channel::

     ip link set dev wlan0 up
     echo background > /sys/kernel/debug/ieee80211/phy0/ath10k/spectral_scan_ctl
     echo trigger > /sys/kernel/debug/ieee80211/phy0/ath10k/spectral_scan_ctl
     iw dev wlan0 scan
     echo disable > /sys/kernel/debug/ieee80211/phy0/ath10k/spectral_scan_ctl
     cat /sys/kernel/debug/ieee80211/phy0/ath10k/spectral_scan0 > samples</code>

Spectral scan configuration parameters can be read and changed /sys/kernel/debug/ieee80211/phy0/ath10k/:

- spectral_count: number of scan results requested. Note that the
  "never disable" mode is implemented through the "background" mode in
  specral_scan_ctl, see below. Note that the count number may be ignored
  for 20 MHz and 40 MHz for unknown reasons (see open issues below)
- spectral_bins: contains the number of bins returned in one fft
  sample. Allowed values are 64, 128, and 256. Configuring more bins
  will allow higher resolutions in the fft data. Note that configuring
  64 bins will not work with 80 MHz wide channels (the hardware reports
  samples which appear to be bogus and are not returned to userspace).
- spectral_scan_ctl: Contains the current mode. There are the following
  modes available:

    - disable: spectral scan is disabled 
    - background: spectral scans samples are returned endlessly from the
      currently configured channel. It is running while the hardware is
      not busy with sending/receiving. Must be turned on by writing
      "trigger" into spectral_scan_ctl. 
    - manual: as many spectral scan samples as configured in
      spectral_count are returned from the current channel after writing
      "trigger" into spectral_scan_ctl. 

- spectral_scan0: the relayfs file which returns the spectral scan
  samples. The samples are returned as TLV binary data, see
  drivers/net/wireless/ath/spectral_common.h for the format 

Open issues
-----------

The spectral count issue
~~~~~~~~~~~~~~~~~~~~~~~~

Even when a count is specified, the hardware seems to send endless
samples. It seems to work most of the time in VHT80 mode though, but in
HT20 and HT40 the count value seems to be ignored. To reproduce this,
start hostapd with the desired channel width and do::

   echo 8 > /sys/kernel/debug/ieee80211/phy0/ath10k/spectral_count
   echo manual > /sys/kernel/debug/ieee80211/phy0/ath10k/spectral_scan_ctl
   echo trigger > /sys/kernel/debug/ieee80211/phy0/ath10k/spectral_scan_ctl
   cat /sys/kernel/debug/ieee80211/phy0/ath10k/spectral_scan0 >> /tmp/fft.dump

Repeating the last line and checking the filesize will easily show
whether ath10k still sends samples or not. We would expect 8 samples in
this configuration.

Userspace programs:
-------------------

FFT samples gathered from Atheros NICs could be drawn using userspace
programs:

-  https://github.com/simonwunderlich/FFT_eval
