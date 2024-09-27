**DFS Development**

This page recaps the approach to integrate DFS into Linux wireless presented and discussed at the :doc:`Vancouver-2011 <../summits/vancouver-2011>` summit.

It is designated to serve as a discussion and documentation base during the concept and design phase. RLAN chipset manufacturers interested in getting their devices' supported by the proposed DFS module are invited to participate in this joint effort and assure that the taken approach will support their devices.

Developers / Participants
-------------------------

.. list-table::

   - 

      - **Participant**
      - **Company**
      - **Function**
      - **Contribution**
   - 

      - Kathy
      - Qualcomm/Atheros
      - Manager
      - coordinate Atheros' contribution
   - 

      - Felix
      - Various
      - Developer
      - support design and implementing management component
   - 

      - Assaf
      - TI
      - Manager
      - coordinate TI's contribution
   - 

      - Eyal
      - TI
      - Developer
      - integrate TI's management module
   - 

      - Ohad
      - TI
      - Developer
      - ?
   - 

      - Zefir
      - Neratec AG
      - Developer
      - coordinate detector design, implement pattern detector for ETSI radars
   - 

      - ?
      - Intel
      - ?
      - 
   - 

      - ?
      - Broadcom
      - ?
      - 
   - 

      - ?
      - Ralink
      - ?
      - 
   - 

      - ?
      - ...
      - ?
      - 
   - 

      - ?
      - ?
      - Developer
      - implement pattern detector for FCC radars
   - 

      - ?
      - ?
      - Developer
      - implement pattern detector for MKK radars
   - 

      - ?
      - ...
      - ?
      - 

Requirements
------------

To operate in DFS bands, RLAN master devices must not operate on channels that are used by radar devices. Therefore, they must be able to

#. detect radars
#. manage spectrum based on detections While the core requirement is common in all regulatory domains (FCC, ETSI, MKK), the parameters for those two functional blocks slightly differ.

The DFS management functionality is part of 802.11h, whereas the detection is outside the scope of the standard and specified by the regulatory bodies.

Management
~~~~~~~~~~

To prevent interferences with radar devices, RLAN master devices must

::

     - monitor a channel for radars **before** transmission (Channel Availability Check Time ~60s) 
     - perform in-service monitoring **while** operating on channel 
     - stop operation on radar detection 
     -  * inform stations on channel switch (CSA) 
     -  * switch to another channel (Channel Move Time ~10s) 
     -  * leave radar channel alone (Non Occupancy Period ~30min) 

Detection
~~~~~~~~~

Radar patterns are defined as a series of pulses, where each pulse is defined by its

::

     -   * time stamp (TS) 
     -   * pulse width (W) 
     -   * pulse height (RSSI) Regulatory domains define different sets of radar patterns a RLAN master device must be able to detect with a given minimum detection probability when operating under defined test environments. 

Detection Device Types
~~~~~~~~~~~~~~~~~~~~~~

.. image:: DetectorTypes.png
   :alt: DetectorTypes.png

Two types of detector devices are supported by the DFS module:

::

     -     - radar detection fully performed by HW (?...) 
     -     - pulse detection performed in HW, pattern matching in SW (Atheros, ...) While the first device types perform radar pulse detection and pattern matching in HW, the second type of devices detect radar pulses and let the SW figure out whether a series of them form any defined pattern. 

Detection Sensitivity vs. Tolerance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The pattern matching algorithms to detect defined radar types must consider

::

     -       - missing pulses 
     -       -  * not seen when phy is transmitting (~50% for defined test environments) 
     -       -  * otherwise not detected (interferences, pulse detection config, etc.) 
     -       -   false pulses 
     -       -    * interferences wrongly interpreted as pulses 
     -       -    * highly dependent on environment Increasing a detector's sensitivity inherently decreases its tolerance, i.e. speculatively reconstructing lost pulses inevitably increases the risk of random false pulses being interpreted as radar pattern. Isolating true from false detections requires computational complexity to cover potential corner-cases in the overlapping zone. 

.. image:: Triangle.png
   :alt: Triangle.png

The regulatory bodies define requirements for sensitivity only, i.e. an extremely sensitive detector might interpret any single pulse as radar and would perfectly pass DFS certification - with being perfectly useless for operations in DFS bands.

This renders the core challenge for pattern matching algorithms to be well balanced between sensitivity, tolerance and computational complexity. Note that by that principle there is no *One Fits All* detector: while the home PC has enough computational power to use some generic algorithms for indoor use, low-power embedded system working in harsh environments need less complex and differently balanced ones.

Management Architecture
-----------------------

**TBD**

Management Design
-----------------

**TBD**

Detector Architecture
---------------------

The chosen detector architecture provides support for both DFS device types. For type 2 devices it maintains flexibility for customized detectors by splitting radar detection into driver specific pulse detection and common pattern matching modules.

Pattern Detection in HW / Driver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|ArchHW-Detector.png| HW based detector drivers report the occurrence of a radar pattern on a channel. A radar event is passed to mac80211 and is forwarded to hostapd. hostapd handles DFS channel states based on the radar events and manages the spectrum (including initiating CSA, moving channel, etc.).

Pattern Detection in Kernel
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|ArchSW-Detector-Kernel.png| Type 2 devices detect pulse events to be matched for given patterns in SW. Pulse events are sent to mac80211 and fed to the wiphy's pattern detector instance. In case of a pattern match, mac80211 reports a radar event to hostapd. The interface to and processing in hostapd are identical to the previous case.

Pattern Detection in User Space
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|ArchSW-Detector-User.png| The common pattern detector available for mac80211 might not suffice requirements for specific environments that require a re-balance between sensitivity, tolerance, and complexity. Those specific detectors with custom usability can be implemented in user space. In those use cases mac80211 forwards the pulse events received from the driver to hostapd, which feeds the wiphy's pattern detector instance. The management functionality in hostapd after a radar detection remains unchanged.

Detector Design
---------------

DFS Capabilities
~~~~~~~~~~~~~~~~

::

   #define DFS_DOMAIN_FCC   0
   #define DFS_DOMAIN_MKK   1
   #define DFS_DOMAIN_ETSI  2

   enum dfs_capabilities {
           DFS_CAP_PULSE_DETECT_FCC   = BIT(DFS_DOMAIN_FCC),
           DFS_CAP_PULSE_DETECT_MKK   = BIT(DFS_DOMAIN_MKK),
           DFS_CAP_PULSE_DETECT_ETSI  = BIT(DFS_DOMAIN_ETSI),
           
           DFS_CAP_RADAR_DETECT_FCC   = BIT(8 + DFS_DOMAIN_FCC),
           DFS_CAP_RADAR_DETECT_MKK   = BIT(8 + DFS_DOMAIN_MKK),
           DFS_CAP_RADAR_DETECT_ETSI  = BIT(8 + DFS_DOMAIN_ETSI),
   };

Pulse Events
~~~~~~~~~~~~

::

   /**
    * struct dfs_pulse_event - pulses detected by driver
    *
    * @ts: monotonic time stamp for start of pulse in [ns]
    * @width: pulse width in [ns]
    * @freq: channel frequency in [MHz]
    * @rssi: rssi value for the given pulse
    * @dfs_domain: DFS domain
    *
    */
   struct dfs_pulse_event {
           u64     ts;
           u32     width;
           u16     freq;
           u8      rssi;
           u8      dfs_domain;
   };

Reporting pulses from driver to mac80211:

::

   extern void ieee80211_add_radar_pulse(struct dfs_pulse_event *pulse);

Radar Events
~~~~~~~~~~~~

::

   struct dfs_radar_event {
           u16     freq;
           u8      dfs_domain;
   };

Reporting radars from driver to mac80211:

::

   extern void ieee80211_radar_detected(struct dfs_radar_event *radar);

.. |ArchHW-Detector.png| image:: ArchHW-Detector.png
.. |ArchSW-Detector-Kernel.png| image:: ArchSW-Detector-Kernel.png
.. |ArchSW-Detector-User.png| image:: ArchSW-Detector-User.png
