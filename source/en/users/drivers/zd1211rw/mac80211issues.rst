mac80211 issues
===============

This page lists the issues blocking zd1211rw moving to the mac80211 stack. Some of these may already be resolved, they just need to be checked.

TX disabling
~~~~~~~~~~~~

In the softmac driver, we temporarily disable TX while updating preamble mode and basic rates. This is not possible to do in mac80211 at the moment.

Basic rates handling
~~~~~~~~~~~~~~~~~~~~

In the softmac driver, we program the basic rates for RTS/CTS based on the association info. Need a similar system in mac80211.

Detailed error statistics
~~~~~~~~~~~~~~~~~~~~~~~~~

Ulrich has greatly improved the zd1211rw 802.11 error statistics. This code needs moving over to the mac80211 driver after figuring out how mac80211 does this.

-  `Detailed error statistics <http://dsd.object4.net/git/?p=zd1211.git;a=commitdiff;h=2c1784a975f39b49037358b061d4f94ed9ffcac2>`__

Testing on ARM and SPARC64
~~~~~~~~~~~~~~~~~~~~~~~~~~

We have happy ARM and SPARC64 users. To my knowledge, mac80211 has not been tested there.

* However, we do test on powerpc and x86 so there's unlikely to be
  problems. Also, who's going to test mac80211 without a driver? IMHO
  this is a requirement that can't be solved. -- JohannesBerg

Fixed issues
------------

* Regulatory domain control 
* Signal level reporting 
* Connectivity loss issues 
* monitor mode not showing all frames 
* monitor mode scanning oops 
* multicasting/IPv6 
* Barker preamble handling 
