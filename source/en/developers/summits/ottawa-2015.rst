Ottawa 2015
===========

This event is going to be a 'workshop' at the `netdev 0.1 conference <https://www.netdev01.org/>`__.

Suggested topics:

-  Is wireless-testing still useful?
-  statistics - what do people need, what is useful in the current counters, what is pointless, etc.?
-  state of 802.11s implementation
-  Bob's wmediumd
-  brief look at rate statistics (johannes)
-  Intel TCP/remote wake demo?
-  secure firmware download (Kathy)
-  congestion control / "bufferbloat"
-  mac80211/driver configuration access and lack of locking
-  TSO/GSO over mac80211
-  60GHz/P2P scan&remain-on-channel flag
-  mac80211 vs. more offloads (e.g. RX) - be more flexible?
-  mac80211 to driver state/failure (auth/assoc/...) feedback operation for debug?
-  report from netconf (johannes)
-  hw address from userspace
-  new wiki
-  multiple radios / p2p-device
-  vendor extensions to existing commands/events (key mgmt offloading)
-  bt coex subsystem
-  LPC in Seattle
-  upper-layer services (P2PS, HS2 config, miracast)
-  ... (please suggest more)

Attendees:

-  Johannes Berg
-  John Linville
-  Kalle Valo
-  Bob Copeland
-  Kathy Giori
-  Avery Pennarun
-  Jouni Malinen
-  Seth Forshee
-  Eric Dumazet

Notes
'''''

-  netconf recap

   -  add sysctl knobs for client-side filtering (needing route lookup) for hotspot 2.0

      -  need to do a route lookup in ipv4 for mcast -- can't tell whether something is multicast or unicast without knowing the netmask
      -  4 new knobs

         -  drop-unicast-IPv4-in-multi/broadcast-L2 (even for RFC SHOULD compliance)

            -  originally suggested code in IP stack broke cluster ip, so sysctl needed

         -  same for IPv6
         -  drop gratuitous ARP
         -  drop unsolicited NA

   -  proxy arp
   -  perceived difficult to add stuff to bridging code
   -  some feedback from mac80211 on queuing time to improve transmit time

-  new wiki

   -  Congratulations, you're reading it!

-  wireless-testing

   -  do we keep it?

      -  no longer has nfc/bt
      -  intel is using it internally
      -  w-t stays updated with RCs while feeders are behind

   -  2 use cases:

      -  where do we point developers?
      -  where do we test recent code?

   -  intel's model:

      -  generate an internal backports tree based on w-t
      -  developers put stuff into gerrit
      -  someone takes stuff from internal tree to send it back upstream

   -  is there an alternative that's more permanent?

      -  linux-next might be a replacement if mac80211-next went into linux-next

   -  Kalle: we need it because no one has any idea which tree to use

      -  Kalle wants to keep it for forseeable future

   -  Johannes: doesn't care, if mac80211 goes into -next
   -  John: will keep it for the next year

-  TCP / congestion control -- TSO/GSO over mac80211

   -  intel: build AMSDU for TSO frames

      -  take one TSO packet, split into AMSDUs
      -  doing AMSDUs without help from TCP stack: have to have some delays, or put in HW queue to do AMPDUs
      -  problem: w/ TSO packets can get really large, AMSDUs max out at 4/8k
      -  when packets don't fit in AMSDU, we have to split them and generate new PNs. If we can guarantee TSO limit, then mac80211 can still PNs

   -  Eric: per-flow size limit for TSO/GSO exist, and packet limits, you need both to protect against peers using tiny MSS
   -  can we start small and increase size once we have some traffic with the stations?
   -  terminology: "DSO" - driver segmentation offload
   -  when doing SW crypto must linearize skbs so can't always use scatter-gather

-  Queuing

   -  2 problems:

      -  sender: might be limited by TCP small queue
      -  receiver: TCP wants to send back ACK, but half-duplex limits TCP because it doesn't send ACKs often enough. GRO partially helps. need to send tons of ACKS (1000s per sec) in reverse path so upper level of stack needs to handle it somehow

   -  delay between ACK trains should depend on RTT
   -  use xmit_more to know when to merge frames
   -  2x throughput increase with xmit_more on ethernet (on ethernet: only write the doorbell register when xmit_more is clear... 200ns to update the doorbell register by itself).
   -  must have BQL in the driver -- tells the qdisc how many bytes it can dequeue for each call into the driver. could use a static limit if we have nothing better (e.g. 64 frames)
   -  can we use something like tx rates to do better than a static BQL limit?
   -  do we expose device queues to qdisc or violate the layers to tell the qdisc what to do?
   -  Eric: qdisc is perhaps not the best model for wireless. in our case, qdisc has no idea how long frames sit in our queues. feedback needs to happen at the very head of the wireless queue to make fq_codel etc work - driver sends a callback or something... kinda tricky - right now original frame is gone, maybe split into segmented frames.
   -  Felix's approach: per-station queueing in the stack, and control bufferbloat there. don't stop netdev queues.
   -  Eric: AQM: have to install it per-station since that's where the bufferbloat is
   -  Result: we should consider Felix's approach and put queue management close to the hardware queues.

-  802.11s
-  wmediumd

   -  interesting test use cases

      -  ACS testing (channel survey)
      -  BSS selection: RSSI

-  statistics

   -  android statistics

      -  how is it defined? packets? MPDUs? MSDUs?

   -  some counters broken, not available in debugfs
   -  what do people want?
   -  should we add a capability for drivers?

      -  or just ask and don't include those we don't have?

   -  currently have survey and per-station statistics
   -  device-level counters not really anywhere (like mcast counters, which are in debugfs now)
   -  rate statistics

      -  tracking a ton of rates uses lots of kernel memory
      -  userspace subscribes to it and then gets updates when over 30 rates or overflow 16-bit counters. Maybe 16-bit counters are too small for high packet rates.

-  TCP/remote wake

   -  upstream already
   -  device starts a TCP connection and wakes up periodically to send a heartbeat; remote server can tell device to wake up

-  Secure firmware download

   -  Regulators might want to require signed firmware
   -  kernel configuration for whether or not signed firmware can be loaded
   -  can hardware enforce checks while allowing independent developers to use it? would need to give developers the signing key, defeating the purpose.
   -  Seth: distribution signs the firmware, kernel validates it

-  mac80211 driver configuration access and lack of locking

   -  intel: tracking TSF and device timestamp internally... driver and mac80211 need to be changed in sync somehow -- updated every time we get a beacon
   -  atheros: duplicating a lot of channel context stuff. How do we use mac80211 data structures inside the driver?
   -  put spinlocks/RCU in the driver? - mac80211 would implement write-side
   -  No good solution here yet

-  60 GHz / p2p

   -  Jouni: for scan - flags for specific 60 GHz rules: no CCK rates, no probe responses, must be used to follow rules. people don't really know how to use p2p-device
   -  Johannes: use p2p-device, then we don't need so many flags

-  multiple radios / p2p-device

   -  new social channel on 60 GHz
   -  some designs have separate radio for 60 GHz + 5/2.4 GHz radio (multiple phy)
   -  for p2p-device: needs to have one mac address even though there are multiple devices. Johannes: you can do that today, one p2p-device per phy

-  mac80211 driver state/failure

   -  today we collect dumps for firmware crashes (dev coredump) -- device memory, FIFOs, etc
   -  Kalle: we have debugfs file that needs converting
   -  Emmanuel is adding an event callback from mac80211 to the driver to tell it that some kind of state failed, like association failed, driver can then dump to get more debugging, e.g. good scan results but no successful association
   -  Jouni: can we use event for more than just debugging? Johannes: potentially, doing that today for RSSI for bt coex

-  hw address from userspace

   -  mfr's want to separate mac address from otp area
   -  "firmware" file that is 6 bytes long and has mac address
   -  some people don't want to add device with empty mac and configure it later
   -  using same interface as firmware loader could be problematic (e.g. would mac address files need to be signed?)
   -  is it just part of the calib data? different groups might be involved at these stages
   -  devicetree?

-  vendor extensions to existing commands (key mgmt offloads)

   -  can we make nl80211 extensible for vendors? adding "vendor data" plus OUI
   -  today, wpa_s uses own custom commands
   -  GTK rekeying offload, 4-way handshake offload
   -  how do we handle for non-upstream drivers? maintenance problems
   -  connect command passing keys and stuff
   -  new attributes in the connect and roaming events
   -  can use exisitng nl80211 attributes in vendor commands to avoid copying them? not validated
   -  problem: vendor extensions could completely change semantics?

-  bt coex subsystem

   -  wireless wants to know BT states, might not have a gpio or register in common, or be on separate chip from BT
   -  possible that BT calls some cfg80211 API, but want to avoid having some tight coupling
   -  some kind of registration thing? no decision today

-  LPC in Seattle - August 19-21st

   -  higher layer wireless stuff -- sessions for Connman
   -  do we want to do something there? Only 3 hour session at last plumbers
   -  other userspace folks there so good for upper layer stuff

-  RX optimizations

   -  receive side steering - hashing in the hardware on flows so each CPU sees a specific flow. Want to offload hardware decryption and PN check to avoid frames coming out of order, maybe A-MPDU reordering, 802.3 conversion, etc.
   -  should driver be the one that's calling all the rx handlers or do we use flags to control fastpaths?
   -  need to make sure statistics, crypto are still functional
   -  Jouni: this can cause fragmentation of features across drivers

-  opw - Jes

   -  converting orinoco to cfg80211
