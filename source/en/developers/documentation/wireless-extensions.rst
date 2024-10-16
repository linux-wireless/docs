About Wireless-Extensions
=========================

`Wireless-Extensions
<https://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/Linux.Wireless.Extensions.html>`__
(WE or Wext) are the extensions added to the kernel circa 1997 by `Jean
Tourrilhes <https://www.hpl.hp.com/personal/Jean_Tourrilhes/>`__. We
don't document WE as `Jean already has documentation for this on his
page
<https://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/Linux.Wireless.Extensions.html>`__
so what we do do here is document things you should know about WE if you
didn't before.

Is WE being further developed ?
-------------------------------

No it is not. Only bug fixes are being accepted for WE.

Why we are abandoning WE
------------------------

WEs are based on ioctl() and although ioctl() has been used and still is
being used as a standard transport for communication between user <-->
kernelspace new transports are being preferred for several reasons.

From Linux Device Drivers - 3rd Edition:

-  *In user space, the ioctl system call has the following prototype:*

.. code-block:: c

   int ioctl(int fd, unsigned long cmd, ...);

* //The prototype stands out in the list of Unix system calls because of
  the dots, which usually mark the function as having a variable number
  of arguments. In a real system, however, a system call can’t actually
  have a variable number of arguments. System calls must have a
  well-defined prototype, because user programs can access them only
  through hardware "gates." Therefore, the dots in the prototype
  represent not a variable number of arguments but a single optional
  argument, traditionally identified as char \*argp. The dots are simply
  there to prevent type checking during compilation.//

It also states:

* //The unstructured nature of the ioctl call has caused it to fall out
  of favor among kernel developers. Each ioctl command is, essentially,
  a separate, usually undocumented system call, and there is no way to
  audit these calls in any sort of comprehensive manner. It is also
  difficult to make the unstructured ioctl arguments work identically on
  all systems; for example, consider 64-bit systems with a userspace
  process running in 32-bit mode.//

What is Wireless-Extensions' replacement
----------------------------------------

New development should be focused on :doc:`cfg80211 <cfg80211>` and
:doc:`nl80211 <nl80211>`.

Isn't this just changing the transport ?
----------------------------------------

No. nl80211 is a complete re-design of how wireless settings work and
more clearly defines the semantics of each command (group).

Do we still use WE ?
--------------------

No, while :doc:`cfg80211 <cfg80211>` still has some backward
compatibility support, and a few ancient drivers still support only
wireless extensions, everything else has long moved on and doesn't
support anything but the most basic features with wireless extensions.
