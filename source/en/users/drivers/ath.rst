ath
===

ath the shared module between Atheros wireless drivers. It contains any
shared common code. It currently only contains the common shared
regulatory code and one common harware helper but can be extended to
contain anything seen shared between all drivers, both 802.11n or legacy
802.11abg devices. The ath modules is currently shared and used between
ath5k, ath9k\*, ath6kl\_\* and carl9170.

TODO
----

Here is the TODO list for the common shared code for Atheros modules.

- When the regpair is detected check first the currently set alpha2 and
  if the regpair matches a group that has that alpha2 use that alpha2
  instead for the regulatory_hint().
- Test firmware upload on ar9271 and if it works as-is then share
  firmware upload code between ar9170 and ar9271 as currently the code
  is identical. There is one exception, the final command but we can
  probably just ignore the error code on that on ar9271 as well.

Regulatory
----------

Atheros devices share the same regulatory implementation. All devices
have a regulatory domain code programmed into their EEPROM. The
programmed regulatory domain code can be of three kinds:

* custom world regulatory domains 
* programmed `country code
  <http://en.wikipedia.org/wiki/ISO_3166-1_numeric|ISO-3166-1-numeric>`__
  (with a few exemptions) 
* a regulatory pair group number Historically the Atheros regulatory
  domains have been mapped to groups as many regulatory domains share
  common definitions. Atheros regulatory domains used to be all embedded
  in the driver source code so space efficiency was important. To save
  space and to allow more diversity regulatory domains were allowed to
  be mapped to a 5 GHz group and a 2 GHz group. When a band was not
  supported a NULL group for the band was used. Each band group had a
  arbitrary group name, such as FCC3 or MKKA. 

To better understand the nomenclatures used it helps to understand the
conventions followed by the old Atheros regulatory group naming
convention. Tendencies to follow "US" similar regulatory domains were
given "FCC" prepend labels after the FCC, European regulatory domains
used the "ETSI" prepend name after the ETSI, Asian countries tended to
fit under "MKK" under the Japanese regulatory agency (I forget what this
stands for), "APL" which I believe stands for "Asia, Pacific and Latin
America". Numbers were appended at the end of each group label for 5 GHz
groups, and letters for 2 GHz band group names.

Examples of 5 GHz regulatory band group names:

* MKK1 
* APL4 
* ETSI1 
* FCC3 
* WOR0 (World regulatory band definition 0) 
* WOR4 (World regulatory band definition 4) Examples of 2 GHz regulatory
  band group names: 

    * MKKA 
    * MKKA1 
    * MKKA2 
    * FCCA 
    * ETSIC 
    * WORLD (there's only one 5 GHz group world regulatory domain)

Each band also had a set of world regulatory definitions. 

Each regulatory band group had an attached set of frequency ranges along
with regulatory flags for the channels. Band groups could be put
together to form a regulatory domain, containing one 5 GHz regulatory
domain group, and a 2 GHz regulatory domain group.

Examples of regulatory domain groups:

* ETSI1_WORLD 
* MKK9_MKKA1 
* WOR9_WORLD 
* ETSI4_ETSIC

Programmed EEPROM regulatory domains codes would map to regulatory
domain groups along with flags specific to that regulatory domain. 

Each regulatory domain group would also have an equivalent *Conformance Test Limit* (CTL) group. There are 3 CTL groups:

* CTL_FCC = 0x10 
* CTL_MKK = 0x40 
* CTL_ETSI = 0x30

The CTL group is used internally by the driver to use the appropriate
CTL index in the EEPROM to figure out the max regulatory EIRP. The CTL
indexes always have a defined regulatory max EIRP and are programmed
into the EEPROM. The CTL index maps frequency ranges to a specific max
EIRP. This CTL index max EIRP is also used to ensure the device will not
use an EIRP higher than should be used without damaging the card.

Customizing Atheros hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vendors or manufacturers who may customize Atheros hardware may likely
choose to enable their customers to use a wider range of frequencies or
to use a higher max EIRP output. Certification would be done by these
manufacturers and as such it is up to them to supply you with a custom
regulatory database for its use. Typically a proprietary Linux driver
would be provided with a customized "HAL" which allows more frequencies
or higher EIRP. Since the upstream Linux drivers do not rely on a "HAL"
anymore for regulatory purpose and instead rely on CRDA, manufacturers
who customize hardware could simply just provide custom signed
regulatory databases and a custom CRDA instead of providing a completely
separate driver.

For details as to how to achieve a custom regulatory wireless-regdb and
public key see the :doc:`Custom_regulatory_information
<../../developers/regulatory>` guidelines.

The 0x0 regulatory domain
^^^^^^^^^^^^^^^^^^^^^^^^^

The 0x0 value of a regulatory domain is to be used by Atheros devices to
map to the "US", always. This is as per Atheros documentation to
manufacturers. Manufacturers wanting to enable users to use cards as
"region free" should supply their own builds of CRDA and a signed
regulatory database.

For more details you can refer to this thread:

http://article.gmane.org/gmane.linux.kernel.wireless.general/38410

EEPROM world regulatory domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Atheros EEPROM can use 12 custom world regulatory domains:

* WOR0_WORLD = 0x60 
* WOR1_WORLD = 0x61 
* WOR2_WORLD = 0x62 
* WOR3_WORLD = 0x63 
* WOR4_WORLD = 0x64 
* WOR5_ETSIC = 0x65 
* WOR01_WORLD = 0x66 
* WOR02_WORLD = 0x67 
* EU1_WORLD = 0x68 
* WOR9_WORLD = 0x69 
* WORA_WORLD = 0x6A 
* WORC_WORLD = 0x6C

0x60, 0x61, 0x62, 0x66, 0x67, 0x68 are only used **today** moving
forward for 2.4 GHz-only band cards. 

5 GHz with world regulatory domain and beacon hints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All Atheros custom world regulatory domains have all 5 GHz channels
marked with a passive scan flags. The non-DFS channels can have their
passive scan flags lifted through a feature implemented in cfg80211
called "beacon hints". For details on that please read the :doc:`beacon
hints <../../developers/regulatory/processing_rules>` documentation.

EEPROM ISO-3166-1-numeric code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Atheros EEPROM regulatory domain can contain an `ISO-3166-1-numeric
country code <http://en.wikipedia.org/wiki/ISO_3166-1_numeric>`__. This
may or not match the exact ISO3166-1-numeric country code, but usually
does. Because it *may not* always match for the new regulatory
infrastructure used in Linux we map the country to the `ISO-3166-alpha2
country code <http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__.

Examples of possible country code numbers a card EEPROM can be
programmed with:

* CTRY_INDONESIA = 360 
* CTRY_IRAN = 364 
* CTRY_IRAQ = 368 
* CTRY_IRELAND = 372 
* CTRY_ISRAEL = 376 
* CTRY_ITALY = 380 
* CTRY_JAMAICA = 388

When a country regulatory domain is used in the EEPROM the card will
also have the COUNTRY_ERD_FLAG (0x8000) set to indicate the EEPROM has a
country code. Without this the assumption is a regulatory pair group has
been programmed in the EEPROM. 

EEPROM regulatory pairs
~~~~~~~~~~~~~~~~~~~~~~~

The Atheros EEPROM can use a *regulatory pair* group. Examples of regulatory pair groups:

* MKK1_MKKA = 0x40 
* ETSI1_WORLD = 0x37 
* FCC1_FCCA = 0x10 
* WOR02_WORLD = 0x67 

The old way
~~~~~~~~~~~

The old way was to define all band groups (5 GHz and 2 GHz) in the
driver code. Each band group would have a set of defined frequency
ranges.

The new way
~~~~~~~~~~~

We have extracted the regulatory domain definitions per ISO3166-alpha2
and converted them to human legible ASCII text file, used by the new
:doc:`Linux regulatory infrastructure <../../developers/regulatory>`.
Each country therefore has a db.txt entry such as::

   country EC:
           (2402 - 2482 @ 40), (N/A, 20)
           (5170 - 5250 @ 20), (6, 17)
           (5250 - 5330 @ 20), (6, 23), DFS
           (5735 - 5835 @ 20), (6, 30)

The custom regulatory domains are kept statically as part of the driver.
The custom regulatory domains are the 12 custom world regulatory
domains.

Regulatory pair regulatory domains are mapped to the first
ISO-3166-alpha2 country.

Driver initialization
~~~~~~~~~~~~~~~~~~~~~

The device programmed EEPROM is read. We then determine if the
regulatory domain code is a country regulatory domain COUNTRY_ERD_FLAG
(0x8000) or a regulatory pair. Based on that, we determine whether we
use an ISO3166-alpha2 country code for a regulatory_hint() or we use a
static world regulatory domain.

In case of the absence of CRDA and because the kernel still has
CONFIG_WIRELESS_OLD_REGULATORY (although deprecated) the ath module
pre-initializes the wiphy channels to apply the default world regulatory
domain (0x64). This is done done in ath_regd_init_wiphy() by using the
cfg80211 provided wiphy_apply_custom_regulatory(). This is done because
CONFIG_WIRELESS_OLD_REGULATORY is still present upstream and if not done
would allow even "JP" channels to be used on cards designed for the
"US". Also, although the static world regulatory domain in cfg80211 is
sufficient for complete world compliance Atheros has always supported a
5 GHz band which is a little more extended. The world regulatory domain
is computed dynamically on a regular basis by using the intersection of
all regulatory domains. Code for computing this can be found on
`intersection.c
<http://git.kernel.org/?p=linux/kernel/git/mcgrof/crda.git;a=blob;f=intersect.c;h=2f4d416577e69f67f1c4056f59fe387e7ee5d5cb;hb=HEAD>`__.
This currently produces a 5 GHz band supporting the frequency ranges::

   5170-5250 Channels [36-48]
   5735-5835 Channels [149-165]

While Atheros' default world regulatory domain covers::

   5140-5360 Channels [36-64]
   5715-5860 Channels [149-165]

An Atheros world roaming card would then support channels 52, 56, 60,
and 64 when world roaming, but by also enabling passive scan, no
beaconing and requiring radar detection on them as well. The number of
allowed HT40 channels would also increase to::

   5180 HT40  +
   5200 HT40 -+
   5220 HT40 -+
   5240 HT40 -+
   5260 HT40 -+
   5280 HT40 -+
   5300 HT40 -+
   5320 HT40 - 

This happens when your card has a world roaming regulatory domain. It
should be also noted that if your card is world roaming your card will
also remove passive-scan flag and no-beaconing flag restrictions if an
AP is found locally on a channel and DFS is not required on that channel
on the 5 GHz band.

Hidden SSIDs
------------

Please read the regulatory documentation on :doc:`hidden SSIDs
<../../developers/regulatory/processing_rules>`. Hidden SSIDs can become
a problem for cards that are world roaming. For QCA cards you can
determine means your :doc:`EEPROM regulatory matches one of the listed
world regulatory domains <ath>`. To verify you can issue a command as
follows::

   system@user:~$ dmesg | grep ath | egrep "regdomain|Country"
   ath: EEPROM regdomain: 0x6a
   ath: Country alpha2 being used: 00

You will see the *00* country code being used if your regulatory domain
on your EEPROM is determined to be a world regulatory domain. For
further reading on understanding any possible issues with hidden SSIDs
be sure to read the regulatory documentation on :doc:`hidden SSIDs
<../../developers/regulatory/processing_rules>`.
