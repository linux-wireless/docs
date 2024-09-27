Developer Documentation
-----------------------

This section tries to organize documentation for new Linux wireless developers.

Development basics
------------------

Essential information on how to hack and contribute to Linux wireless
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`Wireless Developer Summits <summits>`
-  :doc:`MailingLists <mailinglists>` - Subscribe to our mailing lists
-  :doc:`Git-guide <documentation/git-guide>` - learn to use git, emphasis on Linux wireless
-  :doc:`Using sparse <documentation/using-sparse>` - learn to use sparse
-  :doc:`IEEE-802.11 standards <documentation/ieee80211>` - standards we use and interpretations to help development
-  :doc:`SubmittingPatches <documentation/submittingpatches>` - guide on how to submit patches for Linux wireless work
-  :doc:`Glossary <documentation/glossary>` - terms we use throughout the wiki you should be familiar with
-  :doc:`Maintainers <maintainers>` - maintainers of current wireless drivers and driver APIs
-  :doc:`todo-list <todo-list>` - Our current TODO list
-  :doc:`Firmware versioning <documentation/firmware-versioning>` - Suggested firmware versioning rules
-  :doc:`Linux Kernel Wireless (802.11) Implementation <documentation/linuxkernelwirelessimplementation>` - some implementation details

Other interesting information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

     * [[en/developers/Documentation/ChannelList|channel list]] 
     * [[en/developers/Documentation/IEorder|information element order]] 

Driver APIs
-----------

Here are all the driver APIs we use to write drivers in Linux:

::

       * [[en/developers/Documentation/Wireless-Extensions|Wireless-Extensions]] - old wireless driver framework 
       * [[en/developers/Documentation/mac80211|mac80211]] - wireless driver API for [[en/developers/Documentation/Glossary|SoftMAC]] devices 
       * [[en/developers/Documentation/cfg80211|cfg80211]] - new driver configuration API 
       * [[en/developers/Documentation/nl80211|nl80211]] - new userspace <--> kernelspace wireless driver communication transport 
       * [[en/developers/Documentation/specs|Hardware Specifications]] - specifications for chipsets we support or will support soon 
       * [[en/developers/Documentation/radiotap|Radiotap]] - For 802.11 frame injection/reception 
       * [[en/developers/Documentation/Android|Support for Android]] - if you want to know how to add support for Android 
       * [[en/developers/Documentation/modularizing-code|Howto modularize code]] - Examples of how we expect you to modularize code 

802.11 Development process
--------------------------

Check out the :doc:`802.11 development process <process>` page for details of how patches get merged into Linux for 802.11 and what trees are used.

Stable monitor list
-------------------

The :doc:`stable-pending <stable-pending>` section is dedicated to the ensuring we propagate critical patches to the stable series of the Linux kernel. Use it to peg commits which you know are important to get merged.
