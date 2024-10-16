cfg80211
========

.. toctree::

   todo-list/cfg80211-conversion
   todo-list/client-ps-testing
   todo-list/regulatory

Regulatory
~~~~~~~~~~

-  :doc:`Regulatory TODO <todo-list/regulatory>`

Issues
~~~~~~

* make scan timeout variable depending on scan length, in case scans take longer than the current 15 seconds 

mac80211
--------

Mesh
~~~~

* If a mesh join request does not come with a frequency, initiate scan for suitable neighbor MBSS frequency first. 

AP support
~~~~~~~~~~

* :doc:`AP DFS or AP radar detection <dfs>`
* local->total_ps_buffered is totally racy

Issues
~~~~~~

* drivers with IV offload do not correctly report IV/PN to nl80211 
* Need to stop TX/RX when a radar is detected for the duration of scan
  for a new channel. 

Improvements
~~~~~~~~~~~~

* reset the connection and beacon monitor timers when we are able to
  successfully TX data to an AP (we currently do it on RX)
* move survey caching code from ath9k to mac80211 so that other drivers
  can simply update channel survey data once and all cached data can be
  sent back to userspace as ath9k does it
* improve roaming time by collapsing synchronize_rcu() (or even getting
  rid of it by using call_rcu()) in station/key management

power saving
~~~~~~~~~~~~

* move checking for broadcast / multicast frames to mac80211 before
  going to PS. ath9k already has some code for this, this should be
  moved to mac80211. Or just extend documentation to indicate drivers
  are required to do this.
* 11v support (eventually)
* implement a PS library, a la described in
  [[http://marc.info/?l=linux-wireless&m=135838252227053|http://marc.info/?l=linux-wireless&m=135838252227053]]

Offchannel work
~~~~~~~~~~~~~~~

* optimise "offchannel" to not stop beaconing/traffic/etc. when using
  the operating channel
* implement addBA in terms off "offchannel" on the operating channel so
  it blocks other offchannel while waiting for a response
* don't time out RX BA agreements while offchannel
* do TX flushing as appropriate
* Wait for DTIM beacon and multicast traffic before going offchannel

drivers
-------

* :doc:`todo-list/cfg80211-conversion`

testing
-------

* :doc:`todo-list/client-ps-testing`
* q/a procedure for stack
* winlab
* info on test coverage
* tests themselves need to be documented
* instructions how to run tests
