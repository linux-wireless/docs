Rate Control
============

This page describes the minstrel rate control algorithm for mac80211.

Overview
--------

minstrel is a mac80211 rate control algorithm ported over from `MadWifi
<MadWifi>`__ which supports multiple rate retries and claimed to be one
of the best, if not the best, rate control algorithm.

Why did we write it ?
---------------------

I had two identical nodes in my office, both running some rate
algorithm. The rate algorithm was picking 6 MBits/sec as the optimal
rate. Yet, if I took those nodes and used a fixed rate setting, adjusted
the fixed rate until the ideal combination was found, a much better
throughput (12 MBits/sec) could be achieved. Clearly, there was room for
improvement.

A second test was to take those two nodes, with some rate algorithm, and
look at the throughput. One node was moved behind a pillar. The measured
throughput dropped. Then the nodes were moved so that the beam path was
not blocked. But, the measured throughput did not increase. This test
said that the rate algorithm is not responding to changes in the
environment. Surely, something better can be done??

Inspection of the code in different rate algorithms left us bewildered.
Why did all the code bases we looked at contain the assumption that
packets sent at slow data rates are more likely to succeed than packets
sent at higher datarates? The physics behind this assumption baffled us.
A slow data rate packet has the highest possibility of being "shot down"
by some other node sending a packet.

Thus, the decision was made to write an automatic rate algorithm that

- relied solely on measured performance with the minimum of assumptions
- responded to changes in the environment - so it must auto update correctly
- compare the performance of our algorithm at all times with that
  obtained by adjusting the fixed rate setting

What is the basis for the algorithm?
------------------------------------

Some rate algorithms for 802.11 have measured RSSI, and used this figure
as a basis for choosing the rate to use. However, it is not clear which
rate should be used for a given RSSI figure. Any conversion table is
going to give misleading results, as it cannot take into account the
influence of multipath. The radio does provide feedback after each
packet is transmitted - this reports what rate worked and what rates
failed. We have, with this feedback, good evidence for deciding what
rate to use.

Packets sent between two radio devices have some chance of being
successfully sent. The probability of success is an unknown function of
the variables (distance between devices, multipath effects, interference
from other devices). The radio can be used in any environment, where the
relationship between these variables is unknown. Further, we do not know
which variable will predominate. We do not even know what the
interference will look like. If the interference is bursty, then quicker
packets (higher rates) have a better chance of getting through in the
gaps. Given the unknown nature of the environment, we decided that
performance at a particular rate has to be considered as being
independant of performance at a different rate.

Since the relationship between these variables is not known we decided
to take a `heuristic
<http://dictionary.reference.com/search?q=heuristic>`__ approach,
meaning "pertaining to, or based on experimentation, evaluation, or
trial-and-error methods".

The implementation of minstrel provides a rate table for each of the
remote nodes being communicated with. This rate table is found in the
debugfs directory, and shows some interesting things. Sometimes, the
11mbit rate is more likely to succeed, or has a higher throughput, than
the the 2mbit rate.

History of minstrel
-------------------

The minstrel rate control algorithm present on mac80211 was ported from
`MadWifi <MadWifi>`__ by Felix Fietkau. `MadWifi <MadWifi>`__'s minstrel
implementation was released on January 2005, originally designed and
implemented by Derek Smithies Ph.D. `Read minstrel's madwifi
documentation
<http://madwifi-project.org/browser/madwifi/trunk/ath_rate/minstrel/minstrel.txt>`__.

From wikipedia, `definition <http://en.wikipedia.org/wiki/Minstrel>`__,
a minstrel was a medieval European bard who performed songs whose lyrics
told stories about distant places or about real or imaginary historical
events. Minstrels would travel throughout Europe seeking employment at
feasts or festivals. Others worked in royal courts. Essentially then, a
minstrel would endeavour to entertain people with music or poems. If
there was no money - the minstrel would move elsewhere. And so it is
with this rate algorithm. All rates are tried. If a rate works well, it
is used. If a rate works badly, it is ignored. All rates are tried on a
regular basis.

Theory of operation
-------------------

We defined the measure of successfulness (of packet transmission) as the
throughput, which is the number of bits transmitted

::

          Prob_success_transmission \* Mega bits transmitted
          throughput = -------------------------------------------------
                        time for 1 try of 1 packet to be sent on the air</code>

This measure of successfulness will therefore adjust the transmission
speed to get the maximum number of data bits through the radio
interface. Further, it means that the 1 Mbps rate (which typically has a
high probability of successful transmission) will not be used in
preference to the 11 Mbps rate.

We decided that the module should record the successfulness of all
packets that are transmitted. From this data, the module has sufficient
information to decide which packets are more successful than others.
However, a variability element was required. We had to force the module
to examine bit rates other than optimal. Consequently, some percent of
the packets have to be sent at rates regarded as non optimal.

10 times a second (this frequency is alterable by changing the driver
code) a timer fires, which evaluates the statistics table. EWMA
calculations (described below) are used to process the success history
of each rate. On completion of the calculation, a decision is made as to
the rate which has the best throughput, second best throughput, and
highest probability of success. This data is used for populating the
retry chain during the next 100 ms. Note that the retry chain is
described below.

As stated above, the minstrel algorithm collects statistics from all
packet attempts. Minstrel spends a particular percentage of frames,
doing "look around" i.e. randomly trying other rates, to gather
statistics. The percentage of "look around" frames defaults to 10%. The
distribution of lookaround frames is also randomized somewhat to avoid
any potential "strobing" of lookaround between similar nodes.

One of our test networks consisted of three nodes, A, B, C. Node C
snarfed all the packets on the air for analysis in wireshark. With this
network, it was possible to verify that A and B were correctly choosing
the optimal rate (by manually looking at the packet dump on C).
Interestingly, we saw that sometimes there was a 100ms delay between the
receipt of an 802.11 ack packet and the transmission of the next data
packet. Our view is that the TCP congestion control mechanism was the
cause. Since the packet took so long to transmit, the TCP control code
in the kernel was delaying the next data packet. Adding code so that the
retry chain never exceeded 26 ms in length gave a significant increase
in measured throughput.

Retry Chain
-----------

Several devices have built in multirate retry chains. For example
Atheros 802.11abg chipsets have four segments. Each segment is an
advisement to the hardware to try to send the current packet at some
rate, with a fixed number of retry attempts. Once the packet is
successfully transmitted, the remainder of the retry chain is ignored.
Selection of the number of retry attempts was based on the desire to get
the packet out in under 26 ms, or fail.

There is some room for movement here - if the traffic is UDP then the
limit of 26 ms for the retry chain length is "meaningless". However, one
may argue that if the packet was not transmitted after some time period,
it should fail. Further, one does expect UDP packets to fail in
transmission. We leave it as an area for future improvement.

The (re)try segment chain is calculated in two possible manners. If this
packet is a normal tranmission packet (90% of packets are this) then the
retry count is best throughput, next best throughput, best probability,
lowest baserate. If it is a sample packet (10% of packets are this),
then the retry chain is random lookaround, best throughput, best
probability, lowest base rate. In tabular format::


         Try | Lookaround rate    | Normal rate
         ------------------------------------------------
          1  | Random lookaround  | Best throughput
          2  | Best throughput    | Next best throughput
          3  | Best probability   | Best probability
          4  | Lowest Baserate    | Lowest Baserate</code>

The retry count is adjusted so that the transmission time for that
section of the retry chain is less than 26 ms.

We have adjusted the code so that the lowest rate is never used for the
lookaround packet. Our view is that since this rate is used for
management packets, this rate must be working. Alternatively, the link
is set up with management packets, data packets are acknowledged with
management packets. Should the lowest rate stop working, the link is
going to die reasonably soon.

Analysis of information showed that the system was sampling too hard at
some rates. For those rates that never work (54mb, 500m range) there is
no point in sending 10 sample packets (< 6 ms time). Consequently, for
the very very low probability rates, we sample at most twice.

The retry chain above does "work", but performance is suboptimal. The
key problem being that when the link is good, too much time is spent
sampling the slower rates. Thus, for two nodes adjacent to each other,
the throughput between them was several Mbps below using a fixed rate.
The view was that minstrel should not sample at the slower rates if the
link is doing well. However, if the link deteriorates, minstrel should
immediately sample at the lower rates.

Some time later, we realized that the only way to code this reliably was
to use the retry chain as the method of determining if the slower rates
are sampled. The retry chain was modified as::

   Try |         Lookaround rate              | Normal rate
       | random < best    | random > best     |
   --------------------------------------------------------------
    1  | Best throughput  | Random rate       | Best throughput
    2  | Random rate      | Best throughput   | Next best throughput
    3  | Best probability | Best probability  | Best probability
    4  | Lowest Baserate  | Lowest baserate   | Lowest baserate

With this retry chain, if the randomly selected rate is slower than the
current best throughput, the randomly selected rate is placed second in
the chain. If the link is not good, then there will be data collected at
the randomly selected rate. Thus, if the best throughput rate is
currently 54 Mbps, the only time slower rates are sampled is when a
packet fails in transmission. Consequently, if the link is ideal, all
packets will be sent at the full rate of 54 Mbps. Which is good.

EWMA
----

The core of the Minstrel rate algorithm is the EWMA, or Exponential
Weighted Moving Average. The EWMA is defined on wikipedia `here
<http://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average>`__.
Using an EWMA allows us to put more importance on recent results, than
older results. Consequently, we can cope with environmental changes, as
old results (from a potentially different environment) are ignored.

At the beginning of this document, we described a test with two nodes,
and one node was moved behind a pillar (blocking the beam) and then
moving the node out from behind the pillar. For an automatic rate
control algorithm, some method is required to assign more importance to
recent results than old results. By using EWMA, we can achieve this. Old
results have minimal impact on the choice of ideal rate.

The EWMA calculation is carried out 10 times a second, and is run for
each rate. This calculation has a smoothing effect, so that new results
have a reasonable (but not large) influence on the selected rate.
However, with time, a series of new results in some particular direction
will predominate. Given this smoothing, we can use words like inertia to
describe the EWMA.

By "new results", we mean the results collected in the just completed
100 ms interval. Old results are the EWMA scaling values from before the
just completed 100 ms interval.

If no packets have been sent for a particular rate in a time interval,
no calculation is carried out.

The appropriate update interval was selected on the basis of choosing a
compromise between:

* collecting enough success/failure information to be meaningful 
* minimizing the amount of cpu time spent do the updates 
* providing a means to recover quickly enough from a bad rate selection.
  The first two points are self explanatory. When there is a sudden
  change in the radio environment, an update interval of 100 ms will
  mean that the rates marked as optimal are very quickly marked as poor.
  Consequently, the sudden change in radio environment will mean that
  minstrel will very quickly switch to a better rate. 

A sudden change in the transmission probabilities will happen when the
node has not transmitted any data for a while, and during that time the
environment has changed. On starting to transmit, the probability of
success at each rate will be quite different. The driver must adapt as
quickly as possible, so as to not upset the higher TCP network layers.

DebugFs contents
----------------

As noted above, Minstrel keeps state on each node that we are associated
with. Minstrel has a record of the which rates worked, and which rates
failed. This information is available to the user via the debugfs file
system. To mount the debugfs::

   # mount -t debugfs debugfs /sys/kernel/debug/

Inside the ``/sys/kernel/debug/ieee80211/phy0/stations/`` directory
there will be subdirectories, where the subdirectory corresponds to each
node that we are associated with. The name of the subdirectory is the
mac address of the associated node. Take for example (from a box here)
the directory
``/sys/kernel/debug/ieee80211/phy0/stations/00:02:6f:49:41:01``. There
are 6 different files::

   agg_status        report of different parameters for the remote station
   flags             Auth, Assoc, ps authorized preamble, wme, wds, mfp
   inactive_ms       time (ms) since received a last packet
   last_seq_ctrl     for each RX q, last rx seq/frag number from the remote station
   num_ps_buf_frames number of ps frames to transmit to the remote station
   rc_stats          A table of loss/success rates for each data rates

The most interesting file is the ``rc_stats`` file, as it contains the
working information that Minstrel uses to determine the rate for the
next packet, and is a report on which rates work well/badly. While
developing Minstrel, the following command::

   while true; do cat rc_stats ; sleep 1; clear; done

provided much insight as to what was happening.

Example contents of the ``rc_stats`` file is::

   rate   throughput ewma prob this prob  this succ/attempt success  attempts
     P1     0.9       99.9      100.0          0(  0)        105      111
      2     0.4       25.0      100.0          0(  0)          1        1
      5.5   1.2       25.0      100.0          0(  0)          1        1
     11     1.1       12.5       50.0          0(  0)          1        2
      6     0.0        0.0        0.0          0(  0)          0        0
      9     0.0        0.0        0.0          0(  0)          0        0
     12     0.0        0.0        0.0          0(  0)          0        0
     18     0.0        0.0        0.0          0(  0)          0        0
     24     0.0        0.0        0.0          0(  0)          0        0
     36     0.0        0.0        0.0          0(  0)          0        0
    t48    16.0       40.9       88.8          0(  0)          9       10
   T 54    16.2       91.1       91.2        115(126)      96429   109032

   Total packet count::    ideal 5756      lookaround 641

Here, we see the performance figures for two nodes in close proximity
(they are beside each other) operating in bg mode.

* At the very left, there are the letters T, t and P. These  indicate
  the rates with the highest Throughput, second highest througput, and
  highest EWMA probability. Minstrel will use these particular rates for
  the retry chain. 
* The throughput column describes the measured throughput for a packet
  given the probability of success. 
* The ewma probability is the figure  described above - the current time
  weighted chance that a packet at this rate will reach the remote
  station. 
* This prob reports the success chance from the last time interval in
  which minstrel recorded data. Should there be no data, then the figure
  from the earlier time interval (containing data) is used. 
* This succ/attempt reports how many packets were sent (and number of
  successes) in the last time interval. 
* Finally, the global number of success and attempts (that is, since the
  remote node became associated with us). From looking at this table, we
  see that almost all of the data packets have been sent at 54Mbits/sec.
  The total packet count reports the number of packets that have been
  processed by minstrel (modulo 10000). This indicates if data has been
  flowing. 
