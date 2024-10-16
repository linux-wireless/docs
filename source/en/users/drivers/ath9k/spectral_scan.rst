ath9k spectral scan
===================

Atheros 802.11n chipsets include a built-in spectral analysis feature.
AR92xx and AR93xx have the ability to report FFT data from the baseband
under software controlled conditions, including:

- absolute magnitude (\|i|+|q\|, abs() for I/Q phase of the wireless
  signal) for each FFT bin (56 for subcarriers in HT20 mode and 128 in
  HT40 mode)
- an index indicating the strongest FFT bin
- the maximum signal magnitude for each sample

These information can be used to create an open source spectrum analyzer
or interference classifier. To try it out, you must first have a kernel
compiled with config option ``ATH9K_COMMON_SPECTRAL`` and one or both of
``ATH9K_DEBUGFS`` and ``ATH9K_HTC_DEBUGFS``. Then you can use the
following commands to acquire samples for all channels which can be
scanned::

   echo chanscan > /sys/kernel/debug/ieee80211/phy0/ath9k/spectral_scan_ctl
   iw dev wlan0 scan
   cat /sys/kernel/debug/ieee80211/phy0/ath9k/spectral_scan0 > samples
   echo disable > /sys/kernel/debug/ieee80211/phy0/ath9k/spectral_scan_ctl

Spectral scan configuration parameters can be read and changed ``/sys/kernel/debug/ieee80211/phy0/ath9k/``:

- **spectral_count**: number of scan results requested. Note that the
  "never disable" mode is implemented through the "background" mode in
  specral_scan_ctl, see below.
- **spectral_short_repeat**: controls the short_repeat parameter, see
  "Spectral scan parameters" below
- **spectral_fft_period**: controls the *fft_period* parameter, see
  "Spectral scan parameters" below
- **spectral_period**: controls the *period* parameter, see "Spectral
  scan parameters" below
- **spectral_scan_ctl**: Contains the current mode. There are the
  following modes available:

   - ``disable``: spectral scan is disabled
   - ``background``: spectral scans samples are returned endlessly from
     the currently configured channel. It is running while the hardware
     is not busy with sending/receiving. Must be turned on by writing
     "trigger" into spectral_scan_ctl.
   - ``manual``: as many spectral scan samples as configured in
     spectral_count are returned from the current channel after writing
     "trigger" into spectral_scan_ctl.
   - ``chanscan``: as many spectral scan samples as configured in
     spectral_count are returned for each channel when performing a
     scan.

-  **spectral_scan0**: the relayfs file which returns the spectral scan samples. The samples are returned as TLV binary data, see ``drivers/net/wireless/ath/ath9k/spectral.h`` and/or ``drivers/net/wireless/ath/spectral_common.h`` for the format

Spectral scan parameters
------------------------

- *fft_period*: when active and triggered, PHY passes FFT frames to MAC every (fft_period+1)*4uS
- *period*: when active, time period between successive spectral scan entry points (period*256*Tclk). Tclk = 44MHz for HT20 operation, 88MHz for HT40 operation
- *count*: number of scan results requested. There are special meanings in some chip revisions:

   - AR92xx: highest bit set (>=128) is interpreted as "never disable"
   - AR9300 and newer: 0 is interpreted as "never disable"

- *short_repeat*: controls whether the chip is in spectral scan mode for 4 usec (enabled) or 204 usec (disabled)

Frame format
------------

HT20::

          0       1       2       3       4       5       6       7       8
          +---------------------------------------------------------------+
     0    |       [7:0]: bin -28 magnitude (|i| + |q|) >> max_exp         |
          +---------------------------------------------------------------+
     1    |       [7:0]: bin -27 magnitude (|i| + |q|) >> max_exp         |
          +---------------------------------------------------------------+
     2-54 |                                                               |
          +---------------------------------------------------------------+
     55   |       [7:0]: bin 27 magnitude (|i| + |q|) >> max_exp          |
          +---------------------------------------------------------------+
     56   |       [7:0]: all_bins {max_magnite[1:0], bitmap_weight[5:0]}  |
          +---------------------------------------------------------------+
     57   |               [7:0]: all_bins {max_magnite[9:2]}              |
          +---------------------------------------------------------------+
     58   |       [7:0]: all_bins {max_index[5:0], max_magnite[11:10]}    |
          +---------------------------------------------------------------+
     59   |                       [3:0] max_exp                           |
          +---------------------------------------------------------------+


HT40::

          0       1       2       3       4       5       6       7       8
          +---------------------------------------------------------------+
    0     |       [7:0]: bin -64 magnitude (|i| + |q|) >> max_exp         |
          +---------------------------------------------------------------+
    1     |       [7:0]: bin -63 magnitude (|i| + |q|) >> max_exp         |
          +---------------------------------------------------------------+
    2-125 |                                                               |
          +---------------------------------------------------------------+
    127   |       [7:0]: bin 63 magnitude (|i| + |q|) >> max_exp          |
          +---------------------------------------------------------------+
    128   |    [7:0]: lower_bins {max_magnite[1:0], bitmap_weight[5:0]}   |
          +---------------------------------------------------------------+
    129   |               [7:0]: lower_bins {max_magnite[9:2]}            |
          +---------------------------------------------------------------+
    130   |       [7:0]: lower_bins {max_index[5:0], max_magnite[11:10]}  |
          +---------------------------------------------------------------+
    131   |    [7:0]: upper_bins {max_magnite[1:0], bitmap_weight[5:0]}   |
          +---------------------------------------------------------------+
    132   |               [7:0]: upper_bins {max_magnite[9:2]}            |
          +---------------------------------------------------------------+
    133   |       [7:0]: upper_bins {max_index[5:0], max_magnite[11:10]}  |
          +---------------------------------------------------------------+
    134   |                       [3:0] max_exp                           |
          +---------------------------------------------------------------+

Received power computation
--------------------------

Assuming the noise floor is equal to -96dbm(\*) and the magnitude of
each sample in a 20MHz bin equals the RSSI, the received signal strength
of each FFT bin on HT20 channel can be computed as follow::

   power(i) = nf + RSSI + 10*log(b(i)^2) - bin_sum

where:

- *RSSI* is computed on control chain 0
- *b(i)* is the magnitude in each bin, unscaled by *max_exp*
- *bin_sum* = 10*log(sum[i=1..56](b(i)^2))

For 40MHz channel, previous formula should be used for 64 bins of
control and extension channels, keeping in mind for HT40+ mode the
extension channel is above the primary one (lower=ctl, upper=ext) and
for HT40- the extension channel is below the primary one (lower=ext,
upper=ctl).

(\*) nf can differ from -96dbm due to noise and spikes leading to a reduced reported RSSI.

Userspace programs
------------------

FFT samples gathered from Atheros NICs could be drawn using userspace
programs:

- https://github.com/simonwunderlich/FFT_eval (HT20 only)
- https://github.com/LorenzoBianconi/ath_spectral
- https://github.com/bcopeland/speccy

(based on Adrian Chadd's documentation
`https://wiki.freebsd.org/dev/ath_hal%284%29/SpectralScan
<https://wiki.freebsd.org/dev/ath_hal(4)/SpectralScan>`__)
