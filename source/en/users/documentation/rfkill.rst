About rfkill
============

rfkill is a small userspace tool to query the state of the rfkill
switches, buttons and subsystem interfaces. Some devices come with a
hard switch that lets you kill different types of RF radios: 802.11 /
Bluetooth / NFC / UWB / WAN / WIMAX / FM. Some times these buttons may
kill more than one RF type. The Linux kernel rfkill subsystem exposes
these hardware buttons and lets userspace query its status and set its
status through a /dev/rfkill. Given that at times some RF devices do not
have hardware rfkill buttons rfkill the Linux kernel also exposes
software rfkill capabilities that allows userspace to mimic a hardware
rfkill event and turn on or off RF.

Getting rfkill
--------------

Release tarballs of rfkill are available from
http://kernel.org/pub/software/network/rfkill/.

Alternatively, you can download rfkill from git:
http://git.kernel.org/?p=linux/kernel/git/jberg/rfkill.git.

Help
----

Just enter::

   rfkill help

on your command line and it will print out the commands it supports.

Printing the current rfkill status
----------------------------------

::

   rfkill list

Listening to events
-------------------

Just use

::

   rfkill event

Setting/clearing a soft block
-----------------------------

Use

::

   rfkill list

to get the rfkill index, then use

::

   rfkill block <index>|<type>

or

::

   rfkill unblock <index>|<type>
