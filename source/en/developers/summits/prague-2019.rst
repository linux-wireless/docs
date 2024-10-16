2019 wireless workshop
======================

Logistics
---------

Netdev 0x13 has been announced for Prague, Czech Republic, March 20-22:

http://netdevconf.org/0x13/

We're going to hold the next wireless workshop there, on March 20th.

Formalities are as usual - open (discussion) session, you only have to be registered for netdev to attend (but you can add yourself below so we have an idea of who's coming to talk about what).

Topics
------

-  fq_codel and airtime fairness integration in the wireless stack (Kevin Hayes, Kan Yan)
-  HE/11ax

   -  client side should be more or less done?
   -  AP side pretty much open - one thing to remember was configuration being not just in the beacon elements but also outside (we wanted to learn from VHT :-))
   -  much more multi-user TX/RX, are TXQs sufficient? but likely will need different scheduling

-  802.3/802.11 frame conversion offload with mac80211
-  eBPF integration into the wireless stack cont'd - for future statistics etc.

   -  old proposal from Johannes exists, but is pretty bare (and not done yet)
   -  are there other places where hooks should be added?
   -  XDP support for WiFi?

-  CRDA deprecation plan
-  CSI reporting
-  vendor command/event handling upstream

   -  TX power table switching?

-  upstream mechanisms for non-public features
-  security issue handling - can/should we sync better among ourselves?
-  What's the next for rtw88?
-  802.11ax timeline and testing discussion
-  release cadence? (iw, wpa_supplicant et al)
-  removing NAN APIs?
-  Android APIs

   -  RX filter?
   -  BT Coex enable/disable/auto?
   -  ...?

-  radiotap, in particular TLV format?
-  extended key ID support
-  S1G (mac80211, radiotap)

planning to attend
------------------

-  Johannes Berg
-  Kalle Valo
-  Yan Hsuan, Chuang
-  Stanislaw Gruszka
-  Toke Høiland-Jørgensen (parts of it; need to run `a tutorial <https://netdevconf.org/0x13/session.html?tutorial-XDP-hands-on>`__ as well)
-  Jouni Malinen
-  Maya Haim (Erez)
-  Michał Kazior
-  Kevin Hayes
-  Kan Yan
-  Kirtika Ruchandani
-  Brian Norris
-  Matthias May
-  Wojciech Dubowik
