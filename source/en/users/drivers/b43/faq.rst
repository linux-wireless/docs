Linux Broadcom b43/b43legacy driver Frequently Asked Questions
==============================================================

Q: The LEDs do not work.
~~~~~~~~~~~~~~~~~~~~~~~~

A: You have to enable LEDs support in the kernel configuration. The
config options you have to enable are: CONFIG_LEDS_CLASS,
CONFIG_LEDS_TRIGGERS, CONFIG_MAC80211_LEDS.

Q: The radio-enable-button on my laptop does not work.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A: You have to enable RF-kill support in the kernel configuration. The
config options you have to enable are: CONFIG_RFKILL,
CONFIG_RFKILL_INPUT, CONFIG_INPUT_POLLDEV.

Q: After enabling the config options, LEDs/RF-kill still don't work.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A: If you have the b43/b43legacy driver built-in (not as a module), you
must also enable all the LEDs/RF-kill options (see above) built-in (not
as a module).

Q: I'm confused about this b43/b43legacy business. Which one do I need?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A: If your chipset is 802.11b-only or BCM4306 rev 2, you need to use
b43legacy. All other devices, including BCM4306 rev 3, use b43.

You can also ignore this issue and simply compile both drivers, they
will automatically detect which one you need by themselves and the
appropriate one will be loaded.
