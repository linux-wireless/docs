**Note: The design on this page is WIP:** http://thread.gmane.org/gmane.linux.kernel.wireless.general/93044

Design notes on dedicated P2P interface API
-------------------------------------------

Rationale
~~~~~~~~~

Some drivers/devices would like to

-  use a separate MAC address
-  use a separate control path for P2P usage. This could even help mac80211-based drivers like iwlagn since currently, iwlagn needs to enable P2P in the device when a remain-on-channel is done, and disable it after a timeout or when a P2P interface is used.

API notes
~~~~~~~~~

A separate netdev would be the most obvious choice, but can be confusing:

::

     * to the user -- new interface is there, what does it do? 
     * to the developer -- no data traffic on this interface 

Better: use dedicated API in nl80211:

::

       * start-P2P -> returns cookie 
       * stop-P2P -> uses cookie 

(or maybe don't have "stop-P2P" but simply stop when socket is closed like mgmt frame subscriptions)

The only issue with this is that things like scan, mgmt-tx etc. need a netdev index now. However, this can be changed, idea:

::

         * use cookie to identify the P2P device interface 
         * internally, create a <code>struct wireless_dev</code> but **without** a netdev 
         * modify cfg80211 API (e.g. <code>scan</code>, <code>remain_on_channel</code>) to take <code>struct wireless_dev</code> instead of netdev, driver can check what the type is etc. 
         * this needs separate P2P-device iftype that can't really be used as an iftype, which is fine Questions: 
           * lifetime: does the P2P-device interface become the P2P-group/client interface like in wpa_supplicant, which means that it is removed before/when the real netdev is added? (personally I prefer it would stay around I think since I think discovery/public action things would still be done with it, not the real interface -- Johannes) 
           * pure software implementation of this in mac80211 for drivers that don't care, to unify API? but wpa_s needs old code anyway for backward compatibility 

additional thoughts
~~~~~~~~~~~~~~~~~~~

This could also be a good framework for additional features that we'll need to add:

::

             * device-based P2P listen/search timing (soon) 
             * maybe some more P2P offloads (WoP2P anyone? :-) ) 
