ath10k driver
=============

Building
~~~~~~~~

To build ath10k enable these kernel build configuration options, for example with make menuconfig:

- CONFIG_ATH10K
- CONFIG_ATH10K_PCI
- CONFIG_ATH10K_DEBUG (optional)
- CONFIG_ATH10K_DEBUGFS (optional)
- CONFIG_ATH10K_TRACING (optional) The debug and tracing options are optional, but it's strongly recommended to enable to make it easier to debug issues.

ath10k options can be found from location::

   -> Device Drivers
    -> Network device support (NETDEVICES [=y])
      -> Wireless LAN (WLAN [=y])
        -> Atheros Wireless Cards (ATH_CARDS [=m])

Loading the modules
~~~~~~~~~~~~~~~~~~~

The ath10k modules should be loaded automatically in most systems. If
that's not happening, first load ath10k_core.ko and then ath10k_pci.ko.

hostapd
-------

ath10k uses the standard :doc:`upstream hostapd
<../../documentation/hostapd>`. For features like 802.11ac, DFS or ACS
please use hostapd 2.2 or later.

Building hostapd
~~~~~~~~~~~~~~~~

When building hostapd enable these configuration options::

     * CONFIG_IEEE80211AC 
     * CONFIG_ACS 

Configuring hostapd
~~~~~~~~~~~~~~~~~~~

Example hostapd config to use 11ac VHT80 mode with ath10k::

   interface=wlan0
   driver=nl80211

   ssid=ath10k-test

   hw_mode=a
   channel=36
   ht_capab=[HT40+]
   ieee80211n=1
   ieee80211ac=1
   vht_oper_chwidth=1
   vht_oper_centr_freq_seg0_idx=42

vht_oper_centr_freq_seg0_idx is calculated for VHT80 with channel + 6.
If you get "set channel failed to set in kernel" error message, most
likely your regulatory database doesn't support 80 MHz channels.

To enable ACS set channel to zero::

   channel=0

To enable DFS enable 11d and 11h as well as set country code::

   country_code=FI
   ieee80211d=1
   ieee80211h=1

Current implementation of ath radar pattern detector supports only ETSI
regulatory domain. It means radar detection works only when master
region is set to ETSI. It can be done by setting regulatory domain to
country from Europe (DE, FI, FR, PL, ...)::

    iw reg set DE

Other regulatory domains like JP (Japan), US (FCC master region) are
currently not supported. Starting AP on DFS channel in DFS master region
different that ETSI will cause radar event at first suspicious RF signal
even it was not radar.

See :doc:`hostapd wiki page <../../documentation/hostapd>` and
`hostapd.conf documentation
<http://hostap.epitest.fi/gitweb/gitweb.cgi?p=hostap.git;a=blob_plain;f=hostapd/hostapd.conf>`__
for more information.

Mu-MIMO configuration
~~~~~~~~~~~~~~~~~~~~~

To enable Mu-MIMO configuration::

    vht_capab=[MAX-MPDU-11454][RXLDPC][SHORT-GI-80][TX-STBC-2BY1][RX-STBC-1][MAX-A-MPDU-LEN-EXP7][RX-ANTENNA-PATTERN][TX-ANTENNA-PATTERN][SU-BEAMFORMER][SU-BEAMFORMEE][MU-BEAMFORMER][MU-BEAMFORMEE][BF-ANTENNA-4][SOUNDING-DIMENSION-4]

The values for "BF-ANTENNA" and "SOUNDING-DIMENSION" refer to the number
of radio chains. Here the value is used as 4 which means that the target
has 4 radio chains.

mBSSID
~~~~~~

Multiple BSSID (mBSSID) is a feature where you can have multiple virtual
APs on one physical device. Here is an example how you can dynamically
create and remove virtual APs.

ath10.conf is the master device, as of this writing (2014-11-19) you
cannot remove this while hostapd is running::

   interface=wlan0
   driver=nl80211
   ctrl_interface=/var/run/hostapd

   ssid=ath10k
   bssid=02:00:00:00:03:00

   hw_mode=a
   channel=36
   ht_capab=[HT40+]
   ieee80211n=1
   ieee80211ac=1
   vht_oper_chwidth=1
   vht_oper_centr_freq_seg0_idx=42

   wpa=3
   wpa_passphrase=1234567890
   wpa_key_mgmt=WPA-PSK
   wpa_pairwise=TKIP CCMP
   rsn_pairwise=CCMP

ath10k-1.conf, the first virtual AP::

   interface=wlan0-1

   ssid=ath10k-1
   bssid=02:00:00:00:03:01

ath10k-2.conf, the second virtual AP::

   interface=wlan0-2

   ssid=ath10k-2
   bssid=02:00:00:00:03:02

   wpa=2
   wpa_passphrase=0987654321
   wpa_key_mgmt=WPA-PSK
   rsn_pairwise=CCMP

For mBSSID start hostapd using -b switch::

   hostapd -g /var/run/hostapd/global -b phy0:ath10k.conf -b phy0:ath10k-1.conf -b phy0:ath10k-2.conf

To remove an interface::

   wpa_cli -g /var/run/hostapd/global raw REMOVE wlan0-2

To add an interface::

   wpa_cli -g /var/run/hostapd/global raw ADD bss_config=phy0:ath10k-2.conf

Full hostapd configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is the full hostapd configuration file which enables all features
ath10k supports.

::

   ### hostapd configuration file
   ctrl_interface=/var/run/hostapd
   interface=wlan0
   driver=nl80211
   bridge=br-lan

   ### IEEE 802.11
   ssid=ath10k
   hw_mode=a
   channel=0
   max_num_sta=128
   auth_algs=1
   disassoc_low_ack=1

   ### DFS
   ieee80211h=1
   ieee80211d=1
   country_code=FR

   ### IEEE 802.11n
   ieee80211n=1
   ht_capab=[HT40+][LDPC][SHORT-GI-20][SHORT-GI-40][TX-STBC][RX-STBC1][DSSS_CCK-40]

   ### IEEE 802.11ac
   ieee80211ac=1
   vht_oper_chwidth=1
   vht_capab=[MAX-MPDU-11454][RXLDPC][SHORT-GI-80][TX-STBC-2BY1][RX-STBC-1][MAX-A-MPDU-LEN-EXP7][RX-ANTENNA-PATTERN][TX-ANTENNA-PATTERN]

   ### WPA/IEEE 802.11i
   wpa=2
   wpa_key_mgmt=WPA-PSK
   wpa_passphrase=12345678
   wpa_pairwise=CCMP

   ### Wi-Fi Protected Setup (WPS)
   wps_state=2
   ap_setup_locked=0
   wps_pin_requests=/var/run/hostapd_wps_pin_requests
   device_name=QCA Access Point
   manufacturer=Qualcomm Atheros
   device_type=6-0050F204-1
   config_methods=virtual_push_button physical_push_button label keypad virtual_display
   pbc_in_m1=1
   ap_pin=12345670
   upnp_iface=br-lan
   eap_server=1

   ### hostapd event logger configuration
   logger_syslog=127
   logger_syslog_level=2
   logger_stdout=127
   logger_stdout_level=2

   ### WMM
   wmm_enabled=1
   uapsd_advertisement_enabled=1
   wmm_ac_bk_cwmin=4
   wmm_ac_bk_cwmax=10
   wmm_ac_bk_aifs=7
   wmm_ac_bk_txop_limit=0
   wmm_ac_bk_acm=0
   wmm_ac_be_aifs=3
   wmm_ac_be_cwmin=4
   wmm_ac_be_cwmax=10
   wmm_ac_be_txop_limit=0
   wmm_ac_be_acm=0
   wmm_ac_vi_aifs=2
   wmm_ac_vi_cwmin=3
   wmm_ac_vi_cwmax=4
   wmm_ac_vi_txop_limit=94
   wmm_ac_vi_acm=0
   wmm_ac_vo_aifs=2
   wmm_ac_vo_cwmin=2
   wmm_ac_vo_cwmax=3
   wmm_ac_vo_txop_limit=47
   wmm_ac_vo_acm=0

   ### TX queue parameters
   tx_queue_data3_aifs=7
   tx_queue_data3_cwmin=15
   tx_queue_data3_cwmax=1023
   tx_queue_data3_burst=0
   tx_queue_data2_aifs=3
   tx_queue_data2_cwmin=15
   tx_queue_data2_cwmax=63
   tx_queue_data2_burst=0
   tx_queue_data1_aifs=1
   tx_queue_data1_cwmin=7
   tx_queue_data1_cwmax=15
   tx_queue_data1_burst=3.0
   tx_queue_data0_aifs=1
   tx_queue_data0_cwmin=3
   tx_queue_data0_cwmax=7
   tx_queue_data0_burst=1.5

When the client side interface is included in a bridge, add -b
<bridge_interface> when running wpa_supplicant. Please add the following
on hostapd.conf to enable 4-address mode::

   wds_sta=1
