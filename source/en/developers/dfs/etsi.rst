ETSI DFS regulatory
===================

Overview
--------

The ETSI regulatory standard EN-301-893 specifying DFS is still in draft
mode, with the current version V1.5.1 (2008-12) being tagged as final
draft.

The latest evolution from V1.4.1 (2007-07) to 1.5.1 among others
included changes in the definition of radar test signals that have
significant impact on the implementation of DFS detection algorithms,
especially the balancing between true and false positives.

For a better overview and comparison, the relevant information from
those freely available draft documents are put together on this page,
basically taken from the appendices D.

ETSI V1.4.1
-----------

Table D.1: DFS requirement values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   - 
      - Parameter
      - Value
   - 
      - Channel Availability Check Time
      - 60 s
   - 
      - Channel move time
      - 10 s
   - 
      - Channel Closing Transmission Time
      - 260 ms
   - 
      - Non-Occupancy Period
      - 30 min

Table D.2 and D.3: Interference threshold values, master / slave
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   - 
      - Maximum transmit power (EIRP) [mW]
      - Value master [dBm]
      - Value slave [dBm]
   - 
      - >= 200
      - -64
      - -64
   - 
      - < 200
      - -62
      - N/A

.. note::

   This is the level at the input of the receiver assuming a 0 dBi receive antenna.

Table D.4: Parameters of DFS test signals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   - 
      - Radar test signal
      - Pulse Width [µs]
      - PRI [pps]
      - Pulses per burst [ppb]
   - 
      - 1 - Fixed
      - 1
      - 750
      - 15
   - 
      - 2 - Variable
      - 1, 2, 5
      - 200, 300, 500, 800, 1000
      - 10
   - 
      - 3 - Variable
      - 10, 15
      - 200, 300, 500, 800, 1000
      - 15
   - 
      - 4 - Variable
      - 1, 2, 5, 10, 15
      - 1200, 1500, 1600
      - 15
   - 
      - 5 - Variable
      - 1, 2, 5, 10, 15
      - 2300, 3000, 3500, 4000
      - 25
   - 
      - 6 - Variable modulated
      - 20, 30
      - 2000, 3000, 40000
      - 20

The detection probability P\ :sub:`d` at 30% channel load is given as 60% for all test signals.

ETSI V1.5.1 final draft
-----------------------

Table D.1: DFS requirement values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   - 
      - Parameter
      - Value
   - 
      - Channel Availability Check Time
      - 60 s (see note 1)
   - 
      - Maximum Off-Channel CAC Time
      - 4 hours (see note 2)
   - 
      - Channel Move Time
      - 10 s
   - 
      - Channel Closing Transmission Time
      - 1 s
   - 
      - Non-Occupancy Period
      - 30 minutes

.. note::

     - For channels whose nominal bandwidth falls completely or partly
       within the band 5 600 MHz to 5 650 MHz, the Channel Availability
       Check Time shall be 10 minutes.
     - For channels whose nominal bandwidth falls completely or partly
       within the band 5 600 MHz to 5 650 MHz, the Maximum Off-Channel
       CAC Time shall be 24 hours.

Table D.2: Interference threshold values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   -
      - EIRP Spectral Density [dBm/MHz]
      - Value [dBm] (see notes 1 and 2)
   -
      - 10
      - -62

.. note::

   - This is the level at the input of the receiver of a RLAN device
     with a maximum EIRP density of 10 dBm/MHz and assuming a 0 dBi
     receive antenna. For devices employing different EIRP spectral
     density and/or a different receive antenna gain G (dBi) the DFS
     threshold level at the receiver input follows the following
     relationship::

         DFS Detection Threshold (dBm) = -62 + 10 - EIRP Spectral Density (dBm/MHz) + G (dBi)

     However the DFS threshold level shall not be lower than -64 dBm
     assuming a 0 dBi receive antenna gain.

   - Slave devices with a maximum EIRP of less than 23 dBm do not have
     to implement radar detection.

Tables D.3 and D.4: Parameters of the reference DFS and radar test signals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   -
      - Test signal #
      - Pulse width [µs]
      - Pulse repetition frequency PRF [pps]
      - # of PRFs
      - Pulses per burst [ppb]
   -
      - 0 (ref.)
      - 1
      - 700
      - 1
      - 18
   - 
      - 1
      - 0,8 ... 5
      - 200 ... 1000
      - 1
      - 10
   - 
      - 2
      - 0,8 ... 15
      - 200 ... 1600
      - 1
      - 15
   - 
      - 3
      - 0,8 ... 15
      - 2300 ... 4000
      - 1
      - 25
   - 
      - 4
      - 20 ... 30
      - 2000 ... 4000
      - 1
      - 20
   - 
      - 5
      - 0,8 ... 2
      - 300 ... 400
      - 2/3
      - 10
   - 
      - 6
      - 0,8 ... 2
      - 400 ... 1200
      - 2/3
      - 15

Table D.5: Detection probability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 2

   - 
      - Parameter
      - Detection Probability (P\ :sub:`d`) [%]
      - 
   - 
      - 
      - Channels whose nominal bandwidth falls partly or completely within the 5 600 MHz to 5 650 MHz band
      - Other channels
   - 
      - CAC, Off-Channel CAC
      - 99,99
      - 60
   - 
      - In-Service Monitoring
      - 60
      - 60

.. note::

   * P\ :sub:`d` gives the probability of detection per simulated
     radar burst and represents a minimum level of detection performance
     under defined conditions. Therefore Pd does not represent the
     overall detection probability for any particular radar under real
     life conditions.
