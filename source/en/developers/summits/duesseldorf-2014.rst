Düsseldorf 2014
===============

Proposal for Wireless Networking Micro-conference at Linux Plumbers Conference 2014 in Düsseldorf, Germany...

http://wiki.linuxplumbersconf.org/2014:network_wireless

etherpad notes (copied from https://etherpad.fr/p/LPC2014_Wireless)

::

   Wireless Networking Microconference Notes

   Welcome to Linux Plumbers Conference 2014.

   The structure will be short introductions to an issue or topic followed  by a discussion with the audience. A limit of 3 slides per  presentation is enforced to ensure focus and allocate enough time for  discussions. 

   Please use this etherpad to take notes. Microconf leaders will be giving a summary of their microconference during the Friday afternoon closing session.
   Please remember there is no video this year, so your notes are the only record of your microconference.

   Schedule

   1:30 -- What's missing for Miracast? -- David Herrmann
   miracast = wireless display, essentially
   demo - using laptop as sink (projector), phone as source
   software built using wpa_s
   few ms delay (demo with game)
   low framerate (30fps)
   his software also implements the source side
   his implementation shows up the data as a separate GPU which is problematic for the current UI stack, Wayland helps here
   different USB wifi devices failed horribly, demo using Intel PCIe, only one USB (Atheros) worked at all
   why separate GPU - why not use virtual output from GPU? should be supported and let the GPU encode the stream? implementation is also providing userspace APIs to bypass decode/encode

   what really is missing?
    - supplicant that works - e.g. P2P_DEVICE support can cause spurious errors
    - NetworkManager/Connman support for P2P (the latter is WIP)


   1:45 -- Extremely high speed and high coverage home wifi -- Avery Pennarun
   2:00 -- Cloud-based wireless packet capture, sharing, analysis, and diagnosis -- Avery Pennarun
   "How we're doing WiFi @Google Fiber"
   problem of selling gbit service - wifi is too slow, WAN faster than LAN
   no longer a question of whether customers will be disappointed or not, just a matter of how disappointed :)
   wifi speeds drop with distance - so now APs in each TV box; this causes problems roaming
   http://6-dot-gfblip.appspot.com/ - measures latency in http session, can do DNS queries
   new version will record & upload the data for customer support purposes
   other tool: isoping to measure upstream/downstream latency/jitter
   http://wavedroplet.appspot.com/ - upload pcap (radiotap headers) and show 802.11 data graphed
   q: bufferbloat, how does it affect you?
   a: when things are going well the systems often can't even catch up with the wan link so not a problem there; solutions to bufferbloat all on ethernet so far but wifi is really what they need, where it's a much harder problem
   ...
   network stack may have to be changed to deal with more dynamic queues due to changing stations/link conditions

   2:15 -- Break

   2:30 -- AP Group Features -- Helmut Schaa
   AP group is a set of APs managed centrally, a lot of problems could be solved with such a framework if it were to exist
   proposal to create a new protocol specific to hostapd for cooperation between APs


   2:45 -- "Minstrel-Blues" - Practical Joint Rate und Power Control in Linux mac80211 with todays 802.11b/g/a/n Chips -- Thomas Huehn
   rate control algorithm that incorporates tx power adjustment to reduce interference
   modifications to minstrel, working w/ ath5k & ath9k
   new mac80211 driver flags for power control capabilities
   current work to extend to minstrel_ht

   3:00 -- generalized firmware coredump support  -- Johannes Berg
   framework merged in 3.18
   register a buffer or method for access
   creates device_coredump device class in sysfs
   implemented in iwlwifi
   not specific to wifi drivers

   3:15 -- Break

   3:30 -- randomized MAC address scanning -- Johannes Berg
   originally from Apple (keybote), helps with privacy concerns
   implementation in hostapd
   When to randomize?  randomization breaks some use cases
   only when not associated?  pre-association exchanges
   should not be enabled by default -- end user option?  probably...

   3:45 -- Batman mesh -- Simon Wunderlich
   overview of l2 mesh technology, generally used w/ wireless networking
   mesh connection based on ad-hoc links
   protocol decisions based on packet loss (OGMv2)
   url: open-mesh.org

   4:00 -- 802.11s mesh -- Kathy Giori
   new life for 802.11s, QCA acquired copyrights from Cozybit for firmware (could be used in ath10k)
   some implementations can work better by breaking the spec slightly -- will we accept patches?  (likely yes, not guaranteed)

   4:15 -- regulatory -- Luis Rodriguez
   efforts to push CRDA functionality into the kernel
   timing issues exist w/ userland implementation, some use the in-kernel static database instead
   use in-kernel signing infrastructure to validate rules database BLOBs coming from userland
