Developer Documentation
=======================

This section tries to organize documentation for new Linux wireless developers.

Development basics
------------------

Essential information on how to hack and contribute to Linux wireless
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 1

   Wireless Developer Summits <summits>
   MailingLists <mailinglists>
   Git-guide <documentation/git-guide>
   Using sparse <documentation/using-sparse>
   IEEE-802.11 standards <documentation/ieee80211>
   Submitting Patches <documentation/submittingpatches>
   Glossary <documentation/glossary>
   Maintainers <maintainers>
   Current TODO list <todo-list>
   Firmware versioning <documentation/firmware-versioning>
   Linux Kernel Wireless (802.11) Implementation <documentation/linuxkernelwirelessimplementation>

Other interesting information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 1

   documentation/channellist
   documentation/ieorder

Driver APIs
-----------

Here are all the driver APIs we use to write drivers in Linux:

.. toctree::
   :maxdepth: 1

   documentation/api-list
   documentation/wireless-extensions
   documentation/mac80211
   documentation/cfg80211
   documentation/nl80211
   documentation/specs
   documentation/radiotap
   documentation/android
   documentation/modularizing-code
   documentation/qos
   documentation/pm-qos

802.11 Development process
--------------------------

Check out the :doc:`802.11 development process <process>` page for
details of how patches get merged into Linux for 802.11 and what trees
are used.

Stable monitor list
-------------------

The :doc:`stable-pending <stable-pending>` section is dedicated to the
ensuring we propagate critical patches to the stable series of the Linux
kernel. Use it to peg commits which you know are important to get
merged.
