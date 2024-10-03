Notes
=====

full-mac support
~~~~~~~~~~~~~~~~

-  Need more capability info for card's supported features
-  add request IEs to cfg80211_connected() & to nl80211 event
-  add wpa version, cipher suites etc. from IW_AUTH to CONNECT cmd
-  add cfg80211_register_netdev(netdev)
-  add cfg80211_register_iwpriv(netdev, handlers) to support vendor drivers moving to cfg80211, MUST be done BEFORE cfg80211_register_netdev

test mode
~~~~~~~~~

::

     * <code>   {
         .cmd = NL80211_CMD_TESTMODE,
         .dumpit = NULL,
         .doit = NULL,
         .policy = NULL,
         .flags = GENL_ADMIN_PERM,
    }</code>
     * testmode.dumpit = driver_ops.testmode_dumpit etc. 
     * no API rules 
     * compiled out by default, hard to enable, depends on CONFIG_DEBUG? 
     * small example tool in userspace? 
     * new multicast ID, nl80211_test_event(skb), maybe overwrite the CMD 

antenna settings
~~~~~~~~~~~~~~~~

::

       * new antenna settings API needed 

rate control (and userspace API)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

         * for debug: set of bitrates, legacy & ht (this is generic) 
         *  * optionally with _MAC attribute for per-station setting (e.g. for fixed links in a mesh) 
         *  * also export this information back in station info in nl80211 
         *   noop bitrate algorithm for TI 1271 chip 
         *   need generic HT rate algorithm 
         *   need simpler rate control algorithm due to CPU usage (PID?) 
         *   want API for switching algorithm, export list of names, select by name 
         *   stick with debugfs for more advanced per algo control/debug 
         *   we want to have multicast bitrate control (e.g. by looking through station list) 
         *   have allowed-multicast-rates bitmap 
         *   add ht bitrate reporting to GIWRATE, just export the speed 

wext deprecation
~~~~~~~~~~~~~~~~

::

         *   * publish community statement that we no longer want wext 

action frame processing
~~~~~~~~~~~~~~~~~~~~~~~

::

         *     * receive action frame multicast group per interface 
         *     * use _FRAME attribute for the frames 
         *     * send action frame, TA verified in cfg80211 
         *     * commitment for handling action frames when mcast group is used 
         *     * restrict group to one process (is that even possible?) 
         *     * require extra commitment command, but commitment goes away once process dies, closes socket, unbinds mcast group 
         *     * frame should be buffered during scan 
         *     * (maybe later: location frame, add channel attribute in send cmd?) 
         *     * good capability handling for all of this 
         *     * filter (-EINVAL) when wrong frame is transmitted (e.g. != public-action before association, != action while associated...) 

channel stats/noise reporting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

         *       * channel statistics (currently channel use, maybe noise floor later) 
         *       * add flag to request this while starting a scan 
         *       * remove iwconfig noise report 

ROAMING (moving within ESS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

         *         * good bg scan algorithm 
         *         * export roaming capabilities of driver/device combination (mac80211==none, iwm==full) 
         *         * link quality event? 
         *         *  * signal change 
         *         *  * packet loss 
         *         *  * rate going down 
         *         *  * beacon loss this needs configurable thresholds from userspace 
