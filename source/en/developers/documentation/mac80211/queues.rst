Queues
======

For QoS/WMM (EDCA) a mac80211 driver needs to have at least four queues.
mac80211 will then program the queues according to the advertised access
parameters.

**Legend:**

-  **MQ**: mac80211 queue
-  **AC**: Access Class
-  **ACI**: Access Class Index

mac80211 queue mapping:

.. list-table::
   :header-rows: 1

   - 

      - AC
      - MQ
   - 

      - BK
      - 3
   - 

      - BE
      - 2
   - 

      - VI
      - 1
   - 

      - VO
      - 0

802.11 uses the following number scheme (cf. Table 7-36)

.. list-table::
   :header-rows: 1

   - 

      - AC
      - ACI
   - 

      - BK
      - 01 (1)
   - 

      - BE
      - 00 (0)
   - 

      - VI
      - 10 (2)
   - 

      - VO
      - 11 (3)

Therefore, we have:

.. list-table::
   :header-rows: 1

   - 

      - AC
      - ACI
      - MQ
   - 

      - BK
      - 1
      - 3
   - 

      - BE
      - 0
      - 2
   - 

      - VI
      - 2
      - 1
   - 

      - VO
      - 3
      - 0

Due to internal collisions (we don't really know what this means either)
the queue numbering is important, and queue 0 is highest priority, 3
lowest. If your hardware has a different idea of queue priority, you may
need to rewrite the queue number, but make sure to do it everywhere
mac80211 passes a queue number (conf_tx, skb_get_queue_mapping).

The user priority is used as follows (802.11-2007 table 9-1):

.. list-table::
   :header-rows: 1

   - 

      - UP
      - AC
      - Priority
   - 

      - 1
      - BK
      - Lowest
   - 

      - 2
      - BK
      - .
   - 

      - 0
      - BE
      - .
   - 

      - 3
      - BE
      - .
   - 

      - 4
      - VI
      - .
   - 

      - 5
      - VI
      - .
   - 

      - 6
      - VO
      - .
   - 

      - 7
      - VO
      - Highest

TOS
---

mac80211 currently determines the UP based only on the IPv4 TOS field,
unless the packet priority is set to 256..263 with
setsockopt(SO_PRIORITY), in which case this maps directly to the UP
(priority - 256) for testing.

The IPv4 TOS field maps into the UP as follows, but keep in mind that the lowest two bits of the TOS are reserved (or used for ECN):

.. list-table::
   :header-rows: 1

   - 

      - TOS
      - UP
   - 

      - 0 - 31
      - 0
   - 

      - 32 - 63
      - 1
   - 

      - ...
      - 
   - 

      - 224 - 255
      - 7

DSCP (RFC 2474)
---------------

Alternatively you can set the IP_TOS with setsockopt, then you need to
ask how DSCP maps into the UP. DSCP is defined in the Differentiated
Services (`DiffServ <DiffServ>`__) model as the six most significant
bits of the `DiffServ <DiffServ>`__\ (DS) Field.

.. list-table::

   - 

      - DS5 (P2)
      - DS4 (P1)
      - DS3 (P0)
      - DS2
      - DS1
      - DS0
      - ECN
      - ECN

The classes of DSCP in wide usage are:

.. list-table::
   :header-rows: 1

   - 

      - DSCP Class
      - Codepoint(s)
   - 

      - Default
      - 0x00
   - 

      - Expedited Forwarding (EF)
      - 0x2E
   - 

      - Assured Forwarding (AF1)
      - 0xA, 0xC, 0xE
   - 

      - Assured Forwarding (AF2)
      - 0x12, 0x14, 0x16
   - 

      - Assured Forwarding (AF3)
      - 0x1A, 0x1C, 0x1E
   - 

      - Assured Forwarding (AF4)
      - 0x22, 0x24, 0x26

The 3 Precedence bits of DSCP (**P2, P1, P0**) are used for mapping to 802.1D tags and AC values as:

.. list-table::
   :header-rows: 1

   - 

      - P2 P1 P0
      - 802.1D
      - AC
   - 

      - 0 0 0
      - 0
      - BE
   - 

      - 0 0 1
      - 1
      - BK
   - 

      - 0 1 0
      - 2
      - BK
   - 

      - 0 1 1
      - 3
      - BE
   - 

      - 1 0 0
      - 4
      - VI
   - 

      - 1 0 1
      - 5
      - VI
   - 

      - 1 1 0
      - 6
      - VO
   - 

      - 1 1 1
      - 7
      - VO

Testing
-------

* Use ping ( with -Q option, see manpage ) 
* use iperf: ``iperf -S 0xE0 -c <IP>``
* Use iptables. Example session with 2 iperf streams: 

    * ``iptables -t mangle -A OUTPUT -p tcp –dport 5000 -j DSCP –set-dscp-class "EF"``
    * ``iptables -t mangle -A OUTPUT -p tcp –dport 5001 -j DSCP –set-dscp-class "BE"``
