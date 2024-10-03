What this is about
==================

For an introduction see the `slides <http://pdxplumbers.osuosl.org/2010/ocw/system/presentations/639/original/lpc-p2p.pdf>`__ for the "Wi-Fi Peer-to-Peer on Linux" talk given by Johannes Berg during the Linux Plumbers Conference 2010.

Basic P2P Architecture Stack
----------------------------

<code> \| <---------- D-Bus Application API +--------------------+

.. list-table::

   - 

      - connection manager
   - 

      - or p2p control app

+--------------------+

::

           |  <---------- D-Bus supplicant API
           |              or socket control interface

+--------------------+

.. list-table::

   - 

      - wpa_supplicant

+--------------------+

::

           |  <---------- nl80211

+--------------------+

.. list-table::

   - 

      - cfg80211

+--------------------+

::

           |  <---------- struct API

+--------------------+

.. list-table::

   - 

      - mac80211

+--------------------+

::

           |  <---------- mac80211's driver API

+--------------------+

.. list-table::

   - 

      - driver

+--------------------+</code>

Interfaces
----------

D-Bus Application API
~~~~~~~~~~~~~~~~~~~~~

::

   NOTE: This doesn't exist yet! There's no integration
         with connection managers or any other control
         application yet!

We're currently working on seeing if this is at all feasible to define, but it would be good if applications could use a standard API that the connection manager offers. There are multiple reasons for having the connection manager offer this, like the need for a coordinator of all wifi usage.

Since there are multiple connections managers, a good approach to defining this would be a freedesktop.org standard.

supplicant API
~~~~~~~~~~~~~~

D-Bus API
^^^^^^^^^

API has been posted for review: http://thread.gmane.org/gmane.linux.drivers.hostap/22469

socket control interface
^^^^^^^^^^^^^^^^^^^^^^^^

This interface offers basic P2P primitives like p2p_find, p2p_stop_find, p2p_connect, etc.

Here's a full list:

-  p2p_find
-  p2p_stop_find
-  p2p_connect
-  p2p_listen
-  p2p_group_remove
-  p2p_group_add
-  p2p_prov_disc
-  p2p_get_passphrase
-  p2p_serv_disc_req
-  p2p_serv_disc_cancel_req
-  p2p_serv_disc_resp
-  p2p_service_update
-  p2p_serv_disc_external
-  p2p_service_flush
-  p2p_service_add
-  p2p_service_del
-  p2p_reject
-  p2p_invite
-  p2p_peers
-  p2p_peer
-  p2p_set
-  p2p_flush
-  p2p_presence_req
-  p2p_ext_listen This API can be used on dedicated/embedded systems like a printer, but applications that must play together with other applications can't really use it.

Both D-Bus and socket interfaces (will) also have events indicating when new P2P devices were found, etc.

nl80211
~~~~~~~

Currently, the P2P-related extensions are:

::

     * NL80211_CMD_REMAIN_ON_CHANNEL 
     * NL80211_CMD_CANCEL_REMAIN_ON_CHANNEL 
     *  * This indicates to the device that it should stay on a given channel for a given time, to implement a P2P listen phase. Can also be canceled, since it is also used to implement off-channel TX for group negotiation or invitation (but see below) 
     *   NL80211_CMD_FRAME (previously NL80211_CMD_ACTION) 
     *    * Transmit a management frame, with channel checking. This can be used during a remain-on-channel phase to transmit frames on that channel, or at other times to transmit on the operating channel. This also allows off-channel transmission, i.e. transmit on a given channel and wait for a response for a given time (including the ability to cancel the wait) which in a sense combines REMAIN_ON_CHANNEL and MGMT_TX into just a single MGMT_TX for some operations. (wpa_supplicant changes for this enhanced offload haven't been merged upstream yet) 
     *     NL80211_CMD_REGISTER_FRAME 
     *      * Allow a userspace application to register for receiving a given type of (management) frame through nl80211, and also replying to it. Applications can also specify a filter so for example they don't have to handle all the different action frames but just a subset. For action frames, a side effect is that the kernel will not reply to unknown action frames when they are registered by userspace. Used by wpa_supplicant for P2P also for probe requests. Related events: NL80211_CMD_FRAME, NL80211_CMD_FRAME_TX_STATUS. Prior to some work, this was called NL80211_CMD_REGISTER_ACTION, NL80211_CMD_ACTION, NL80211_CMD_ACTION_TX_STATUS. 
     *       (not a command) the ability to restrict the supported rates so 
     *        * that the P2P requirement of not using 11b rates can be fulfilled. This is still somewhat WIP for scanning, action frame TX etc. 

cfg80211's struct API
~~~~~~~~~~~~~~~~~~~~~

This just mirrors nl80211 with function/method calls etc.

mac80211's driver API
~~~~~~~~~~~~~~~~~~~~~

::

     *         * A remain_on_channel (see above in nl80211) hardware offload 
     *         *  * complete with canceling it and events 
     *         *   WIP: complete hardware offload for mgmt-tx (see above in nl80211) 
     *         *    * through a single function call 

Interface types
---------------

nl80211/cfg80211 currently define the P2P interface types P2P_CLIENT and P2P_GO, but wpa_supplicant doesn't use them, it still uses regular STA/AP interfaces. This is mostly because we haven't figured out a good way in the supplicant to distinguish between normal "STA" and P2P-client yet. The new P2P interface types will be needed later.

Driver considerations
---------------------

Drivers must currently only support AP and STA modes, and must be able to function during off-channel periods. They must also be able to receive probe requests even while in station mode, as indicated by mac80211 by the FIF_PROBE_REQ filter flag.

With the patches that I'm working on, drivers may optionally implement the p2p_start_listen/stop_listen callback to allow offload to the device for these operations. Additionally, they will be able to implement off-channel TX callbacks (but this is still WIP).
