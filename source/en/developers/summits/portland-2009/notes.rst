Notes
=====

Staging
-------

The staging tree has a few goals. It is a way for code that is not up to standard to get into the kernel. It is also enables distribution drivers to be in one spot, which is very helpful to users. Drivers in staging will be dropped when there is a duplicate driver upstream. Duplication is decided based on device id and not always features - even so, the decision to drop a driver from staging will always be deferred to the driver developer.

Compat wireless
---------------

Familiar to many this is auto-backporting of wireless drivers. Recently it started to focus on stable kernels. Considering how far back to support kernels ... perhaps oldest on kernel.org.

Some talk surrounding how to use compat-wireless in a distribution. Some distros use depmod and others rely on order. Including prefix "compat" to symbols will enable distro to only use one driver from compat-wireless. Distribution can thus still use original mac stack and drivers for all devices and then new stack and driver for one piece of hardware.

Trees
-----

John reviewed how the different wireless trees tie together. A question was raised on where to obtain reliable commit ids since this is needed when communicating with distributions. The commit ids from wireless-2.6 and wireless-next-2.6 are not immutable, the ids from net-2.6 and net-next-2.6 are. John proposed that if you need to provide commit ids you can take it from linux-2.6 or net-next-2.6, even so, it is always helpful to communicate also which tree you obtained the commit ids from.

Regarding the wireless-testing tagging: merge-x is equivalent to Linux rc release, master-x is after all the new patches have been applied. If you have to bisect in wireless-testing, do your bisect between these tags. (Use merge-x with latest date and whichever master-x is appropriate so long as its date is later than the merge-x date. -- JWL)

Radiotap
--------

A list of things people would like to see in Radiotap was created:

-  want to see aggregated frames as aggregated in wireshark
-  need 11n extension support in Radiotap (maybe mcs rates are already supported)
-  need vendor extension support, for example to see transmit descriptors in wireshark
-  perhaps even extend wireshark for ftrace framework Discussion was mostly about things that need to be done and the process in which things should be accomplished. Nobody volunteered to take on this work.

Testing
-------

Distributions asked for direction on how to communicate issues. Recommendation is to report a bug at kernel.org bugzilla with a post on linux-wireless as a second best option. Ubuntu has a "crack of the day" package that can be used for upstream testing, even so, testing is limited and most issues really only start to be reported when rc1 has been released.

Unfortunately the GSoC testing project did not work out to help with testing.

There was some talk about availability of test suites and how it will be used. Can it maybe be used and required for every patch? Possibly not, but it will help developer. Need to enable final user to run tests - this will provide significant data. Do not require to support wext, new test suite only need to support nl80211.

Userland interfaces
-------------------

There was some talk about a new "libwireless" that will take care of translation to have all drivers move to cfg80211.

Some discussion surrounding when to drop support for hardware that do not support cfg80211. There are still a significant number of current drivers (about half dozen) that need to be converted before wext can be removed. Now listed on :doc:`cfg80211-conversion <../../todo-list/cfg80211-conversion>` . wext will be put in feature-removal and marked as deprecated.

wpa_supplicant need to be the target for new userspace applications

There was some interest in a nl80211 library. Currently if you want to write a little tool then you rip iw code. .... nl80211 code is also copied into supplicant, so it may also be a user of libnl80211 if it exists.

Some talk surrounding the building of wpa_supplicant. Talk about building wpa_supplicant to have library that contains selected components to enable build of small library with only needed components. Whatever is decided there is also a requirement to be built by visual studio so cannot rely on Linux tools, maybe cmake can be used. Would like to have build configuration without the significant usage of ifdef.

GSoC project has AP mode support in NM. Code is complete, under review. Talk about merging AP mode support to only rely on wpa_supplicant for this using NM for configuration. This will then be in the library.

WiMAX
-----

Discussed requirements to get WiMAX support in NM. Need support for protocol that is used by carrier to provide information to client including connection (authentication) information and firmware. Network in Portland (Clear) does not require this protocol, some other carriers do. Some information can now be obtained via scanning.

Roaming
-------

Background scanning now supported. Event from driver that indicates roaming occured already present

Need more information from driver on when to roam:

::

     * Drivers know when beacons are lost, but this is not communicated to users. 
     * Can also monitor signal strength. 
     * Transmission errors would be nice to have also. Need to look at way to get these events to userspace. 

wpa_supplicant has scanning/roaming framework that is currently disabled. This can be optimized by only doing background scanning on channels in which APs have been found previously.

Above is to decide when and where to roam to. 80211r then is used to do it most efficiently. 11k is also a standard to consider here in which neighborhood is known

Hardware (iwm) can also do its own roaming. Even so, it may still want option to use upper layers to do roaming.

Can connect command have whitelist/blacklist of bssid to which can roam to? - not sure there are devices that use blacklist

When supplicant has roaming support it will direct the scanning requests to ensure up to date information is used. Actually ... would like an event notification that is triggered when signal strength changes.

Peer-to-Peer
------------

There was a high-level overview of some upcoming peer-to-peer functionality for 802.11 networks. This will provide something analagous to IP Autoconfig (but at layer-2) or Bluetooth service discovery, with individual servers acting as APs for tiny networks related to that specific server. Details were light due to the specification being unavailable only to Wi-Fi Alliance members. -- JWL

Auto-connect
------------

Some firmware support background scanning with notification to host if pre-configured ssid has been found. User can thus program device with a few preferred ssids and background scanning can be done for these ssids and host notified when ssid is found - host can then associate to found ssid to perform "auto connect". Advantage is to save a lot of host power. Discuss how to fit this into the stack. Some firmware only can do this while not connected.

Loading ucode during probe ?
----------------------------

Talk moved to address issue where device may support different features based on which ucode loaded. This needs to be communicated before interface is up to be able to know what device support. Talk discussed potential load of ucode asynchronously in probe. The callback will know if ucode load failed and can potentially unbind device so that other driver may be able to try. This is not supported in kernel now (async load of ucode is), but unbinding driver needs a lot of work - userspace is only spot that it can be requested now. Since this is not supported we do not know if something will try to rebind the device - which may trigger a loop.

mac80211 registration then done after ucode is up.

Generic interface to obtain firmware version
--------------------------------------------

Moved on to request to have generic interface to obtain firmware version - perhaps this can be added to ethtool - may have hooks for this in cfg80211 and have this displayed with iw

hwsim testing
-------------

would like to support "poor links" to be able to simulate packet loss. There is currently feature to have "groups" where only sta in group can see each other, but this does not really accomplish the goal. Potential solution is to move all simulation decisions up to userspace and then communicate that via character driver. (There was also some discussion of using the TUN device to monitor this traffic. Also, control interface should cover channel change, etc for simulated airspace. -- JWL)

Bluetooth3
----------

bt2.1 + wifi can be bt3. Wanted to have transport over UWB but since that is not going anywhere, will do it over Wifi. Connection setup via BT, and then it discovers "AMPs" (UWB or Wifi) and it can switch there. mac80211 can tell BT that it cannot act as AMP or mac80211 needs to register an AMP so that devices do not need to. mac80211 needs to emulate hci device, need to figure the details out especially if you want a Wifi connection at same time. amps are used on demand - not persistent. Cannot really use Wifi for transfer at same time as BT uses it - can maybe suspend transfer at that time. (AMP == "alternative MAC/Phy" -- JWL)

Frequency broker
----------------

May have feature to have hardware coex turned off when BT is disabled to be able to save power. Sometimes BT coex is broken and then need freq broker to handle this. BT take ownership of entire 2.4Ghz band, but can be told which channels \_not\_ to use. Propose for easy prototype and potential complexity to have daemon in userspace, maybe move it to kernel later. Wifi/BT device inform freq broker of resources used may also use broker to help with decision on what channel to use for optimal behavior (like on which channel to start AP). (Overall purpose is to allow drivers that use RF bandwidth to communicate their usage of that bandwidth and how other users might effect their performance and capabilities. It also presupposes some sort of decision engine in userland for resolving conflicts when enabling a feature one device will disable or degrade service on another. -- JWL)

uAPSD
-----

Discussion was that we need a separate queue to enable this delivery mechanism. There was some discussion of what the userspace interface should be for this or whether it should be automatic, but with no solid conclusion. -- JWL

SM powersave
------------

(My notes are bad...) This turns-off one or more 802.11n Tx chains to save power. There was some discussion of how to make the rate control algorithms aware of this...

Userspace interface to rfkill
-----------------------------

Connman has the "airplane" mode to swith everything off. Talk about rfkilld capabilities, to let it be able to switch off all radios and applications use it. When rfkill disabled then Networkmanager will be responsible to bring interface up again.

Flush
-----

May help if api exists to instruct driver to flush pending frames before mac80211 triggers a scan, before sending PS frame. Also need to flush queue before disassociate so that we do not send frames and get error from AP saying that it is received from unauthenticated station.
