pktgen
------

Using pktgen with mac80211_hwsim
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using pktgen together with :doc:`mac80211_hwsim <../users/drivers/mac80211_hwsim>` allows to accurately measure the performance impact of code changes onto the rx and tx path of mac80211 (without outside influences that would happen with real devices like interference).

In order to run pktgen through mac80211 we need to set up for example one AP (wlan0) and one station (wlan1) interface (see :doc:`mac80211_hwsim <../users/drivers/mac80211_hwsim>`).

First, load the pktgen module:

::

   modprobe pktgen

Set up pktgen to use wlan1 as transmitter:

::

   cd /proc/net/pktgen
   echo "rem_device_all" > kpktgend_0
   echo "add_device wlan1" > kpktgend_0

Now set up some parameters (frame size, number of buffers to send etc.):

::

   echo "count 10000" > wlan1
   echo "pkt_size 600" > wlan1
   echo "dst 192.168.1.1" > wlan1
   echo "dst_mac 01:02:03:04:05:06" > wlan1

If you want the AP interface to receive the frames use the AP interface MAC address as dst_mac.

Start transmitting:

::

   echo "start" > pgctrl

The results can be read afterwards using:

::

   > cat wlan1
   Params: count 100000 min_pkt_size: 600 max_pkt_size: 600
    frags: 0 delay: 0 clone_skb: 0 ifname: wlan1
    flows: 0 flowlen: 0
    queue_map_min: 0 queue_map_max: 0
    dst_min: 192.168.1.1 dst_max: 
    src_min: src_max: 
    src_mac: 02:00:00:00:01:00 dst_mac: 02:00:00:00:00:00
    udp_src_min: 9 udp_src_max: 9 udp_dst_min: 9 udp_dst_max: 9
    src_mac_count: 0 dst_mac_count: 0
    Flags: 
   Current:
    pkts-sofar: 100000 errors: 0
    started: 409540069us stopped: 424989620us idle: 12551us
    seq_num: 100001 cur_dst_mac_offset: 0 cur_src_mac_offset: 0
    cur_saddr: 0x201a8c0 cur_daddr: 0xff01a8c0
    cur_udp_dst: 9 cur_udp_src: 9
    cur_queue_map: 0
    flows: 0
   Result: OK: 15449550(c15436999+d12551) nsec, 100000 (600byte,0frags)
    6472pps 31Mb/sec (31065600bps) errors: 0

Links
~~~~~

`pktgen <http://www.linuxfoundation.org/collaborate/workgroups/networking/pktgen>`__
