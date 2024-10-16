mac80211 driver API notes
=========================

There surely are errors and omissions in this list, please help. Also,
if you maintain a driver, please look through this list.

A driver must (alternatives in order of preference)

-  set the IEEE80211_HW_2GHZ_SHORT_PREAMBLE_INCAPABLE hw flag if it cannot receive short preamble transmissions
-  either honour the IEEE80211_TX_RC_USE_RTS_CTS flag or implement the set_rts_threshold call
-  either honour the IEEE80211_TX_RC_USE_CTS_PROTECT flag or honour bss_conf's use_cts_prot value
-  honour bss_conf's use_short_slot or set the IEEE80211_HW_2GHZ_SHORT_SLOT_INCAPABLE hw flag
-  honour bss_conf's basic_rates bitmap to set up the control response frame bitrate (cf. IEEE 802.11-2007 9.6 "Multirate support" paragraph 7)
-  honour IEEE80211_TX_CTL_NO_ACK unless the hardware does based on the multicast bit
-  honour IEEE80211_TX_CTL_ASSIGN_SEQ (only if you implement any mode that requires beaconing)
-  honour IEEE80211_TX_CTL_REQ_TX_STATUS or always report TX status
-  not change it's operating mode based on IEEE80211_CONF_RADIOTAP
-  clear/set MAC address filters/control response frame generation based on the interface add/remove callbacks
-  set up beacon access parameters based on the interface mode (ibss/ap)
-  use SET_IEEE80211_DEV and SET_IEEE80211_PERM_ADDR
-  set the wiphy interface modes
-  ... It also should

   -  honour IEEE80211_TX_RC_USE_SHORT_PREAMBLE or honour bss_conf's use_short_preamble
   -  set one of the IEEE80211_HW_SIGNAL\_\* hw flags, preferably support dBm For QoS/WME, it must

      -  support at least four queues
      -  support configurable access parameters for those queues
      -  not override the sequence numbers on frames that don't have the IEEE80211_TX_CTL_ASSIGN_SEQ flag set
      -  ... For AP mode, it must

         -  honour IEEE80211_TX_CTL_SEND_AFTER_DTIM or set IEEE80211_HW_HOST_BROADCAST_PS_BUFFERING and use the ieee80211_get_buffered_bc() function
         -  must honour IEEE80211_TX_RC_USE_SHORT_PREAMBLE or never do short-preamble transmissions
         -  When sending probe response frames, the timestamp must be adjusted by the hardware or firmware. This is important to power saving stations that happen to adjust their TSF from the timestamp in the probe response frame.
         -  implement sequence numbering for frames with the IEEE80211_TX_CTL_ASSIGN_SEQ flag (or ask the hardware to do it for those frames)
         -  react to the set_tim() callback or fetch each beacon from mac80211 For MESH mode, it must

            -  allow beacons to be transmitted for NL80211_IFTYPE_MESH_POINT interfaces. These can be AP or IBSS style beacons.
            -  receive beacons and control frames for NL80211_IFTYPE_MESH_POINT interfaces
            -  set the NL80211_IFTYPE_MESH_POINT bit in the hw->wiphy->interface_modes mask to indicate that MP mode is supported.
            -  support the FIF_OTHER_BSS filter flag For AP/IBSS/MESH modes, it

               -  must support the enable_beacon config to turn on/off beaconing
               -  should support the tx_last_beacon() callback When implementing hardware crypto, it must

                  -  leave the protected bit set in decrypted frames For HT, it must

                     -  support QoS
                     -  [need help, Tomas/Ron?]
                     -  ... For spectrum management, it must

                        -  [unfinished]
                        -  ...
