Interface-specific methods provided by the driver
=================================================

(open entries indicate need to research more)

.. list-table::
   :header-rows: 1

   -
      - method
      - station/P2P-client
      - AP/GO
      - IBSS
      - mesh
      - P2P-Device
      - OCB
   -
      - add_key
      - y
      - y
      - y
      - y
      -
      -
   -
      - get_key
      - y
      - y
      - y
      - y
      -
      -
   -
      - del_key
      - y
      - y
      - y
      - y
      -
      -
   -
      - set_default_key
      -
      -
      -
      -
      -
      -
   -
      - set_default_mgmt_key
      -
      -
      -
      -
      -
      -
   -

      - start_ap
      -
      - y
      -
      -
      -
      -
   -

      - change_beacon
      -
      - y
      -
      -
      -
      -
   -

      - stop_ap
      -
      - y
      -
      -
      -
      -
   -

      - add_station
      - TDLS
      - w/o SME
      - ?
      -
      -
      -
   -

      - del_station
      - TDLS
      - w/o SME
      - ?
      -
      -
      -
   -

      - change_station
      - TDLS?
      - w/o SME
      - ?
      -
      -
      -
   -

      - get_station
      - y
      - y
      - y
      -
      -
      -
   -

      - dump_station
      - y
      - y
      - y
      -
      -
      -
   -

      - add_mpath
      -
      -
      -
      - y
      -
      -
   -

      - del_mpath
      -
      -
      -
      - y
      -
      -
   -

      - change_mpath
      -
      -
      -
      - y
      -
      -
   -

      - get_mpath
      -
      -
      -
      - y
      -
      -
   -

      - dump_mpath
      -
      -
      -
      - y
      -
      -
   -

      - get_mpp
      -
      -
      -
      - y
      -
      -
   -

      - dump_mpp
      -
      -
      -
      - y
      -
      -
   -

      - get_mesh_config
      -
      -
      -
      - y
      -
      -
   -

      - update_mesh_config
      -
      -
      -
      - y
      -
      -
   -

      - join_mesh
      -
      -
      -
      - y
      -
      -
   -

      - leave_mesh
      -
      -
      -
      - y
      -
      -
   -

      - join_ocb
      -
      -
      -
      -
      -
      - y
   -

      - leave_ocb
      -
      -
      -
      -
      -
      - y
   -

      - change_bss
      -
      - y
      -
      -
      -
      -
   -

      - set_txq_params
      -
      - y
      -
      -
      -
      -
   -

      - scan
      - y
      -
      -
      -
      -
      -
   -

      - auth
      - [1]
      -
      -
      -
      -
      -
   -

      - assoc
      - [1]
      -
      -
      -
      -
      -
   -

      - deauth
      - [1]
      -
      -
      -
      -
      -
   -

      - disassoc
      - [1]
      -
      -
      -
      -
      -
   -

      - connect
      - [2]
      -
      -
      -
      -
      -
   -

      - disconnect
      - [2]
      -
      -
      -
      -
      -
   -

      - join_ibss
      -
      -
      - y
      -
      -
      -
   -

      - leave_ibss
      -
      -
      - y
      -
      -
      -
   -

      - set_mcast_rate
      -
      -
      -
      -
      -
      -
   -

      - set_tx_power
      -
      -
      -
      -
      -
      -
   -

      - get_tx_power
      -
      -
      -
      -
      -
      -
   -

      - set_bitrate_mask
      -
      -
      -
      -
      -
      -
   -

      - set_pmksa
      -
      -
      -
      -
      -
      -
   -

      - del_pmksa
      -
      -
      -
      -
      -
      -
   -

      - flush_pmksa
      -
      -
      -
      -
      -
      -
   -

      - remain_on_channel
      -
      -
      -
      -
      - y
      -
   -

      - cancel_remain_on_channel
      -
      -
      -
      -
      - y
      -
   -

      - mgmt_tx
      -
      -
      -
      -
      - y
      -
   -

      - mgmt_tx_cancel_wait
      -
      -
      -
      -
      - y
      -
   -

      - set_power_mgmt
      - y
      -
      -
      -
      -
      -
   -

      - set_cqm_rssi_config
      -
      -
      -
      -
      -
      -
   -

      - set_cqm_txe_config
      -
      -
      -
      -
      -
      -
   -

      - mgmt_frame_register
      - y
      - y
      -
      -
      - y
      -
   -

      - sched_scan_start
      -
      -
      -
      -
      -
      -
   -

      - sched_scan_stop
      -
      -
      -
      -
      -
      -
   -

      - set_rekey_data
      -
      -
      -
      -
      -
      -
   -

      - tdls_mgmt
      -
      -
      -
      -
      -
      -
   -

      - tdls_oper
      -
      -
      -
      -
      -
      -
   -

      - probe_client
      -
      -
      -
      -
      -
      -
   -

      - set_noack_map
      -
      -
      -
      -
      -
      -
   -

      - get_channel
      -
      -
      -
      -
      -
      -
   -

      - start_p2p_device
      -
      -
      -
      -
      -
      -
   -

      - stop_p2p_device
      -
      -
      -
      -
      -
      -
   -

      - set_mac_acl
      -
      -
      -
      -
      -
      -
   -

      - start_radar_detection
      -
      -
      -
      -
      -
      -
   -

      - update_ft_ies
      -
      -
      -
      -
      -
      -
   -

      - crit_proto_start
      -
      -
      -
      -
      -
      -
   -

      - crit_proto_stop
      -
      -
      -
      -
      -
      -
   -

      - set_coalesce
      -
      -
      -
      -
      -
      -
   -

      - channel_switch
      -
      -
      -
      -
      -
      -
   -

      - set_qos_map
      -
      -
      -
      -
      -
      -
   -

      - set_ap_chanwidth
      -
      -
      -
      -
      -
      -
   -

      - add_tx_ts
      -
      -
      -
      -
      -
      -
   -

      - del_tx_ts
      -
      -
      -
      -
      -
      -
   -

      - tdls_channel_switch
      -
      -
      -
      -
      -
      -
   -

      - tdls_cancel_channel_switch
      -
      -
      -
      -
      -
      -

[1], [2]: one set of these two is required
