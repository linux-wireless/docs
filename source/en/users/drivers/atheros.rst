Go back –> :doc:`Linux wireless drivers <../drivers>`

Atheros Linux wireless drivers
------------------------------

This page documents all `Atheros Communications <http://www.atheros.com/>`__ Linux wireless drivers.

Contribution map
----------------

We have a `Google Drive spreadsheet <https://docs.google.com/spreadsheet/ccc?key=0AtNdeeyGJEJ7dG45U2xrZldlQm80Nlg5QzEwUmtNUGc>`__ with graphs you can view. Several formats are available:

-  `HTML <https://docs.google.com/spreadsheet/pub?key=0AtNdeeyGJEJ7dG45U2xrZldlQm80Nlg5QzEwUmtNUGc&output=html>`__
-  `PDF <https://docs.google.com/spreadsheet/pub?key=0AtNdeeyGJEJ7dG45U2xrZldlQm80Nlg5QzEwUmtNUGc&output=pdf>`__
-  `ATOM <https://spreadsheets.google.com/feeds/list/0AtNdeeyGJEJ7dG45U2xrZldlQm80Nlg5QzEwUmtNUGc/od6/public/basic>`__
-  `RSS <https://spreadsheets.google.com/feeds/list/0AtNdeeyGJEJ7dG45U2xrZldlQm80Nlg5QzEwUmtNUGc/od6/public/basic?alt=rss>`__
-  `ODS <https://docs.google.com/spreadsheet/pub?key=0AtNdeeyGJEJ7dG45U2xrZldlQm80Nlg5QzEwUmtNUGc&output=ods>`__
-  `CSV <https://docs.google.com/spreadsheet/pub?key=0AtNdeeyGJEJ7dG45U2xrZldlQm80Nlg5QzEwUmtNUGc&output=csv>`__

If you'd like to contribute please contact one of the device driver maintainers.

Shared modules
--------------

Atheros drivers tend to follow a lineage of hardware families and as they progress pick things up from one family or another and sometimes keep things the same. So hardware or EEPROM layouts can share certain characteristics and the same code can be reused through different hardware families.

Shared module for Atheros 802.11 drivers:

::

     * [[en/users/Drivers/ath|ath]] - code that is common amongst all hardware families 

IRC
---

For support and development for all drivers we use the :doc:`#linux-wireless IRC channel <../support>` on irc.freenode.net.

PCI / PCI-E / AHB Drivers
-------------------------

.. list-table::

   - 

      - **Technology**
      - **Upstream driver**
   - 

      - 802.11abg
      - :doc:`ath5k <ath5k>`
   - 

      - 802.11abgn
      - :doc:`ath9k <ath9k>`
   - 

      - 802.11ac
      - :doc:`ath10k <ath10k>`
   - 

      - 802.11ad
      - :doc:`wil6210 <wil6210>`

USB Drivers
-----------

.. list-table::

   - 

      - **Technology**
      - **Legacy driver**
      - **Upstream driver**
   - 

      - 802.11b
      - None
      - `zd1201 <en/users/Drivers/zd1201>`__
   - 

      - 802.11bg
      - `zd1211 <http://sf.net/projects/zd1211/>`__
      - :doc:`zd1211rw <zd1211rw>`
   - 

      - 802.11abg
      - None
      - :doc:`ar5523 <ar5523>`
   - 

      - 802.11abgn
      - :doc:`otus <otus>` / :doc:`ar9170 <ar9170>`
      - :doc:`carl9170 <carl9170>` (:doc:`carl9170.fw GPLv2 <carl9170.fw>`)
   - 

      - 802.11abgn
      - None
      - :doc:`ath9k_htc <ath9k_htc>`

Mobile (SDIO & CF)
------------------

::

       * [[en/users/Drivers/ar6k|ar6k]] - Non-upstream GPL mobile driver, as used by [[OpenMoko|OpenMoko]] 
       * [[en/users/Drivers/ath6kl|ath6kl]] - Reference driver from Atheros for AR600x with cfg80211 support 

Licensing
---------

To help other FOSS Operating Systems, when possible, Atheros licenses their device drivers source code under a permissive license. Atheros picked the `ISC License <http://en.wikipedia.org/wiki/ISC_license>`__ due to historical reasons, mainly that of the ath5k developers also choosing it to help share code between Linux and OpenBSD. Atheros follows this tradition to further assist not only OpenBSD but also other FOSS Operating Systems. There are a few exceptions to using the ISC license on Atheros drivers, when in doubt consult the header of the file for the respective license of the file.

As far as firmware is concerned Atheros does try to open source firmware when possible with the first release being that of :doc:`ar9170.fw <ar9170.fw>`. When not possible (lack of resources mainly) we do try to work with the community to see if this can be done through side community work, and only if not possible at all do we release firmware as binary with a friendly standard redistributable license.
