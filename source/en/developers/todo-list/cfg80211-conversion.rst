drivers needing full conversion
===============================

-  airo
-  atmel
-  ipw2x00 (some trivial work done)
-  prism54 - as much as we'd like to kill it, it still the only option for some users of some specific FullMAC cards where p54pci does not work
-  ray (`802.11-legacy mode <http://en.wikipedia.org/wiki/IEEE_802.11_%28legacy_mode%29>`__)
-  wl3501 (`802.11-legacy mode <http://en.wikipedia.org/wiki/IEEE_802.11_%28legacy_mode%29>`__)
-  zd1201 (some of these are for ancient hardware that likely nobody cares about any more, not converting them might mean that future userspace breaks but that doesn't seem problematic)

drivers that have partial conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* orinoco 
* libertas 

drivers to kill
~~~~~~~~~~~~~~~

* hostap (?) From this list, only ipw2200 and libertas are 802.11**g** hardware. All others are only 802.11**b**, except ray and wl3501. 
