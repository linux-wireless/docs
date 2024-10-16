Linux wireless vendor support and regulatory compliance
=======================================================

Enhancing vendor relationship
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Distributions and Linux wireless developers would like to see vendor
support for FOSS drivers for their wireless chipsets. Today most 802.11
vendors are working upstream with wireless developers in the community
in providing sane drivers for proper Linux kernel inclusion and support.
Historically though, **years ago**, a few vendors only provided
proprietary solutions for their drivers. This was based on advice from
third parties which usually prevented these drivers from being supported
by the community and getting included into the Linux kernel. On the
second wireless summit which was held in London in 2007 we attempted to
reach out to as many wireless vendors as possible so we could properly
address their concerns in providing FOSS drivers.

Addressing vendor concerns
~~~~~~~~~~~~~~~~~~~~~~~~~~

Based on discussions and conference calls before and after the 2007
summit it became clear that the main vendor concern over supporting FOSS
drivers was to provide a mechanism to enforce regulatory compliance to
satisfy their own and their hardware vendors (OEMs like Dell, HP, IBM)
legal department's concerns over legal liability. Additional concerns
have been that a FOSS driver may force hardware vendors to certify their
platforms under new Software Defined Radio regulations. Additionally,
also that the FCC is only one of the many regulatory agencies vendors
take into consideration for certifying devices -- the major vendor's
geographies of interest are governed under the FCC, ETSI and MKK.
Vendors explained their concerns over getting devices certified under
FCC SDR regulations is the uncertainty of the details involved for such
certification. Vendors need to provide driver solutions which meet legal
criteria on all of their geographies of interest.

Technical difficulties on solutions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The obvious solution to all of these vendor concerns in providing
support for FOSS drivers is to provide restrictions in hardware based on
geography but it has been argued by **vendors** that this proves to be
**economically unfeasible**. Likewise, this would also create a problem
for **some users** wanting to **roam** outside of their geography using
the same wireless hardware. Current vagueness under FCC Part 15 rules
have allowed vendors to move forward with supporting proprietary driver
solutions for management and enforcement of regulatory restrictions.
Although security through obscurity is ultimately not a great security
model it is one which some vendors rely on, even for Linux proprietary
drivers, as it has satisfied both their own and their customers' legal
departments. Alternative solutions to the problem has been to
incorporate regulatory restrictions on the microcode of the resulting
firmware for use on a wireless device, which does allow for a complete
FOSS driver, but this approach is **looked down upon by vendors** as it
confines the vendors to smaller amount of space available for
development on the microcode and increases complexity.

Our stance and solution
~~~~~~~~~~~~~~~~~~~~~~~

Security through obscurity is simply not bullet proof but we do have
precedents of its use to allow vendors to support drivers on Linux,
either through a FOSS driver and binary firmware or through a binary
driver. **Real technical solutions** can be used instead of relying on
archaic security through obscurity mechanisms for support of FOSS
wireless drivers on the Linux kernel. Our solutions have been to get
commitment from the community developers to not accept patches upstream
which alter regulatory considerations for drivers and to pave the way
for open platforms to embrace a framework supported by the community to
further advance regulatory considerations.

Linux wireless regulatory support statement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For more details the non-technical details of our position please see
our :doc:`Linux wireless regulatory support statement
<../developers/regulatory/statement>`.

Technical review of our regulatory infrastructure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For technical details on our solution on this work please see the
documentation of our :doc:`regulatory infrastructure
<../developers/regulatory>` page.
