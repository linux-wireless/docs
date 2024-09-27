RF Transceivers
~~~~~~~~~~~~~~~

Each ZD1211-based WLAN adapter actually combines an RF transceiver chip with the ZD1211 (RF: *radio frequency*). The RF chip is basically a radio, responsible for transmitting data into the air at the specified frequency, and for listening for incoming data.

The RF chip must be programmed from the device driver, and this task is complicated by the fact that different ZD1211-based products come with different RF chips.

Some RF chips are better than others, some of them only work with 802.11b/g, others work with 802.11a/b/g.

It appears that the USB ID does not determine RF type, as various devices have been spotted with the same IDs but different RFs.

The AL2230 and RF2959 devices were common in earlier ZyDAS devices, with a few AL7230B devices appearing as well for 802.11a support. As of February 2007, the primary devices being produced now appear to be either AL2230S-based or UW2453-based.

How do I find out which RF is present in my device?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the zd1211rw driver:

::

   # dmesg | grep 'zd1211b\? chip'
   zd1211 chip 07b8:6001 v4330 full 00-12-0e RF2959_RF pa0 g----

In the above example, you can see that my RF is the RF2959.

Please note that the AL2230 comes in 2 forms: AL2230 and AL2230S. With zd1211rw, the difference between the 2 is denoted by the 'S' flag at the end of the chip ID line. For example, the following device is AL2230S:

::

   zd1211b chip 0ace:1215 v4810 high 00-02-72 AL2230_RF pa0 g--NS

This one is standard AL2230:

::

   zd1211b chip 0ace:1215 v4810 high 00-02-72 AL2230_RF pa0 g--N-

If you are using the `ZyDAS-based driver <http://zd1211.ath.cx/download/>`__, you can find out your RF type as follows:

::

   # dmesg | grep -A 1 "PA type" | tail --l 1
   AiroHa AL2230RF

The vendor driver explicitly detects AL2230 and AL2230S, so you do not have to worry about the difference there.

If you have a RF which is not listed here, please report it to the mailing list.

Known RF types
~~~~~~~~~~~~~~

Airoha AL2230 - 802.11b/g
^^^^^^^^^^^^^^^^^^^^^^^^^

The `AL2230 <http://www.airoha.com.tw/AL2230.htm>`__ appears to be fairly decent in terms of signal reception without any external antenna. Airoha publish a `datasheet <http://www.airoha.com.tw/pdf/AL2230S.pdf>`__ about the chip, but the public version does not include technical details.

We have tried contacting Airoha for more detailed technical documentation, however they became unresponsive after they realised that we are not a huge corporation wanting to buy thousands of their devices...

Airoha AL7230B - 802.11a/b/g
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `AL7230B <http://www.airoha.com.tw/AL7230.htm>`__ (`datasheet <http://www.airoha.com.tw/pdf/AL7230.pdf>`__) is probably just an extended version of the AL2230 which supports 802.11a. Interestingly, the first sighting of this RF (in a Trendnet device) is only advertised as b/g compatible. Someone should check and see if RF type is really the only factor that decides whether a device supports 802.11a.

RFMD RF2959 - 802.11b/g
^^^^^^^^^^^^^^^^^^^^^^^

We suspect the RF2959 is one of the cheaper RF transceivers available on the market, however it appears to work relatively well.

RFMD were kind enough to provide us with technical documentation about these devices, under non-distributive terms.

Ubec UW2453 - 802.11b/g
^^^^^^^^^^^^^^^^^^^^^^^

The `UW2453 RF <http://www.ubec.com.tw/product/uw2543.html>`__ started appearing in devices in 2007. At least to someone with limited understanding of RF chips, this appears to be similar to the other available RF's. Ubec publish `full technical specifications <http://www.ubec.com.tw/product/downfiles/uw2453/DS-2453-01%20v1%200.pdf>`__ for this chip.

UW2453 support will be added to zd1211rw as of Linux 2.6.23.

Airoha AL2230S - 802.11b/g
^^^^^^^^^^^^^^^^^^^^^^^^^^

The `AL2230S <http://www.airoha.com/AL2230.htm>`__ appears to be the next generation version of the earlier AL2230. The exact differences are unclear. This RF started appearing in ZD1211 devices in 2007.

AL2230S support will be added to zd1211rw as of Linux 2.6.22.
