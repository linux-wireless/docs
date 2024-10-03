Compat wireless old 2.6.22 bug
==============================

compat-wireless-old currently disables support for 2.6.22 because of a
kernel crash you get if its enabled. The oops is below and the exact
line where it hits is showed as well::

   wme_qdiscop_dequeue+0x120
   __qdisc_run
   ieee80211_send_probe_req+0x1a0
   ieee80211_send_probe_req+0x1a0
   dev_queue_xmit+0x218
   ieee80211_sta_scan_work+0xe6
   ieee80211_sta_scan_work+0x0
   run_workqueue+0x81

Using gdb to get the exact culprit::

   mcgrof@tesla /lib/modules/2.6.22-15-generic/updates/net/mac80211 $ gdb mac80211.ko
   GNU gdb 6.8-debian
   Copyright (C) 2008 Free Software Foundation, Inc.
   License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
   This is free software: you are free to change and redistribute it.
   There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
   and "show warranty" for details.
   This GDB was configured as "i486-linux-gnu"...
   (gdb) l *(wme_qdiscop_dequeue+0x120)
   0x18a20 is in wme_qdiscop_dequeue (/home/mcgrof/devel/compat-wireless-2.6/net/mac80211/ieee80211_i.h:768).
   warning: Source file is more recent than executable.
   763     static inline struct ieee80211_sub_if_data *
   764     IEEE80211_DEV_TO_SUB_IF(struct net_device *dev)
   765     {
   766             struct ieee80211_local *local = wdev_priv(dev->ieee80211_ptr);
   767     
   768             BUG_ON(!local || local->mdev == dev);
   769     
   770             return netdev_priv(dev);
   771     }
   772     
   (gdb) 

So line 768 is the culprit.
