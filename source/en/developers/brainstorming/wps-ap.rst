WPS support in NM (AP)
----------------------

When wpa_supplicant is an AP it only supports basic functionality where it is the registrar too.

When connection sharing (as an AP) is active with WPS support, there could simply be a dialog "enroll new device", like this:

::

   +-----------------------------------------------------+
   |  Enroll new device                                  |
   +-----------------------------------------------------+
   | Depending on your device's capabilities, select     |
   | an enrollment method.                               |
   |                                                     |
   | If your device is capable of using PIN enrollment,  |
   | have it generate a PIN and enter it here:           |
   | PIN from device: [________]  [enroll with PIN]      |
   |                                                     |
   | Otherwise, it can support the push-button method,   |
   | push the button here and on the device to enrol it. |
   |                        [enroll with button method]  |
   |                                                     |
   |                                            [cancel] |
   +-----------------------------------------------------+
