A Linux Kernel Radio Frequency Broker

`marcel@holtmann.org </mailto/marcel@holtmann.org>`__ `timg@tpi.com </mailto/timg@tpi.com>`__ `mcgrof@gmail.com </mailto/mcgrof@gmail.com>`__ `inaky.perez-gonzalez@intel.com </mailto/inaky.perez-gonzalez@intel.com>`__

Ubuntu Developer Summit, Sevilla (Spain) May 2007

--------------

Objective
---------

A frequency broker to coordinate the usage of frequency bands amongst all the radios in a Linux system. As well, to provide regulatory information that drivers can use to be fully compliant depending on geography.

Code
----

We have an scratch out of the data structures and modules at `http:bughost.org/repos.hg/frbr.hg]], accessible with [[http:\ selenic.com/mercurial|Mercurial <http://bughost.org/repos.hg/frbr.hg>`__.

It currently has no implementation of the regulatory controller and only registers bands that the drivers provide. Waiting to have some more time to work on it :)

Random notes about usage models
-------------------------------

User space sets a regulatory spectral mask (based on geo location, for example).

Device driver registers frequency band capabilities (ie: bands where they can tx/rx, at which max power, type of technology, flags, etc).

By some management action, the device is going to be asked to use a frequency in a band. Device queries the broker to see if that frequency band is used or can be shared with other devices or not. The decission can come of as:

-  result of a passive/active scan
-  user selection
-  Ask for a frequency to use to the broker (any which is free). After querying, an answer arrives: you can use band X or you don't have any band to use.

If there is no band to use:

::

     * Driver/device won't emit any radiation in that frequency/power. 
     * Further behaviour is subsystem dependent. It might decide to try other band or wait for management action. 
     * Broker sends userspace a message for user action. If accepted: 
       * The band is refcounted as used and the caller registerd as one of the owners 
       * device is allowed to transmit in that frequency with the assigned power limitation 

Operations
----------

::

         * <code>register()</code>: Register name/devicename/callbacks, etc maybe register initial list of bands? 
         * <code>band_add()</code>: Register band/s that a device can use. It can be invoked at any time while registered.  
         * <code>band_rm()</code>: Remove a usable band usable by a device. If that band is currently active, the driver is assumed to have ceased operation on the band before removing it. 
         * <code>unregister()</code>: Undoes register(), cleans up registered bands. 
         * <code>__allocate_bands()</code>: [internal note] Needs to notify devices that have active bands on spread-spectrum/soft when somebody steps on their band. 
         * <code>query_bands()</code>: Similar to get, but doesn't allocate, just reports if used? not clear that we really need it. 
         * <code>get_bands()</code>: The device wants to start using a band/s; if they are all free, return success and assign them to the device. Else the band/s are taken and device can't use them. 

We want to allow devices to share channels. If devices are the same technology sharing is on by default, else is not. We need a force parameter/priority override. A prioritization can be:

::

         *  * per type default priority 
         *  * per device default priority (defaults to per type) 
         *  * per cap priority (defaults to per device)          
         *   <code>put_bands()</code>: release previously assigned bands. 

Callbacks
---------

When a device wants to activate a band he calls \_get(), which checks for regulatory and then conflicts.

For each conflict, \_get() calls back the owners and says "Can you share?" or "You have to release" [note: still not clear if this should be two different cbs]. The owner releases if ordered to or agrees or disagrees to share.

::

         *   * **Rationale:** devices might not be able to share in some circumstances (eg: other channels are full). At that point the caller gets his request refused and bubbles up to the user space agent for resolution. 

If share disagreement, \_get() caller doesn't get the band and the broker notifies user space for a conflict.

Types of callbacks:

::

         *     * Some band that the device cares about is now de/activated by other device 
         *     * Some band that the device is actively using now de/activated by othre device 
         *     * The regulatory information has changed (general) Provides a link to the new/removed one? 
         *     * Regulatory conflict notificaton: the device are using a band that is not allowed to be used after a change in regulatory information. If we do a regulatory mask change, we scan the active band list and if there is a conflict, we send a notification for the callee to take action for compliance (eg: shut the channel off, reduce power, etc). 

Sysfs tree
----------

Sample, castle in the air

::

   sys/subsys/freqbroker
     regulatory/
       addband
       removeband
       band1
       badn2
     active/
       typename-symlink1 to band1   # or separate directories for each type
       typename-symlink2 to band5
     dev1/
       device -> link to the owner
       band1/         # names/of the channels
         device -> link to the devX owner
         active
         center
         width
         maxpower
         flags
         etc...
       band2/
       band3/

Broker life cycle and startup
-----------------------------

One initialization the broker should be empty until filled up by user space. During deployment, there will be gaps until user space support is widely deployed. In the meantime, we have to behave somehow.

Options:

::

         *       - Regulatory db is empty, we deny everything 
         *       - Regulatory db is empty, we accept everything 
         *       - We initialize from the device bands declared by drivers [they come from the device's eeproms] 
         *       - We have a set of wired in defaults that englobe all the settings around the world. The last two options is just #2, as it basically means we allow the device to do whatever. 
         *         * NOTE: this might cause usability problems when rolling it forward (if distros don't have regulatory info ready to move), so it might make sense to make the default 1 or 2 depending on a command line option, settable via /sysfs. 

Data types
----------

band
~~~~

Specifies a contiguous range of Mhz.

<code> band center freq (integer MHz)

::

     band width                     (integer MHz)
     maximum power emission         (integer / 1000 dBm)
     bandtype                       (see below)
     name                           (driver name + device instance)
     priority
     flags
       spread spectrum              Bluetooth -- bt uses a frequency
                                    range and hops around and will obey
                                    freq blockout. Spectrum is used as
                                    widely as possible (starts big and
                                    shrinks it).
                                    soft/advisory
                                    See note
     refcount/usecount</code>

Band type
~~~~~~~~~

Type of the technology that is using that band specification.

<code> 802.11{b,a,n,c,g}, 802.16, GPS, GSM, BT, uwb ...

::

     default priority</code>

Notes
-----

NOTE: when suspending, tell broker channel is not active any more

NOTE: bt uses a full range on ISM, hops around but cannot block out

::

         *           * any ranges. So BT needs to do an 'advisory' reservation, so that other devices know that they can expect 'some' interference from BT.  Make a mechanism to tell BT not to use certain channels when we get a request for them -- hw not guaranteed to follow it, but some will. 

NOTE: passive to active scanning concern -- consider active scan

::

         *             * something we ignore as a txing (side effects). 
