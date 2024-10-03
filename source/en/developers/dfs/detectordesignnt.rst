Design Proposal for DFS Pattern Detector
========================================

About
-----

We at Neratec started working on DFS when we realized that radar
detection is of no or minor relevance for mac80211 / ath9k development.
After inspecting the latest ETSI requirements for radar datection
(V1.5.1, see :doc:`ETSI specs <etsi>`) we assumed that reliable
detection of the patterns defined there will be difficult to achieve wrt
the higher probability of false positives with the updated specs.

Assuming the core problem to be the right balance between true and false
pattern detection, we implemented a test framework capable to perform
statistical analyses of pattern detection algorithms based on SW
generated test patterns. With this test system we are able to compare
the detection reliability of different approaches and to fine-tune the
detection parameters to statistically match a given tradeoff between
true and false detections.

In the next step we integrated a pattern detector into mac80211 and
interfaced it to ath9k to verify that the detection works with physical
HW.

This page gives a short overview of how we initially planned to
integrate DFS functionality and how we would have designed it. Now that
DFS will be implemented by joint efforts, we propose our chosen design
approach for discussion. Patches for a working proof-of-concept are
posted at the mailing-list.

Goals / Assumptions
-------------------

Our approach aims to provide a HW independent pattern matching entity
located in the mac80211.

We assume that there are three types of HW devices:

#. chipsets that are not capable of detecting radar pulses
#. chipsets tha can detect single radar pulses
#. chipsets that detect radar patterns fully in HW The proposed detector
   module is designed to support type 2 HW. In this approach the HW is
   responsible to reliably detect a radar pulse and forward it to the
   detector. The detector evaluates the pulses and in case of pattern
   detection reports it to mac80211 to trigger further processing.

Design
------

Incorporating DFS pattern detection with the given approach requires
following interfaces

- HW -> mac80211: reporting radar pulses
- mac80211 -> pattern detector: feeding radar events
- pattern detector -> mac80211: notify about detected radar

Note that we are discussing only the bare detection here, excluding all
those actions that must follow a detection event.

Pattern Detector Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~

Pattern detection as specified by ETSI (TBC: and FCC?) works solely
based on a given set of input parameters, namely

.. code-block:: c

   /**
    * struct pulse_event - events fed to the dfs handler
    *
    * @ts: absolute time stamp for start of pulse in [us] (e.g. from TSF)
    * @freq: channel frequency in [MHz]
    * @rssi: rssi value for the given pulse
    * @width: pulse width in [us]
    *
    */
   struct pulse_event {
           u64 ts;
           u16 freq;
           u8  rssi;
           u8  width;
   };

Interface to mac80211
~~~~~~~~~~~~~~~~~~~~~

The mac80211 must provide at least two methods to support pattern
detection functionality:

.. code-block:: c

   extern void ieee80211_add_radar_pulse(u16 freq, u64 ts, u8 rssi, u8 width);
   extern void ieee80211_radar_detected(u16 freq);

The first one is to be used by PHY to continuously report detected pulse
events. Those events are then fed into the pattern detector.

When the pattern detector detects a match, mac80211 is informed about it
with the second function. Here is the central place to perform all
actions required after radar is detected at a given frequency.

.. code-block:: c

   ieee80211_radar_detected()

should also be used by chipsets which do the detection in HW to trigger
execution of post radar detection actions.

DFS Handler Interface
~~~~~~~~~~~~~~~~~~~~~

Pattern detectors are implemented as part of DFS handler instances with
the following interface

.. code-block:: c

   struct dfs_handler {
           /* VFT */
           void (*exit)(struct dfs_handler *_this);
           int (*add_pulse)(struct dfs_handler *_this, struct pulse_event *event);

           /* private data */
           struct dfs_data *data;
   };

   /**
    * dfs_handler_init - DFS handler constructor
    *
    * @dfs_domain: DFS domain to detect radar patterns for
    *
    * A DFS handler instance is allocated via this constructor.
    * On failure NULL is returned.
    */
   struct dfs_handler *dfs_handler_init(enum dfs_domain dfs_domain);

A DFS handler is instantiated with the DFS regulatory domain as
parameter. It is then fed by ``ieee80211_add_radar_pulse()`` with radar
events and will detect radar test patterns as defined for this domain.
On detection, ieee80211 is informed via ``ieee80211_radar_detected()``.

Proof-of-Concept Implementation
-------------------------------

The patches to test this concept of common pattern detectors integrated
in mac80211 are posted on the mailing list.

In this sections some information is provided on how to run and test it.

We tested it with

* OpenWRT (r23885)
* ath9k / AR9280 (rev 2)
* Rohde & Schwarz SMBV100A Vector Signal Generator (R&S)
* cabled environment

Start-Up
~~~~~~~~

At boot up, the pattern specs are printed, you should see

::

   [...]
   INIT: print_detector_specs: valid ranges: width=[0, 30], pri=[240, 5010], dur=112950
   INIT: dfs_handler_init: ok

Testing with Radar Pulse Generator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After boot up, setup to operate on DFS channel:

::

   uci set wireless.radio0.disabled=0; \
   uci set wireless.radio0.hwmode=11a; \
   uci set wireless.radio0.channel=100; \
   uci set wireless.radio0.country=US; \
   wifi up

At the R&S, load ETSI V1.5.1 reference DFS radar test signal and fire it
via single trigger (5500 MHz, -30 dBm). The events fed to the detector
and the result are logged, you should see

::

   INFO: e->width=0, e->ts=7875473, delta_ts=1427, e->rssi=30, e->freq=5500
   INFO: e->width=0, e->ts=7876902, delta_ts=1429, e->rssi=30, e->freq=5500
   INFO: e->width=0, e->ts=7878333, delta_ts=1431, e->rssi=44, e->freq=5500
   INFO: e->width=0, e->ts=7879759, delta_ts=1426, e->rssi=30, e->freq=5500
   INFO: e->width=0, e->ts=7881189, delta_ts=1430, e->rssi=43, e->freq=5500
   INFO: e->width=0, e->ts=7882616, delta_ts=1427, e->rssi=30, e->freq=5500
   INIT: detector_check_match: XXXXXXXXXXXXXXXXXXXXXXX MATCH on type 1
   Radar detected at freq=5500

DebugFS
~~~~~~~

::

   /sys/kernel/debug/dfs

gives access to logging verbosity and to a radar pattern generator to test the detector without HW.

::

   debug_level

holds the bit-field of enabled levels => write 0 to disable output fully.

DFS radar pattern generator is

* configured by parameters ``radar_{freq, ppb, pss, rssi, width}``
* executed by writing 1 to ``generate_radar``

Upon invocation, the radar events configured are passed to mac80211 and
forwarded to the detector. With default values you should see

::

   INFO: e->width=1, e->ts=1286281794469507, delta_ts=1428, e->rssi=30, e->freq=5500
   INFO: e->width=1, e->ts=1286281794470935, delta_ts=1428, e->rssi=30, e->freq=5500
   INFO: e->width=1, e->ts=1286281794472363, delta_ts=1428, e->rssi=30, e->freq=5500
   INFO: e->width=1, e->ts=1286281794473791, delta_ts=1428, e->rssi=30, e->freq=5500
   INFO: e->width=1, e->ts=1286281794475219, delta_ts=1428, e->rssi=30, e->freq=5500
   INFO: e->width=1, e->ts=1286281794476647, delta_ts=1428, e->rssi=30, e->freq=5500
   INIT: detector_check_match: XXXXXXXXXXXXXXXXXXXXXXX MATCH on type 1
   Radar detected at freq=5500
