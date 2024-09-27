Regulatory rules processing
---------------------------

This section is intended to help document cfg80211's algorithm for processing regulatory rules and applying them. You can read this if you are not so well versed with code or don't want to bother reading it.

Internal core rules
-------------------

cfg80211 has regulatory compliance built into it, this means each registered device obeys cfg80211's regulatory interpretations and provides an API for drivers (cfg80211 or mac80211 drivers) to provide hints to it as to what rules should be enforced. A device registers with cfg80211 a list of supported bands and each band has a list of supported channels. During registration cfg80211 will ensure only the allowed channels for the currently set regulatory domain will be left enabled.

Wireless core initialization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upon the initialization of the wireless core (cfg80211) a world regulatory domain (highly restrictive) will be set as the central regulatory domain. If CRDA is present the latest dynamic world regulatory domain is queried from CRDA; if it is not then a statically defined list is used.

When a wiphy is registered to cfg80211 the effective set of permitted channels/maximum power is calculated for that device based on the current regulatory domain. As initially that will be the world regulatory domain, devices start out being restricted to that.

Initial driver registration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Prior to registration a wireless device sets on its channel data structures what it is allowed to use / is capable of. Upon registration cfg80211 uses this to allow the wireless regulatory infrastructure to never enable more on a card than what was intended or designed. The wireless core ensures this by caching original parameters in \_orig attributes for each defined channel. The wireless core always uses this as the maximum allowed permission for each channel. Drivers should register **all supported hardware channels** to the wireless core.

After the driver has registered to cfg80211 the world regulatory domain settings will have been set by default, drivers wishing to ignore the first world regulatory domain hint can specify this to the wireless core by supplying the flag WIPHY_FLAG_CUSTOM_REGULATORY. This is done to tell cfg80211 the driver has its own custom regulatory domain settings.

<code> \* @WIPHY_FLAG_CUSTOM_REGULATORY: tells us the driver for this device \* has its own custom regulatory domain and cannot identify the \* ISO / IEC 3166 alpha2 it belongs to. When this is enabled \* we will disregard the first regulatory hint (when the \* initiator is %REGDOM_SET_BY_CORE).</code> If a driver has a regulatory domain that it should follow and wants to ignore all hints until its hint is applied it can apply the WIPHY_FLAG_STRICT_REGULATORY flag to the device.

<code> \* @WIPHY_FLAG_STRICT_REGULATORY: tells us the driver for this device will \* ignore regulatory domain settings until it gets its own regulatory \* domain via its regulatory_hint() unless the regulatory hint is \* from a country IE. After its gets its own regulatory domain it will \* only allow further regulatory domain settings to further enhance \* compliance. For example if channel 13 and 14 are disabled by this \* regulatory domain no user regulatory domain can enable these channels \* at a later time. This can be used for devices which do not have \* calibration information guaranteed for frequencies or settings \* outside of its regulatory domain. If used in combination with \* WIPHY_FLAG_CUSTOM_REGULATORY the inspected country IE power settings \* will be followed.</code>

Drivers with EEPROM regulatory information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Drivers that have country information in their EEPROM should provide an ISO/IEC 3166-1 alpha2 code to cfg80211 as a hint about the current regulatory domain. This should be done after wiphy registration.

For the special case where the EEPROM regulatory information must be observed **at all times**, the driver will not register any other channels.

In the special case where the EEPROM regulatory information must be observed **unless 802.11 country information is received**, the driver may register a regulatory notifier and restrict any information that CRDA supplied to the EEPROM information depending on the cause of the regulatory change.

Drivers without EEPROM regulatory information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Drivers with no EEPROM regulatory information can simply rely on the world regulatory domain, wait for an 802.11 country information or pass custom regulatory domains, or supply a flag that indicates to cfg80211 that the driver already has a custom regulatory domain applied by using WIPHY_FLAG_CUSTOM_REGULATORY documented above.

Secondary driver settings
^^^^^^^^^^^^^^^^^^^^^^^^^

Each driver can hint to cfg80211 which regulatory domain should be used by providing an ISO-3166 alpha2 country code or by providing to it a custom regulatory domain; this is intended to be used as a first start-up hint based on the device's EEPROM / custom table of regulatory settings. Custom regulatory domains are only used for the wireless card supplying them, driver hints with a specific ISO3166 country code is used for the wireless core and use to restrict devices further upon registration later. Each type of driver regulatory hint is documented further below.

Conflicts can arise when you have multiple wireless devices present on a system which claim different regulatory domains. Arbitrarily complex algorithms could be invented to resolve such conflicts; for now the regulatory domain selected by the first wireless card is chosen and if cards have their own regulatory domain that regulatory domain is always respected for that card.

Once an alpha2 is suggested to the wireless core it will query CRDA for a regulatory domain for that alpha2. The wireless core will then iterate overall all registered wireless devices and update the device's list of enabled channels, max power, max bandwidth and max antenna gain for each of them.

Country definition
------------------

Lets start out first by understanding how a country is defined. We start by declaring it with the key word "country" followed by the respective `ISO 3166 alpha2 <http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code followed by a colon. So for example:

::

   country CR:

Regulatory rules
~~~~~~~~~~~~~~~~

Each country can have a set of regulatory rules. Each regulatory rule has an attached frequency range and a respective power rule. An example of one regulatory rule follows:

<code> (2402 - 2482 @ 40), (N/A, 20)</code> A country can have multiple regulatory rules.

Frequency range
~~~~~~~~~~~~~~~

Each frequency range provides a starting frequency and ending frequency in MHz followed by the maximum allowed bandwidth that a channel of communication can have in that frequency range. So for example, in the following regulatory rule:

<code> (2402 - 2482 @ 40), (N/A, 20)</code> The frequency range is just:

<code> (2402 - 2482 @ 40)</code> This is telling us that you can use a channel of communication of max bandwidth of up to 40 MHz in the frequency range 2402 MHz - 2482 MHz.

Power rule
~~~~~~~~~~

The power rule is the last section in a regulatory rule. For example in the regulatory rule:

<code> (2402 - 2482 @ 40), (N/A, 20)</code> the power rule is:

<code> (N/A, 20)</code> This tells us the maximum allowed EIRP that can be used on a frequency range, and the maximum antenna gain if it is known. If the maximum antenna gain is not known *N/A* can be used to annotate this. The maximum EIRP is assumed to be in dBm, the maximum antenna gain is assumed to be in dBi.

Reading a regulatory rule
~~~~~~~~~~~~~~~~~~~~~~~~~

Now lets read a regulatory rule all together. The following regulatory rule:

<code> (2402 - 2482 @ 40), (N/A, 20)</code> then tell us that we can use a channel of communication of up to 40 MHz in the frequency range 2402 MHz - 2482 MHz with a maximum EIRP output power of 20 dBm. No maximum antenna gain is known.

20 MHz channels
~~~~~~~~~~~~~~~

cfg80211 assumes all 802.11 cards want to use 20 MHz channels so channels get disabled if no 20 MHz channels are allowed in a given frequency range defined by the country the card is in.

.. _mhz-channels-1:

40 MHz channels
~~~~~~~~~~~~~~~

40 MHz channels will only be allowed if 20 MHz channels are allowed as well. 40 MHz channels work by using a regular 20 MHz channel and then using an extra 20 MHz channel either on the left hand side of the first channel or the right hand side. We refer to this as either HT40- or HT40+, respectively.

cfg80211 checks if an HT40- or HT40+ channel fits on each center frequency for each power rule and will enable HT40- or HT40+ on each channel. This HT40 allow map is available currently only through debugfs. For example, here is an output:

::

   root@tux:~# cat /sys/kernel/debug/ieee80211/phy0/ht40allow_map 
   2412 HT40  +
   2417 HT40  +
   2422 HT40  +
   2427 HT40  +
   2432 HT40 -+
   2437 HT40 -+
   2442 HT40 -+
   2447 HT40 - 
   2452 HT40 - 
   2457 HT40 - 
   2462 HT40 - 
   2467 Disabled
   2472 Disabled
   2484 Disabled
   5180 HT40  +
   5200 HT40 -+
   5220 HT40 -+
   5240 HT40 -+
   5260 HT40 -+
   5280 HT40 -+
   5300 HT40 -+
   5320 HT40 - 
   5500 HT40  +
   5520 HT40 -+
   5540 HT40 -+
   5560 HT40 -+
   5580 HT40 - 
   5600 Disabled
   5620 Disabled
   5640 Disabled
   5660 HT40  +
   5680 HT40 -+
   5700 HT40 - 
   5745 HT40  +
   5765 HT40 -+
   5785 HT40 -+
   5805 HT40 -+
   5825 HT40 - 

This list is not exposed via nl80211 as cfg80211 will get a revisit as to how this is handled after the regulatory rules are restructured in the future.

80 MHz 802.11ac VHT channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

cfg80211 relies on a regulatory band to have listed 80 MHz as an allowed bandwidth before a channel is allowed to use it. cfg80211 checks this and if the desired center of freq fits in the specified 80 MHz band via by checking a if a channel fits in a specific regulatory rule via freq_in_rule_band()

60 GHz 802.11ad channels
~~~~~~~~~~~~~~~~~~~~~~~~

cfg80211 supports 802.11ad 60 GHz channels. Right now only channels 1..3 are enable by default in the world regulatory domain. cfg80211 checks this and if the desired center of freq fits in the specified 60 GHz band via by checking a if a channel fits in a specific regulatory rule via freq_in_rule_band()

Processing channels in cfg80211
-------------------------------

When cfg80211 initializes it will have a list of wiphy devices. Each 802.11 card has a respective single wiphy device. Multiple interfaces can be attached to a wiphy device. The wiphy device has a list of channels which are shared. When a wiphy is registered to cfg80211 it has a list of supported 802.11 channels with a respective center frequency. The currently regulatory domain is read and each wiphy is processed to apply the regulatory domain to it. A wiphy device can have its own regulatory domain though. This allows us to enable two different cards which have two different regulatory domains to be present on a single system and for cfg80211 to respect it. When this happens there will be three regulatory domains, one for each wiphy and a core central regulatory domain which will consist of the intersection between the two wiphy's regulatory domains.

If a wiphy has no regulatory domain of its own cfg80211 will use its own core central regulatory domain to iterate over the card's 802.11 channels and apply rules, otherwise cfg80211 will use the card's own regulatory domain.

Example analysis
~~~~~~~~~~~~~~~~

Suppose a wiphy is registered to cfg80211 and the driver that registers it claims that the wiphy has a regulatory domain of its own which indicates it is a card which is programmed to operate in *Costa Rica*. In this case cfg80211 would have queried CRDA for CR's regulatory domain and CRDA would reply with:

::

   country CR:
           (2402 - 2482 @ 40), (N/A, 20)
           (5170 - 5250 @ 20), (3, 17)
           (5250 - 5330 @ 20), (3, 23), DFS
           (5735 - 5835 @ 20), (3, 30)

Now the wiphy that was registered to cfg80211 has these channels:

<code> Frequencies:

::

                         * 2412 MHz [1]
                         * 2417 MHz [2]
                         * 2422 MHz [3]
                         * 2427 MHz [4]
                         * 2432 MHz [5]
                         * 2437 MHz [6]
                         * 2442 MHz [7]
                         * 2447 MHz [8]
                         * 2452 MHz [9]
                         * 2457 MHz [10]
                         * 2462 MHz [11]
                         * 2467 MHz [12]
                         * 2472 MHz [13]
                         * 2484 MHz [14]

::

                 Frequencies:
                         * 5180 MHz [36]
                         * 5200 MHz [40]
                         * 5220 MHz [44]
                         * 5240 MHz [48]
                         * 5260 MHz [52]
                         * 5280 MHz [56]
                         * 5300 MHz [60]
                         * 5320 MHz [64]
                         * 5500 MHz [100]
                         * 5520 MHz [104]
                         * 5540 MHz [108]
                         * 5560 MHz [112]
                         * 5580 MHz [116]
                         * 5600 MHz [120]
                         * 5620 MHz [124]
                         * 5640 MHz [128]
                         * 5660 MHz [132]
                         * 5680 MHz [136]
                         * 5700 MHz [140]
                         * 5745 MHz [149]
                         * 5765 MHz [153]
                         * 5785 MHz [157]
                         * 5805 MHz [161]
                         * 5825 MHz [165]</code>

What cfg80211 will do next is iterate over each channel's center frequency and see from the current regulatory domain on what regulatory rule a channel of 20 MHz bandwidth using the channel's center frequency fits in. If no match is found the channel is disabled. If a match is found cfg80211 will enable 20 MHz communication on the channel.

Post processing mechanisms
~~~~~~~~~~~~~~~~~~~~~~~~~~

Once cfg80211 processes a regulatory domain on a wiphy device it goes through a series of post processing on the wiphy. Below we document the different types of post processing performed by cfg80211.

Beacon hints
^^^^^^^^^^^^

cfg80211 has a feature called *beacon hinting* to assist cfg80211 in allowing a card to lift *passive-scan* and *no-beaconing* flags. *Passive-scan* flags are used on channels to ensure that an interface will not issue a probe request out. The *no-ir* flag exists to allow regulatory domain definitions to disallow a device from initiating radiation of any kind and that includes using beacons, so for example AP/IBSS/Mesh/GO interfaces would not be able to initiate communication on these channels unless the channel does not have this flag. If either of these flags are present on a channel a device is prohibited from initiating communication on cfg80211.

Old regulatory rule flags like *passive-scan* and *no-beaconing* were originally invented to help with World Roaming, these two are now combined into the one and only *no-ir*, for *no-initiating-radiation*. If you do not know what country you are in you can still behave as an 802.11 STA interface but can wait to enable active scans until you see a beacon from an AP, if the channel being used is not a DFS channel and not channels 12-14 on the 2.4 GHz band. The same can be said for initiating communication, so both the old *passive-scan* and *no-beaconing*, now consolidated in modern kernels as one flag *no-ir* can be lifted if an AP is found beaconing on a non-DFS channel and if the channel is also not channels 12-14 on the 2.4 GHz band. cfg80211 takes advantage of this bit of logic to lift both of these flags **if and only if** the wiphy device is world roaming.

It is also important to note that the Linux kernel beacon hint mechanism only trusts beacons from 802.11 APs, not Mesh or IBSS. Specifically, the Linux kernel beacon hint mechanism ensures that the beacon ESS capability is set:

<code> if (res->pub.capability & WLAN_CAPABILITY_ESS)

::

                 regulatory_hint_found_beacon(wiphy, channel, gfp);  </code>

Driver override on rules
^^^^^^^^^^^^^^^^^^^^^^^^

To allow more driver flexibility cfg80211 allows drivers to review the regulatory settings on the wiphy and override them. This enables more flexibility on regulatory design but also enables drivers to take advantage of offloading most of the regulatory work to cfg80211/CRDA. The way that drivers can override regulatory settings is by defining a wiphy regulatory reg_notifier(). The wiphy's reg_notifier() callback will be called **after** cfg80211 has completed processing its regulatory settings on the wiphy device.

Driver regulatory hints
^^^^^^^^^^^^^^^^^^^^^^^

Drivers can issue their own regulatory domain hints to cfg80211. If they do this the wiphy gets its own regulatory domain. This enables two different 802.11 devices even with the same 802.11 driver to have different regulatory domains. This also enables there to be a central 802.11 regulatory domain which will consists of an intersection between the two present regulatory domains if two cards are present with different regulatory domains.

Country IE processing
^^^^^^^^^^^^^^^^^^^^^

cfg80211 supports enhancing regulatory compliance by allowing cfg80211 to inform it of when a country information element has been received and should be obeyed. The **Country Information Element** (cf. 802.11-2007 7.3.2.9) contains the information required to allow a station to identify the regulatory domain in which the AP is located and to configure its PHY for operation in that regulatory domain. The Country IE contains, amongst other things, the list of permissions (channels and transmit power on those channels) and an ISO/IEC 3166-1 country code. regulatory_hint_11d() is used by cfg80211 to pass an IEEE 802.11 country information element. cfg80211 will parse the information element, build a regulatory domain from it and intersect with what CRDA tells us should apply for the given alpha2. In practice though one can not always trust APs country information element regulatory information due to considerations for **outdated** data, rogue/busted APs. Therefore, the wireless code determines the regulatory permissions based on the **intersection** of data from the APs country information element and what CRDA provides for the given country code.

The Linux kernel wireless subsystem always enables the dot11MultiDomainCapabilityEnabled flag. Therefore, STA devices in the Linux kernel try to follow country information received in AP beacons.

If an AP supports sending the Country IE it will send the country IE appended on every beacon. Since we have an initial regulatory setting (set by the driver, user, or core) we don't pay attention to the country IE **until we try to associate to the AP**. Upon association we will parse the country IE, convert it to a cfg80211 regulatory domain structure and pass it up as a country IE regulatory hint to the wireless core. Processing of country IEs is done automatically for both cfg80211 and mac80211 drivers by the core (cfg80211) issuing regulatory_hint_11d() when processing an AP's IEs. regulatory_hint_11d() is optimized to ignore hints from the same AP or that match the same country IE checksum, but it should be noted that we only issue regulatory_hint_11d() once upon a successful association to an AP.

APs may support 3 bands (2.4 GHz, 5 GHz, 60 GHz) or 2 bands (2.4 GHz and 5 GHz) or one band (2.4 GHz, 5 GHz, or 60 GHz). When an AP supports 1 band, as per `IEEE-802.11 2007 country IE clarification request <http://tinyurl.com/11d-clarification>`__ the AP **may** send a subset of the allowed regulatory rules and not the complete set. Because of this the cfg80211 regulatory infrastructure trusts its original regulatory requests if the AP does not send any information on a band it does not support. Since band information is purely artificial in cfg80211 we conclude an AP does not support a band if it has no channel information in its country IE that fits within 2 GHz of the tested band. We can can tune this as we see fit, in freq_in_rule_band().

If an AP has no information on a supported device band we trust the last trusted regulatory request. The last trusted regulatory request will vary depending on the device.

Enabling users to enhance regulatory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Users can enhance regulatory settings by further restricting devices by picking a regulatory domain. This will enable users to **help** compliance further. Currently regulatory rules for certain countries ("US" and "JP") do not allow users to select their regulatory domain though so blindly trusting a user is not something that can be allowed if you are in certain regulatory domain. If a user picks a regulatory domain channels will be restricted further on a device if the device has its own regulatory domain already listed.

Cellular base station regulatory hints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cell base station towers can inform mobile / laptop devices of their location with great accuracy. To be precise Mobile Country Codes (MCC) or Mobile Network Codes (MNC) can be used. As of the 3.6 release Linux supports the ability for cell base station towers to supply a regulatory hint to the Linux kernel in a very restrictive manner. Support is provided by allowing an attribute to the Linux kernel to be passed that classifies the hint as coming from a cellular base station. By default this attribute will always be ignored. Device drivers require testing / compliance prior to enabling this feature due to possible synchronization issues with a device's firmware when the device implements some regulatory functionality in firmware and also depending on the regulatory agency that the device is certified for. Supporting cellular base station hints also requires some userspace support / features and as such a full system solution needs to be considered and tested.

Device drivers on systems which need to go through validation for this feature and for which they have at least one region they need to support this can make the alpha2 from cellular base stations available for parsing by enabling a Kconfig kernel configuration option. By default this feature is disabled and encouraged to be disabled. Cellular base station hints depend on the kconfig :doc:`CONFIG_CFG80211_CERTIFICATION_ONUS <../regulatory>` kernel configuration option. After enabling this kernel configuration option, a device driver would further require setting the wiphy->features NL80211_FEATURE_CELL_BASE_REG_HINTS flag to enable listening to these type of hints,. Upon cfg802111 registration the driver would then inform the subsystem that there is at least one driver present that supports complaint and tested cellular base station hints. cfg80211 will ignore cellular base station hints unless one device driver is present with one device (wiphy) that supports this feature. If all devices have been removed dynamically from the system that support this feature the cell base station hints would be ignored afterwards (consider hotpluggable USB 802.11 devices).

Userspace software solutions are expected to implement support for this feature through a dbus event and enabling such event to send a cell base station regulatory hint from wpa_supplicant to the kernel by using the NL80211_ATTR_USER_REG_HINT_TYPE attribute and classifying the hint as NL80211_USER_REG_HINT_CELL_BASE. Note that specifically this is for hints coming directly from cellular base station tower. System integrators which enable this feature must ensure cell base station hints is not a feature enabled for users to use manually, or that no other mechanism other than hints directly from the cell base station tower are used. This feature is designed for userspace software to implement a hint only when a cell modem has detected we are in a new country from a cellular base station with confidence.

The NL80211_USER_REG_HINT_CELL_BASE is followed as follows as part of *enum nl80211_user_reg_hint_type*

https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/tree/include/uapi/linux/nl80211.h#n2358

::

   /**                                                                             
    * enum nl80211_user_reg_hint_type - type of user regulatory hint               
    *                                                                              
    * @NL80211_USER_REG_HINT_USER: a user sent the hint. This is always            
    *      assumed if the attribute is not set.                                    
    * @NL80211_USER_REG_HINT_CELL_BASE: the hint comes from a cellular             
    *      base station. Device drivers that have been tested to work              
    *      properly to support this type of hint can enable these hints            
    *      by setting the NL80211_FEATURE_CELL_BASE_REG_HINTS feature              
    *      capability on the struct wiphy. The wireless core will                  
    *      ignore all cell base station hints until at least one device            
    *      present has been registered with the wireless core that                 
    *      has listed NL80211_FEATURE_CELL_BASE_REG_HINTS as a                     
    *      supported feature.                                                      
    */                                                                             
   enum nl80211_user_reg_hint_type {                                               
           NL80211_USER_REG_HINT_USER      = 0,                                    
           NL80211_USER_REG_HINT_CELL_BASE = 1,                                    
   }; 

It should be noted that support for this feature can vary country to country. At least for the US we have record of the FCC putting out through their public `KDB 594280 <https://apps.fcc.gov/eas/comments/GetPublishedDocument.html?id=327&tn=528122>`__ the following on page 14:

::

   Mobile Country Codes (MCC) or Mobile Network Codes
   (MNC) are not acceptable for programming host
   compliance

This has been discussed on at least one `public mailing lists thread <http://permalink.gmane.org/gmane.linux.kernel.wireless.general/110859>`__ so far. If you are a system integrator be sure to do your homework on proper full system compliance. We can implement support for features but full system integration from userspace down to hardware needs to be considered for this functionality given the complexity of supporting the feature.

Concurrent GO Relaxation
^^^^^^^^^^^^^^^^^^^^^^^^

Generally, a P2P GO is not allowed to operate on channels on which transmissions are not allowed. However, some regulatory bodies consider to relax the conditions under which a P2P GO is allowed to operate, enabling operation of a P2P GO on such channels in case that:

-  The device that desires to operate the P2P GO is under the guidance of an authorized master, i.e., the device is also concurrently connected on a station interface to an AP that is an authorized master (with DFS and radar detection capabilities).
-  The device that desires to operate the P2P GO is operating in an indoor surroundings and can guarantee indoor operation, i.e., the device is connected to AC power or the device is under the control of a local master that is acting as an AP and is connected to AC power. These relaxations are among others discussed by the FCC in `Considerations of “Soft” Configurations or Configurations of “non-Software Defined Radios” <https://apps.fcc.gov/eas/comments/GetPublishedDocument.html?id=327&tn=528122>`__

The above relaxations are supported by the regulatory core (disabled by default), allowing a P2P GO operation on a channel on which initiating radiation is not allowed in case that:

::

     * The channel allows the Concurrent GO operation and there is a station interface associated to an AP on the same channel on the 2 GHz band or the same UNII band (in the 5 GHz band). 
     * The channel allows only indoor operation and there is a hint from user space that the platform on which the device is attached is operating in indoor surroundings, i.e., is AC powered. Note that the regulatory core does not verify that all the conditions for the relaxations are met and relies on user space to guarantee them. In addition the regulatory core expects user space to evict the P2P GO from the operating channel in case that the conditions that allow the relaxations are no longer valid. In order to prevent daisy chain scenarios, user space should prevent legacy clients from connecting to the GO in case that it is instantiated due to one of the above relaxations. These relaxations should not be enabled unless there is a system wise adherence to the regulatory bodies expectations. 

To enable these relaxations CONFIG_CFG80211_REG_RELAX_NO_IR (depends on kconfig :doc:`CONFIG_CFG80211_CERTIFICATION_ONUS <../regulatory>` configuration option) should be enabled and in addition the device driver needs to report that it allows these relaxations by setting REGULATORY_ENABLE_RELAX_NO_IR in the wiphy regulatory flags during registration.

Hidden SSIDs
------------

Hidden SSIDs should be avoided in any AP scenario and and in fact its :doc:`not supported if you are to support WPS <../../users/documentation/wpa_supplicant>`. If you insist on using hidden SSIDs be sure you are not enabling support for WPS as an option then. Communication with hidden SSIDs can become problematic if your card is world roaming under specific scenarios documented here.

You can determine if you are world roaming as follows:

::

   maria@pupusas ~ $ iw reg get
   country 00:
           (2402 - 2472 @ 40), (3, 20)
           (2457 - 2482 @ 20), (3, 20), PASSIVE-SCAN, NO-IBSS
           (2474 - 2494 @ 20), (3, 20), NO-OFDM, PASSIVE-SCAN, NO-IBSS
           (5170 - 5250 @ 40), (3, 20), PASSIVE-SCAN, NO-IBSS
           (5735 - 5835 @ 40), (3, 20), PASSIVE-SCAN, NO-IBSS

If you get a *00* country code it means you are world roaming.

World roaming means we cannot **initiate radiation** on certain channels given that certain countries may prohibit initiating radiation on some channels or may require **DFS master support** prior to initiating any radiation. **DFS master support** for client devices requires quite a lot of work and is not yet implemented on mac80211 / cfg80211. This means that if your AP is in a channel that requires **DFS** then you will not be able to send probe requests to them. Since SSIDs are hidden the only way to communicate with them is to send probe requests / association requests to them directly, but if you cannot initiate radiation on that channel then you obviously not be able to communicate with them.

If the channel your AP is on is not a DFS channel but a 5 GHz channel that requires passive scan, the passive scan flags are lifted through :doc:`beacon hints <processing_rules>`, but we only process beacon hints **if** obviously the AP is beaconing. We also do not process :doc:`beacon hints <processing_rules>` for DFS channels. To determine if you are seeing beacon hints you can query dmesg as follows:

::

   jose@chupacabras ~ $ dmesg| grep beacon
   cfg80211: Found new beacon on frequency: 5180 MHz (Ch 36) on phy0
   cfg80211: Found new beacon on frequency: 5200 MHz (Ch 40) on phy0
   cfg80211: Found new beacon on frequency: 5220 MHz (Ch 44) on phy0
   cfg80211: Found new beacon on frequency: 5240 MHz (Ch 48) on phy0
   cfg80211: Found new beacon on frequency: 5745 MHz (Ch 149) on phy0
   cfg80211: Found new beacon on frequency: 5805 MHz (Ch 161) on phy0

You can also monitor for the events with iw event, for example, leave a window open with *iw event* running and then issue the *iw dev wlan0 scan* command, you should see something as follows:

::

   pedro@pulperia:~$ iw event -t
   1343339185.840035: wlan0 (phy #0): scan started
   1343339189.395215: phy #0: beacon hint:
   phy0 5765 MHz [153]:
           o active scanning enabled
           o beaconing enabled
   1343339189.613367: phy #0: beacon hint:
   phy0 5785 MHz [157]:
           o active scanning enabled
           o beaconing enabled
   1343339189.886251: wlan0 (phy #0): scan finished: 2412 2417 2422 2427 2432 2437 2442 2447 2452 2457 2462 2467 2472 5180 5200 5220 5240 5260 5280 5300 5320 5500 5520 5540 5560 5580 5600 5620 5640 5660 5680 5700 5745 5765 5785 5805 5825, ""

If you do not see these then you are not getting the beacon hints.

Best is to simply avoid hidden SSIDs. They buy you no security at all and are clearly incompatible with WPS.
