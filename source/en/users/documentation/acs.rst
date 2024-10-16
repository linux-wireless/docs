ACS (Automatic Channel Selection)
=================================

Automatic Channel Selection algorithms and implementations are used to
enable interfaces to automatically figure out which channel
configuration to use for initiating communication, for any mode of
operation which initiates radiation (AP, Mesh, IBSS, P2P).

There are different algorithms that can be used to finding an ideal
channel. We currently only have one, described below.

ACS code
--------

All algorithms can be dumped into a generic permissively licensed
userspace application which can then be used for integration into
different projects.

Survey based algorithm
----------------------

The survey based algorithm relies on the nl80211 survey API command to
query the interface for channel active time, channel busy time, channel
tx time and noise. The active time consists of the amount of time the
radio has spent on the channel. The busy time consists of the amount of
time the radio has spent on the channel but noticed the channel was busy
and could not initiate communication if it wanted to. The tx time is the
amount of time the radio has spent on the channel transmitting data. The
survey algorithm relies on these values to build an *interference
factor* to give a sense of how much interference was detected on the
channel and then picks the channel with the lowest *interference
factor*.

The *interference factor* is defined as the ratio of the observed busy
time over the time we spent on the channel, this value is then amplified
by the noise floor observed on the channel in comparison to the lowest
noise floor observed on the entire band.

This corresponds to::

   (busy time - tx time) / (active time - tx time) * 2^(chan_nf - band_min_nf)

The coefficient of of 2 reflects the way power in "far-field" radiation
decreases as the square of distance from the antenna. What this does is
it decreases the observed busy time ratio if the noise observed was low
but increases it if the noise was high, proportionally to the way "far
field" radiation changes over distance. Using a minimum noise instead of
some "known low noise" value allows this code to be agnostic to any card
used, even if the card is yielding incorrect values for noise floor. The
minimum noise floor would be the lowest recorded noise floor from all
surveyed channels. It is worth showing a few examples of what the
multiplier produces to demonstrate how it amplifies the value for high
noise. Since we have recorded the lowest observed noise floor by using
the delta between what we observed and the lowest observed noise floor
on the band we would get multipliers that are always positive and the
lowest multiplier would be a value of 1 given that 2^0 = 1. Lets assume
the lowest recorded noise floor was -110 dBm here are a few example
values::

   mcgrof@tux ~ $ calc
   C-style arbitrary precision calculator (version 2.12.3.3)
   Calc is open software. For license details type:  help copyright
   [Type "exit" to exit, or "help" for help.]

   ; define f(x) = 2^(x - -110)
   f(x) defined
   ; f(-110)
           1
   ; f(-109)
           2
   ; f(-108)
           4

The right hand value of the formula then can be thought of as the
amplifier of the observed 'business'.

If channel busy time is not available the fallback is to use channel rx
time.

Since noise floor is in dBm it is necessary to convert it into Watts so
that combined channel intereference (e.g. HT40, which uses two channels)
can be calculated easily.

::

   (busy time - tx time) / (active time - tx time) * 2^(10^(chan_nf/10) + 10^(band_min_nf/10))

However to account for cases where busy/rx time is 0 (channel load is
then 0%) channel noise floor signal power is combined into the equation
so a channel with lower noise floor is preferred. The equation becomes::

   10^(chan_nf/5) + (busy time - tx time) / (active time - tx time) * 2^(10^(chan_nf/10) + 10^(band_min_nf/10))

This "interference factor" is purely subjective and ony time will tell
how usable this is. By using the minimum noise floor we remove any
possible issues due to card calibration. The computation of the
interference factor then is dependent on what the card itself picks up
as the minimum noise, not an actual real possible card noise value.

Total interference factor
-------------------------

The above channel interference factor is calculated with no respect to
target operational bandwidth.

To find an ideal channel the above data is combined by taking into
account the target operational bandwidth and selected band. E.g. on
2.4GHz channels overlap w/ 20MHz bandwidth, but there is no overlap for
20MHz bandwidth on 5GHz.

Each valid and possible channel spec (i.e. channel + width) is taken and
its interference factor is computed by summing up interferences of each
channel it overlaps. The one with least total interference is picked up.

Note: This implies base channel interference factor must be non-negative
allowing easy summing up.

Example survey-based ACS analysis printout from hostapd
-------------------------------------------------------

::

   ACS: Trying survey-based ACS
   ACS: Survey analysis for channel 1 (2412 MHz)
   ACS:  1: min_nf=-113 interference_factor=0.0802469 nf=-113 time=162 busy=0 rx=13
   ACS:  2: min_nf=-113 interference_factor=0.0745342 nf=-113 time=161 busy=0 rx=12
   ACS:  3: min_nf=-113 interference_factor=0.0679012 nf=-113 time=162 busy=0 rx=11
   ACS:  4: min_nf=-113 interference_factor=0.0310559 nf=-113 time=161 busy=0 rx=5
   ACS:  5: min_nf=-113 interference_factor=0.0248447 nf=-113 time=161 busy=0 rx=4
   ACS:  * interference factor average: 0.0557166
   ACS: Survey analysis for channel 2 (2417 MHz)
   ACS:  1: min_nf=-113 interference_factor=0.0185185 nf=-113 time=162 busy=0 rx=3
   ACS:  2: min_nf=-113 interference_factor=0.0246914 nf=-113 time=162 busy=0 rx=4
   ACS:  3: min_nf=-113 interference_factor=0.037037 nf=-113 time=162 busy=0 rx=6
   ACS:  4: min_nf=-113 interference_factor=0.149068 nf=-113 time=161 busy=0 rx=24
   ACS:  5: min_nf=-113 interference_factor=0.0248447 nf=-113 time=161 busy=0 rx=4
   ACS:  * interference factor average: 0.050832
   ACS: Survey analysis for channel 3 (2422 MHz)
   ACS:  1: min_nf=-113 interference_factor=2.51189e-23 nf=-113 time=162 busy=0 rx=0
   ACS:  2: min_nf=-113 interference_factor=0.0185185 nf=-113 time=162 busy=0 rx=3
   ACS:  3: min_nf=-113 interference_factor=0.0186335 nf=-113 time=161 busy=0 rx=3
   ACS:  4: min_nf=-113 interference_factor=0.0186335 nf=-113 time=161 busy=0 rx=3
   ACS:  5: min_nf=-113 interference_factor=0.0186335 nf=-113 time=161 busy=0 rx=3
   ACS:  * interference factor average: 0.0148838
   ACS: Survey analysis for channel 4 (2427 MHz)
   ACS:  1: min_nf=-114 interference_factor=1.58489e-23 nf=-114 time=162 busy=0 rx=0
   ACS:  2: min_nf=-114 interference_factor=0.0555556 nf=-114 time=162 busy=0 rx=9
   ACS:  3: min_nf=-114 interference_factor=1.58489e-23 nf=-114 time=161 busy=0 rx=0
   ACS:  4: min_nf=-114 interference_factor=0.0186335 nf=-114 time=161 busy=0 rx=3
   ACS:  5: min_nf=-114 interference_factor=0.00621118 nf=-114 time=161 busy=0 rx=1
   ACS:  * interference factor average: 0.0160801
   ACS: Survey analysis for channel 5 (2432 MHz)
   ACS:  1: min_nf=-114 interference_factor=0.409938 nf=-113 time=161 busy=0 rx=66
   ACS:  2: min_nf=-114 interference_factor=0.0432099 nf=-113 time=162 busy=0 rx=7
   ACS:  3: min_nf=-114 interference_factor=0.0124224 nf=-113 time=161 busy=0 rx=2
   ACS:  4: min_nf=-114 interference_factor=0.677019 nf=-113 time=161 busy=0 rx=109
   ACS:  5: min_nf=-114 interference_factor=0.0186335 nf=-114 time=161 busy=0 rx=3
   ACS:  * interference factor average: 0.232244
   ACS: Survey analysis for channel 6 (2437 MHz)
   ACS:  1: min_nf=-113 interference_factor=0.552795 nf=-113 time=161 busy=0 rx=89
   ACS:  2: min_nf=-113 interference_factor=0.0807453 nf=-112 time=161 busy=0 rx=13
   ACS:  3: min_nf=-113 interference_factor=0.0310559 nf=-113 time=161 busy=0 rx=5
   ACS:  4: min_nf=-113 interference_factor=0.434783 nf=-112 time=161 busy=0 rx=70
   ACS:  5: min_nf=-113 interference_factor=0.0621118 nf=-113 time=161 busy=0 rx=10
   ACS:  * interference factor average: 0.232298
   ACS: Survey analysis for channel 7 (2442 MHz)
   ACS:  1: min_nf=-113 interference_factor=0.440994 nf=-112 time=161 busy=0 rx=71
   ACS:  2: min_nf=-113 interference_factor=0.385093 nf=-113 time=161 busy=0 rx=62
   ACS:  3: min_nf=-113 interference_factor=0.0372671 nf=-113 time=161 busy=0 rx=6
   ACS:  4: min_nf=-113 interference_factor=0.0372671 nf=-113 time=161 busy=0 rx=6
   ACS:  5: min_nf=-113 interference_factor=0.0745342 nf=-113 time=161 busy=0 rx=12
   ACS:  * interference factor average: 0.195031
   ACS: Survey analysis for channel 8 (2447 MHz)
   ACS:  1: min_nf=-114 interference_factor=0.0496894 nf=-112 time=161 busy=0 rx=8
   ACS:  2: min_nf=-114 interference_factor=0.0496894 nf=-114 time=161 busy=0 rx=8
   ACS:  3: min_nf=-114 interference_factor=0.0372671 nf=-113 time=161 busy=0 rx=6
   ACS:  4: min_nf=-114 interference_factor=0.12963 nf=-113 time=162 busy=0 rx=21
   ACS:  5: min_nf=-114 interference_factor=0.166667 nf=-114 time=162 busy=0 rx=27
   ACS:  * interference factor average: 0.0865885
   ACS: Survey analysis for channel 9 (2452 MHz)
   ACS:  1: min_nf=-114 interference_factor=0.0124224 nf=-114 time=161 busy=0 rx=2
   ACS:  2: min_nf=-114 interference_factor=0.0310559 nf=-114 time=161 busy=0 rx=5
   ACS:  3: min_nf=-114 interference_factor=1.58489e-23 nf=-114 time=161 busy=0 rx=0
   ACS:  4: min_nf=-114 interference_factor=0.00617284 nf=-114 time=162 busy=0 rx=1
   ACS:  5: min_nf=-114 interference_factor=1.58489e-23 nf=-114 time=162 busy=0 rx=0
   ACS:  * interference factor average: 0.00993022
   ACS: Survey analysis for channel 10 (2457 MHz)
   ACS:  1: min_nf=-114 interference_factor=0.00621118 nf=-114 time=161 busy=0 rx=1
   ACS:  2: min_nf=-114 interference_factor=0.00621118 nf=-114 time=161 busy=0 rx=1
   ACS:  3: min_nf=-114 interference_factor=0.00621118 nf=-114 time=161 busy=0 rx=1
   ACS:  4: min_nf=-114 interference_factor=0.0493827 nf=-114 time=162 busy=0 rx=8
   ACS:  5: min_nf=-114 interference_factor=1.58489e-23 nf=-114 time=162 busy=0 rx=0
   ACS:  * interference factor average: 0.0136033
   ACS: Survey analysis for channel 11 (2462 MHz)
   ACS:  1: min_nf=-114 interference_factor=1.58489e-23 nf=-114 time=161 busy=0 rx=0
   ACS:  2: min_nf=-114 interference_factor=2.51189e-23 nf=-113 time=161 busy=0 rx=0
   ACS:  3: min_nf=-114 interference_factor=2.51189e-23 nf=-113 time=161 busy=0 rx=0
   ACS:  4: min_nf=-114 interference_factor=0.0432099 nf=-114 time=162 busy=0 rx=7
   ACS:  5: min_nf=-114 interference_factor=0.0925926 nf=-114 time=162 busy=0 rx=15
   ACS:  * interference factor average: 0.0271605
   ACS: Survey analysis for channel 12 (2467 MHz)
   ACS:  1: min_nf=-114 interference_factor=0.0621118 nf=-113 time=161 busy=0 rx=10
   ACS:  2: min_nf=-114 interference_factor=0.00621118 nf=-114 time=161 busy=0 rx=1
   ACS:  3: min_nf=-114 interference_factor=2.51189e-23 nf=-113 time=162 busy=0 rx=0
   ACS:  4: min_nf=-114 interference_factor=2.51189e-23 nf=-113 time=162 busy=0 rx=0
   ACS:  5: min_nf=-114 interference_factor=0.00617284 nf=-113 time=162 busy=0 rx=1
   ACS:  * interference factor average: 0.0148992
   ACS: Survey analysis for channel 13 (2472 MHz)
   ACS:  1: min_nf=-114 interference_factor=0.0745342 nf=-114 time=161 busy=0 rx=12
   ACS:  2: min_nf=-114 interference_factor=0.0555556 nf=-114 time=162 busy=0 rx=9
   ACS:  3: min_nf=-114 interference_factor=1.58489e-23 nf=-114 time=162 busy=0 rx=0
   ACS:  4: min_nf=-114 interference_factor=1.58489e-23 nf=-114 time=162 busy=0 rx=0
   ACS:  5: min_nf=-114 interference_factor=1.58489e-23 nf=-114 time=162 busy=0 rx=0
   ACS:  * interference factor average: 0.0260179
   ACS: Survey analysis for selected bandwidth 20MHz
   ACS:  * channel 1: total interference = 0.121432
   ACS:  * channel 2: total interference = 0.137512
   ACS:  * channel 3: total interference = 0.369757
   ACS:  * channel 4: total interference = 0.546338
   ACS:  * channel 5: total interference = 0.690538
   ACS:  * channel 6: total interference = 0.762242
   ACS:  * channel 7: total interference = 0.756092
   ACS:  * channel 8: total interference = 0.537451
   ACS:  * channel 9: total interference = 0.332313
   ACS:  * channel 10: total interference = 0.152182
   ACS:  * channel 11: total interference = 0.0916111
   ACS:  * channel 12: total interference = 0.0816809
   ACS:  * channel 13: total interference = 0.0680776
   ACS: Ideal channel is 13 (2472 MHz) with total interference factor of 0.0680776

Driver implementation details
-----------------------------

User space can get survey using ``NL80211_CMD_GET_SURVEY`` command. It
requires:

- ``cfg80211`` drivers to implement ``dump_survey`` callback
- ``mac80211`` drivers to implement ``get_survey`` callback

As explained is algorithm section, driver needs to provide (fill) few
different informations about a channel:

- Noise floor (``SURVEY_INFO_NOISE_DBM``) put into ``NL80211_SURVEY_INFO_NOISE``
- Channel time (``SURVEY_INFO_TIME``) put into ``NL80211_SURVEY_INFO_TIME``
- Time of channel unavailability which is **one** of:

   - RX time (``SURVEY_INFO_TIME_RX``) put into ``NL80211_SURVEY_INFO_TIME_RX``
   - Busy time (``SURVEY_INFO_TIME_BUSY``) put into ``NL80211_SURVEY_INFO_TIME_BUSY``

Hostapd setup
-------------

Only the following drivers support the current (2014-08-19) survey based
ACS implmenetation in hostapd
(https://w1.fi/cgit/hostap/tree/hostapd/defconfig#n329).

- ath5k
- ath9k (The pcie version only)
- ath10k When building make sure you enable ACS in hostapd's .config file::

     CONFIG_ACS=y

To make hostapd do ACS during runtime make sure your hostapd.conf has
either::

   channel=0

or::

   channel=acs_survey

Hostapd picks a channel automatically. If you don't configure HT40 it
will not use HT40. If you do configure HT40 it will use it or fail if
it's impossible to setup HT40 (e.g. due regulatory).

Status
------

* initial implementation is now complete, `ACS hostapd RFC patches
  <http://marc.info/?l=linux-wireless&m=130870274629048&w=2>`__ have
  been posted.
* `improved implementation has been posted <http://marc.info/?l=hostap&m=137569522705154&w=2>`__
* As of 31 Aug 2013 ACS has been **merged** into upstream hostapd
  (`final commit <http://w1.fi/gitweb/gitweb.cgi?p=hostap.git;a=commit;h=50f4f2a066e60be7cc03e291635e9a0f953922bd>`__)

References
----------

* `Initial ACS algorithm proposal <http://marc.info/?t=130624150700002&r=1&w=2>`__
* `ACS code announcement <http://marc.info/?t=130775164000002&r=1&w=2>`__
