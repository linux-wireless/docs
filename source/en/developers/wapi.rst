WAPI Overview
=============

WLAN Authentication and Privacy Infrastructure (`WAPI
<http://en.wikipedia.org/wiki/WLAN_Authentication_and_Privacy_Infrastructure>`__)
is a Chinese National Standard for Wireless LANs. WAPI became China’s
mandatory national standard in May, 2003 by AQSIQ (General
Administration of Quality Supervision, Inspection and Quarantine of the
People’s Republic of China). For a few years now it has been impossible
to implement WAPI on Linux due to the proprietary nature of the
specification and the classification of the `SMS4
<http://en.wikipedia.org/wiki/SMS4>`__ encryption algorithm. On 2005 the
'National body of China' tried to clarify via the `ISO/IEC WAPI N33
<http://www.chinabwips.org/doc/N_33_WAPI_and_Cipher_issue_by_CNB__Beijing_Meeting_8-12_August_2005.pdf>`__
that their WAPI ISO proposal was in compliance with ISO's
standardization process, they argued that *"WAPI defines the interface
of cipher algorithm according to the ISO’s common regulation of cipher
algorithm"*. Essentially they argued that their ISO proposal allowed
countries to choose the encryption algorithm used, SMS4 was just one
optional encryption algorithm and since it was classified it would be
used only in China. Eventually though the WAPI ISO proposal was
rejected.

In January 2006 the `SMS4 <http://en.wikipedia.org/wiki/SMS4>`__
encryption algorithm was declassified. In October, 2009 the 'National
body of China' resubmitted WAPI for ISO standardization. With the
declassification of SMS4 and the intent behind the *National body of
China* of making WAPI an ISO standard we should be able implement a full
WAPI solution on Linux using public documentation as reference. The new
ISO submission was `voted on on in January 2010
<http://isotc.iso.org/livelink/livelink?func=ll&objId=8685212&objAction=Open&vernum=1>`__
with a majority of votes in favor for the ISO proposal. The major
opponents were the US and UK standardization bodies with comments
concerned over the unsynchronized effort this would create given that
the ISO/IEC 8802-11 tends to be updated based on IEEE's own 802.11
group.

Despite the issues with the standardization bodies the ISO proposal got
a majority favorable vote which means we likely need to support WAPI
upstream somehow. Market-wise there is not much evidence of WAPI being
used anywhere except sometimes in China. Even in China WAPI does not
seem to be exclusively used. For this reason WAPI will help those users
in China connect and sell products where WAPI is required.

Components
----------

There are two components to WAPI:

- wpa_supplicant changes - this has yet to be implemented
- mac80211 changes - these are merged already, if you use hardware SMS4
  support Some hardware supports the SMS4 encryption algorithm in
  hardware, we can start off supporting those devices first. We need to
  scope out the effort required for the supplicant changes.

Possible issues
---------------

The WAPI ISO proposal is to provide a *alternative security mechanism*
by trying to annex the Annex ISO/IEC8802‐11. The ISO/IEC8802‐11 is the
international standardization of the IEEE-802.11 work, and as such
annexing ISO/IEC8802‐11 without first updating the respective
IEEE-802.11 standards can create interoperability with future 802.11
working group amendments such as IEEE 802.11e/j/k/n/r/w and work in
progress amendments such as IEEE 802.11 p/s/u/v/z/aa/ac/ad.

Due to the possible current/future interoperability/conflict issues with
WAPI and IEEE if WAPI gets added upstream and into wpa_supplicant it
must be a selectable option which can be disabled.

cfg80211 WAPI API
-----------------

You *should* be able to use a WAPI supplicant with cfg80211 as of 2.6.3x
(fill me in) kernel. This section documents how you can accomplish this.

cfg80211 WAPI managed mode API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All APIs required for WAPI for STA mode are in place on
cfg80211/nl80211. Refer to *NL80211_ATTR_CONTROL_PORT_ETHERTYPE* and
*NL80211_ATTR_CONTROL_PORT_NO_ENCRYPT*. You would give those to the
assoc() or connect() command to replace the control port protocol, which
defaults to EAPOL, by the WAPI protocol (and the WAPI requirement to not
encrypt). Your supplicant will use this protocol to negotiate WPI-SMS4
keys, which to cfg80211 is just a regular cipher, however mac80211
doesn't implement it in software, so make sure the device supports it as
one of the ciphers, the cipher suite is 00-14-72:1 (0x00147201 in
cfg80211).

cfg80211 WAPI AP mode API
~~~~~~~~~~~~~~~~~~~~~~~~~

Same as managed mode, the attributes are used with the crypto settings
given when setting the beacon (aka starting AP)

References
----------

When implementing WAPI you'll likely want to read

* `WAPI ISO submission - ISO/IEC JTC 1 N 9880 <http://isotc.iso.org/livelink/livelink?func=ll&objId=8500308&objAction=Open&vernum=1>`__
* `SMS4 description in English <http://eprint.iacr.org/2008/329.pdf>`__
* `WAPI ISO proposal voting results and comments <http://isotc.iso.org/livelink/livelink?func=ll&objId=8685212&objAction=Open&vernum=1>`__
