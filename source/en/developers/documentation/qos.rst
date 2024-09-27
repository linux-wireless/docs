Wireless Quality of Service (QoS)
---------------------------------

Overview
~~~~~~~~

Quality of Service is supported on wireless devices which have WMM (Wi-Fi Multimedia) support. But it's still open how applications should use QoS. The intent of this page is to document all aspects of the problem and hopefully found a universal solution how QoS support can, and should be, implemented in applications.

Goal
~~~~

The goal is to have a guideline document for the Linux developers how to properly utilise QoS support in applications. The guidelines should work on different network technologies, be it Wi-Fi, DSL, cellular or whatever. Also they should be supported for a long time (read: years), so that proprietary applications can also benefit from QoS.

Problem
~~~~~~~

Currently it's not clear how applications should utilise QoS. The QoS documentation and specifications are very scattered and no-one really makes a stand how QoS really should be used by the applications.

Just to take IPv4 as an example. RFC 791 first defined TOS field with values low delay, high troughput, high reliability and precenence bits. The precedence bits are following:

::

   111 - Network Control
   110 - Internetwork Control
   101 - CRITIC/ECP
   100 - Flash Override
   011 - Flash
   010 - Immediate
   001 - Priority
   000 - Routine

These doesn't tell much, if any, for a normal application developer. For example, what does CRITIC/ECP mean?

Later RFC 2474 renamed the TOS field to Differentiated Services (DiffServ). DS field contains 6 bit Differentiated Service Control Point (DSCP) and 2 bit ECN field. But DiffServ doesn't take stance on meaning of the DSCP values, different networks can use different meanings for the values.

DiffServ contains "Class Selector PHB" which is meant to be help with backwards compatibility with the original TOS field with IP precedence bits. But the implementation of this optional and it doesn't clear up the meaning of IP precedence values at all.

Also it's not clear either in kernel side how to use it. For example, cfg80211 (including mac80211) uses skb->priority values 256-263 or IEEE 802.1d values in DSCP field. Applications can set skb->priority values with SO_PRIORITY, but meaning of the values is not documented anywhere. Also the use of 802.1d values as DSCP is a mystery.

Use cases and benefits
~~~~~~~~~~~~~~~~~~~~~~

Some examples how users can benefit and why we care:

-  easier to prioritise background traffic to not interfere with offer traffic, eg. interactive ssh connection
-  wireless: with U-APSD smaller power consumption on a VoIP call

Solutions
~~~~~~~~~

The solution for this mess is to come up with a common solution, document it and make the guideline available for developers.

There are few different methods, which are described below. Most probably there are even more, please add them to this wiki page.

`KalleValo <KalleValo>`__ has promised to write the guideline as soon as the technical parts are clear.

Solution 1: SO_PRIORITY with values 0-7
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Easy, applications need to just use setsockopt() and be done with it. It's unknown how widely supported values 0-7 are and the exact meaning of them, but at least they make sense (0 default, 1 lowest priority and 7 highest priority). The problem is that the priority is used only in the first link, rest of the route is not able to benefit from the classification.

Pros:

::

     * easy for applications 
     * works with both IPv4 and IPv6 Cons: 
       * only visible in in the first L2 link, not visible to upper layers (IP) 
       * no well defined meaning for the priority values 

Solution 2: SO_PRIORITY with values 256-263
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

mac80211 uses these values to map the packets to DSCP classes. Most probably non other stack or driver (even non-wifi ones) use these values. Otherwise similar as Solution 1.

Pros:

::

         * easy for applications 
         * works with both IPv4 and IPv6 Cons: 
           * only visible in in the first L2 link, not visible to upper layers (IP) 
           * no well defined meaning for the priority values 
           * using values over 256 is not intuitive 

Solution 3: IPv4 DSCP field with values 0-7
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Most, if not all, wifi drivers should use it. And, in theory, the receiver should also benefit from the classification, unless ISPs modify it of course. But the standardisation for IPv4 QoS bits is a mess.

Pros:

::

             * visible in IP layer (but ISPs change the value often?) Cons: 
               * applications need to handle IPv4 and IPv6 separately 

References
~~~~~~~~~~

`netdev: Question about IP_TOS and DSCP handling <http://marc.info/?l=linux-netdev&m=125875775229644&w=2>`__

`glibc bug#10789: netinet/ip.h lacks DSCP definitions <http://sourceware.org/bugzilla/show_bug.cgi?id=10789>`__

`linux-wireless: WMM classification guideline for applications? <http://www.spinics.net/lists/linux-wireless/msg43921.html>`__

`Wireless Summit 2 report <http://devresources.linux-foundation.org/shemminger/Wireless2/summary.html>`__
