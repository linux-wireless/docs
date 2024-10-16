ath10k FAQ
==========

Q:If ath10k support ad-hoc mode?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Why I cannot start an AP in an 80 MHz channel / in 11ac mode?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you get "nl80211: Failed to set channel" error from hostapd, most
likely that means that regulatory database doesn't support 80 MHz
channels (which were introduced in 11ac). You can check that with iw::

   $ iw reg get
   country FI: DFS-ETSI
           (2402 - 2482 @ 40), (N/A, 20)
           (5170 - 5250 @ 80), (N/A, 20)
           (5250 - 5330 @ 80), (N/A, 20), DFS
           (5490 - 5710 @ 80), (N/A, 27), DFS
           (57240 - 65880 @ 2160), (N/A, 40), NO-OUTDOOR

If you do not see "@ 80" within the frequency range you are using, it
means that the regulatory database doesn't support 80 MHz channels.

Other problem is that configuring VHT (= 802.11ac) in hostapd is not
very intuitive, pay extra attention how you configure it. Especially
vht_oper_centr_freq_seg0_idx is challenging. See `example configuration
<http://wireless.kernel.org/en/users/Drivers/ath10k/configuration#Configuring_hostapd>`__
and `hostapd configuration file documentation
<http://hostap.epitest.fi/gitweb/gitweb.cgi?p=hostap.git;a=blob_plain;f=hostapd/hostapd.conf>`__.

Why my MAC address is 00:03:07:12:34:56?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most likely a problem with the calibration data or firmware does not
support the board in question. Try updating the firmware first.

How can I run latest ath10k on older kernels?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use :doc:`backports project <backports>`.

How do I update the firmware?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See :doc:`firmware <firmware>`.

Why the TX rate reported to user space is wrong?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ath10k firmware does not inform the used TX rate to the host, so there's
no way for ath10k to report that to user space. Better to ignore the TX
rate completely.

Can I use ath10k as a 802.11ac sniffer?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, see page :doc:`ath10k monitor mode <monitor>`.

How do I get the best possible throughput with ath10k?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here are some tips for throughput:

- Make sure that you are using 80 MHz channels.
- Disable CONFIG_ATH10K_DEBUG and CONFIG_ATH10K_DEBUGFS.
- Disable all kernel debug options.
- Make sure that you using correct hostapd configuration: :doc:`Full hostapd configuration <configuration>`
