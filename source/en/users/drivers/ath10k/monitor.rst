ath10k monitor mode
===================

ath10k supports monitor mode. Recommended firmware version for a sniffer
is 10.1.467.2-1. Also use recent enough wireshark which supports 11ac.

To tune into 80 MHz channel, in this example channel 36 (5180 MHz)::

   ip link set wlan0 down
   iw wlan0 set type monitor
   ip link set wlan0 up
   iw wlan0 set freq 5180 80 5210

To capture HT40+ on channel 36::

   iw wlan0 set freq 5180 40 5190

Known issues
~~~~~~~~~~~~

- Assoc Request frames not captured (Assoc Response shows up fine)
- cannot see Add BA action frames
- frames do not come up with FCS value in them
- the management frames do not contain mac timestamp as data/control frames
