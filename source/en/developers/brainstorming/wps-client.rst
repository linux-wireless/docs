WPS support in NM (client mode)
-------------------------------

Simple push-button (PBC) support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The most simple is push-button support, it could look like this:

.. image:: WPS-mockup.png
   :alt: WPS-mockup.png

The AP name is obtained from the WPS scan results (see new versions of iw for how to parse this).

Then once the button on the AP is pushed, wpa_supplicant sends an event WPS-AP-AVAILABLE-PBC. At that point, the scan results are checked (akin ``wpa_cli scan_results``) whether the selected BSS contains WPS-PBC, like this:

::

   00:1d:7e:4a:a1:ab       2432    69      [WPA2-PSK-TKIP+CCMP][WPS-PBC]   jo

If it does, the button "Connect with WPS" becomes available. When pressed, we do the equivalent of ``wpa_cli wps_pbc 00:1d:7e:4a:a1:ab`` and wpa_supplicant does the rest, finally connecting to the network. We then obtain the network key from wpa_supplicant's network config stanza and save it. Alternatively, we could do wps_cred_processing=1 and then connect to the network once we have the credentials.

/!\\ This is how I got it working, I think it's supposed to work the other way around, you do ``wpa_cli wps_pbc <BSSID>`` first, then it probes the AP until the AP enables PBC. The other way around works for me as well, but how do you discover that the AP is ready?

PIN mode
~~~~~~~~

Cf. for example http://kb.netgear.com/app/answers/detail/a_id/39. The odd thing is that for instance my AP claims to support PIN (or is this not discoverable?!?) but there's nowhere in the web interface to enter the client's PIN.
