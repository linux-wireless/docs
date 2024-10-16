Testing client powersave
========================

This is concerned with testing the AP to see that it behaves correctly.

Right now, this is just a collection of ideas

- johannes

implementation ideas
--------------------

There are two sides to this -- ideally, there'd be a tool that runs on two systems::

   +-------------------+
   | test machine 1    |
   | (wired only)      |
   +-------------------+
             |
   +-------------------+
   |     AP to test    |
   +-------------------+
             |
   +-------------------+
   | test machine 2    |
   | (special client)  |
   +-------------------+

If testing a special driver the "AP" and "test machine 1" should be the
same machine to allow some finer-grained control and checks. Testing the
packets "in the AP" is always possible since they're sent by the test
application on test machine 1, but to test the mac80211 APIs it's
necessary to ensure that the packets are in the low-level
driver/hardware queues already.

The "test machine 2" needs to run special wifi software, probably using
ath9k or a similar soft-MAC chipset that allows fine-grained control.
Ideally, this includes a debug mechanism to actually be able to turn
powersave on and off, or at least make the hardware not ACK packets
while in an application-controlled "powersave" state.

testcases
---------

null data packets
~~~~~~~~~~~~~~~~~

go to sleep / wake up
^^^^^^^^^^^^^^^^^^^^^

Clearly the easiest testcase, have the client go to sleep/wake up with
random/heavy traffic. With and without aggregation.

PS-Poll
~~~~~~~

no traffic
^^^^^^^^^^

If no traffic, check TIM bits are all clear. AP responds to PS-Poll with
(QoS) null data frame with more-data bit unset.

non-aggregated (light traffic)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Light traffic, turning off aggregation, send packets on each AC and poll
for them. Also check TIM bit for the client's AID. Check packets are
released from VO first, etc. Check TIM bit is set while there are
packets on any queue, and is cleared when no packets left. Check that
more-data bit is set until no more packets are queued in the AP. Check
behaviour of PS-Poll when no more data is queued (like previous test.)

non-aggregated (light traffic)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Same, but with heavy traffic.

When testing the AP driver try to ensure that as the client goes to
sleep there are frames on the hardware queues. This should easily be
achieved by a large socket buffer size and link saturation. Check TIM
bit like before. Make sure packets are not reordered between TIDs. Same
checks as above.

aggregated
^^^^^^^^^^

With aggregation on, repeat the tests and checks.

This time, make sure frames are on the hardware/driver queue for
aggregation, and are released properly one-by-one from there. Check for
reordering and in particular TIM bit/more-data issues.

uAPSD (and mixed with PS-Poll)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

all ACs delivery-/trigger-enabled
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

uAPSD triggers
''''''''''''''

Same tests as PS-Poll but this time with uAPSD trigger frames.

mixed
'''''

Same tests, mixing PS-Poll and trigger frames.

not all ACs delivery-/trigger-enabled
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Same tests, but the thing to look for is that the more-data bit is set
correctly and responses come only from, but from all, of the
delivery-enabled ACs.
