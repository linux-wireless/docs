Replacing iwconfig with iw
==========================

Consider using iw from git

Getting info on wlan0
~~~~~~~~~~~~~~~~~~~~~

::

   iwconfig wlan0

is be replaced by

::

   iw dev wlan0 link

Connecting to an open network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   iwconfig wlan0 essid foo

is replaced by

::

   iw wlan0 connect foo

If you want to set the channel:

::

   iwconfig wlan0 essid foo freq 2432M
   -or-
   iwconfig wlan0 freq 2432M
   iwconfig wlan0 essid foo

you instead simply use

::

   iw wlan0 connect foo 2432

Connecting to a protected network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For WPA/WPA2 encryption, you have to use wpa_supplicant.

For WEP protection, you can use

::

   iw wlan0 connect foo keys 0:abcde d:1:0011223344

instead of

::

   iwconfig wlan0 key s:abcde
   iwconfig wlan0 key '[2]0011223344'
   iwconfig wlan0 key '[2]'
   iwconfig wlan0 essid foo

Note that ``iwconfig`` uses 1-based key numbers and ``iw`` uses 0-based key numbers like the 802.11 standard.

Join an IBSS (ad-hoc network)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   iwconfig wlan0 mode ad-hoc
   iwconfig wlan0 essid foo-adhoc

in iw:

::

   iw wlan0 set type ibss
   iw wlan0 ibss join foo-adhoc 2412

Leave an IBSS (ad-hoc network)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   iwconfig wlan0 essid off

**might** work, but doesn't always work properly.

in iw, it will always work:

::

   iw wlan0 ibss leave
