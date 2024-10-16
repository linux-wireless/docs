ath6kl todo
===========

Cleanup items
-------------

High priority:

- cleanup locking

    - review all locking
    - document what each lock is supposed to protect
    - try to reduce the number of locks, semaphores and mutexes
    - convert semaphores to mutexes
    - the DMA bounce buffer should probably be protected by a lock so
      dueling threads don't corrupt it

- use ath6kl prefix everywhere
- Implement 802.11 ieee disconnect reasons
- high coupling between main.c and init.c
- confusion with header files

    - function prototypes not in corresponding .h files
    - no core.h
    - no init.h
    - no main.h
    - no txrx.h

- merge structs

    - merge struct htc_target to struct ath6kl
    - merge struct ath6kl_device to struct ath6kl
    - merge struct aggr_info to struct ath6kl
    - merge struct wmi to struct ath6kl

- replace all void pointers with proper types

    - for example, use property or unions
    - if not possible for some reason, then document properly what types void pointer might contain

        - (There are about three void pointers in htc.h, this would result in significant amount of cleanup)

- remove nl80211_tx_power_setting comment
- ath6kl_cfg80211_change_iface() needs to change mode before function returns
- useless memset(ar->ssid, 0, sizeof(ar->ssid))
- ath6kl_cfg80211_get_key() should not call the callback in the -ENOENT case
- remove ieee80211com from a comment
- ath6kl_priv() should return a proper type
- scat_list should be scat_list[ ATH6KL_SCATTER_ENTRIES_PER_REQ] rather than scat_list[1]
- memcpy mess in htc_setup_tx_complete()
- ath6kl_cleanup_amsdu_rxbufs is racy

    - can't drop lock with list_for_each macros

- list_empty() in ath6kl_alloc_amsdu_rxbuf() is useless

    - you can iterate an empty list

- use ieee80211_data_to_8023()

    - instead of ath6kl_wmi_dot11_hdr_remove()

Low priority:

- use align macro in aggr_slice_amsdu()
- clean up arEvent usage
- clean up wmitimeout usage
- remove mdelay()
- remove casts from ar6k_priv() users
- cleanup wait_event apis
- bmi: use struct for commands, not memcpy()
- fix 0x%lX debug format

    - use %p
    - remove (unsigned long) casts
    - use decimals when printing lengths

- change all read/write functions' buf to a void pointer
- move WARN_ON() inside if test
- cleanup ath6kl_init_netdev() & co
- replace ntohs() with be16_to_cpu()
- rename wmip to wmi
- ath6kl firmware fetch fails if it's linked to kernel (Y choise)
- ATH_COMMON kconfig enables some code which is not needed by ath6kl
- fix all FIXMEs
- remove ath6kl_cookie (vasanth)

    - needs significant code change

- inspect structs for alignment and packing appropiateness

    - http://marc.info/?l=linux-wireless&m=131053135626622&w=2

- switch from cfg80211_inform_bss_frame() to cfg80211_inform_bss()

    - was there a reason why we actually need \_frame() variant?

- logic in htc_tx_from_ep_txq() is convoluted
- buffer tx packets

    - to improve throughput and avoid excessive stopping of queues

- create separate queues for each AC

    - so that they can be stopped individually

- use of ar->nw_type is not consistent

    -  some places we test it with '==' even though '&' should be used as it's a bitfield

- interface to enable tx uart with hi_serial_enable register

    - maybe using debugfs? Then an item is done, please mark it with
      [STRIKEOUT:strike through].

If you plan to work on something, please mark the item with "(nick)".
