Distribution specific notes
===========================

Some distributions have additional, specific information. Please check
there first:

-  `Ubuntu's Linux wireless guide <https://wiki.ubuntu.com/KernelTeam/LinuxWireless>`__
-  `openSUSE's wireless wiki <http://en.opensuse.org/Tracking_down_wireless_problems>`__

Relevant software
-----------------

Wireless drivers are just one component of the software stack necessary
for wireless devices to function. There are also userspace components,
namely `NetworkManager
<http://www.gnome.org/projects/NetworkManager/>`__, `wpa_supplicant
<http://hostap.epitest.fi/wpa_supplicant/>`__, `wireless-tools
<http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/Tools.html>`__,
:doc:`wireless-regdb <../../developers/regulatory>`, :doc:`CRDA
<../../developers/regulatory/crda>`, :doc:`iw <iw>` and possibly many
more (as always, there are lots of options to choose from).

It is best if you to try to determine where the issue is before
reporting it since you can then report it to the right place. If unsure
you can check out :doc:`user support IRC channel <../support>` and ask
there.

Kernel panics/hangs
-------------------

Kernel panics are kernel bugs, and should be reported immediately.
Kernel hangs are usually kernel bugs as well and should be reported too.
If you can, you should try to determine whether the bug persists in the
latest vanilla stable linux release. Vanilla stable kernel means you got
it from kernel.org and it is a stable kernel.

Other issues
------------

Please also report other issues, for example when things are not working
correctly. In this case, you are encouraged to try out the latest
:doc:`wireless-testing git tree
<../../developers/documentation/git-guide>` or the latest
:doc:`compat-wireless snapshot <../download>`.

If you are not sure if your issues is driver or userspace specific
consider asking on our :doc:`user support IRC channel <../support>` for
help.

Identifying the bug
-------------------

You can save us and yourself a lot of time by trying a few things before
reporting a bug.

If you are unsure about where the bug lies you can start by turning off
`NetworkManager <http://www.gnome.org/projects/NetworkManager/>`__ (if
you're using it) and then try running wpa_supplicant yourself with your
own configuration file. To reproduce a configuration file similar to the
one NetworkManager uses you can check the log (usually /var/log/messages
or /var/log/syslog) for the settings it used. To stop NetworkManager
use::

   # Red Hat based systems
   sudo /sbin/service NetworkManager stop

   # Debian
   sudo /etc/init.d/NetworkManager stop
   sudo killall -TERM wpa_supplicant

   # On Ubuntu 9.10
   sudo service network-manager stop
   sudo killall -TERM wpa_supplicant

If you can still reproduce the issue you should report it, and include
the wpa_supplicant configuration file with your report. If this works
fine, please report it to the NetworkManager maintainers.

If you're not using NetworkManager you can still try to reproduce the
issue with just wpa_supplicant.

Bug information
---------------

In order to effectively work on your bug (maybe even reproduce it), we
need some information from you.

Software versions
~~~~~~~~~~~~~~~~~

Please include the versions of all relevant software, especially the
exact kernel version you are using.

Wireless driver
~~~~~~~~~~~~~~~

We need to know the driver you are using. If you are unsure of which
wireless card you have or which driver you are using, check which
modules are loaded and maybe include that list in your bug report. If it
is a PCI device, ``lspci -k`` can help, if it is a USB device include
the USB IDs if possible.

kernel messages
~~~~~~~~~~~~~~~

Always include the kernel messages (you can retrieve them with the
``dmesg`` command) in your bug report. Please take care not to line-wrap
them, if you must attach a file rather than pasting them into email.

If possible, configure your kernel to include the options

::

   CONFIG_MAC80211_HT_DEBUG=y
   CONFIG_MAC80211_VERBOSE_PS_DEBUG=y
   CONFIG_MAC80211_VERBOSE_DEBUG=y

If you use compat-wireless you can edit config.mk and enable them there.
Note that each driver may also have their own respective debug
parameters which help as well.

iw event log
~~~~~~~~~~~~

Sometimes an iw event log is useful, for that please install :doc:`iw
<iw>` and provide the output of the ``iw event -t`` in your bug report.

invocation information
~~~~~~~~~~~~~~~~~~~~~~

If you're using command line tools, always include their command line.
This is especially important with wpa_supplicant -- we need to know
whether you're using ``-Dwext`` or ``-Dnl80211``.

Where to report bugs
--------------------

NetworkManager bugs
~~~~~~~~~~~~~~~~~~~

Please report bugs on the GNOME bugzilla, in the `NetworkManager product
<http://bugzilla.gnome.org/browse.cgi?product=NetworkManager>`__.

wpa_supplicant bugs
~~~~~~~~~~~~~~~~~~~

You can report bugs on the `hostap mailing list
<http://lists.shmoo.com/mailman/listinfo/hostap>`__.

drivers, mac80211, cfg80211 -- kernel wireless bugs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You should report them on the :doc:`Linux wireless mailing list
<../../developers/mailinglists>`.

Kernel bugs are fixed according to :doc:`the fix propagation
<fix_propagation>`, so depending on the severity any fixes might not
propagate to the version of the kernel you are currently using.
