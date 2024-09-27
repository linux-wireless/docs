DFS (Dynamic Frequency Selection)
---------------------------------

Overview
~~~~~~~~

We will put in place here design ideas for a future mac80211 DFS implementation. This page is work in progress.

Dynamic Frequency Selection allows 5 GHz capable 802.11 devices to share spectrum with radar devices. Radars are used by airports, weather stations, and military. For example some weather stations use weather radars to help with directing airplanes to airports more accurately. Interference with radars then is carefully regulated by countries that make use of them as they share spectrum in the 5 GHz band.

The general idea behind how DFS works with 802.11 is master 802.11 devices must first monitor DFS channel for radar pulses for a period of time before it actually enables communication on it. Once it starts using that channel it must then commit to routinely check for radar pulses and if a pulse pattern is detected that matches a radar signal the master device must tell all connected clients it is switching channels and switch over to a new channel within a specific period of time. The master device must also ensure to not come back to that channel again for period of time after which it can white-list the channel and eventually use it again.

Software then is needed for:

-  Management of which channels have seen radar pulses recently / timers to clean them
-  Management of informing connected clients of switching channels
-  Algorithms to help identify the next best channel - think the requirement is to actually choose one randomly
-  Hardware radar detection We need software to do all this.

High-level Design
~~~~~~~~~~~~~~~~~

Proposed software design in order to share as much as possible across different hardware.

wpa_supplicant (apply domain rules logic) / hostapd (invoke actions such as change channel?) (user space)

::

     * || cfg80211 (mostly pass commands up/down) 
       * || mac80211 (mostly pass commands up/down) 
         * || TI firmware (radar detection) or ath9k driver (radar detection) or other hw  

We need to define a common API between the low-level firmware or driver software and the rest of the stack. Can someone document this?

A more detailed description of the code enhancements and added functions required by each major component shown above would also be useful to add here.

DFS requirements world wide
---------------------------

DFS is currently a requirement in the US, EU, and Japan, but it seems some other countries are starting to consider requiring DFS as well.

Concepts
~~~~~~~~

::

           * Non Occupancy List (NOL): channels which we know have recent radar pulses and we cannot use 
           * Channel Availibility Check (CAC) Time: amount of time we should sit idle on a channel checking for radar pulses before initiating 802.11 frames on 

Pulse types
~~~~~~~~~~~

The different types of radar pulses are distinguished based on:

::

             * Pulse Repetition Frequency - PRF - EU uses this 
             * Pulse Repetition Interval - PRI - FCC / JP uses this 
             * Pulse width 
             * Pulse burst length Note: PRI and PRF are equivalent, since PRI = 1 / PRF. 

FCC specification
~~~~~~~~~~~~~~~~~

FCC Short Pulse Radar Test Waveforms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::

   - 

      - **Radar test signal**
      - **Pulse Width (µs)**
      - **PRI**
      - **Pulses per burst**
      - **Minimum % of successful detection**
      - **Number of Trials(Times)**
   - 

      - 1
      - 1
      - 1428
      - 18
      - 60%
      - 30
   - 

      - 2
      - 1-5
      - 150-230
      - 23-29
      - 60%
      - 30
   - 

      - 3
      - 6-10
      - 200-500
      - 16-18
      - 60%
      - 30
   - 

      - 4
      - 11-20
      - 200-500
      - 12-16
      - 60%
      - 30
   - 

      - 1-4
      - x
      - x
      - x
      - 80%
      - 120

FCC Long Pulse Radar Test Waveforms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::

   - 

      - **Radar type**
      - **Pulse Width (µs)**
      - **Chirp width (MHz)**
      - **PRI**
      - Number of pulses'
      - **Minimum % of successful detection**
      - **Number of Trials(Times)**
   - 

      - 5
      - 50-100
      - 5-20
      - 1000-2000
      - 1-3
      - 8-20
      - 80%

Frequency Hopping Radar Test Waveforms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::

   - 

      - **Radar type**
      - **Pulse Width (µs)**
      - **PRI**
      - **Pulses per hop**
      - **Hopping rate (MHz)**
      - **Hopping sequence Length (msec)**
      - **Minimum % of successful detection**
      - **Number of Trials(Times)**
   - 

      - 6
      - 1
      - 333
      - 9
      - 0.333
      - 300
      - 70%
      - 30

ETSI specification
~~~~~~~~~~~~~~~~~~

The ETSI specification for V1.4.1 and V1.5.1 moved to the :doc:`ETSI <dfs/etsi>` sub-page.

Japan / Telec specification
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Japan Specific Radar Test Waveform (W53)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::

   - 

      - **Radar type**
      - **Pulse Width (µs)**
      - **PRI(µs)**
      - **Number of pulses**
      - **Minimum % of successful detection**
   - 

      - J1-1
      - 1
      - 1428
      - 18
      - 60%
   - 

      - J1-2
      - 2.5
      - 3846
      - 18
      - 60%

Japan Specific Radar Test Waveform (W56)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::

   - 

      - **Radar type**
      - **Pulse Width (µs)**
      - **PRI(µs)**
      - **Number of pulses**
      - **Minimum % of successful detection**
   - 

      - J2-1
      - 0.5
      - 1388
      - 18
      - 60%
   - 

      - J2-2
      - 2
      - 4000
      - 18
      - 60%

Development roadmap
-------------------

DFS will be implemented first for AR9280 through ath9k, ath9k_hw TI will eventually review how to program DFS for their devices and list required cfg80211 knobs

Map countries to a DFS region bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This involves mapping each regulatory domain to one of the three DFS regions.

Patches posted: http://marc.info/?l=linux-wireless&m=129286456607063&w=2

Get DFS region to the driver through cfg80211
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This involves parsing the regulatory information and sending the DFS region to the driver through cfg80211. With this the drivers should know what DFS region they belong to:

::

               * FCC 
               * ETSI 
               * JP We need to query as many regulatory experts as possible to find out if we have other regions or what this pictures will look like 10 years from now. By the time we get done with this we should be able to start requesting for DFS parameters to eventually program them into hardware. 

Patches posted: http://marc.info/?l=linux-wireless&m=129286456607063&w=2

Where do we stuff DFS parameters for each region
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One idea is to use the request_firmware() API as it is expected these parameters will be region and chipset specific. This requires a good review of all chipsets and with priority on the ones who have vendors or we have documentation for that we want to support in existing drivers. Today this means Atheros hardware and TI hardware. Atheros will also have check with their mobile drivers (Vipin, Len).

Program hw DFS parameters
~~~~~~~~~~~~~~~~~~~~~~~~~

ath9k_hw already has some knobs for this, Felix already submitted some of these changes upstream. Most of the work required here will take place on ath9k.

DFS events
~~~~~~~~~~

Most of the work here will involve hooking things up for mac80211 / cfg80211 / nl80211. This will consists of receiving DFS events from the driver for radar detection, keeping the NOL list, sending it to hostapd, choosing a random channel, and sending CSA to STAs.

Proposed architecture approach in 18 Jan 2011 DFS IRC discussion:

.. list-table::

   - 

      - \**DFS Function \*\*
      - **Code affected**
   - 

      - channel selection
      - userspace (hostapd)
   - 

      - CAC/NOL
      - cfg80211
   - 

      - pulse detection
      - ath9k (driver)

Compliance Testing
------------------

Testing DFS compliance is time consuming and costly. Atheros plans to offer its support (test teams and test beds) to perform compliance testing of its reference designs periodically. Complete hw testing at this level should occur when new or updated chips and reference platforms are available, and when changes to hardware specific ini values that affect DFS are modified.

Atheros has a novel idea to help software developers test DFS software without the need for the expensive test rigs and related time/effort. We will run multiple trials of the various radar types through actual hardware and log the pulse data to a text file. Parameters in that text file would follow a specific format so that they can be passed as input to the software. Example format of "pulse data" dump that would be sent to the radar classifier software:

timestamp \| rssi \| width \| ...

At a high-level, the DFS software will first run the pulse data through a "radar classifier" function. The output of the radar classifier function will be "radar detection" information. All the upper level logic will then process and execute based on those radar detection data.

With the above approach, Atheros can take care of all hardware testing and log the data as snapshot files that the software would normally be acting on in real-time. Then the software teams can process the data, tweak the software, process, tweak, etc until everything works correctly. Each time changes to the DFS radar classification, detection, and compliance algorithms are made, a developer can simply re-run the "pulse data" files through the software logic to examine success or failure.

Weekly Meetings
---------------

Weekly discussions used to take place each Tuesday, 9am PST on IRC:

server: irc.freenode.net channel: #linux-wireless

But now they are scheduled only on an as-needed basis.

2010-12-14
~~~~~~~~~~

IRC log: `dfs-2010-12-14.txt <dfs-2010-12-14.txt>`__

::

                 * Review the different basic concepts of DFS and willing participants of implementation. So far we have these companies: 
                 *  * Atheros 
                 *  * TI 
                 *  * saxnet.de 
                 *  * neratec.com 
                 *   Review the different software components required and where the components are going to go upstream (hostapd/mac80211). 

Related Information
-------------------

DFS slides presented at the Linux Wireless summit in Vancouver 2011: `Vancouver2011-Slides-DFS.pdf <Vancouver2011-Slides-DFS.pdf>`__
