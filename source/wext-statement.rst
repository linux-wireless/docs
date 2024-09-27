\**This page is currently not readable to people who are not logged on because I don't want it to be widely linked *yet*, and it will also move to another place.

This statement is WORK IN PROGRESS.*\*

--------------

**Wireless extension deprecation**

With the recent advances in cfg80211, the userspace API nl80211 is now mostly at feature parity over wireless extensions, in some areas much exceeding the feature set already. At the same time, cfg80211 has gained support for emulating wireless extensions, so that applications using wireless extensions can continue to work for drivers implementing the richer and better defined cfg80211 API instead.

This represents a huge leap forward -- more than ten years after they were introduced wireless extensions can now be confined to the compatibility code in cfg80211. Many drivers in the kernel that are actively maintained are now being or have been ported to the new internal cfg80211 API to take advantage of the new features and improved semantics and to remove duplicate code that previously couldn't be shared among drivers.

As most modern drivers are now available with cfg80211 support, we encourage application developers to begin porting their applications to use the richer and more intuitive nl80211 instead of (or in addition to) wireless extensions. BSD-licensed example code can be found in the iw tool, see :doc:`en/users/Documentation/iw <en/users/documentation/iw>`. Applications that currently just script ``iwconfig``, ``iwevent`` or ``iwlist`` can use ``iw`` instead.

At the same time, new kernel drivers for full-MAC chips that do not use mac80211 need to be written using the cfg80211 API to allow the rich configuration and feature discovery with new userspace tools. As such, drivers written without cfg80211 can no longer be accepted into the mainline kernel, just like new wireless stacks as part of drivers are not acceptable and those drivers need to be ported or rewritten to mac80211, new drivers for hardware not using mac80211 need to be ported to cfg80211 APIs.
