Wireless device queues
######################

Typically, wireless devices have four queues for the different access
categories, and additionally buffer somewhere for aggregation in HT
mode. For background information on how the queues are numbered, look at
:doc:`documentation/mac80211/queues`. Queue selection is done by
looking at the packet contents and putting the packet into the right AC
according to its IPv4 ToS markings, and to allow the administrator to
override this, the skb->priority field may override this. We were
discussing this in the context of "tc" and at some point this will
likely change to be more flexible.

Schematically:

.. image:: ../../media/en/developers/queues.png

Note that the software queues exist for each virtual interface, and the
aggregation queue there exists for each aggregation session. The above
picture reflects iwlwifi, for ath9k the aggregation queues are in the
driver instead but the mapping is identical.

The FIFOs are typically shallow and only used to buffer DMA latencies.
In any case, they typically can't be changed anyway.

Aggregation might collect up to 64 frames into a single aggregate, and
all those frames must be on the queue first, so those queues should be
allowed to get a fair number of frames to allow forming aggregates most
effectively; note that some drivers limit the aggregate length to less
than 64 (iwlwifi, for example, currently limits it to 31).

iwlwifi also separates virtual interfaces a bit more and gives each of
the two virtual interfaces its own set of hardware queues, but that
doesn't really make a big difference.

Wireless specific issues
************************

AP
~~

If a wireless device operates as an access point, it can be transmitting
to multiple stations at the same time, at very different speeds. If, for
example, the link to some station is really bad, a single short frame to
it might take more time than a number of longer frames to another
station that has better signal.

aggregation
~~~~~~~~~~~

Aggregation is controlled by driver (ath9k) or the device (iwlwifi).
There's a potential delay there -- packets may be held in preparation
for aggregation for some amount of time before they are transmitted so
that they can be aggregated at all -- if they were just put into the
device queue on ath9k they'd all be sent one by one. For iwlwifi the
device makes aggregation decisions, but it needs to have a number of
frames in the queue to make good ones. However, this complicates
estimating the queue airtime since the aggregation decisions aren't
known to the driver and the airtime heavily depends on them.

ath9k notes
***********

It should be possible to dynamically change the size of the internal
driver queues based on specific parameters. Specifically one current
idea is to use a `new adaptive algorithm
<http://www.hamilton.ie/tianji_li/buffersizing.pdf>`__ to change the
buffer size. This is being reviewed but patches and other ideas are
welcomed.
