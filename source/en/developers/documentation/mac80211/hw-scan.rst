HW-Scan
=======

<seqdia> title "scanning (with device offload)"

participant userspace participant mac80211 participant driver

userspace->mac80211: scan request note over mac80211: split into bands, add IEs alt for each band mac80211->driver: hw_scan() note over driver: execute scan driver->mac80211: ieee80211_scan_completed() end mac80211->userspace: scan done </seqdia>
