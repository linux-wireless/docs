San Francisco 2010
==================

.. toctree::

   notes from this summit <sanfranciscobayarea-2010/notes>

This event will be September 9-10, 2010 (Thursday-Friday) in San
Francisco. Meeting space will be in Marriott Union Square San Francisco
at 480 Sutter Street. A group rate of $159/night at the hotel is
available for two nights (September 9-11) with group code "wifwifa".
Direct link to the reservation page:
http://www.marriott.com/hotels/travel/sfous?groupCode=wifwifa&app=resvlink&fromDate=9/9/10&toDate=9/11/10

Topics
~~~~~~

-  Overview of Wi-Fi Alliance
-  `Wi-Fi Direct <https://www.wi-fi.org/draft_specifications.php>`__ (P2P)

    - Introduction to the protocol
    - Driver requirements
    - mac80211 design
    - wpa_supplicant/hostapd functionality
    - Planning for communication with other than core WLAN components

-   cfg80211/mac80211 issues with different channels on different virtual interfaces
-   Enabling more spectrum availability when roaming through `GeoClue <GeoClue>`__, passing accuracy values to the kernel for regulatory hints
-   Requirements for wireless-regdb patches
-   powersaving in multi-interface scenarios
-   automated testing of the drivers and Linux WLAN
-   define mac80211 callback order (e.g. station notification before/after bss_info_changed?)
-   RSN IBSS

    -  iwlwifi might require knowing this to disable hw group crypto, not sure what happens if simply no key exists

-   GTK handling in mac80211
-   HT IBSS
-   a-MSDU TX support
-   usage of BUG_ON in wireless core and drivers
-   Improving the relationship with the community on legacy drivers / documentation

Schedule
~~~~~~~~

The meeting room will be "Union Square North". Dining will be in the adjacent "Union Square South".

Thursday
^^^^^^^^

.. list-table::

   - 

      - **Time**
      - **Session**
      - **Owner**
   - 

      - 7:30 - 9:00
      - **Breakfast**
      - 
   - 

      - 9:00 - 9:30
      - Welcome, introduction, agenda bashing
      - Linville
   - 

      - 9:30 - 10:30
      - WFA Overview, P2P introduction
      - Jouni/Henry
   - 

      - 10:30 - 11:00
      - **Break**
      - 
   - 

      - 11:00 - 11:30
      - P2P demo; mac80211/wpa_supplicant design (`code upstream <http://hostap.epitest.fi/gitweb/gitweb.cgi?p=hostap.git;a=summary>`__!)
      - Jouni
   - 

      - 11:30 - 12:00
      - P2P UI, user space next step
      - Jouni
   - 

      - 12:00 - 13:00
      - **Lunch**
      - 
   - 

      - 13:00 - 14:00
      - P2P virtual interfaces, power saving, etc. needed functionality
      - Jouni
   - 

      - 14:00 - 15:00
      - multi-channel operation in cfg80211/mac80211
      - Johannes
   - 

      - 15:00 - 15:30
      - **Break**
      - 
   - 

      - 15:30 - 16:00
      - `Requirements for wireless-regdb patches <http://lists.infradead.org/mailman/listinfo/wireless-regdb>`__
      - Linville/Luis
   - 

      - 16:00 - 16:30
      - World roaming and `GeoClue <http://www.freedesktop.org/wiki/Software/GeoClue>`__
      - Luis
   - 

      - 16:30 - 17:00
      - Backporting
      - Johannes
   - 

      - 17:00 - 18:00
      - Automated WiFi Testing (use `Autotest <http://autotest.kernel.org/>`__)
      - SamLeffler

Friday
^^^^^^

.. list-table::

   - 

      - **Time**
      - **Session**
      - **Owner**
   - 

      - 7:30 - 9:00
      - **Breakfast**
      - 
   - 

      - 09:00 - 10:30
      - Legacy drivers support / documentation
      - Luis
   - 

      - 10:30 - 11:00
      - **Break**
      - 
   - 

      - 11:00 - 12:00
      - Maintainer Issues / Community Relations
      - Linville
   - 

      - 12:00 - 13:00
      - **Lunch**
      - 
   - 

      - 13:00 - 14:00
      - Specialized APIs
      - Felix / Johannes ?
   - 

      - 14:00 - 15:00
      - powersaving bcast / mcast / multichannel
      - Luis / Johannes
   - 

      - 15:00 - 15:30
      - **Break**
      - 
   - 

      - 15:30 - 16:00
      - IBSS issues (RSN/GTKs, HT)
      - Johannes

Attendees
~~~~~~~~~

- Jouni Malinen
- Johannes Berg
- Kalle Valo
- Henry Ptasinski
- Lennert Buytenhek
- Luis R. Rodriguez
- Luciano Coelho
- John Linville
- Brett Rudley
- Wey-Yi Guy
- Ajit Pal Singh
- Nohee Ko
- Tim Gardner
- Jason Young
- Sam Leffler
- Paul Stewart
- Irfan Sheriff
- Dimitry Shmidt
- Abhijeet Kolekar
- Ajay Gupta
- Cyrille Vignon
- Gery Kahn
- Rik Logan
- Jayant Sane
- Guru
- Howard Harte
- Felix Fietkau
- Ohad Ben-Cohen
- Francois Amand
- Nicolas Petit
- Vipin Mehta
