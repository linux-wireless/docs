802.11 Bluetooth coexistence
============================

An 802.11 device and Bluetooth can interfere with each other when the
802.11 device operates on the 2.4 GHz band. All Bluetooth devices
operate at the 2.4 GHz band. This section documents the technical
details regarding the causes of interferences and solutions implemented
in drivers, the 802.11 stack, and possible future enhancements.

802.11 spectrum use
-------------------

802.11 defines channels on the 2.4 GHz band, each 20 MHz wide. Then,
802.11n allows for 40 MHz wide channels where you have a primary and an
adjacent extension channel.

Bluetooth spectrum use
----------------------

Bluetooth defines 79 channels for communication on the 2.4 GHz band each
channel being separated by 1 MHz. The frequency range used is between
2.402 GHz and 2.480 GHz. Bluetooth's transmitted signal is spread across
this 2.4 GHz band and the specification allows for 1600 frequency hops
per second, the advantage being that since information is spread across
a wide band of frequencies signals transmitted by other systems using a
portion of the same frequency spectrum may appear as noise to only some
of the frequencies used by Bluetooth device using frequency hopping and
similarly only a portion of a Bluetooth transmission may interfere with
signals transmitted by other systems.

802.11 and BT spectrum map
--------------------------

.. list-table::
   :header-rows: 1

   - 

      - Center of frequency / freq-range (MHZ)
      - 802.11 Channel number
      - BT Channel
   - 

      - 2412 2402-2422
      - 1
      - 1-20
   - 

      - 2417 2407-2427
      - 2
      - 5-25
   - 

      - 2422 2412-2432
      - 3
      - 10-30
   - 

      - 2427 2417-2437
      - 4
      - 15-35
   - 

      - 2432 2422-2442
      - 5
      - 20-40
   - 

      - 2437 2427-2447
      - 6
      - 25-45
   - 

      - 2442 2432-2452
      - 7
      - 30-50
   - 

      - 2447 2437-2457
      - 8
      - 35-55
   - 

      - 2452 2442-2462
      - 9
      - 40-60
   - 

      - 2457 2447-2467
      - 10
      - 45-65
   - 

      - 2462 2452-2472
      - 11
      - 50-70
   - 

      - 2467 2457-2477
      - 12
      - 55-75
   - 

      - 2472 2462-2482
      - 13
      - Not used
   - 

      - 2484 2474-2492
      - 14
      - Not used

Interference
------------

Each 802.11 channel then equals to 20 Bluetooth channels. When
communication is enabled on an Bluetooth device you will get
interference when the Bluetooth device hops on to any of the 20
Bluetooth channels equivalent to your 802.11 channel. Even if a
Bluetooth device hops at the max allowed frequency rate of 1600
frequency hops per second there are only 79 channels available so at
this rate each channel will be used around 20 times in a second.

Coexistence techniques
----------------------

To aid with 802.11 and Bluetooth interference issues several techniques
have been implemented on Bluetooth device firmware and 802.11 devices.
We elaborate on each of these techniques below.

Adaptive Frequency Hopping (AFH)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With this technique, required for Bluetooth devices following the 1.2
spec, Bluetooth devices will scan for fixed sources of interference and
adapt its own frequency pattern to avoid those with interference. This
works great in low noise environments in a noisy environment could end
up disabling Bluetooth communication completely.

Channel skipping
~~~~~~~~~~~~~~~~

When a Bluetooth device sits on the same system as an 802.11 device the
802.11 device can inform the Bluetooth device the 802.11 channel it is
operating on and the Bluetooth device can preemptively disable
communication on the respective Bluetooth channels. The advantage to
this solution is the preemptive nature of preventing interference but
you also end up limiting the Bluetooth's own spectrum.

Time Division Multiplexing
~~~~~~~~~~~~~~~~~~~~~~~~~~

With this scheme an 802.11 device and Bluetooth device can take turns in
using the spectrum for communication. The 802.11 device would use a
*WLAN_ACTIVE* signal when it is active and a Bluetooth device can use a
*BT_PRIORITY* to categorize the priority of its different own signals.

Typically signals between an 802.11 and Bluetooth device are triggered
using GPIO lines.

2-wire Bluetooth Coexistence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Under the *2-wire* Bluetooth Coexistence scheme two signals are
supported:

- *WLAN_ACTIVE* - signals when an 802.11 device is active, 802.11-->BT
- *BT_PRIORITY* - categorizes the Bluetooth signal, BT-->802.11

3-wire Bluetooth Coexistence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *3-wire* Bluetooth Coexistence scheme extends *2-wire* scheme with a
new signal from the bluetooth device::

     * //BT_STATE//: signals the presence of a Bluetooth transmission.

Interoperability
----------------

Apart from AFS and channel skipping techniques Bluetooth coexistence is
typically tested with bundled 802.11 and Bluetooth devices. This becomes
more evident with 2-wire and 3-wire which relies on GPIO pins for
signaling.

Driver Bluetooth coexistence
----------------------------

This section refers to Bluetooth coexistence support on existing 802.11
Linux drivers.

* :doc:`2-wire and 3-wire Bluetooth coexistence on ath9k <../drivers/ath9k/btcoex>`

Ideas for development
---------------------

Once the :doc:`Frequency broker <../../developers/frequencybroker>` is
implemented add a trigger on an 802.11 channel switch to the disable the
respective Bluetooth channels. This would be a general cheap BT-coex
scheme independent of device interoperability.

References
----------

* http://www.tekgear.com/PDF/WHP-050004-1V0%20Bluetooth%20and%20802.11%20Coexistence.pdf
* http://www.freshpatents.com/Enhanced-2-wire-and-3-wire-wlan-bluetooth-coexistence-solution-dt20070712ptan20070161349.php
