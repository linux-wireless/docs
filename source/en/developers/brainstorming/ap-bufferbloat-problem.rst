AP Buffebloat Problem
=====================

I was thinking about bufferbloat & how to counter it in mac80211, in
particular on the AP side, and had some thoughts about how it compares
to wired, so I'm dumping some things here.

Consider a typical **wired** scenario::

   machine A === 1000mbps link ==== [switch] === 1000mbps === machine B
                                        |
                                        +--- 100mbps link --- machine C

Now say A is pumping data to both B and C at very high speeds. Obviously
the switch in the middle will start buffering a bit, and then drop
frames to C, so the stream there will back off quite quickly. If you
attempt to pump data to both at 300 mbps, the link to B will not be
affected at all.

In wireless though, there's no switch in the middle. Say A is the AP,
3x3 HT, B is a client with 3x3 and C is a legacy 11g client. The maximum
throughput to B might be 300mbps (is that even realistic? no matter) but
to C it'll be 24mbps at most. However, here airtime is the limit, and A
can't send 300+24mbps like it could on wired.

Obviously the fairness here will be different, and what should it be?
Should both get the same throughput, even though that probably means C
uses 80+% of airtime? Should both get the same airtime, so they can get
150 and 12 mbps respectively?

Regarding bufferbloat though the issue is worse because deeper queues
are needed to feed the link to B than to C, but all the frames are
sitting on the same queue today. And we really don't want to reserve
2007*4 queues (max stations \* ACs) all the time ...
