cfg80211 driver API notes
=========================

Notes on this page are mostly for :doc:`FullMAC <../glossary>` devices,
:doc:`mac80211 <../mac80211>` has its own :doc:`API notes
<../mac80211/api>`.

Access Point mode
~~~~~~~~~~~~~~~~~

Support for AP mode requires some control over management frames that
hardware sends. This may vary between devices depending on the FullMAC
implementation.

Most FullMAC drivers will need to implement following callbacks:

- ``start_ap`` - to configure hardware to use requested channel and send
  beacons with provided data
- ``stop_ap`` - to stop AP mode
- ``del_station`` - to allow disconnecting client If the hardware is
  capable of sending/receiving any management frames, you may also need
  to implement ``mgmt_tx`` and ``mgmt_frame_register``.
