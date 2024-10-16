Notes
=====
P2P UI/next steps
~~~~~~~~~~~~~~~~~

-  wpa_supplicant deemed complete, no integration of things like directly communicating with avahi etc. since it may or may not be suitable for the system
-  necessary to have new p2p management component
-  p2p mgmt component would offer public API and consume wpa_supplicant's (dbus) APIs

P2P needed functionality
~~~~~~~~~~~~~~~~~~~~~~~~

::

     * better virtual interface support 
     * advertise "feature matrix", virtual interface combinations 
     * beacon interval restrictions 
     * power saving 
     * need normal powersaving in place first 

multi-channel operation
~~~~~~~~~~~~~~~~~~~~~~~

::

       * part of feature advertisement matrix 
       * implement r-o-c per interface, OK to remove per-wiphy version of it 
       * need mac80211 design for multiple chans, backward compat with single-channel devices 
       * r-o-c offload to hardware 

regdb patch requirements
~~~~~~~~~~~~~~~~~~~~~~~~

::

         * basically [[http://marc.info/?l=linux-wireless&m=128414096127554&w=2|the processes we talked about earlier]] 
         * use wireless-regdb mailing list 

world roaming
~~~~~~~~~~~~~

::

           * mostly userspace problem 
           * kernel - enable overwriting regdom from world roaming? 
           * mostly an issue of trust 

backporting
~~~~~~~~~~~

::

             * remove pcmcia to remove issues 
             * maybe look at more ifdefs 
             * maybe make some patches for older kernels optional 

automated testing
~~~~~~~~~~~~~~~~~

::

               * presentation by Sam/Paul 
               * they'd like 
               *  * HT radiotap (Johannes to post RFA) 
               *  * ? (ISTR there was something else) 

legacy drivers / documentation / open firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Companies tend to do a good job with new drivers but slack hard when it comes to supporting older legacy drivers as there is a monetary lack of incentive to continue dedicating resources towards legacy drivers. Companies are used to dealing with drivers this way as drivers tend to just be obsoleted and dropped for support. With Linux we need companies to think differently and take advantage of the fact that we have skilled folks willing to help upkeep a driver.

To help with this companies need to start considering evaluation their own chipset / firmware documentation and release more documentation to the community. As a chipset becomes old, it should be easier to release more documentation about the chipset. Some community members are even willing to accept receiving documentation under NDA and the Linux foundation has partnerships set up for this if companies need intermediaries. Companies simply do not have processes today to review and categorize documentation. If companies want to take advantage of the development model on Linux they should invest resources to review and categorize documentation so that after a specific period of time some documentation becomes public, some can be given under NDA, and developers can contact a company for this documentation, and all this is kept track of.

In the ideal situation a company would release both documentation and even source code to firmware for legacy chipsets. Open firmware can help the community fix bugs a company may never have had resources to address and in some cases even enhance legacy drivers further. This is possible today and a perfect example of a success story for this is the :doc:`carl9170 driver <../../../users/drivers/carl9170>`, which has its own open GPLv2 :doc:`carl9170.fw firmware <../../../users/drivers/carl9170.fw>`.

maintenance issues / community relations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are not working on wireless-testing.git you are likely going to run into many development issues. If your driver is no upstream on the wireless-testing.git, you are likely in the worst possible situation for company.

To better understand how things work refer to our :doc:`development process <../../process>` documentation.

private/specialised APIs
~~~~~~~~~~~~~~~~~~~~~~~~

::

               *   * example: microAP (Marvell), but this should have proper API once the code requiring it goes into mainline; Johannes noted that often enough not doing this leads to APIs that, while somewhat generic, don't quite port to other drivers. 
               *   * example: BT coex -- currently sysfs (Nokia); discussion: could add APIs that are part of mainline, defined in nl80211, but not as generic as the regular APIs, defined in a specialised namespace. Do not want to add back dynamic registration of commands, as that would enable out of tree drivers to come up with crap. John noted that some things may simply require out of tree patches for specialised devices/platforms, and that sysfs files, while ugly, solve the problem "well enough". 

Powersaving / Roaming / Offchannel operation enhancements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We are currently dropping broadcast / multicast frames when doing a bgscan and going to power save. We need to ensure we wait for all broadcast / multicast data is received before going to power save. ath9k already has code for this, this should just be moved to mac80211. This has been :doc:`added to the power save TODO <../../todo-list>` section.

We also need the same enhancements when doing roaming, we should follow the DTIM count, not just assume we are always on the DTIM count. In the worst case scenario of a DTIM of 1 we will loose frames though, specially if we have to scan on a passive scan channel, it means we may wait on the passive scan channel longer than 1 beacon internal so we have no option but to loose broadcast / multicast frames. We can enhance this by simply avoiding bgscan unless required. For this we'll need a force scan command, so that we know if we are willing to afford loosing frames when doing a bgscan. This command can also be used to also notify userspace when we hit a deadzone: when we can RX data from an AP but cannot TX to it. This is caused by the AP typically being able to transmit at a higher power than STAs. We can notify userspace we hit a deadzone when the beacon monitor is OK but the connection monitor in mac80211 is not OK. Userspace can then decide it wants to force us to roam off to another BSS on the ESS and use this new force scan command.

Other enhancements can be taken into consideration for offchannel operation like BA tweaks.

All these enhancements have now been documented on the :doc:`wireless TODO list <../../todo-list>`.

IBSS
~~~~

::

               *     * IBSS not really liked by anyone much 
               *     * however, still required 
               *     * desire for complete IBSS (including RSN) to avoid having to support WPA-None hacks 
               *     * per-STA GTK also useful for fast transition (FT, 802.11r) 
               *     * GTK patch needs APIs to allow driver to remove key from hw crypto if needed (e.g. when GTKs for multiple STAs are present) -- this is needed for TX with keys if they must be removed from hw (rather than just disabled for RX) 
               *     * need STA_DEL notifications 

tracing
~~~~~~~

::

               *       * Johannes gave short demo of iwlwifi tracing 
               *       * short discussion on adding more tracepoints, seems good 
