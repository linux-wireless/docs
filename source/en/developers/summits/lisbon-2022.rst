2022 Wireless workshop in Lisbon
================================

Logistics
---------

Netdev 0x16 is in Lisbon, Portugal, from October 24th to 28th:

http://netdevconf.org/0x16/

We will have a wireless workshop there:

https://netdevconf.info/0x16/session.html?Wireless-Workshop

Formalities are as usual - open (discussion) session, you only have to be registered for netdev to attend (but you can add yourself below so we have an idea of who's coming to talk about what).

Topics
------

Add a proposed topic to the list below you would like to discuss in the workshop. Include your name so that we know who added it!

-  Wi-Fi 7 (EHT) support (Kalle)

   -  EHT puncturing (Johannes)

-  improved module parameters (Kalle)
-  keeping MAINTAINERS file up-to-date (Kalle)

Planning to attend
------------------

-  Kalle Valo
-  Jouni Malinen

Agenda
------

-  Wi-Fi 7 (EHT & MLO) support (Kalle)

   -  EHT puncturing (Johannes)
   -  IGMP Tx path for AP MLO
   -  MLO and 4-addr frames
   -  RX deduplication of multicast
   -  AP RX of unicast addr for each affiliated link (e.g., for RSN preauth) with one netdev
   -  BSS color change
   -  CSA
   -  Radar detection
   -  Mac80211 rate scaling
   -  Unicast TX link selection
   -  Dynamic link management
   -  Mesh? Anything to discuss?

-  improved module parameters (Kalle)
-  keeping MAINTAINERS file up-to-date (Kalle)
-  state of wireless? pros and cons of shared tree? (Kalle)
-  P802.11bh (how to handle random MAC addresses on the AP side)
-  P802.11bi / privacy improvements (STA and also AP)
-  Wi-Fi 6E (6&7 GHz)

   -  AFC
   -  Power modes - LPI, VLP, …

Minutes
-------

Wi-Fi 7 (EHT & MLO) support
^^^^^^^^^^^^^^^^^^^^^^^^^^^

EHT puncturing
''''''''''''''

AP vs. STA use cases somewhat different

Kernel interface might not matter (AP gets configured from user space; STA gets configured automatically by association information), but there is impact to kernel internal implementation/data structures in mac80211 and to some extent in cfg80211 and channel context.

STA issue with virtual case where two netdevs are used and the channel context combination may look incompatible with hw capabilities due to mismatching puncturing patterns. The same channel context is shared by the virtual STA netdevs, so complexities in encoding the puncturing pattern there.

Two patches under review pending determination on what to do,

Try to get the review discussion going forward on the mailing list.

IGMP Tx path for AP MLO / multicast delivery
''''''''''''''''''''''''''''''''''''''''''''

AP MLD can have multiple links (e.g., 2.4, 5, and 6 GHz) and non-AP MLDs/STAs may connect to different combinations of those affiliated links. On which links would the AP transmit multicast frames, e.g., when a STA that is associated only on the 6 GHz link has joined a specific multicast group; no point in sending multicast frames for that group on 2.4 and 5 GHz links. So how will we make WLAN stack know which links to use?

Can we use/extend bridge layer IGMP snooping or do we need to make yet another copy of that for WLAN?

Also related to multicast-to-unicast and some vxlan use cases. Challenging to get bridge code changes accepted if they touch the hot path.

There are proposed patches that were not accepted. Maybe try again with the new use cases as justification and identify this as subport forwarding.

Independently of the multicast link delivery selection, there are possible optimizations to convert some multicast groups to unicast (e.g., based on a small number of subscribers). The converted unicast case would behave like any unicast case, i.e., in MLO, it would be sent on a single link (with potential link layer retries on other links, if needed).

https://github.com/eqvinox/vpls-linux-kernel/commits/mdb-hack-v4 <-- 5 year old code that went into this direction

MLO and 4-addr frames
'''''''''''''''''''''

Currently disabled explicitly for MLO, but only because of not having been fully reviewed; not for a particular known issue.

Hopefully needs just cleanup and review to re-enable

Should also check IEEE P802.11be rules in the related areas (even though 4-address uses are not defined).

Are all CCMP/GCMP changes ok?

What about automatic discovery using Data nullfunc frames? Using link addresses? Or should something else be added using MLD addresses (and custom protocol design; e.g., vendor specific robust Action frame).

RX deduplication of multicast
'''''''''''''''''''''''''''''

Some designs will do with firmware, e.g., when providing Ethernet frames to the host.

Some designs will do this in host software, e.g., in mac80211 with sequence number checks. Nothing has been contributed yet.

AP RX of unicast address for each affiliated link (e.g., for RSN preauth) with one netdev
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Need to make networking stack aware of multiple BSSIDs (one per affiliated link in AP MLD) with our model of a single netdev so that frames targeted to any of the BSSIDs get delivered.

There probably already exists functionality to register an additional address. See dev_uc_add() (and the matching dev_uc_del() for cleanup). Someone needs to do some experimentation.

BSS color change and CSA and radar detection
''''''''''''''''''''''''''''''''''''''''''''

The design for each of these needs to be modified to cover multi-link cases.

Some of this is still a moving target from the IEEE 802.11 standard view point.

mac80211 rate scaling
'''''''''''''''''''''

Is anyone planning to implement something for this? Or assume drivers will take care of this anyway?

Unicast link selection
''''''''''''''''''''''

Is anyone planning to implement something for this? Or assume drivers will take care of this anyway?

Dynamic link management
'''''''''''''''''''''''

Station, and potentially also AP, adding/removing/disabling/re-enabling links dynamically during an MLO association.

Impact to roaming? Should this impact candidate AP MLD selection? More generally, would it be helpful to provide information to user space about other competing needs or co-existence constraints on frequency ranges (BT, LTE, etc.)

-  Consider adding this information to the channel list to keep state

-  Event when updated

-  May solve part of the issue of link selection conflicting with roaming selection

Where to do roaming decisions and link enabling/activation decisions for mac80211-based drivers? In user space with additional information on capabilities from the driver? Or move to the driver?

Should note that there is currently no roaming decision implementation based on the multi-link cases.

Mesh? Anything to discuss?
''''''''''''''''''''''''''

MLO is not defined for mesh (MBSS) and it does not look like anyone is working on defining this IEEE 802.11

WEXT support
''''''''''''

Some WEXT events are not delivered when using MLO; same for some ioctls

In theory, this could be considered a regression for cases where a WEXT-only application is used to monitor connection status (while another application is establishing the MLO connection).

Do we care enough? Would this break anything noticeable in practice?

And even if we do, could we really do anything to fix/work around this?

https://patchwork.kernel.org/project/linux-wireless/patch/alpine.LNX.2.00.1412302351030.31609@pobox.suse.cz/ show one prior attempt or the outcome from that..

Wi-Fi 7, and in particular MLO, could be a better justification to disable WEXT completely now at least for drivers that support MLO

Maybe add a deprecation warning now (cfg80211) that with Wi-Fi 7 HW the ioctl will stop working

Improved module parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^

Per-device parameters instead of per-driver/module

Not necessarily through module parameters, but something that would be available before started the device/firmware (or be willing to restart firmware if parameters are changed; also problematic if WLAN capabilities towards the stack change based on the parameter value)

Maybe not specific to WLAN, so might need to be discussed with wider audience

Proof of concept patch (etc.) might be helpful next step

Keeping MAINTAINERS file up-to-date
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some really old entries remaining in the file..

Can we get this updated?

What happens to cases where this would result in no remaining maintainer in the file?

State of wireless? Pros and cons of shared tree?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

wireless/wireless-next.git

I.e., no more mac80211/mac80211-next.git or wireless-drivers/wireless-drivers-next.git (or well, those trees do still exist, but have not be updated and should likely be removed or renamed to avoid issues with accidental use of old snapshots)

P802.11bh (how to handle random MAC addresses on the AP side)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Addresses issues of STAs using random MAC addresses on existing networks

Not much to do except perhaps hostapd/wpa_s to get/set the network identifier

P802.11bi / privacy improvements (STA and also AP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Addresses user privacy including APs

So far proposed:

-  Hide MAC address over the air using random MAC addresses, potentially changing during association, while using long(er) term MAC address in the Ethernet network; potentially hiding also Ethernet devices when they communicate with WiFi clients.

-  Start hiding more of elements (e.g. association request) to avoid fingerprinting, e.g. derive some keys first and then use them to encrypt association request frames (generated in mac80211). Similar thing exists for FILS. Will likely have an impact on authentication as well.

-  Protecting AP privacy e.g. SSID, elements, randomised BSSID; some changes might not be backwards compatible; significant differences for beacon frames

Wi-Fi 6E (6&7 GHz)
^^^^^^^^^^^^^^^^^^

AFC
'''

n/a

Power modes - LPI, VLP, …
'''''''''''''''''''''''''

n/a
